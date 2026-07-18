#!/usr/bin/env python3
"""HTTP-layer real-path tests for the JWT Auth Test Kit.

Discipline (carried over from the webhook + idempotency + rate-limit + pagination
kits): every request is fired over actual HTTP to a handler running on an
ephemeral port — never an in-process shortcut. Two reference stubs are exercised:

  - the CORRECT stub (stub_handler.py: pins an alg allowlist, verifies the HS256
    signature, and enforces exp/nbf/aud/iss): the harness reports all nine
    properties PASS.
  - the NAIVE stub (stub_handler_naive.py: accepts alg:none, is vulnerable to
    algorithm-confusion, and skips exp/nbf/aud/iss): the harness correctly FLAGS
    alg-none / alg-confusion / expired / not-yet-valid / audience / issuer, and
    (honestly) does NOT flag valid-accepted / signature / malformed — those three
    don't distinguish the stubs, and the kit says so. This is the value proof.

All time claims are fixed offsets from the real clock (±1h), so no test waits on a
real clock and the whole suite runs in well under a second.

Run:  python3 -m unittest -v   (from this directory)
"""
import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path

import jatk
import stub_handler
import stub_handler_naive

FIXTURE = "hs256_bearer"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


class _ServerCase(unittest.TestCase):
    def _start(self, httpd: ThreadingHTTPServer) -> str:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _spec(self):
        return jatk.AuthSpec.from_fixture(FIXTURE)

    def _secret(self):
        return jatk.DEFAULT_SECRET

    def _pubkey(self):
        return jatk.load_pubkey()

    def _correct(self, aud="jatk-demo-api", iss="jatk-demo-issuer"):
        return self._start(stub_handler.serve(0, expected_aud=aud, expected_iss=iss))

    def _naive(self):
        return self._start(stub_handler_naive.serve(0))


# --------------------------------------------------------------------------- #
# Fixtures + manifest real-shape assertions
# --------------------------------------------------------------------------- #
class FixtureTests(_ServerCase):
    def test_manifest_parses_and_has_two_config_stems(self):
        manifest = jatk.load_manifest()
        self.assertEqual(set(manifest), {"hs256_bearer", "hs256_no_claims"})

    def test_every_manifest_entry_has_the_required_keys(self):
        for stem, entry in jatk.load_manifest().items():
            spec = jatk.AuthSpec.from_fixture(stem)
            self.assertTrue(spec.path.startswith("/"), stem)
            self.assertTrue(spec.auth_scheme, stem)
            self.assertTrue(spec.subject, stem)

    def test_default_fixture_matches_the_stub(self):
        spec = jatk.AuthSpec.from_fixture("hs256_bearer")
        self.assertEqual(spec.path, "/protected")
        self.assertEqual(spec.expected_aud, "jatk-demo-api")
        self.assertEqual(spec.expected_iss, "jatk-demo-issuer")

    def test_no_claims_fixture_disables_aud_and_iss(self):
        spec = jatk.AuthSpec.from_fixture("hs256_no_claims")
        self.assertIsNone(spec.expected_aud)
        self.assertIsNone(spec.expected_iss)

    def test_public_key_fixture_is_a_pem(self):
        pem = self._pubkey()
        self.assertIn(b"-----BEGIN PUBLIC KEY-----", pem)
        self.assertIn(b"-----END PUBLIC KEY-----", pem)

    def test_sample_tokens_fixture_parses_and_tokens_are_three_segments(self):
        obj = json.loads((FIXTURES / "sample_tokens.json").read_text(encoding="utf-8"))
        toks = obj["tokens"]
        # every non-malformed sample token has exactly three segments
        for name, tok in toks.items():
            if name.startswith("malformed_"):
                continue
            self.assertEqual(tok.count("."), 2, name)


# --------------------------------------------------------------------------- #
# Token-minting unit coverage
# --------------------------------------------------------------------------- #
class MintTests(unittest.TestCase):
    def setUp(self):
        self.spec = jatk.AuthSpec.from_fixture(FIXTURE)
        self.secret = jatk.DEFAULT_SECRET
        self.pubkey = jatk.load_pubkey()
        self.tokens = jatk.attack_tokens(self.spec, self.secret, self.pubkey, now=1_800_000_000)

    def test_valid_token_verifies_against_the_secret(self):
        claims = stub_handler.verify_jwt(self.tokens["valid"], self.secret,
                                         self.spec.expected_aud, self.spec.expected_iss,
                                         now=1_800_000_000)
        self.assertEqual(claims["sub"], self.spec.subject)

    def test_alg_none_token_has_empty_signature_and_none_header(self):
        h, p, s = self.tokens["alg_none"].split(".")
        self.assertEqual(s, "")
        header = json.loads(stub_handler.b64url_decode(h))
        self.assertEqual(header["alg"], "none")

    def test_confusion_token_is_signed_with_the_public_key_bytes(self):
        # It verifies as an HMAC under the PUBLIC key, not the secret.
        import hashlib
        import hmac
        h, p, s = self.tokens["confusion"].split(".")
        signing_input = (h + "." + p).encode("ascii")
        expect = hmac.new(self.pubkey, signing_input, hashlib.sha256).digest()
        self.assertEqual(stub_handler.b64url_decode(s), expect)

    def test_wrong_key_token_does_not_verify_against_the_secret(self):
        with self.assertRaises(stub_handler.JWTError):
            stub_handler.verify_jwt(self.tokens["wrong_key"], self.secret,
                                    self.spec.expected_aud, self.spec.expected_iss,
                                    now=1_800_000_000)

    def test_malformed_tokens_are_not_three_valid_segments(self):
        self.assertNotEqual(self.tokens["malformed_twoseg"].count("."), 2)
        self.assertEqual(self.tokens["malformed_fourseg"].count("."), 3)


# --------------------------------------------------------------------------- #
# verify_jwt direct unit coverage (the reference verifier)
# --------------------------------------------------------------------------- #
class VerifyJwtTests(unittest.TestCase):
    def setUp(self):
        self.spec = jatk.AuthSpec.from_fixture(FIXTURE)
        self.secret = jatk.DEFAULT_SECRET
        self.pubkey = jatk.load_pubkey()
        self.now = 1_800_000_000
        self.tokens = jatk.attack_tokens(self.spec, self.secret, self.pubkey, now=self.now)

    def _reason(self, key):
        with self.assertRaises(stub_handler.JWTError) as cm:
            stub_handler.verify_jwt(self.tokens[key], self.secret,
                                    self.spec.expected_aud, self.spec.expected_iss, now=self.now)
        return cm.exception.reason

    def test_alg_none_reason(self):
        self.assertEqual(self._reason("alg_none"), "alg_none")

    def test_confusion_is_a_bad_signature_for_a_pinned_verifier(self):
        self.assertEqual(self._reason("confusion"), "bad_signature")

    def test_expired_reason(self):
        self.assertEqual(self._reason("expired"), "expired")

    def test_not_yet_valid_reason(self):
        self.assertEqual(self._reason("not_yet_valid"), "not_yet_valid")

    def test_bad_audience_reason(self):
        self.assertEqual(self._reason("wrong_aud"), "bad_audience")
        self.assertEqual(self._reason("missing_aud"), "bad_audience")

    def test_bad_issuer_reason(self):
        self.assertEqual(self._reason("wrong_iss"), "bad_issuer")
        self.assertEqual(self._reason("missing_iss"), "bad_issuer")

    def test_malformed_reasons(self):
        for k in ("malformed_notjwt", "malformed_twoseg", "malformed_fourseg", "malformed_badb64"):
            self.assertEqual(self._reason(k), "malformed", k)

    def test_naive_verify_accepts_the_confusion_token(self):
        # The exact bypass the kit exists to catch: the naive verifier HMACs the
        # token against the public key and accepts it.
        claims = stub_handler_naive.naive_verify(self.tokens["confusion"], self.secret, self.pubkey)
        self.assertEqual(claims["sub"], self.spec.subject)

    def test_naive_verify_accepts_alg_none(self):
        claims = stub_handler_naive.naive_verify(self.tokens["alg_none"], self.secret, self.pubkey)
        self.assertEqual(claims["sub"], self.spec.subject)


# --------------------------------------------------------------------------- #
# CORRECT stub — every property passes
# --------------------------------------------------------------------------- #
class CorrectStubTests(_ServerCase):
    def _run(self, name):
        url = self._correct()
        return jatk.CHECKS_BY_NAME[name](url, self._spec(), self._secret(), self._pubkey())

    def test_valid_accepted(self):
        passed, detail = self._run("valid-accepted")
        self.assertTrue(passed, detail)

    def test_alg_none_rejected(self):
        passed, detail = self._run("alg-none-rejected")
        self.assertTrue(passed, detail)

    def test_signature_rejected(self):
        passed, detail = self._run("signature-rejected")
        self.assertTrue(passed, detail)

    def test_alg_confusion_rejected(self):
        passed, detail = self._run("alg-confusion-rejected")
        self.assertTrue(passed, detail)

    def test_expired_rejected(self):
        passed, detail = self._run("expired-rejected")
        self.assertTrue(passed, detail)

    def test_not_yet_valid_rejected(self):
        passed, detail = self._run("not-yet-valid-rejected")
        self.assertTrue(passed, detail)

    def test_audience_enforced(self):
        passed, detail = self._run("audience-enforced")
        self.assertTrue(passed, detail)

    def test_issuer_enforced(self):
        passed, detail = self._run("issuer-enforced")
        self.assertTrue(passed, detail)

    def test_malformed_rejected(self):
        passed, detail = self._run("malformed-rejected")
        self.assertTrue(passed, detail)

    def test_valid_token_returns_200_over_http(self):
        url = self._correct()
        spec = self._spec()
        tokens = jatk.attack_tokens(spec, self._secret(), self._pubkey(), __import__("time").time())
        status, _b = jatk.fire_token(url, spec, tokens["valid"])
        self.assertEqual(status, 200)

    def test_each_attack_returns_401_over_http(self):
        url = self._correct()
        spec = self._spec()
        tokens = jatk.attack_tokens(spec, self._secret(), self._pubkey(), __import__("time").time())
        for key in ("alg_none", "tampered", "wrong_key", "confusion", "expired",
                    "not_yet_valid", "wrong_aud", "missing_aud", "wrong_iss", "missing_iss",
                    "malformed_notjwt", "malformed_twoseg", "malformed_fourseg", "malformed_badb64"):
            status, _b = jatk.fire_token(url, spec, tokens[key])
            self.assertEqual(status, 401, f"{key} should be 401, got {status}")

    def test_missing_bearer_is_401(self):
        url = self._correct()
        status, _b = jatk.fire(url, "GET", "/protected")
        self.assertEqual(status, 401)

    def test_full_suite_green_against_correct_stub(self):
        url = self._correct()
        failures = jatk.run_suite(url, self._spec(), self._secret(), self._pubkey())
        self.assertEqual(failures, 0)


# --------------------------------------------------------------------------- #
# NAIVE stub — the kit FLAGS the bypasses (the value proof)
# --------------------------------------------------------------------------- #
class NaiveStubTests(_ServerCase):
    def _run(self, name):
        url = self._naive()
        return jatk.CHECKS_BY_NAME[name](url, self._spec(), self._secret(), self._pubkey())

    def test_kit_flags_alg_none(self):
        passed, detail = self._run("alg-none-rejected")
        self.assertFalse(passed, "kit should FLAG the alg:none accept")
        self.assertIn("ACCEPTED", detail)

    def test_kit_flags_algorithm_confusion(self):
        passed, detail = self._run("alg-confusion-rejected")
        self.assertFalse(passed, "kit should FLAG the confusion accept")
        self.assertIn("ACCEPTED", detail)

    def test_kit_flags_expired(self):
        passed, detail = self._run("expired-rejected")
        self.assertFalse(passed)

    def test_kit_flags_not_yet_valid(self):
        passed, detail = self._run("not-yet-valid-rejected")
        self.assertFalse(passed)

    def test_kit_flags_audience(self):
        passed, detail = self._run("audience-enforced")
        self.assertFalse(passed)

    def test_kit_flags_issuer(self):
        passed, detail = self._run("issuer-enforced")
        self.assertFalse(passed)

    def test_valid_accepted_still_passes_on_naive(self):
        passed, _ = self._run("valid-accepted")
        self.assertTrue(passed)

    def test_signature_still_rejected_on_naive(self):
        # tampered + wrong-key match NEITHER the secret NOR the public key -> rejected.
        passed, _ = self._run("signature-rejected")
        self.assertTrue(passed)

    def test_malformed_still_rejected_on_naive(self):
        passed, _ = self._run("malformed-rejected")
        self.assertTrue(passed)

    def test_full_suite_flags_exactly_six(self):
        url = self._naive()
        failures = jatk.run_suite(url, self._spec(), self._secret(), self._pubkey())
        # alg-none + alg-confusion + expired + not-yet-valid + audience + issuer = 6;
        # valid-accepted + signature + malformed pass.
        self.assertEqual(failures, 6)


# --------------------------------------------------------------------------- #
# SKIP paths — aud/iss not configured, and confusion without a pubkey
# --------------------------------------------------------------------------- #
class SkipPathTests(_ServerCase):
    def test_audience_and_issuer_skip_when_not_configured(self):
        # A correct stub that enforces NO aud/iss, driven by the no-claims fixture.
        url = self._start(stub_handler.serve(0, expected_aud="", expected_iss=""))
        spec = jatk.AuthSpec.from_fixture("hs256_no_claims")
        aud_passed, aud_detail = jatk.check_audience_enforced(url, spec, self._secret(), self._pubkey())
        iss_passed, iss_detail = jatk.check_issuer_enforced(url, spec, self._secret(), self._pubkey())
        self.assertIsNone(aud_passed, aud_detail)
        self.assertIsNone(iss_passed, iss_detail)
        self.assertIn("SKIP", aud_detail)
        self.assertIn("SKIP", iss_detail)

    def test_no_claims_valid_token_is_accepted(self):
        url = self._start(stub_handler.serve(0, expected_aud="", expected_iss=""))
        spec = jatk.AuthSpec.from_fixture("hs256_no_claims")
        passed, detail = jatk.check_valid_accepted(url, spec, self._secret(), self._pubkey())
        self.assertTrue(passed, detail)

    def test_confusion_skips_without_a_pubkey(self):
        url = self._correct()
        passed, detail = jatk.check_alg_confusion_rejected(url, self._spec(), self._secret(), b"")
        self.assertIsNone(passed)
        self.assertIn("SKIP", detail)

    def test_no_claims_suite_is_green_with_two_skips(self):
        url = self._start(stub_handler.serve(0, expected_aud="", expected_iss=""))
        spec = jatk.AuthSpec.from_fixture("hs256_no_claims")
        failures = jatk.run_suite(url, spec, self._secret(), self._pubkey())
        self.assertEqual(failures, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
