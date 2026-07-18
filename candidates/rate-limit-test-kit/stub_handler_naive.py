#!/usr/bin/env python3
"""Example NAIVE / BROKEN rate-limited endpoint — the mistakes this kit catches.

This handler *looks* like it rate-limits, but it ships the bugs a from-scratch
limiter usually has before the author reads RFC 6585 / the RateLimit draft:

  - OFF-BY-ONE: it allows `limit`+1 requests through before it 429s (it uses
    `count <= limit + 1` instead of `<= limit`). Your "100/hour" limit actually
    lets 101 through — a real, common quota leak.
  - 429 WITH NO Retry-After: when it finally does 429, it sends NO `Retry-After`
    header, so a client has no idea when to retry and either hammers or gives up.
  - INCONSISTENT RateLimit-* HEADERS: it emits `X-RateLimit-Remaining` STUCK at
    the limit (it never decrements — the client can't see itself running out)
    and `X-RateLimit-Reset` as a FIXED timestamp already in the PAST (a stale
    reset copied from a template) — so the advertised reset never arrives.

It DOES reset its window on time, so `under-limit` and `window-reset` pass on
both this stub and the correct one — those two properties do NOT distinguish a
broken limiter from a correct one, and the kit says so honestly (mirrors how the
Idempotency kit's `distinct-keys` property doesn't distinguish its stubs).

It ships in the kit ON PURPOSE so the test suite (test_http_realpath.py) can
DEMONSTRATE that the harness FLAGS the broken behaviour, not only that it passes
a correct one. Against this stub the kit correctly FLAGS:

  - over-limit          : request `limit`+1 is accepted (2xx) instead of 429.
  - retry-after         : the 429 (when it comes, at `limit`+2) has no Retry-After.
  - headers             : Remaining never decrements; Reset is in the past.
  - retry-after-honored : no Retry-After to honour, so a client can't time a retry.

Same debug surface as the correct stub (GET /_debug/state, POST /_debug/reset).

Run standalone:  python3 stub_handler_naive.py 8000
"""
import json
import os
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# A fixed timestamp deliberately in the PAST — the "stale reset" bug. A real
# limiter must compute this fresh each window; copying a constant means the
# advertised reset time has always already passed.
_STALE_RESET_EPOCH = 1_600_000_000  # 2020-09-13 — always in the past


class _NaiveWindow:
    def __init__(self, limit: int, window_ms: int):
        self.limit = limit
        self.window_s = window_ms / 1000.0
        self._lock = threading.Lock()
        self._start = time.monotonic()
        self._count = 0

    def take(self):
        with self._lock:
            now = time.monotonic()
            if now - self._start >= self.window_s:
                self._start = now
                self._count = 0
            self._count += 1
            # THE OFF-BY-ONE BUG: `<= limit + 1` lets one extra request through.
            allowed = self._count <= self.limit + 1
            return allowed

    def state(self):
        with self._lock:
            return {"limit": self.limit, "count": self._count}

    def reset(self):
        with self._lock:
            self._start = time.monotonic()
            self._count = 0


def make_handler(win: _NaiveWindow):
    class Naive(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            if self.path == "/_debug/state":
                self._json(200, win.state(), rate=False)
                return
            self._handle()

        def do_POST(self):
            if self.path == "/_debug/reset":
                win.reset()
                self._json(200, {"ok": True}, rate=False)
                return
            self._handle()

        def _handle(self):
            length = int(self.headers.get("Content-Length", 0))
            if length:
                self.rfile.read(length)
            allowed = win.take()
            if allowed:
                self._json(200, {"id": "req_" + uuid.uuid4().hex, "status": "ok"},
                           rate=True)
            else:
                # BUG: 429 but NO Retry-After header.
                self._json(429, {"error": "rate limit exceeded"}, rate=True)

        def _json(self, code, body, rate):
            data = json.dumps(body).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            if rate:
                # BUG: Remaining STUCK at the limit (never decrements), and
                # Reset is a FIXED timestamp already in the past.
                self.send_header("X-RateLimit-Limit", str(win.limit))
                self.send_header("X-RateLimit-Remaining", str(win.limit))
                self.send_header("X-RateLimit-Reset", str(_STALE_RESET_EPOCH))
            self.end_headers()
            self.wfile.write(data)

    return Naive


def serve(port: int, limit: int = 5, window_ms: int = 1000) -> ThreadingHTTPServer:
    win = _NaiveWindow(limit, window_ms)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(win))
    httpd.limiter = win
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _limit = int(os.environ.get("RLTK_LIMIT", "5"))
    _window = int(os.environ.get("RLTK_WINDOW_MS", "1000"))
    print(f"NAIVE (broken) rate-limited stub on http://127.0.0.1:{_port} — "
          f"the kit should FLAG this one (limit={_limit}/{_window}ms)")
    serve(_port, _limit, _window).serve_forever()
