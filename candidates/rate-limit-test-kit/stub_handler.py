#!/usr/bin/env python3
"""Example CORRECT rate-limited endpoint — stdlib only, ~160 lines.

Reference code you can adapt. It does the things a correct server-side API rate
limiter must (see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the sources
— RFC 6585 §4 for 429 + Retry-After, RFC 9110 for the Retry-After forms, and the
IETF draft "RateLimit header fields for HTTP" for the RateLimit-* fields). A
short, configurable FIXED WINDOW so the reset test runs fast.

The contract this handler honours:

  1. UNDER THE LIMIT → 2xx. The first `limit` requests inside a window succeed.
  2. AT/OVER THE LIMIT → 429. Request number `limit`+1 within the window returns
     **429 Too Many Requests** (RFC 6585 §4) — no off-by-one that lets `limit`+1
     through.
  3. A VALID Retry-After ON THE 429. The 429 carries `Retry-After: <delay>` in
     positive, sane delay-seconds (RFC 9110 §10.2.3 also allows an HTTP-date;
     this stub uses delay-seconds) telling the client exactly how long to wait.
  4. CONSISTENT RateLimit-* HEADERS. Every response carries `RateLimit-Limit`,
     `RateLimit-Remaining` (decrements each request, hits 0 exactly at the 429
     boundary), and `RateLimit-Reset` (delta-seconds until the window resets, a
     positive value pointing into the future). Legacy `X-RateLimit-*` aliases
     are emitted too so a client on either convention sees consistent values.
  5. THE WINDOW RESETS. After `Retry-After`/`RateLimit-Reset` elapses, the count
     resets and requests succeed again — and the advertised delay matches when
     the service actually resumes.

A tiny in-memory fixed-window counter holds (window_start, count) for a single
bucket (one caller). Real deployments key per client/IP/token and often use a
token bucket or sliding window in Redis; the 429 + Retry-After + RateLimit-*
CONTRACT this models is the same. A GET /_debug/state exposes the live counter,
and POST /_debug/reset starts a fresh window, so the kit's tests are
deterministic.

`rltk` fires bursts at a handler like this. Run standalone:
    python3 stub_handler.py 8000
Optional env:
    RLTK_LIMIT=5           # requests allowed per window
    RLTK_WINDOW_MS=1000    # window length in milliseconds (short = fast reset)
    RLTK_HEADER_STYLE=both # ratelimit | legacy | both (which header names to emit)
"""
import json
import math
import os
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class FixedWindowLimiter:
    """A single-bucket fixed-window limiter. `limit` requests per `window_ms`.
    Thread-safe; one lock guards the window so a concurrent burst is counted
    exactly. Real limiters key per client/IP/token — the CONTRACT (2xx under the
    limit, 429 + Retry-After at it, a resetting window) is what this models."""

    def __init__(self, limit: int, window_ms: int):
        self.limit = limit
        self.window_s = window_ms / 1000.0
        self._lock = threading.Lock()
        self._window_start = time.monotonic()
        self._count = 0

    def _roll_if_elapsed(self, now: float):
        if now - self._window_start >= self.window_s:
            self._window_start = now
            self._count = 0

    def take(self):
        """Account for one request. Returns (allowed, remaining, reset_secs).
        `reset_secs` is the whole seconds until the current window resets
        (>= 1), used for both RateLimit-Reset and Retry-After."""
        with self._lock:
            now = time.monotonic()
            self._roll_if_elapsed(now)
            self._count += 1
            remaining = max(0, self.limit - self._count)
            reset_secs = max(1, math.ceil(self._window_start + self.window_s - now))
            allowed = self._count <= self.limit
            return allowed, remaining, reset_secs

    def state(self):
        with self._lock:
            now = time.monotonic()
            self._roll_if_elapsed(now)
            reset_secs = max(1, math.ceil(self._window_start + self.window_s - now))
            return {"limit": self.limit, "count": self._count,
                    "remaining": max(0, self.limit - self._count),
                    "reset_secs": reset_secs, "window_ms": int(self.window_s * 1000)}

    def reset(self):
        with self._lock:
            self._window_start = time.monotonic()
            self._count = 0


def _make_resource(path: str) -> dict:
    return {"id": "req_" + uuid.uuid4().hex, "path": path, "status": "ok",
            "served": int(time.time())}


def make_handler(limiter: FixedWindowLimiter, header_style: str):
    emit_ratelimit = header_style in ("ratelimit", "both")
    emit_legacy = header_style in ("legacy", "both")

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            if self.path == "/_debug/state":
                self._json(200, limiter.state(), rate=False)
                return
            self._handle()

        def do_POST(self):
            if self.path == "/_debug/reset":
                limiter.reset()
                self._json(200, {"ok": True}, rate=False)
                return
            self._handle()

        def _handle(self):
            length = int(self.headers.get("Content-Length", 0))
            if length:
                self.rfile.read(length)  # body is ignored; this is a throttle test
            allowed, remaining, reset_secs = limiter.take()
            if allowed:
                self._json(200, _make_resource(self.path), rate=True,
                           remaining=remaining, reset_secs=reset_secs)
            else:
                # (2) at/over the limit → 429 with (3) a valid Retry-After.
                self._json(429, {"error": "rate limit exceeded",
                                 "code": "too_many_requests"},
                           rate=True, remaining=0, reset_secs=reset_secs,
                           retry_after=reset_secs)

        # ---- helpers ----------------------------------------------------- #
        def _rate_headers(self, remaining, reset_secs):
            if emit_ratelimit:
                self.send_header("RateLimit-Limit", str(limiter.limit))
                self.send_header("RateLimit-Remaining", str(remaining))
                self.send_header("RateLimit-Reset", str(reset_secs))
            if emit_legacy:
                self.send_header("X-RateLimit-Limit", str(limiter.limit))
                self.send_header("X-RateLimit-Remaining", str(remaining))
                self.send_header("X-RateLimit-Reset", str(reset_secs))

        def _json(self, code, body, rate, remaining=0, reset_secs=1, retry_after=None):
            data = json.dumps(body).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            if rate:
                self._rate_headers(remaining, reset_secs)
            if retry_after is not None:
                self.send_header("Retry-After", str(retry_after))
            self.end_headers()
            self.wfile.write(data)

    return Handler


def serve(port: int, limit: int = 5, window_ms: int = 1000,
          header_style: str = "both") -> ThreadingHTTPServer:
    limiter = FixedWindowLimiter(limit, window_ms)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(limiter, header_style))
    httpd.limiter = limiter  # expose for in-process callers/tests
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _limit = int(os.environ.get("RLTK_LIMIT", "5"))
    _window = int(os.environ.get("RLTK_WINDOW_MS", "1000"))
    _style = os.environ.get("RLTK_HEADER_STYLE", "both")
    print(f"correct rate-limited stub on http://127.0.0.1:{_port} "
          f"(limit={_limit}/{_window}ms, header_style={_style})")
    serve(_port, _limit, _window, _style).serve_forever()
