#!/usr/bin/env python3
"""HTTP-layer real-path tests for the Shopify Webhook Test Kit.

Discipline (the lane's D1 lesson, carried over from the Stripe/GitHub/Slack
kits): every request is signed with the REAL X-Shopify-Hmac-Sha256 scheme
(base64 HMAC-SHA256 of the raw body) and POSTed over actual HTTP to a handler
running on an ephemeral port — never a payload synthesised from memory, never an
in-process shortcut. The HMAC implementation itself is asserted against a pinned
kit-internal known-answer (Shopify publishes no fixed constant of its own).

Run:  python3 -m unittest -v   (from this directory)
"""
import base64
import binascii
import hashlib
import hmac
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import shwtk
import stub_handler

FIX = Path(__file__).resolve().parent / "fixtures"
# A FAKE test secret — never a real value. Real values live in env, not code.
TEST_SECRET = "shwtk_test_webhook_secret_v0_1_not_a_real_secret"


def _insecure_handler():
    """A handler that does NOT verify signatures — accepts anything. The kit
    must flag this when fired with --forge/--unsigned/--tamper/--malformed."""
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


def _crashing_handler():
    """A handler that mishandles a malformed base64 header — it dies on the bad
    input and drops the connection with no HTTP response (the observable
    behaviour of an unhandled exception in stdlib http.server). The kit's
    --malformed check catches this: a dropped connection is a FAIL, distinct
    from a clean 4xx rejection."""
    class Crashing(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            self.rfile.read(length)
            provided = self.headers.get("X-Shopify-Hmac-Sha256", "")
            try:
                base64.b64decode(provided, validate=True)
            except (binascii.Error, ValueError):
                # No response written + close the socket -> the client sees the
                # connection dropped, exactly as an unhandled 500 would present.
                self.close_connection = True
                return
            body = json.dumps({"ok": True}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    return Crashing


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
        return shwtk.load_fixture(stem)

    def _ct(self, stem):
        return shwtk.content_type_for(stem)

    def _topic(self, stem):
        return shwtk.topic_for(stem)

    # -- the kit-internal known-answer vector --------------------------------- #
    def test_known_answer_vector(self):
        # secret + body -> the pinned base64 constant.
        self.assertEqual(shwtk.shopify_hmac(shwtk.VECTOR_BODY, shwtk.VECTOR_SECRET),
                         shwtk.VECTOR_HMAC)

    def test_signature_matches_independent_hmac(self):
        payload = self._bytes("orders_create")
        header = shwtk.shopify_hmac(payload, TEST_SECRET)
        expected = base64.b64encode(
            hmac.new(TEST_SECRET.encode(), payload, hashlib.sha256).digest()
        ).decode("ascii")
        self.assertEqual(header, expected)

    def test_signature_is_base64_not_hex(self):
        # A hex digest would be 64 lowercase hex chars; base64 of 32 bytes is 44
        # chars ending in '='. Guard against a copy that regressed to hex.
        header = shwtk.shopify_hmac(self._bytes("orders_create"), TEST_SECRET)
        self.assertEqual(len(header), 44)
        self.assertTrue(header.endswith("="))
        self.assertEqual(len(base64.b64decode(header)), 32)

    # -- fixture real-shape assertions ---------------------------------------- #
    def test_manifest_covers_every_fixture(self):
        manifest_stems = set(shwtk.load_manifest().keys())
        on_disk = {p.stem for p in FIX.glob("*.json")}
        on_disk.discard("MANIFEST")
        self.assertEqual(manifest_stems, on_disk)
        self.assertEqual(len(manifest_stems), 3)

    def test_all_fixtures_are_json_with_topic(self):
        for stem in shwtk.list_fixtures():
            self.assertEqual(self._ct(stem), "application/json")
            self.assertIn("/", self._topic(stem))  # e.g. orders/create
            json.loads(self._bytes(stem))  # parses

    def test_orders_create_fixture_shape(self):
        payload = json.loads(self._bytes("orders_create"))
        self.assertEqual(self._topic("orders_create"), "orders/create")
        self.assertIn("id", payload)
        self.assertIn("line_items", payload)

    def test_products_update_fixture_shape(self):
        payload = json.loads(self._bytes("products_update"))
        self.assertEqual(self._topic("products_update"), "products/update")
        self.assertIn("variants", payload)

    def test_app_uninstalled_fixture_shape(self):
        payload = json.loads(self._bytes("app_uninstalled"))
        self.assertEqual(self._topic("app_uninstalled"), "app/uninstalled")
        self.assertIn("myshopify_domain", payload)

    # -- real HTTP: valid webhooks accepted ----------------------------------- #
    def test_valid_signature_accepted_all_fixtures(self):
        url = self._correct_url()
        for stem in shwtk.list_fixtures():
            body, headers = shwtk.build_request(self._bytes(stem), self._ct(stem),
                                                self._topic(stem), secret=TEST_SECRET)
            status, resp = shwtk.post_request(url, body, headers)
            self.assertEqual(status, 200, f"{stem}: HTTP {status} — {resp}")
            self.assertTrue(shwtk.normal_fire_pass(status))

    def test_orders_create_routed_by_topic(self):
        url = self._correct_url()
        body, headers = shwtk.build_request(self._bytes("orders_create"),
                                            self._ct("orders_create"),
                                            self._topic("orders_create"), secret=TEST_SECRET)
        status, resp = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 200)
        data = json.loads(resp)
        self.assertEqual(data["topic"], "orders/create")
        self.assertEqual(data["order_id"], json.loads(self._bytes("orders_create"))["id"])

    def test_app_uninstalled_routed_by_topic(self):
        url = self._correct_url()
        body, headers = shwtk.build_request(self._bytes("app_uninstalled"),
                                            self._ct("app_uninstalled"),
                                            self._topic("app_uninstalled"), secret=TEST_SECRET)
        status, resp = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(resp)["shop_domain"], "example-store.myshopify.com")

    # -- real HTTP: hostile webhooks rejected --------------------------------- #
    def test_forged_signature_rejected(self):
        url = self._correct_url()
        body, headers = shwtk.build_request(self._bytes("orders_create"),
                                            self._ct("orders_create"),
                                            self._topic("orders_create"),
                                            secret=TEST_SECRET, forge=True)
        status, resp = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 401)
        self.assertIn("does not match", resp)

    def test_unsigned_request_rejected(self):
        url = self._correct_url()
        body, headers = shwtk.build_request(self._bytes("orders_create"),
                                            self._ct("orders_create"),
                                            self._topic("orders_create"), secret=None)
        self.assertNotIn(shwtk.HMAC_HEADER, headers)
        status, resp = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 401)
        self.assertIn("missing", resp)

    def test_tampered_body_rejected(self):
        url = self._correct_url()
        raw = self._bytes("orders_create")
        tampered = raw + b" "
        # sign the ORIGINAL body, send the TAMPERED body
        body, headers = shwtk.build_request(tampered, self._ct("orders_create"),
                                            self._topic("orders_create"),
                                            secret=TEST_SECRET, sign_body=raw)
        self.assertEqual(body, tampered)
        status, resp = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 401)
        self.assertIn("does not match", resp)

    def test_malformed_base64_rejected_cleanly(self):
        url = self._correct_url()
        body, headers = shwtk.build_request(self._bytes("orders_create"),
                                            self._ct("orders_create"),
                                            self._topic("orders_create"), malformed=True)
        self.assertEqual(headers[shwtk.HMAC_HEADER], "!!!not-valid-base64!!!")
        status, resp = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 401)  # a clean rejection, NOT a 500 crash
        self.assertIn("not valid base64", resp)

    def test_kit_flags_insecure_handler(self):
        url = self._start(_insecure_handler())
        body, headers = shwtk.build_request(self._bytes("orders_create"),
                                            self._ct("orders_create"),
                                            self._topic("orders_create"),
                                            secret=TEST_SECRET, forge=True)
        status, _ = shwtk.post_request(url, body, headers)
        # insecure handler accepts the forged webhook (2xx) ...
        self.assertTrue(200 <= status < 300)
        # ... and the kit's rejected-fire verdict correctly marks that a FAIL.
        self.assertFalse(shwtk.rejected_fire_pass(status))

    def test_kit_flags_crashing_handler_on_malformed(self):
        # A handler that base64-decodes the header without guarding raises on the
        # malformed input and drops the connection (stdlib http.server sends no
        # 500); post_request returns status 0, which the kit's verdicts mark a
        # FAIL (neither a 2xx accept nor a clean 4xx reject) instead of raising.
        url = self._start(_crashing_handler())
        body, headers = shwtk.build_request(self._bytes("orders_create"),
                                            self._ct("orders_create"),
                                            self._topic("orders_create"), malformed=True)
        status, _ = shwtk.post_request(url, body, headers)
        self.assertEqual(status, 0)
        self.assertFalse(shwtk.rejected_fire_pass(status))
        self.assertFalse(shwtk.normal_fire_pass(status))


if __name__ == "__main__":
    unittest.main(verbosity=2)
