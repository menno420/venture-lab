#!/usr/bin/env python3
"""Example NAIVE / BROKEN cursor-paginated endpoint — the mistakes this kit catches.

This handler *looks* like it paginates, but it ships the bugs a from-scratch
pager usually has before the author reads the keyset-pagination literature:

  - OFFSET/LIMIT PAGINATION. The "cursor" is just a numeric OFFSET
    (`?cursor=<int>`), so a page is `ORDER BY (created_at, id) LIMIT n OFFSET
    cursor`. When rows are INSERTED or DELETED between page fetches the offset
    window shifts, so items present throughout get SKIPPED or DUPLICATED. This is
    the classic offset-pagination bug and the headline this kit exists to prove.
  - NO OVER-MAX CLAMP. It honours whatever `limit` the client asks for, unbounded
    (it still advertises `X-Page-Size-Max`, copied from a template, but never
    enforces it) — so `?limit=100000` returns the whole table, a cheap DoS.
  - FORGED CURSOR ACCEPTED. A malformed/garbage cursor doesn't 400 — `int()`
    fails and it silently falls back to offset 0, serving page 1. A client (or an
    attacker) that sends junk gets a 200, never the 400 a real cursor API returns.

It DOES traverse correctly in a STATIC dataset (no overlap, no gap), orders
rows consistently, and signals the terminal page — so `traversal`, `ordering`,
and `terminal` PASS on both this stub and the correct one. Those three properties
do NOT distinguish a broken pager from a correct one, and the kit says so honestly
(mirrors how the Rate-Limit kit's `under-limit`/`window-reset` and the
Idempotency kit's `distinct-keys` don't distinguish their stubs).

It ships in the kit ON PURPOSE so the test suite (test_http_realpath.py) can
DEMONSTRATE that the harness FLAGS the broken behaviour, not only that it passes a
correct one. Against this stub the kit correctly FLAGS:

  - stable-under-mutation : deleting a row already returned shifts the offset
                            window, so a later page SKIPS an item present
                            throughout.
  - page-size             : `?limit` over the advertised max is served unbounded
                            (no clamp).
  - cursor-tamper         : a forged/garbage cursor returns 200 (page 1) instead
                            of 400.

Same debug surface as the correct stub (GET /_debug/all, POST /_debug/reset,
POST /_debug/insert, POST /_debug/delete).

Run standalone:  python3 stub_handler_naive.py 8000
"""
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from stub_handler import CANONICAL, _sort_key


class OffsetStore:
    def __init__(self, max_page: int):
        self._lock = threading.Lock()
        self.max_page = max_page  # advertised but NOT enforced (the bug)
        self._rows = [dict(r) for r in CANONICAL]

    def page(self, limit, cursor):
        # THE BUGS: `limit` is used unclamped, and a bad cursor -> offset 0.
        try:
            n = max(1, int(limit))
        except (TypeError, ValueError):
            n = 3
        try:
            offset = max(0, int(cursor)) if cursor not in (None, "") else 0
        except (TypeError, ValueError):
            offset = 0  # forged/garbage cursor silently coerced to page 1
        with self._lock:
            ordered = sorted(self._rows, key=_sort_key)
            window = ordered[offset:offset + n]
            nxt = None
            if offset + n < len(ordered) and window:
                nxt = str(offset + n)  # a plain integer offset — not opaque
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


def make_handler(store: OffsetStore):
    class Naive(BaseHTTPRequestHandler):
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
                # BUG: never 400s a bad cursor; never clamps limit.
                items, nxt = store.page(limit, cursor)
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

    return Naive


def serve(port: int, max_page: int = 5) -> ThreadingHTTPServer:
    store = OffsetStore(max_page)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(store))
    httpd.store = store
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _max = int(os.environ.get("PGTK_MAX", "5"))
    print(f"NAIVE (broken) offset-paginated stub on http://127.0.0.1:{_port} — "
          f"the kit should FLAG this one (max_page={_max}, {len(CANONICAL)} rows)")
    serve(_port, _max).serve_forever()
