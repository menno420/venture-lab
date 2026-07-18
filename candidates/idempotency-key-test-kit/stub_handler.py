#!/usr/bin/env python3
"""Example CORRECT idempotent endpoint — stdlib only, ~150 lines.

Reference code you can adapt. It does the things a correct `Idempotency-Key`
implementation must (see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the
sources — Stripe's idempotency docs + the IETF draft "The Idempotency-Key HTTP
Header Field"). Behaviour specifics follow Stripe's widely-used model.

The contract this handler honours:

  1. SAFE RETRY. The same `Idempotency-Key` + the same request body triggers the
     side effect EXACTLY ONCE. The replay returns the STORED original response
     (same status + same body) — it does NOT re-execute (no second charge).
  2. KEY REUSE WITH A DIFFERENT BODY IS AN ERROR. The same key with a body whose
     fingerprint differs from the first request is rejected (HTTP 422) — never
     silently returning the old result and never executing a second time.
  3. IN-FLIGHT LOCK. Two concurrent requests with the same key produce ONE side
     effect; the second waits on a per-key lock and then returns the stored
     response (the loser could alternatively get a 409 — this handler replays).
  4. MISSING KEY follows a DOCUMENTED policy (configurable): require it (400) or
     pass through (process without idempotency). Default: require (IKT_REQUIRE_KEY).
  5. KEYS ARE SCOPED PER ENDPOINT. The store is keyed on (METHOD, PATH, key), so
     the same key on POST /charges and POST /orders is two independent effects.

A tiny in-memory store holds, per (method, path, key): the request FINGERPRINT
(sha256 of the raw body) and the stored (status, body). A per-key lock serialises
concurrent same-key requests. A GET /_debug/side_effects counter exposes how many
times the side effect actually ran, so the kit can PROVE "exactly once".

`ikt` fires the scenarios at a handler like this. Run standalone:
    python3 stub_handler.py 8000
Optional env:
    IKT_REQUIRE_KEY=1   # 1 (default) => missing key is 400; 0 => pass-through
    IKT_EXEC_DELAY_MS=0 # simulated work inside the side effect (makes the
                        # in-flight overlap real for the concurrency scenario)
"""
import hashlib
import json
import os
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

IDEMPOTENCY_HEADER = "Idempotency-Key"

# Resource id prefix per endpoint (illustrative — see fixtures/PROVENANCE.md).
_PREFIX = {"/charges": "ch_", "/orders": "or_"}


def _fingerprint(raw: bytes) -> str:
    """The request fingerprint the stored key is bound to: sha256 of the raw
    body bytes. Reusing a key with a body whose fingerprint differs is the
    documented error case (HTTP 422)."""
    return hashlib.sha256(raw).hexdigest()


class IdempotencyStore:
    """In-memory (method, path, key) -> {fingerprint, status, body}, with a
    per-key lock so concurrent same-key requests serialise onto ONE execution.
    A single process, single store — real deployments use Redis/Postgres with a
    TTL; the semantics modelled here are the same (see GOTCHAS.md #5)."""

    def __init__(self):
        self._records = {}                 # (method, path, key) -> record dict
        self._key_locks = {}               # (method, path, key) -> threading.Lock
        self._guard = threading.Lock()     # guards _key_locks + _side_effects
        self._side_effects = 0             # how many times the effect ACTUALLY ran

    def lock_for(self, ident):
        with self._guard:
            lock = self._key_locks.get(ident)
            if lock is None:
                lock = threading.Lock()
                self._key_locks[ident] = lock
            return lock

    def get(self, ident):
        return self._records.get(ident)

    def put(self, ident, record):
        self._records[ident] = record

    def bump_side_effects(self):
        with self._guard:
            self._side_effects += 1
            return self._side_effects

    @property
    def side_effects(self):
        with self._guard:
            return self._side_effects

    def reset(self):
        with self._guard:
            self._records.clear()
            self._key_locks.clear()
            self._side_effects = 0


def _execute_side_effect(store: IdempotencyStore, path: str, payload: dict,
                         delay_ms: int) -> dict:
    """The real work: create a resource EXACTLY ONCE. Increments the counter and
    mints a fresh resource id. A configurable delay simulates real work so the
    in-flight lock has something to serialise over during the concurrency test."""
    store.bump_side_effects()
    if delay_ms > 0:
        time.sleep(delay_ms / 1000.0)
    prefix = _PREFIX.get(path, "obj_")
    return {
        "id": prefix + uuid.uuid4().hex,
        "object": path.strip("/").rstrip("s") or "object",
        "amount": payload.get("amount"),
        "currency": payload.get("currency"),
        "status": "succeeded",
        "created": int(time.time()),
    }


def make_handler(store: IdempotencyStore, require_key: bool, delay_ms: int):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        # ---- debug/inspection surface (the kit uses this to prove exactly-once)
        def do_GET(self):
            if self.path == "/_debug/side_effects":
                self._json(200, {"count": store.side_effects})
                return
            self._json(404, {"error": "not found"})

        def do_POST(self):
            if self.path == "/_debug/reset":
                store.reset()
                self._json(200, {"ok": True})
                return

            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            key = self.headers.get(IDEMPOTENCY_HEADER)

            # (4) Missing key: documented, configurable policy.
            if not key:
                if require_key:
                    self._json(400, {"error": f"{IDEMPOTENCY_HEADER} header required"})
                    return
                # pass-through: process WITHOUT idempotency (each call executes).
                payload = self._parse(raw)
                if payload is None:
                    return
                self._json(200, _execute_side_effect(store, self.path, payload, delay_ms))
                return

            ident = ("POST", self.path, key)
            fingerprint = _fingerprint(raw)

            # (3) In-flight lock: serialise concurrent same-key requests so the
            # side effect happens once and the loser replays the stored response.
            lock = store.lock_for(ident)
            with lock:
                record = store.get(ident)
                if record is not None:
                    # (2) Key reuse with a DIFFERENT body is an error.
                    if record["fingerprint"] != fingerprint:
                        self._json(422, {
                            "error": f"{IDEMPOTENCY_HEADER} reused with a different "
                                     f"request body (idempotency conflict)",
                            "code": "idempotency_key_reuse",
                        })
                        return
                    # (1) Same key + same body: REPLAY the stored response byte
                    # for byte — no second side effect.
                    self._raw(record["status"], record["body"], replayed=True)
                    return

                # First time for this key: parse, execute ONCE, store, return.
                payload = self._parse(raw)
                if payload is None:
                    return
                resp = _execute_side_effect(store, self.path, payload, delay_ms)
                body = json.dumps(resp).encode("utf-8")
                store.put(ident, {"fingerprint": fingerprint, "status": 201, "body": body})
                self._raw(201, body, replayed=False)

        # ---- helpers ----------------------------------------------------- #
        def _parse(self, raw):
            try:
                return json.loads(raw) if raw else {}
            except (ValueError, json.JSONDecodeError) as e:
                self._json(400, {"error": f"unparseable body: {e}"})
                return None

        def _json(self, code, body):
            self._raw(code, json.dumps(body).encode("utf-8"), replayed=False)

        def _raw(self, code, data, replayed):
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            # Advisory: tell the client this was served from the idempotency
            # store (Stripe sends `Idempotent-Replayed: true`). The kit does NOT
            # rely on this header — it proves exactly-once by comparing the
            # response bodies — but a real client can use it.
            self.send_header("Idempotent-Replayed", "true" if replayed else "false")
            self.end_headers()
            self.wfile.write(data)

    return Handler


def serve(port: int, require_key: bool = True, delay_ms: int = 0) -> ThreadingHTTPServer:
    store = IdempotencyStore()
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(store, require_key, delay_ms))
    httpd.store = store  # expose for in-process callers/tests
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _require = os.environ.get("IKT_REQUIRE_KEY", "1") not in ("0", "false", "no", "")
    _delay = int(os.environ.get("IKT_EXEC_DELAY_MS", "0"))
    print(f"correct idempotent stub on http://127.0.0.1:{_port} "
          f"(require_key={_require}, exec_delay_ms={_delay})")
    serve(_port, _require, _delay).serve_forever()
