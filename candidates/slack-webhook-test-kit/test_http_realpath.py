#!/usr/bin/env python3
"""HTTP-layer real-path tests for the Slack Webhook Test Kit.

Discipline (the lane's D1 lesson, carried over from the Stripe/GitHub kits):
every request is signed with the REAL X-Slack-Signature v0 scheme and POSTed
over actual HTTP to a handler running on an ephemeral port — never a payload
synthesised from memory, never an in-process shortcut. The HMAC implementation
itself is asserted against Slack's OWN published worked example.

Run:  python3 -m unittest -v   (from this directory)
"""
import hashlib
import hmac
import json
import threading
import time
import unittest
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import swtk
import stub_handler

FIX = Path(__file__).resolve().parent / "fixtures"
# A FAKE test secret — never a real value. Real values live in env, not code.
TEST_SECRET = "swtk_test_signing_secret_v0_1_not_a_real_secret"


def _insecure_handler():
    """A handler that does NOT verify signatures — accepts anything. The kit
    must flag this when fired with --forge/--unsigned/--stale/--tamper."""
    class Insecure(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            body = json.dumps({"ok": True}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    return Insecure


class RealPathTests(unittest.TestCase):
    def _start(self, handler_cls):
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler_cls)
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _correct_url(self):
        return self._start(stub_handler.make_handler(TEST_SECRET))

    def _bytes(self, stem):
        return swtk.load_fixture(stem)

    def _ct(self, stem):
        return swtk.content_type_for(stem)

    # -- Slack's own published worked example --------------------------------- #
    def test_official_slack_vector(self):
        # secret 8f742231…, timestamp 1531420618, the documented slash-command
        # body must produce Slack's published v0=a2114d57… constant.
        self.assertEqual(
            swtk.slack_signature(swtk.VECTOR_BODY, swtk.VECTOR_SECRET, swtk.VECTOR_TIMESTAMP),
            swtk.VECTOR_SIGNATURE,
        )

    def test_slash_command_fixture_reproduces_vector(self):
        # The vendored slash_command fixture IS Slack's worked-example body, so
        # signing it with the documented secret+timestamp yields the constant.
        body = self._bytes("slash_command")
        self.assertEqual(body, swtk.VECTOR_BODY)
        self.assertEqual(
            swtk.slack_signature(body, swtk.VECTOR_SECRET, swtk.VECTOR_TIMESTAMP),
            swtk.VECTOR_SIGNATURE,
        )

    def test_signature_matches_independent_hmac(self):
        payload = self._bytes("event_callback_app_mention")
        ts = 1600000000
        header = swtk.slack_signature(payload, TEST_SECRET, ts)
        basestring = b"v0:" + str(ts).encode() + b":" + payload
        expected = hmac.new(TEST_SECRET.encode(), basestring, hashlib.sha256).hexdigest()
        self.assertEqual(header, "v0=" + expected)

    # -- fixture real-shape assertions ---------------------------------------- #
    def test_manifest_covers_every_fixture(self):
        manifest_stems = set(swtk.load_manifest().keys())
        on_disk = {p.stem for p in FIX.glob("*.json")} | {p.stem for p in FIX.glob("*.txt")}
        on_disk.discard("MANIFEST")
        self.assertEqual(manifest_stems, on_disk)
        self.assertEqual(len(manifest_stems), 4)

    def test_url_verification_fixture_shape(self):
        payload = json.loads(self._bytes("url_verification"))
        self.assertEqual(payload["type"], "url_verification")
        self.assertIn("challenge", payload)

    def test_event_callback_fixture_shape(self):
        payload = json.loads(self._bytes("event_callback_app_mention"))
        self.assertEqual(payload["type"], "event_callback")
        self.assertEqual(payload["event"]["type"], "app_mention")
        self.assertIn("event_id", payload)

    def test_slash_command_fixture_is_flat_form(self):
        raw = self._bytes("slash_command")
        self.assertFalse(raw.startswith(b"payload="))
        fields = urllib.parse.parse_qs(raw.decode())
        self.assertEqual(fields["command"][0], "/webhook-collect")

    def test_interactive_fixture_is_payload_wrapped(self):
        raw = self._bytes("interactive_block_actions")
        self.assertTrue(raw.startswith(b"payload="))
        inner = json.loads(urllib.parse.parse_qs(raw.decode())["payload"][0])
        self.assertEqual(inner["type"], "block_actions")
        self.assertEqual(inner["actions"][0]["action_id"], "approve_button")

    # -- real HTTP: valid requests accepted ----------------------------------- #
    def test_valid_signature_accepted_all_fixtures(self):
        url = self._correct_url()
        for stem in swtk.list_fixtures():
            body, headers = swtk.build_request(self._bytes(stem), self._ct(stem), secret=TEST_SECRET)
            status, resp = swtk.post_request(url, body, headers)
            self.assertEqual(status, 200, f"{stem}: HTTP {status} — {resp}")
            self.assertTrue(swtk.normal_fire_pass(status))

    def test_url_verification_echoes_challenge(self):
        url = self._correct_url()
        raw = self._bytes("url_verification")
        body, headers = swtk.build_request(raw, self._ct("url_verification"), secret=TEST_SECRET)
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 200)
        self.assertEqual(resp, json.loads(raw)["challenge"])  # echoed verbatim

    def test_slash_command_accepted_and_parsed(self):
        url = self._correct_url()
        body, headers = swtk.build_request(self._bytes("slash_command"),
                                           self._ct("slash_command"), secret=TEST_SECRET)
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(resp)["command"], "/webhook-collect")

    def test_interactive_accepted_and_parsed(self):
        url = self._correct_url()
        body, headers = swtk.build_request(self._bytes("interactive_block_actions"),
                                           self._ct("interactive_block_actions"), secret=TEST_SECRET)
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(resp)["action_id"], "approve_button")

    # -- real HTTP: hostile requests rejected --------------------------------- #
    def test_forged_signature_rejected(self):
        url = self._correct_url()
        body, headers = swtk.build_request(self._bytes("event_callback_app_mention"),
                                           self._ct("event_callback_app_mention"),
                                           secret=TEST_SECRET, forge=True)
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 400)
        self.assertIn("does not match", resp)

    def test_unsigned_request_rejected(self):
        url = self._correct_url()
        body, headers = swtk.build_request(self._bytes("event_callback_app_mention"),
                                           self._ct("event_callback_app_mention"), secret=None)
        self.assertNotIn("X-Slack-Signature", headers)
        self.assertNotIn("X-Slack-Request-Timestamp", headers)
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 400)
        self.assertIn("missing", resp)

    def test_stale_timestamp_rejected_even_though_signature_valid(self):
        url = self._correct_url()
        old_ts = int(time.time()) - 3600
        raw = self._bytes("event_callback_app_mention")
        body, headers = swtk.build_request(raw, self._ct("event_callback_app_mention"),
                                           secret=TEST_SECRET, timestamp=old_ts)
        # the signature IS valid for that (old) timestamp ...
        basestring = b"v0:" + str(old_ts).encode() + b":" + raw
        expected = "v0=" + hmac.new(TEST_SECRET.encode(), basestring, hashlib.sha256).hexdigest()
        self.assertEqual(headers["X-Slack-Signature"], expected)
        # ... yet the handler rejects it on the replay window.
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 400)
        self.assertIn("stale timestamp", resp)

    def test_tampered_body_rejected(self):
        url = self._correct_url()
        raw = self._bytes("event_callback_app_mention")
        tampered = raw + b" "
        # sign the ORIGINAL body, send the TAMPERED body
        body, headers = swtk.build_request(tampered, self._ct("event_callback_app_mention"),
                                           secret=TEST_SECRET, sign_body=raw)
        self.assertEqual(body, tampered)
        status, resp = swtk.post_request(url, body, headers)
        self.assertEqual(status, 400)
        self.assertIn("does not match", resp)

    def test_kit_flags_insecure_handler(self):
        url = self._start(_insecure_handler())
        body, headers = swtk.build_request(self._bytes("event_callback_app_mention"),
                                           self._ct("event_callback_app_mention"),
                                           secret=TEST_SECRET, forge=True)
        status, _ = swtk.post_request(url, body, headers)
        # insecure handler accepts the forged request (2xx) ...
        self.assertTrue(200 <= status < 300)
        # ... and the kit's rejected-fire verdict correctly marks that a FAIL.
        self.assertFalse(swtk.rejected_fire_pass(status))

    def test_insecure_handler_accepts_stale(self):
        # An insecure handler that doesn't enforce the window accepts a replay.
        url = self._start(_insecure_handler())
        old_ts = int(time.time()) - 3600
        body, headers = swtk.build_request(self._bytes("event_callback_app_mention"),
                                           self._ct("event_callback_app_mention"),
                                           secret=TEST_SECRET, timestamp=old_ts)
        status, _ = swtk.post_request(url, body, headers)
        self.assertTrue(200 <= status < 300)
        self.assertFalse(swtk.rejected_fire_pass(status))


if __name__ == "__main__":
    unittest.main(verbosity=2)
