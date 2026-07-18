#!/usr/bin/env python3
"""Example NAIVE / BROKEN endpoint — the mistake this kit exists to catch.

This handler IGNORES the `Idempotency-Key` header entirely: every POST executes
the side effect and mints a NEW resource. It is the from-scratch implementation
someone writes before they know the idempotency contract — the "double charge on
a retry" bug in the flesh.

It ships in the kit ON PURPOSE so the test suite (test_http_realpath.py) can
DEMONSTRATE that the harness catches a broken implementation, not only that it
passes a correct one. Against this stub the kit correctly FLAGS:

  - replay   : a retried (same key + same body) request re-executes → a SECOND
               resource id → the harness reports a double side effect.
  - mismatch : the same key with a different body is accepted (2xx) instead of
               rejected (4xx).
  - concurrent: two in-flight same-key requests both execute → two resources.
  - missing-key (required mode): a keyless request is accepted (2xx) instead of
               the documented 400.

It does NOT get flagged on `distinct-keys` — creating a fresh resource for every
request trivially satisfies "two different keys → two effects". That property
does not distinguish correct from naive, and the kit says so honestly.

Same debug surface as the correct stub (GET /_debug/side_effects, POST
/_debug/reset) so the counter can show the over-execution.

Run standalone:  python3 stub_handler_naive.py 8000
"""
import json
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

_PREFIX = {"/charges": "ch_", "/orders": "or_"}


class _Counter:
    def __init__(self):
        self._n = 0
        self._lock = threading.Lock()

    def bump(self):
        with self._lock:
            self._n += 1
            return self._n

    @property
    def value(self):
        with self._lock:
            return self._n

    def reset(self):
        with self._lock:
            self._n = 0


def make_handler(counter: _Counter, delay_ms: int):
    class Naive(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            if self.path == "/_debug/side_effects":
                self._json(200, {"count": counter.value})
                return
            self._json(404, {"error": "not found"})

        def do_POST(self):
            if self.path == "/_debug/reset":
                counter.reset()
                self._json(200, {"ok": True})
                return
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            # THE BUG: the Idempotency-Key header is never read. Every request
            # executes and creates a new resource.
            try:
                payload = json.loads(raw) if raw else {}
            except (ValueError, json.JSONDecodeError) as e:
                self._json(400, {"error": f"unparseable body: {e}"})
                return
            counter.bump()
            if delay_ms > 0:
                time.sleep(delay_ms / 1000.0)
            prefix = _PREFIX.get(self.path, "obj_")
            self._json(201, {
                "id": prefix + uuid.uuid4().hex,
                "object": self.path.strip("/").rstrip("s") or "object",
                "amount": payload.get("amount"),
                "currency": payload.get("currency"),
                "status": "succeeded",
                "created": int(time.time()),
            })

        def _json(self, code, body):
            data = json.dumps(body).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Naive


def serve(port: int, delay_ms: int = 0) -> ThreadingHTTPServer:
    counter = _Counter()
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(counter, delay_ms))
    httpd.store = counter
    return httpd


if __name__ == "__main__":
    import os
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _delay = int(os.environ.get("IKT_EXEC_DELAY_MS", "0"))
    print(f"NAIVE (broken, no-dedup) stub on http://127.0.0.1:{_port} — "
          f"the kit should FLAG this one")
    serve(_port, _delay).serve_forever()
