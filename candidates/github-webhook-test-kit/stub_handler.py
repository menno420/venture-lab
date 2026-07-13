#!/usr/bin/env python3
"""Example CORRECT GitHub webhook handler — stdlib only, ~100 lines.

Reference code you can adapt. It does the five things a real handler must
(see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the sources):

  1. verify X-Hub-Signature-256 (HMAC-SHA256 hex of the RAW request body,
     constant-time compare) and FAIL CLOSED: missing header => 400,
     SHA-1-only => 400 (no downgrade path).
  2. verify the RAW body bytes as received — for form deliveries
     (application/x-www-form-urlencoded) that is the `payload=...` bytes,
     NOT the JSON inside.
  3. route on the X-GitHub-Event HEADER first (the event name is not in the
     payload), then on payload["action"].
  4. answer `ping` with 2xx — it is the first delivery every new webhook gets.
  5. dedupe on X-GitHub-Delivery — GitHub's scheme has no timestamp, so a
     replayed delivery verifies forever; redeliveries reuse the original GUID.

`gwtk` fires test deliveries at a handler like this. Run standalone:
    GWTK_WEBHOOK_SECRET=your_secret python3 stub_handler.py 8000
(the secret is read from the env — never hardcode it).
"""
import hashlib
import hmac
import json
import os
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def verify_signature(raw: bytes, headers, secret: str) -> None:
    """Raise ValueError unless X-Hub-Signature-256 verifies `raw`.

    `raw` must be the exact request body bytes as received. Fail-closed
    rules: a missing sha256 header is an error even if the legacy SHA-1
    header is present and valid (downgrade refusal).
    """
    sig_header = headers.get("X-Hub-Signature-256", "")
    if not sig_header:
        if headers.get("X-Hub-Signature"):
            raise ValueError("only legacy X-Hub-Signature (SHA-1) present — refusing the downgrade; "
                             "GitHub always sends X-Hub-Signature-256 when a secret is set")
        raise ValueError("missing X-Hub-Signature-256 header")
    expected = "sha256=" + hmac.new(secret.encode("utf-8"), raw, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig_header):
        raise ValueError("X-Hub-Signature-256 does not match")


def extract_payload(raw: bytes, content_type: str) -> dict:
    """The event payload dict — AFTER the raw bytes were signature-verified.

    application/json           -> the body IS the JSON document.
    x-www-form-urlencoded      -> the JSON travels in the `payload` field.
    """
    if content_type.startswith("application/x-www-form-urlencoded"):
        fields = urllib.parse.parse_qs(raw.decode("utf-8"))
        docs = fields.get("payload")
        if not docs:
            raise ValueError("form-encoded delivery carries no payload field")
        return json.loads(docs[0])
    return json.loads(raw)


def make_handler(secret: str):
    seen_deliveries = set()  # in-memory GUID dedupe; use durable storage in production

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            try:
                verify_signature(raw, self.headers, secret)
            except ValueError as e:
                self._json(400, {"error": str(e)})
                return
            try:
                payload = extract_payload(raw, self.headers.get("Content-Type", ""))
            except (ValueError, json.JSONDecodeError) as e:
                self._json(400, {"error": f"unparseable payload: {e}"})
                return

            # Route on the HEADER first — the event name is not in the payload.
            event = self.headers.get("X-GitHub-Event", "")
            delivery = self.headers.get("X-GitHub-Delivery", "")

            # Replay/redelivery dedupe: no timestamp exists in GitHub's scheme.
            duplicate = delivery in seen_deliveries
            if delivery:
                seen_deliveries.add(delivery)

            if event == "ping":
                # First delivery every new webhook receives — must 2xx.
                self._json(200, {"pong": True, "zen": payload.get("zen"),
                                 "hook_id": payload.get("hook_id")})
                return

            action = payload.get("action")  # absent on push/ping — that is a real shape
            self._json(200, {
                "received": True,
                "event": event,
                "action": action,
                "delivery": delivery,
                "duplicate": duplicate,  # True => already processed; skip side effects
            })

        def _json(self, code, body):
            data = json.dumps(body).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Handler


def serve(port: int, secret: str) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(("127.0.0.1", port), make_handler(secret))


if __name__ == "__main__":
    _secret = os.environ.get("GWTK_WEBHOOK_SECRET")
    if not _secret:
        sys.exit("set GWTK_WEBHOOK_SECRET — read from env, never hardcoded")
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"stub handler listening on http://127.0.0.1:{_port}")
    serve(_port, _secret).serve_forever()
