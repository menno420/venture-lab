#!/usr/bin/env python3
"""Example CORRECT cursor-paginated endpoint — stdlib only, ~190 lines.

Reference code you can adapt. It does the things a correct keyset/cursor
paginated API must (see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the
sources — the common keyset-pagination pattern and the Stripe/Slack/GitHub
cursor-pagination docs). A small in-memory dataset with debug hooks so the kit's
mutation test runs fast and deterministically.

The contract this handler honours (`GET /items?limit=N&cursor=<opaque>`):

  1. KEYSET TRAVERSAL. Rows are totally ordered by a stable sort key plus a
     UNIQUE tiebreaker — here `(created_at, id)`. A page returns the next `limit`
     rows *strictly after* the position named by the cursor
     (`WHERE (created_at, id) > (cur_created_at, cur_id)`), so following the
     next-cursor walks the whole ordered set with NO overlap and NO gap;
     concatenating all pages reproduces the set exactly once.
  2. STABLE UNDER MUTATION. Because the cursor names a ROW POSITION (a value in
     the ordered space), not a numeric OFFSET, inserting or deleting rows between
     page fetches does not skip or duplicate the rows present throughout. This is
     the property naive OFFSET/LIMIT pagination fails.
  3. OPAQUE, TAMPER-EVIDENT CURSOR. The cursor is `base64url(payload).base64url(
     hmac_sha256(payload))` — an opaque token the client must not construct or
     edit. A malformed or forged cursor (bad base64, bad JSON, or a bad
     signature) is rejected with **400**, never silently coerced to page 1.
  4. PAGE-SIZE HONORED + CLAMPED. `limit` is honored up to a documented maximum
     (`X-Page-Size-Max`); a request over the max is CLAMPED to the max, never
     served unbounded (an unbounded page is a cheap DoS).
  5. TERMINAL SIGNAL. The final page returns `next_cursor: null`, so a client
     loop terminates instead of spinning forever.

A tiny list-backed store holds the rows; `GET /_debug/all` exposes the ground-
truth ordered ids, `POST /_debug/reset` restores the canonical dataset, and
`POST /_debug/insert` / `POST /_debug/delete` mutate it — so the kit can perform
a controlled mid-traversal mutation and assert set-integrity. Real deployments
back this with a SQL keyset query or a vendor cursor; the externally-visible
CONTRACT this models is the same.

`pgtk` traverses a handler like this. Run standalone:
    python3 stub_handler.py 8000
Optional env:
    PGTK_MAX=5             # documented maximum page size (over-max is clamped)
    PGTK_SECRET=...        # HMAC key for the opaque cursor (demo default if unset)
"""
import base64
import hashlib
import hmac
import json
import os
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

# Canonical demo dataset: 12 rows, totally ordered by (created_at, id). The ties
# at 100 (a1<a2), 110 (c1<c2) and 130 (g1<g2) are deliberate — they are why a
# UNIQUE tiebreaker (the id) is required for a stable total order.
CANONICAL = [
    {"id": "a1", "created_at": 100, "name": "alpha"},
    {"id": "a2", "created_at": 100, "name": "alkaline"},
    {"id": "b1", "created_at": 105, "name": "bravo"},
    {"id": "c1", "created_at": 110, "name": "charlie"},
    {"id": "c2", "created_at": 110, "name": "cobalt"},
    {"id": "d1", "created_at": 115, "name": "delta"},
    {"id": "e1", "created_at": 120, "name": "echo"},
    {"id": "f1", "created_at": 125, "name": "foxtrot"},
    {"id": "g1", "created_at": 130, "name": "golf"},
    {"id": "g2", "created_at": 130, "name": "granite"},
    {"id": "h1", "created_at": 135, "name": "hotel"},
    {"id": "i1", "created_at": 140, "name": "india"},
]

DEFAULT_SECRET = b"pgtk-demo-cursor-key-not-a-secret"


def _sort_key(row):
    return (row["created_at"], row["id"])


class KeysetStore:
    """A list-backed store paginated by keyset on (created_at, id). Thread-safe;
    one lock guards the row list so a concurrent mutation is consistent."""

    def __init__(self, secret: bytes, max_page: int):
        self._lock = threading.Lock()
        self._secret = secret
        self.max_page = max_page
        self._rows = [dict(r) for r in CANONICAL]

    # ---- cursor encode/decode ------------------------------------------- #
    def _sign(self, payload: bytes) -> bytes:
        return hmac.new(self._secret, payload, hashlib.sha256).digest()

    def encode_cursor(self, row) -> str:
        payload = json.dumps({"k": row["created_at"], "id": row["id"]},
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
        sig = self._sign(payload)
        return (_b64(payload) + "." + _b64(sig))

    def decode_cursor(self, token: str):
        """Return (created_at, id) or raise ValueError for a malformed/forged
        cursor. Any tampering (bad base64, bad JSON, or a signature mismatch)
        raises — the handler turns that into a 400."""
        if not token or "." not in token:
            raise ValueError("cursor is not a signed token")
        p_b64, s_b64 = token.split(".", 1)
        payload = _unb64(p_b64)
        sig = _unb64(s_b64)
        expected = self._sign(payload)
        if not hmac.compare_digest(sig, expected):
            raise ValueError("cursor signature mismatch (forged or tampered)")
        obj = json.loads(payload.decode("utf-8"))
        return (obj["k"], obj["id"])

    # ---- pagination ----------------------------------------------------- #
    def page(self, limit: int, cursor: str):
        """Return (items, next_cursor). `limit` is clamped to max_page."""
        n = max(1, min(int(limit), self.max_page))
        with self._lock:
            ordered = sorted(self._rows, key=_sort_key)
            start = 0
            if cursor:
                after = self.decode_cursor(cursor)  # may raise ValueError -> 400
                start = 0
                for i, row in enumerate(ordered):
                    if _sort_key(row) > after:
                        start = i
                        break
                else:
                    start = len(ordered)
            window = ordered[start:start + n]
            nxt = None
            if start + n < len(ordered) and window:
                nxt = self.encode_cursor(window[-1])
            return [dict(r) for r in window], nxt

    def all_ids(self):
        with self._lock:
            return [r["id"] for r in sorted(self._rows, key=_sort_key)]

    def reset(self):
        with self._lock:
            self._rows = [dict(r) for r in CANONICAL]

    def insert(self, row):
        with self._lock:
            self._rows = [r for r in self._rows if r["id"] != row["id"]]
            self._rows.append(dict(row))

    def delete(self, row_id):
        with self._lock:
            before = len(self._rows)
            self._rows = [r for r in self._rows if r["id"] != row_id]
            return len(self._rows) < before


def _b64(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def _unb64(s: str) -> bytes:
    pad = "=" * (-len(s) % 4)
    return base64.urlsafe_b64decode(s + pad)


def make_handler(store: KeysetStore):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            parsed = urlparse(self.path)
            if parsed.path == "/_debug/all":
                self._json(200, {"ids": store.all_ids(), "count": len(store.all_ids())})
                return
            if parsed.path == "/items":
                q = parse_qs(parsed.query)
                limit = q.get("limit", ["3"])[0]
                cursor = q.get("cursor", [""])[0]
                try:
                    lim = int(limit)
                except (TypeError, ValueError):
                    self._json(400, {"error": "limit must be an integer"})
                    return
                try:
                    items, nxt = store.page(lim, cursor)
                except ValueError as e:
                    # (3) a malformed/forged cursor is a 400, never page 1.
                    self._json(400, {"error": "invalid cursor", "detail": str(e)})
                    return
                self._json(200, {"items": items, "next_cursor": nxt},
                           extra={"X-Page-Size-Max": str(store.max_page)})
                return
            self._json(404, {"error": "not found"})

        def do_POST(self):
            parsed = urlparse(self.path)
            body = self._read_body()
            if parsed.path == "/_debug/reset":
                store.reset()
                self._json(200, {"ok": True})
                return
            if parsed.path == "/_debug/insert":
                store.insert(body)
                self._json(200, {"ok": True, "count": len(store.all_ids())})
                return
            if parsed.path == "/_debug/delete":
                ok = store.delete(body.get("id"))
                self._json(200, {"ok": ok, "count": len(store.all_ids())})
                return
            self._json(404, {"error": "not found"})

        # ---- helpers ---------------------------------------------------- #
        def _read_body(self):
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b""
            try:
                return json.loads(raw.decode("utf-8")) if raw else {}
            except (ValueError, UnicodeDecodeError):
                return {}

        def _json(self, code, obj, extra=None):
            data = json.dumps(obj).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(data)

    return Handler


def serve(port: int, max_page: int = 5, secret: bytes = None) -> ThreadingHTTPServer:
    store = KeysetStore(secret or DEFAULT_SECRET, max_page)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(store))
    httpd.store = store  # expose for in-process callers/tests
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _max = int(os.environ.get("PGTK_MAX", "5"))
    _secret = os.environ.get("PGTK_SECRET")
    _sec = _secret.encode("utf-8") if _secret else DEFAULT_SECRET
    print(f"correct cursor-paginated stub on http://127.0.0.1:{_port} "
          f"(max_page={_max}, {len(CANONICAL)} rows, keyset on (created_at, id))")
    serve(_port, _max, _sec).serve_forever()
