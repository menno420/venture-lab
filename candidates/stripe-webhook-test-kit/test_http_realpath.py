#!/usr/bin/env python3
"""HTTP-layer real-path tests for the Stripe Webhook Test Kit.

Discipline (the D1 lesson): every event is signed with the REAL Stripe-Signature
scheme and POSTed over actual HTTP to a handler running on an ephemeral port —
never a payload synthesised from memory, never an in-process shortcut. Fixtures
are read as raw bytes and signed byte-for-byte (fixtures/PROVENANCE.md).

Run:  python3 -m unittest -v   (from this directory)
"""
import json
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import swtk
import stub_handler

FIX = Path(__file__).resolve().parent / "fixtures"
# A FAKE test secret — never a real whsec_ value. Real values live in env, not code.
TEST_SECRET = "whsec_test_swtk_v0_1_not_a_real_secret"


def _insecure_handler():
    """A handler that does NOT verify signatures — accepts anything. The kit must
    flag this when fired with --forge."""
    class Insecure(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            body = json.dumps({"received": True}).encode()
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
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _correct_url(self):
        return self._start(stub_handler.make_handler(TEST_SECRET))

    def _bytes(self, name):
        return (FIX / name).read_bytes()

    # -- fixture real-shape assertions -------------------------------------- #
    def test_checkout_fixture_has_null_top_level_email(self):
        obj = json.loads(self._bytes("checkout_session_completed.json"))["data"]["object"]
        self.assertIsNone(obj["customer_email"])
        self.assertTrue(obj["customer_details"]["email"])
        self.assertEqual(obj["object"], "checkout.session")

    def test_legacy_fixture_uses_top_level_email(self):
        obj = json.loads(self._bytes("checkout_session_completed_legacy_email.json"))["data"]["object"]
        self.assertIsNone(obj["customer_details"])
        self.assertTrue(obj["customer_email"])

    def test_payment_intent_fixture_shape(self):
        ev = json.loads(self._bytes("payment_intent_succeeded.json"))
        self.assertEqual(ev["type"], "payment_intent.succeeded")
        obj = ev["data"]["object"]
        self.assertEqual(obj["object"], "payment_intent")
        self.assertEqual(obj["status"], "succeeded")

    # -- signature scheme --------------------------------------------------- #
    def test_signature_matches_independent_hmac(self):
        import hashlib
        import hmac
        payload = self._bytes("checkout_session_completed.json")
        ts = 1719849600
        header = swtk.stripe_signature(payload, TEST_SECRET, ts)
        parts = dict(p.split("=", 1) for p in header.split(","))
        self.assertEqual(parts["t"], str(ts))
        expected = hmac.new(TEST_SECRET.encode(), f"{ts}.".encode() + payload, hashlib.sha256).hexdigest()
        self.assertEqual(parts["v1"], expected)

    # -- real HTTP: valid / forged / stale ---------------------------------- #
    def test_valid_signature_accepted(self):
        url = self._correct_url()
        payload = self._bytes("checkout_session_completed.json")
        sig = swtk.stripe_signature(payload, TEST_SECRET, int(time.time()))
        status, body = swtk.post_event(url, payload, sig)
        self.assertEqual(status, 200)
        self.assertTrue(swtk.normal_fire_pass(status))
        self.assertEqual(json.loads(body)["buyer_email"], "ada.lovelace@example.com")

    def test_forged_signature_rejected_by_correct_handler(self):
        url = self._correct_url()
        payload = self._bytes("checkout_session_completed.json")
        sig = swtk.stripe_signature(payload, TEST_SECRET + "_WRONG", int(time.time()))
        status, _ = swtk.post_event(url, payload, sig)
        self.assertEqual(status, 400)
        self.assertTrue(swtk.forged_fire_pass(status))

    def test_kit_flags_insecure_handler(self):
        url = self._start(_insecure_handler())
        payload = self._bytes("checkout_session_completed.json")
        sig = swtk.stripe_signature(payload, TEST_SECRET + "_WRONG", int(time.time()))
        status, _ = swtk.post_event(url, payload, sig)
        # insecure handler accepts the forged event (2xx) ...
        self.assertTrue(200 <= status < 300)
        # ... and the kit's forged-fire verdict correctly marks that a FAIL.
        self.assertFalse(swtk.forged_fire_pass(status))

    def test_stale_timestamp_rejected(self):
        url = self._correct_url()
        payload = self._bytes("checkout_session_completed.json")
        sig = swtk.stripe_signature(payload, TEST_SECRET, int(time.time()) - 10_000)
        status, body = swtk.post_event(url, payload, sig)
        self.assertEqual(status, 400)
        self.assertIn("tolerance", body)

    def test_legacy_event_accepted_via_fallback(self):
        url = self._correct_url()
        payload = self._bytes("checkout_session_completed_legacy_email.json")
        sig = swtk.stripe_signature(payload, TEST_SECRET, int(time.time()))
        status, body = swtk.post_event(url, payload, sig)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["buyer_email"], "guest.buyer@example.net")

    def test_payment_intent_event_accepted(self):
        url = self._correct_url()
        payload = self._bytes("payment_intent_succeeded.json")
        sig = swtk.stripe_signature(payload, TEST_SECRET, int(time.time()))
        status, _ = swtk.post_event(url, payload, sig)
        self.assertEqual(status, 200)

    # -- buyer email resolution + url lint ---------------------------------- #
    def test_resolve_email_prefers_customer_details(self):
        obj = json.loads(self._bytes("checkout_session_completed.json"))["data"]["object"]
        email, source = swtk.resolve_buyer_email(obj)
        self.assertEqual(email, "ada.lovelace@example.com")
        self.assertEqual(source, "customer_details.email")

    def test_resolve_email_legacy_fallback(self):
        obj = json.loads(self._bytes("checkout_session_completed_legacy_email.json"))["data"]["object"]
        email, source = swtk.resolve_buyer_email(obj)
        self.assertEqual(email, "guest.buyer@example.net")
        self.assertEqual(source, "customer_email")

    def test_lint_rejects_checkout_email_placeholder(self):
        issues = swtk.lint_success_url("https://x/s?session_id={CHECKOUT_EMAIL}")
        self.assertTrue(any(i["level"] == "error" and "CHECKOUT_EMAIL" in i["msg"] for i in issues))

    def test_lint_accepts_session_id_placeholder(self):
        issues = swtk.lint_success_url("https://x/s?session_id={CHECKOUT_SESSION_ID}")
        self.assertFalse(any(i["level"] == "error" for i in issues))


if __name__ == "__main__":
    unittest.main(verbosity=2)
