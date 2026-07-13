#!/usr/bin/env python3
"""HTTP-layer real-path tests for the GitHub Webhook Test Kit.

Discipline (the lane's D1 lesson, carried over from the Stripe kit): every
delivery is signed with the REAL X-Hub-Signature-256 scheme and POSTed over
actual HTTP to a handler running on an ephemeral port — never a payload
synthesised from memory, never an in-process shortcut. Fixtures are vendored
byte-for-byte from GitHub's own example set and signed byte-for-byte
(fixtures/PROVENANCE.md); the HMAC implementation itself is asserted against
GitHub's OWN published test vector.

Run:  python3 -m unittest -v   (from this directory)
"""
import hashlib
import hmac
import json
import threading
import unittest
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import gwtk
import stub_handler

FIX = Path(__file__).resolve().parent / "fixtures"
# A FAKE test secret — never a real value. Real values live in env, not code.
TEST_SECRET = "gwtk_test_secret_v0_1_not_a_real_secret"


def _insecure_handler():
    """A handler that does NOT verify signatures — accepts anything. The kit
    must flag this when fired with --forge/--unsigned."""
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

    def _signed(self, payload, secret=TEST_SECRET, event="push", delivery="d-1",
                form=False, sha1_only=False):
        return gwtk.build_request("unused", payload, event, delivery,
                                  secret=secret, form=form, sha1_only=sha1_only)

    # -- GitHub's own published test vector ---------------------------------- #
    def test_official_github_vector(self):
        # secret "It's a Secret to Everybody" + payload "Hello, World!" must
        # produce GitHub's documented sha256=757107ea… constant (PROVENANCE.md).
        self.assertEqual(gwtk.hub_signature_256(gwtk.VECTOR_PAYLOAD, gwtk.VECTOR_SECRET),
                         gwtk.VECTOR_SIG_256)

    def test_signature_matches_independent_hmac(self):
        payload = self._bytes("push.json")
        header = gwtk.hub_signature_256(payload, TEST_SECRET)
        expected = hmac.new(TEST_SECRET.encode(), payload, hashlib.sha256).hexdigest()
        self.assertEqual(header, f"sha256={expected}")

    # -- fixture real-shape assertions --------------------------------------- #
    def test_every_fixture_has_an_event_mapping(self):
        events = gwtk.load_events()
        names = {n[:-5] for n in gwtk.list_fixtures()}
        self.assertEqual(names, set(events.keys()))
        self.assertEqual(len(names), 5)

    def test_ping_fixture_shape(self):
        payload = json.loads(self._bytes("ping.json"))
        self.assertIn("zen", payload)
        self.assertIn("hook_id", payload)
        self.assertNotIn("action", payload)  # the routing gotcha, real shape

    def test_push_fixture_shape(self):
        payload = json.loads(self._bytes("push.json"))
        for key in ("ref", "before", "after", "commits", "repository", "pusher"):
            self.assertIn(key, payload)
        self.assertNotIn("action", payload)  # push deliveries carry no action

    def test_pull_request_fixture_shape(self):
        payload = json.loads(self._bytes("pull_request_opened.json"))
        self.assertEqual(payload["action"], "opened")
        self.assertEqual(payload["pull_request"]["state"], "open")
        self.assertEqual(payload["number"], payload["pull_request"]["number"])

    def test_issue_comment_fixture_shape(self):
        payload = json.loads(self._bytes("issue_comment_created.json"))
        self.assertEqual(payload["action"], "created")
        self.assertIn("body", payload["comment"])
        self.assertIn("issue", payload)

    def test_check_run_fixture_shape(self):
        payload = json.loads(self._bytes("check_run_completed.json"))
        self.assertEqual(payload["action"], "completed")
        self.assertEqual(payload["check_run"]["status"], "completed")

    def test_action_values_collide_across_event_types(self):
        # The routing gotcha the kit teaches: "completed"/"created" are not
        # unique to one event type — the header is the only safe router.
        self.assertEqual(json.loads(self._bytes("check_run_completed.json"))["action"],
                         "completed")
        self.assertEqual(json.loads(self._bytes("issue_comment_created.json"))["action"],
                         "created")
        events = gwtk.load_events()
        self.assertNotEqual(events["check_run_completed"], events["issue_comment_created"])

    # -- real HTTP: valid / forged / unsigned / sha1-only --------------------- #
    def test_valid_signature_accepted_all_fixtures(self):
        url = self._correct_url()
        events = gwtk.load_events()
        for stem, event in sorted(events.items()):
            body, headers = self._signed(self._bytes(stem + ".json"),
                                         event=event, delivery=f"d-{stem}")
            status, resp = gwtk.post_delivery(url, body, headers)
            self.assertEqual(status, 200, f"{stem}: HTTP {status}")
            self.assertTrue(gwtk.normal_fire_pass(status))

    def test_forged_signature_rejected_by_correct_handler(self):
        url = self._correct_url()
        body, headers = self._signed(self._bytes("push.json"), secret=TEST_SECRET + "_WRONG")
        status, _ = gwtk.post_delivery(url, body, headers)
        self.assertEqual(status, 400)
        self.assertTrue(gwtk.rejected_fire_pass(status))

    def test_unsigned_delivery_rejected(self):
        url = self._correct_url()
        body, headers = self._signed(self._bytes("push.json"), secret=None)
        self.assertNotIn("X-Hub-Signature-256", headers)
        self.assertNotIn("X-Hub-Signature", headers)
        status, resp = gwtk.post_delivery(url, body, headers)
        self.assertEqual(status, 400)
        self.assertIn("missing X-Hub-Signature-256", resp)

    def test_sha1_only_delivery_rejected(self):
        url = self._correct_url()
        body, headers = self._signed(self._bytes("push.json"), sha1_only=True)
        self.assertNotIn("X-Hub-Signature-256", headers)
        self.assertIn("X-Hub-Signature", headers)  # valid legacy sig IS sent
        status, resp = gwtk.post_delivery(url, body, headers)
        self.assertEqual(status, 400)
        self.assertIn("downgrade", resp)

    def test_kit_flags_insecure_handler(self):
        url = self._start(_insecure_handler())
        body, headers = self._signed(self._bytes("push.json"), secret=TEST_SECRET + "_WRONG")
        status, _ = gwtk.post_delivery(url, body, headers)
        # insecure handler accepts the forged delivery (2xx) ...
        self.assertTrue(200 <= status < 300)
        # ... and the kit's rejected-fire verdict correctly marks that a FAIL.
        self.assertFalse(gwtk.rejected_fire_pass(status))

    # -- ping ------------------------------------------------------------------ #
    def test_ping_answered_2xx(self):
        url = self._correct_url()
        body, headers = self._signed(self._bytes("ping.json"), event="ping")
        status, resp = gwtk.post_delivery(url, body, headers)
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(resp)["pong"])

    # -- form-encoded deliveries ------------------------------------------------ #
    def test_form_encoded_delivery_accepted(self):
        # Signature over the RAW form body (payload=…), exactly as GitHub signs it.
        url = self._correct_url()
        body, headers = self._signed(self._bytes("pull_request_opened.json"),
                                     event="pull_request", form=True)
        self.assertTrue(body.startswith(b"payload="))
        self.assertEqual(headers["Content-Type"], "application/x-www-form-urlencoded")
        status, resp = gwtk.post_delivery(url, body, headers)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(resp)["action"], "opened")

    def test_form_delivery_signed_over_inner_json_rejected(self):
        # The bug class --form exists for: verifying the decoded JSON instead of
        # the raw request bytes. A signature over the inner JSON must NOT verify.
        url = self._correct_url()
        payload = self._bytes("pull_request_opened.json")
        form_body = ("payload=" + urllib.parse.quote_plus(payload.decode("utf-8"))).encode()
        wrong_sig = gwtk.hub_signature_256(payload, TEST_SECRET)  # inner JSON, wrong bytes
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "User-Agent": "GitHub-Hookshot/gwtk",
                   "X-GitHub-Event": "pull_request", "X-GitHub-Delivery": "d-form-wrong",
                   "X-Hub-Signature-256": wrong_sig}
        status, _ = gwtk.post_delivery(url, form_body, headers)
        self.assertEqual(status, 400)

    # -- replay ------------------------------------------------------------------ #
    def test_replay_same_delivery_guid_flagged_duplicate(self):
        # No timestamp in GitHub's scheme: the identical bytes verify again.
        # A correct handler accepts the transport and flags the GUID as seen.
        url = self._correct_url()
        body, headers = self._signed(self._bytes("push.json"), delivery="d-replay-1")
        status1, resp1 = gwtk.post_delivery(url, body, headers)
        status2, resp2 = gwtk.post_delivery(url, body, headers)
        self.assertEqual((status1, status2), (200, 200))
        self.assertFalse(json.loads(resp1)["duplicate"])
        self.assertTrue(json.loads(resp2)["duplicate"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
