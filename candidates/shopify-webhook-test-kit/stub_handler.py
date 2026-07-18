#!/usr/bin/env python3
"""Example CORRECT Shopify webhook handler — stdlib only, ~120 lines.

Reference code you can adapt. It does the things a real Shopify webhook handler
must (see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the sources):

  1. Read the RAW request body — BEFORE any JSON parsing. The HMAC covers the
     exact bytes Shopify sent; a re-serialised copy will not match.
  2. Verify X-Shopify-Hmac-Sha256: it is the BASE64 (not hex) HMAC-SHA256 of the
     raw body, keyed with your app's client secret (the "API secret key" for
     API-created webhooks, or the shared secret shown in the admin). Constant-
     time compare the decoded digest bytes.
  3. FAIL CLOSED: a missing signature header => 401. A header that is not valid
     base64 => 401 (decode defensively — never let bad input 500 you).
  4. Only AFTER verifying, route on the X-Shopify-Topic header (Shopify puts the
     topic in a header, not the body), and ack fast (2xx) so Shopify does not
     retry; dedupe on X-Shopify-Webhook-Id since retries re-send it.

`shwtk` fires test webhooks at a handler like this. Run standalone:
    SHOPIFY_WEBHOOK_SECRET=your_secret python3 stub_handler.py 8000
(the secret is read from the env — never hardcode it).
"""
import base64
import binascii
import hashlib
import hmac
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HMAC_HEADER = "X-Shopify-Hmac-Sha256"
TOPIC_HEADER = "X-Shopify-Topic"
WEBHOOK_ID_HEADER = "X-Shopify-Webhook-Id"


def verify_shopify_request(raw: bytes, headers, secret: str) -> None:
    """Raise ValueError unless the request is a correctly-signed Shopify webhook.
    `raw` must be the exact request body bytes as received (before parsing).

    Shopify's scheme: header X-Shopify-Hmac-Sha256 = base64(HMAC-SHA256(secret,
    raw_body)). There is NO timestamp and NO basestring — the signature is over
    the raw body directly.
    """
    provided = headers.get(HMAC_HEADER)
    if not provided:
        raise ValueError("missing X-Shopify-Hmac-Sha256 header")
    # Decode the provided base64 DEFENSIVELY — a malformed header must become a
    # clean 401, never an unhandled 500.
    try:
        provided_digest = base64.b64decode(provided, validate=True)
    except (binascii.Error, ValueError):
        raise ValueError("X-Shopify-Hmac-Sha256 is not valid base64")
    expected_digest = hmac.new(secret.encode("utf-8"), raw, hashlib.sha256).digest()
    # Constant-time compare on the raw digest bytes.
    if not hmac.compare_digest(provided_digest, expected_digest):
        raise ValueError("X-Shopify-Hmac-Sha256 does not match")


def make_handler(secret: str):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            try:
                verify_shopify_request(raw, self.headers, secret)
            except ValueError as e:
                # 401 Unauthorized is the conventional response for a webhook
                # that fails HMAC verification.
                self._json(401, {"error": str(e)})
                return

            # Only NOW parse the (verified) body.
            try:
                payload = json.loads(raw) if raw else {}
            except (ValueError, json.JSONDecodeError) as e:
                self._json(400, {"error": f"unparseable body: {e}"})
                return

            topic = self.headers.get(TOPIC_HEADER, "")
            webhook_id = self.headers.get(WEBHOOK_ID_HEADER)

            # Route on the TOPIC header (not the body). Ack fast (2xx); do heavy
            # work out-of-band and dedupe on webhook_id since retries re-send it.
            if topic == "orders/create":
                self._json(200, {"ok": True, "topic": topic,
                                 "order_id": payload.get("id"),
                                 "webhook_id": webhook_id})
                return
            if topic == "products/update":
                self._json(200, {"ok": True, "topic": topic,
                                 "product_id": payload.get("id"),
                                 "webhook_id": webhook_id})
                return
            if topic == "app/uninstalled":
                # Clean up the shop's records here — the app is gone.
                self._json(200, {"ok": True, "topic": topic,
                                 "shop_domain": payload.get("myshopify_domain"),
                                 "webhook_id": webhook_id})
                return

            # Any other verified topic: still ack 2xx so Shopify does not retry.
            self._json(200, {"ok": True, "topic": topic, "webhook_id": webhook_id})

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
    _secret = os.environ.get("SHOPIFY_WEBHOOK_SECRET")
    if not _secret:
        sys.exit("set SHOPIFY_WEBHOOK_SECRET — read from env, never hardcoded")
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"stub handler listening on http://127.0.0.1:{_port}")
    serve(_port, _secret).serve_forever()
