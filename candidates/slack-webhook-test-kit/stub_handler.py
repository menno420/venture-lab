#!/usr/bin/env python3
"""Example CORRECT Slack request handler — stdlib only, ~120 lines.

Reference code you can adapt. It does the four things a real Slack handler
must (see GOTCHAS.md for the why, fixtures/PROVENANCE.md for the sources):

  1. Read the RAW request body and enforce the timestamp window FIRST:
     reject anything whose X-Slack-Request-Timestamp is more than 300s from
     now (Slack's replay defence). Do this BEFORE trusting the signature.
  2. Verify X-Slack-Signature: recompute v0=HMAC-SHA256(secret,
     "v0:{ts}:{raw_body}") over the RAW bytes and constant-time compare.
     FAIL CLOSED: a missing signature or timestamp header => 400.
  3. Answer a url_verification request by ECHOING its `challenge` value —
     otherwise Slack never verifies your Events API URL.
  4. Only AFTER verifying, parse the body: application/json is the JSON
     document; x-www-form-urlencoded slash commands are flat form fields;
     interactivity nests the JSON in a `payload` field.

`swtk` fires test requests at a handler like this. Run standalone:
    SLACK_SIGNING_SECRET=your_secret python3 stub_handler.py 8000
(the secret is read from the env — never hardcode it).
"""
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REPLAY_WINDOW_SECONDS = 300


def verify_slack_request(raw: bytes, headers, secret: str, now: int = None) -> None:
    """Raise ValueError unless the request is a fresh, correctly-signed Slack
    request. `raw` must be the exact request body bytes as received.

    Order matters: the timestamp window is checked BEFORE the signature, so a
    captured-and-replayed request is rejected on freshness even though its
    signature is still valid.
    """
    now = int(time.time()) if now is None else now
    ts_header = headers.get("X-Slack-Request-Timestamp")
    sig_header = headers.get("X-Slack-Signature")
    if not ts_header or not sig_header:
        raise ValueError("missing X-Slack-Signature or X-Slack-Request-Timestamp header")
    try:
        ts = int(ts_header)
    except ValueError:
        raise ValueError("X-Slack-Request-Timestamp is not an integer")
    if abs(now - ts) > REPLAY_WINDOW_SECONDS:
        raise ValueError(
            f"stale timestamp: {abs(now - ts)}s from now exceeds the "
            f"{REPLAY_WINDOW_SECONDS}s replay window"
        )
    basestring = b"v0:" + str(ts).encode("utf-8") + b":" + raw
    expected = "v0=" + hmac.new(secret.encode("utf-8"), basestring, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig_header):
        raise ValueError("X-Slack-Signature does not match")


def parse_body(raw: bytes, content_type: str):
    """The request payload — AFTER the raw bytes were signature-verified.

    application/json          -> the body IS the JSON document.
    x-www-form-urlencoded:
        interactivity         -> the JSON travels in the `payload` field.
        slash command / etc.  -> flat form fields (a dict of str->str).
    """
    if content_type.startswith("application/x-www-form-urlencoded"):
        fields = urllib.parse.parse_qs(raw.decode("utf-8"))
        if "payload" in fields:  # interactivity
            return json.loads(fields["payload"][0])
        return {k: v[0] for k, v in fields.items()}  # slash command
    return json.loads(raw)


def make_handler(secret: str):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            try:
                verify_slack_request(raw, self.headers, secret)
            except ValueError as e:
                self._json(400, {"error": str(e)})
                return
            content_type = self.headers.get("Content-Type", "")
            try:
                payload = parse_body(raw, content_type)
            except (ValueError, json.JSONDecodeError) as e:
                self._json(400, {"error": f"unparseable body: {e}"})
                return

            # url_verification: echo the challenge or Slack never verifies the URL.
            if isinstance(payload, dict) and payload.get("type") == "url_verification":
                self._text(200, payload.get("challenge", ""))
                return

            # Events API event_callback: ack fast (2xx), process async.
            if isinstance(payload, dict) and payload.get("type") == "event_callback":
                event = payload.get("event", {}) or {}
                self._json(200, {"ok": True, "event_type": event.get("type"),
                                 "event_id": payload.get("event_id")})
                return

            # Interactivity (block_actions etc.) — form-encoded payload=<json>.
            if isinstance(payload, dict) and payload.get("type") == "block_actions":
                actions = payload.get("actions", [])
                self._json(200, {"ok": True, "interaction": "block_actions",
                                 "action_id": actions[0].get("action_id") if actions else None})
                return

            # Slash command — flat form fields carry `command` and `text`.
            if isinstance(payload, dict) and payload.get("command"):
                self._json(200, {"ok": True, "command": payload.get("command"),
                                 "text": payload.get("text", "")})
                return

            self._json(200, {"ok": True})

        def _json(self, code, body):
            data = json.dumps(body).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _text(self, code, body):
            data = body.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Handler


def serve(port: int, secret: str) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(("127.0.0.1", port), make_handler(secret))


if __name__ == "__main__":
    _secret = os.environ.get("SLACK_SIGNING_SECRET")
    if not _secret:
        sys.exit("set SLACK_SIGNING_SECRET — read from env, never hardcoded")
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"stub handler listening on http://127.0.0.1:{_port}")
    serve(_port, _secret).serve_forever()
