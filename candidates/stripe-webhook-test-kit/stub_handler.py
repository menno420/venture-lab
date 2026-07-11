#!/usr/bin/env python3
"""Example CORRECT Stripe webhook handler — stdlib only, ~60 lines.

This is reference code you can adapt. It does the two things a real handler must:
  1. verify the Stripe-Signature (t=,v1= HMAC-SHA256 over "<ts>.<body>", 300s tolerance)
  2. read the buyer email from customer_details.email, falling back to customer_email

`swtk` fires test events at a handler like this. Run standalone:
    SWTK_WEBHOOK_SECRET=whsec_... python3 stub_handler.py 8000
(the secret is read from the env — never hardcode it).
"""
import hashlib
import hmac
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

TOLERANCE = 300  # seconds — matches stripe-go DefaultTolerance


def verify_signature(raw: bytes, sig_header: str, secret: str, tolerance: int = TOLERANCE) -> None:
    """Raise ValueError if the Stripe-Signature header does not verify `raw`."""
    if not sig_header:
        raise ValueError("missing Stripe-Signature header")
    timestamp = None
    signatures = []
    for part in sig_header.split(","):
        key, sep, value = part.partition("=")
        if not sep:
            continue
        key, value = key.strip(), value.strip()
        if key == "t":
            timestamp = value
        elif key == "v1":
            signatures.append(value)
    if timestamp is None:
        raise ValueError("no timestamp (t=) in Stripe-Signature header")
    if not signatures:
        raise ValueError("no v1 signature in Stripe-Signature header")
    try:
        ts = int(timestamp)
    except ValueError:
        raise ValueError("malformed timestamp in Stripe-Signature header")
    signed_payload = str(ts).encode("utf-8") + b"." + raw
    expected = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    if not any(hmac.compare_digest(expected, sig) for sig in signatures):
        raise ValueError("no matching v1 signature")
    if abs(int(time.time()) - ts) > tolerance:
        raise ValueError(f"timestamp outside tolerance ({tolerance}s)")


def resolve_buyer_email(session_obj: dict):
    details = session_obj.get("customer_details") or {}
    return details.get("email") or session_obj.get("customer_email")


def make_handler(secret: str):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            try:
                verify_signature(raw, self.headers.get("Stripe-Signature", ""), secret)
            except ValueError as e:
                self._json(400, {"error": str(e)})
                return
            event = json.loads(raw)
            obj = event.get("data", {}).get("object", {}) or {}
            email = resolve_buyer_email(obj)
            if event.get("type") == "checkout.session.completed" and not email:
                self._json(422, {"error": "no buyer email on completed checkout"})
                return
            self._json(200, {"received": True, "type": event.get("type"), "buyer_email": email})

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
    _secret = os.environ.get("SWTK_WEBHOOK_SECRET")
    if not _secret:
        sys.exit("set SWTK_WEBHOOK_SECRET (whsec_...) — read from env, never hardcoded")
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"stub handler listening on http://127.0.0.1:{_port}")
    serve(_port, _secret).serve_forever()
