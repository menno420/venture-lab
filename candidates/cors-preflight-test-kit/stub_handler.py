#!/usr/bin/env python3
"""Example CORRECT CORS endpoint — stdlib only, ~130 lines.

Reference code you can adapt. It does the things a correct cross-origin server
must (see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the sources — the
WHATWG Fetch Standard "CORS protocol" and MDN's CORS docs).

The contract this handler honours, for an origin ON its allowlist:

  1. PREFLIGHT → 204. A cross-origin OPTIONS with an Origin and an
     Access-Control-Request-Method returns 204 No Content (an ok status), so
     the browser proceeds to the real request.
  2. ALLOW-ORIGIN + VARY. Every CORS response echoes the SPECIFIC request origin
     in Access-Control-Allow-Origin (never `*`, because it also uses
     credentials) and sends `Vary: Origin` so a shared cache never serves one
     origin's Allow-Origin to another.
  3. ALLOW-METHODS. The preflight advertises the methods it permits
     (GET, POST, PUT, DELETE, OPTIONS) via Access-Control-Allow-Methods.
  4. ALLOW-HEADERS. The preflight echoes the browser's requested headers
     (Access-Control-Request-Headers) into Access-Control-Allow-Headers — named
     explicitly, so Authorization is covered (a literal `*` would NOT cover it).
  5. CREDENTIALS DONE RIGHT. Access-Control-Allow-Credentials: true is paired
     with the SPECIFIC origin (not `*`), the only combination browsers accept.
  6. NO OPEN REFLECTION. An origin NOT on the allowlist gets a response with NO
     Access-Control-Allow-* headers at all — the server validates Origin against
     an allowlist instead of blindly reflecting it, so no arbitrary website can
     read authenticated responses.

Real deployments load the allowlist from config and may add Access-Control-
Max-Age tuning; the CONTRACT this models is the same. `cptk` fires a preflight +
actual request at a handler like this.

Run standalone:
    python3 stub_handler.py 8000
Optional env:
    CPTK_ALLOWED_ORIGINS=https://app.example.com,https://admin.example.com
"""
import json
import os
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ALLOWED_METHODS = "GET, POST, PUT, DELETE, OPTIONS"
MAX_AGE = "600"


def make_handler(allowed_origins):
    allowed = set(allowed_origins)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        # ---- preflight ---------------------------------------------------- #
        def do_OPTIONS(self):
            origin = self.headers.get("Origin")
            acrh = self.headers.get("Access-Control-Request-Headers")
            self.send_response(204)
            if origin and origin in allowed:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Vary", "Origin")
                self.send_header("Access-Control-Allow-Methods", ALLOWED_METHODS)
                # Echo the requested headers back, named explicitly (so
                # Authorization is covered — a `*` would not cover it).
                self.send_header("Access-Control-Allow-Headers",
                                 acrh if acrh else "Content-Type, Authorization")
                self.send_header("Access-Control-Allow-Credentials", "true")
                self.send_header("Access-Control-Max-Age", MAX_AGE)
            # A disallowed origin gets NO CORS headers — not a reflected echo.
            self.send_header("Content-Length", "0")
            self.end_headers()

        # ---- actual requests ---------------------------------------------- #
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
                self.rfile.read(length)  # body ignored; this is a CORS test
            origin = self.headers.get("Origin")
            body = json.dumps({"id": "res_" + uuid.uuid4().hex, "status": "ok",
                               "path": self.path}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            if origin and origin in allowed:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Vary", "Origin")
                self.send_header("Access-Control-Allow-Credentials", "true")
            self.end_headers()
            self.wfile.write(body)

    return Handler


def serve(port: int, allowed_origins=None) -> ThreadingHTTPServer:
    if allowed_origins is None:
        allowed_origins = ["https://app.example.com"]
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(allowed_origins))
    httpd.allowed_origins = list(allowed_origins)  # expose for in-process callers/tests
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _origins = [o.strip() for o in
                os.environ.get("CPTK_ALLOWED_ORIGINS", "https://app.example.com").split(",")
                if o.strip()]
    print(f"correct CORS stub on http://127.0.0.1:{_port} (allowlist={_origins})")
    serve(_port, _origins).serve_forever()
