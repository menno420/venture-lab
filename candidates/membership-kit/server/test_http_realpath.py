"""HTTP-layer real-path tests for the Stripe webhook (ORDER 003).

Unlike test_membership.py (which imports and calls functions directly), these
tests start the ACTUAL server from app.py on an ephemeral port in a background
thread and drive it over REAL HTTP — signing and POSTing the exact bytes of the
VENDORED Stripe fixtures in `fixtures/`. This is the evidence the old 13 tests
could never produce: proof that a real `checkout.session.completed` payload,
with a real Stripe signature, grants membership at the HTTP layer.

Run:  python3 -m unittest test_http_realpath -v
"""
import hashlib
import hmac
import json
import os
import threading
import time
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import app

FIXTURES = Path(__file__).resolve().parent / "fixtures"
REAL_FIXTURE = FIXTURES / "checkout_session_completed.json"
LEGACY_FIXTURE = FIXTURES / "checkout_session_completed_legacy_email.json"

TEST_WEBHOOK_SECRET = "whsec_test_order003"  # fake TEST value — never a real secret


def stripe_signature(raw: bytes, secret: str, ts: int | None = None) -> str:
    """Build a real `Stripe-Signature` header for the given raw body bytes."""
    if ts is None:
        ts = int(time.time())
    signed_payload = f"{ts}.".encode("utf-8") + raw
    v1 = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    return f"t={ts},v1={v1}"


class RealPathHTTPTests(unittest.TestCase):
    def setUp(self) -> None:
        # Isolate env: default to MOCK (no keys). Individual tests opt into a
        # webhook secret as needed.
        for var in ("STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET"):
            os.environ.pop(var, None)

        # Reset the module STORE to a fresh in-memory-ish JsonFileStore backed by
        # a throwaway path, so tests are fully independent and never touch the
        # real server/members.json.
        import tempfile
        fd, self._db_path = tempfile.mkstemp(suffix="-members.json")
        os.close(fd)
        os.unlink(self._db_path)  # start from a non-existent path
        app.STORE = app.JsonFileStore(self._db_path)

        # Start the actual server on 127.0.0.1:0 (ephemeral port) in a thread.
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)
        for var in ("STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET"):
            os.environ.pop(var, None)
        for p in (self._db_path, self._db_path + ".tmp"):
            try:
                os.unlink(p)
            except FileNotFoundError:
                pass

    # ---- HTTP helpers ----
    def _url(self, path: str) -> str:
        return f"http://127.0.0.1:{self.port}{path}"

    def _post(self, path: str, body: bytes, headers: dict | None = None):
        req = urllib.request.Request(
            self._url(path), data=body, method="POST", headers=headers or {},
        )
        try:
            resp = urllib.request.urlopen(req, timeout=5)
            return resp.status, resp.read()
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read()

    def _get(self, path: str):
        req = urllib.request.Request(self._url(path), method="GET")
        try:
            resp = urllib.request.urlopen(req, timeout=5)
            return resp.status, resp.read()
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read()

    # ---- tests ----
    def test_real_event_shape_is_as_vendored(self) -> None:
        """The vendored real fixture has top-level customer_email == null and a
        non-empty customer_details.email. This documents the real shape the whole
        fix depends on — the assertion the old 13 tests could never make."""
        event = json.loads(REAL_FIXTURE.read_bytes())
        obj = event["data"]["object"]
        self.assertIsNone(obj["customer_email"])
        self.assertIsInstance(obj["customer_details"]["email"], str)
        self.assertTrue(obj["customer_details"]["email"])
        self.assertEqual(event["type"], "checkout.session.completed")
        self.assertEqual(obj["object"], "checkout.session")

    def test_webhook_real_payload_valid_signature_grants(self) -> None:
        """Real fixture + valid fresh signature -> HTTP 200, granted, email read
        from customer_details.email."""
        os.environ["STRIPE_WEBHOOK_SECRET"] = TEST_WEBHOOK_SECRET
        raw = REAL_FIXTURE.read_bytes()
        sig = stripe_signature(raw, TEST_WEBHOOK_SECRET, ts=int(time.time()))
        status, body = self._post("/webhook", raw, {"Stripe-Signature": sig})
        self.assertEqual(status, 200)
        payload = json.loads(body)
        self.assertTrue(payload["granted"])
        self.assertEqual(payload["email"], "jenny.rosen@example.com")
        self.assertEqual(payload["mode"], "stripe")
        self.assertTrue(app.STORE.is_member("jenny.rosen@example.com"))

    def test_webhook_bad_signature_rejected(self) -> None:
        """Same payload with a garbage v1 -> HTTP 400 and NOT granted."""
        os.environ["STRIPE_WEBHOOK_SECRET"] = TEST_WEBHOOK_SECRET
        raw = REAL_FIXTURE.read_bytes()
        bad_sig = f"t={int(time.time())},v1=deadbeefdeadbeefdeadbeefdeadbeef"
        status, body = self._post("/webhook", raw, {"Stripe-Signature": bad_sig})
        self.assertEqual(status, 400)
        self.assertIn("invalid signature", json.loads(body)["error"])
        self.assertFalse(app.STORE.is_member("jenny.rosen@example.com"))

    def test_webhook_stale_timestamp_rejected(self) -> None:
        """Valid HMAC but timestamp far outside tolerance -> HTTP 400."""
        os.environ["STRIPE_WEBHOOK_SECRET"] = TEST_WEBHOOK_SECRET
        raw = REAL_FIXTURE.read_bytes()
        stale_ts = int(time.time()) - 10_000  # well beyond the 300s tolerance
        sig = stripe_signature(raw, TEST_WEBHOOK_SECRET, ts=stale_ts)
        status, body = self._post("/webhook", raw, {"Stripe-Signature": sig})
        self.assertEqual(status, 400)
        self.assertIn("tolerance", json.loads(body)["error"])
        self.assertFalse(app.STORE.is_member("jenny.rosen@example.com"))

    def test_webhook_legacy_customer_email_grants(self) -> None:
        """Legacy fixture (top-level customer_email populated) + valid signature
        -> HTTP 200 and granted."""
        os.environ["STRIPE_WEBHOOK_SECRET"] = TEST_WEBHOOK_SECRET
        raw = LEGACY_FIXTURE.read_bytes()
        sig = stripe_signature(raw, TEST_WEBHOOK_SECRET, ts=int(time.time()))
        status, body = self._post("/webhook", raw, {"Stripe-Signature": sig})
        self.assertEqual(status, 200)
        payload = json.loads(body)
        self.assertTrue(payload["granted"])
        self.assertEqual(payload["email"], "guest.buyer@example.com")
        self.assertTrue(app.STORE.is_member("guest.buyer@example.com"))

    def test_members_page_resolves_by_session_id(self) -> None:
        """After a webhook grant, GET /members?session_id=<cs_...> serves the
        members page (200), proving the {CHECKOUT_SESSION_ID} success_url lands a
        buyer — not the 402 not-a-member response."""
        os.environ["STRIPE_WEBHOOK_SECRET"] = TEST_WEBHOOK_SECRET
        raw = REAL_FIXTURE.read_bytes()
        session_id = json.loads(raw)["data"]["object"]["id"]
        sig = stripe_signature(raw, TEST_WEBHOOK_SECRET, ts=int(time.time()))
        status, _ = self._post("/webhook", raw, {"Stripe-Signature": sig})
        self.assertEqual(status, 200)

        status, body = self._get(f"/members?session_id={session_id}")
        self.assertEqual(status, 200)
        self.assertIn(b"access granted", body)  # members.html content
        # And an unknown session id still gets the 402 gate.
        status_unknown, _ = self._get("/members?session_id=cs_test_does_not_exist")
        self.assertEqual(status_unknown, 402)

    def test_mock_mode_loud_warning(self) -> None:
        """With NO webhook secret set, POST the raw fixture JSON to /webhook ->
        200 + the MOCK-mode warning in the response (never a silent success)."""
        # setUp already cleared the secret -> mock mode.
        raw = REAL_FIXTURE.read_bytes()
        status, body = self._post("/webhook", raw, {})
        self.assertEqual(status, 200)
        payload = json.loads(body)
        self.assertEqual(payload["mode"], "mock")
        self.assertIn("warning", payload)
        self.assertIn("MOCK MODE", payload["warning"])
        self.assertTrue(payload["granted"])  # still grants, but loudly flagged

    def test_buyer_landing_route_http(self) -> None:
        """GET / serves the buyer landing page over HTTP (200)."""
        status, body = self._get("/")
        self.assertEqual(status, 200)
        self.assertIn(b"<html", body.lower())


if __name__ == "__main__":
    unittest.main()
