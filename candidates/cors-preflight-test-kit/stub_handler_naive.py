#!/usr/bin/env python3
"""Example NAIVE / BROKEN CORS endpoint — the mistakes this kit catches.

This handler *looks* like it does CORS — it even makes the browser's happy path
work for the allowed origin — but it ships the bugs a from-scratch CORS config
usually has before the author reads the Fetch standard:

  - REFLECTS ANY ORIGIN: it copies whatever `Origin` the caller sent straight
    into `Access-Control-Allow-Origin`, with `Access-Control-Allow-Credentials:
    true`. That is OPEN CORS — any website on the internet can make a
    credentialed request and read the authenticated response. The single most
    dangerous CORS misconfiguration.
  - NO `Vary: Origin`: because it echoes a per-origin value without `Vary:
    Origin`, a shared cache can serve one origin's `Allow-Origin` header to a
    different origin, breaking (or leaking) CORS for everyone behind the cache.
  - PREFLIGHT OMITS `Access-Control-Allow-Methods` AND
    `Access-Control-Allow-Headers`: the "I set Allow-Origin and thought that was
    all" bug. A real non-simple request (a JSON POST, or anything with an
    Authorization header) is blocked by the browser because the preflight never
    said the method/headers were allowed.

It DOES return an ok (204) preflight status and DOES pair credentials with the
specific (reflected) origin rather than `*`, so `preflight-status` and
`credentials` pass on both this stub and the correct one — those two properties
do NOT distinguish a broken config from a correct one, and the kit says so
honestly (mirrors how the rate-limit kit's `under-limit`/`window-reset` and the
pagination kit's `traversal`/`ordering` don't distinguish their stubs).

It ships in the kit ON PURPOSE so the test suite (test_http_realpath.py) can
DEMONSTRATE that the harness FLAGS the broken behaviour, not only that it passes
a correct one. Against this stub the kit correctly FLAGS:

  - allow-origin   : echoes the origin but sends NO `Vary: Origin`.
  - allow-methods  : the preflight has no `Access-Control-Allow-Methods`.
  - allow-headers  : the preflight has no `Access-Control-Allow-Headers`.
  - reflect-guard  : it reflects a disallowed probe origin (open CORS).

Run standalone:  python3 stub_handler_naive.py 8000
"""
import json
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def make_handler():
    class Naive(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_OPTIONS(self):
            origin = self.headers.get("Origin")
            self.send_response(204)
            if origin:
                # BUG: reflects ANY origin, with credentials, and NO Vary, and
                # NO Allow-Methods / Allow-Headers on the preflight.
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Access-Control-Allow-Credentials", "true")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def do_GET(self):
            self._actual()

        def do_POST(self):
            self._actual()

        def do_PUT(self):
            self._actual()

        def do_DELETE(self):
            self._actual()

        def _actual(self):
            length = int(self.headers.get("Content-Length", 0))
            if length:
                self.rfile.read(length)
            origin = self.headers.get("Origin")
            body = json.dumps({"id": "res_" + uuid.uuid4().hex, "status": "ok"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            if origin:
                # BUG: same open reflection + credentials, no Vary.
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Access-Control-Allow-Credentials", "true")
            self.end_headers()
            self.wfile.write(body)

    return Naive


def serve(port: int) -> ThreadingHTTPServer:
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler())
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"NAIVE (broken) CORS stub on http://127.0.0.1:{_port} — "
          f"the kit should FLAG this one (reflects any origin, no Vary, no Allow-Methods/Headers)")
    serve(_port).serve_forever()
