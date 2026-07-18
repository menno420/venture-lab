#!/usr/bin/env python3
"""HTTP-layer real-path tests for the Idempotency Key Test Kit.

Discipline (carried over from the webhook kits): every request is POSTed over
actual HTTP to a handler running on an ephemeral port — never an in-process
shortcut. Two reference stubs are exercised:

  - the CORRECT stub (stub_handler.py): the harness reports all five properties
    PASS, and the server-side side-effect counter proves EXACTLY-ONCE.
  - the NAIVE stub (stub_handler_naive.py, no dedup): the harness correctly
    FLAGS the replay / mismatch / concurrent / missing-key violations, and the
    counter shows the over-execution. This is the kit's value proof — it
    distinguishes correct idempotency from a broken implementation.

Run:  python3 -m unittest -v   (from this directory)
"""
import json
import threading
import unittest
from http.server import ThreadingHTTPServer

import ikt
import stub_handler
import stub_handler_naive

PRIMARY = "charge_basic"
VARIANT = "charge_mismatch"


class _ServerCase(unittest.TestCase):
    def _start(self, httpd: ThreadingHTTPServer) -> str:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _correct(self, require_key=True, delay_ms=60):
        httpd = stub_handler.serve(0, require_key=require_key, delay_ms=delay_ms)
        self._correct_httpd = httpd
        return self._start(httpd)

    def _naive(self, delay_ms=60):
        httpd = stub_handler_naive.serve(0, delay_ms=delay_ms)
        self._naive_httpd = httpd
        return self._start(httpd)

    def _side_effects(self, base_url) -> int:
        status, body = ikt.get(base_url, "/_debug/side_effects")
        self.assertEqual(status, 200, body)
        return json.loads(body)["count"]


# --------------------------------------------------------------------------- #
# Fixtures + manifest real-shape assertions
# --------------------------------------------------------------------------- #
class FixtureTests(_ServerCase):
    def test_manifest_covers_every_fixture(self):
        from pathlib import Path
        fix = Path(__file__).resolve().parent / "fixtures"
        manifest_stems = set(ikt.load_manifest().keys())
        on_disk = {p.stem for p in fix.glob("*.json")}
        on_disk.discard("MANIFEST")
        self.assertEqual(manifest_stems, on_disk)
        self.assertEqual(len(manifest_stems), 3)

    def test_all_fixtures_are_json_with_a_path(self):
        for stem in ikt.list_fixtures():
            self.assertEqual(ikt.content_type_for(stem), "application/json")
            self.assertTrue(ikt.path_for(stem).startswith("/"))
            json.loads(ikt.load_fixture(stem))  # parses

    def test_primary_and_variant_share_endpoint_but_differ_in_body(self):
        # The mismatch check needs same endpoint, different bytes.
        self.assertEqual(ikt.path_for(PRIMARY), ikt.path_for(VARIANT))
        self.assertNotEqual(ikt.load_fixture(PRIMARY), ikt.load_fixture(VARIANT))

    def test_order_fixture_targets_a_second_endpoint(self):
        # Key scoping is per (method, path, key); a second path proves it.
        self.assertNotEqual(ikt.path_for("order_create"), ikt.path_for(PRIMARY))


# --------------------------------------------------------------------------- #
# CORRECT stub — every property passes, exactly-once holds
# --------------------------------------------------------------------------- #
class CorrectStubTests(_ServerCase):
    def test_replay_passes_and_side_effect_runs_once(self):
        url = self._correct()
        before = self._side_effects(url)
        passed, detail = ikt.check_replay(url, PRIMARY)
        self.assertTrue(passed, detail)
        # replay fired two requests with one key; the side effect ran ONCE.
        self.assertEqual(self._side_effects(url) - before, 1, detail)

    def test_replay_returns_byte_identical_stored_response(self):
        url = self._correct()
        path, ct, body = ikt.path_for(PRIMARY), ikt.content_type_for(PRIMARY), ikt.load_fixture(PRIMARY)
        key = ikt.new_key()
        s1, b1 = ikt.post(url, path, body, ct, key=key)
        s2, b2 = ikt.post(url, path, body, ct, key=key)
        self.assertTrue(ikt.is_2xx(s1) and ikt.is_2xx(s2))
        self.assertEqual(b1, b2)  # the STORED original response, verbatim

    def test_mismatch_passes(self):
        url = self._correct()
        passed, detail = ikt.check_mismatch(url, PRIMARY, VARIANT)
        self.assertTrue(passed, detail)

    def test_mismatch_does_not_execute_a_second_time(self):
        url = self._correct()
        before = self._side_effects(url)
        ikt.check_mismatch(url, PRIMARY, VARIANT)
        # first request executes once; the conflicting second must NOT execute.
        self.assertEqual(self._side_effects(url) - before, 1)

    def test_distinct_keys_passes(self):
        url = self._correct()
        passed, detail = ikt.check_distinct_keys(url, PRIMARY)
        self.assertTrue(passed, detail)

    def test_concurrent_passes_and_runs_once(self):
        url = self._correct()
        before = self._side_effects(url)
        passed, detail = ikt.check_concurrent(url, PRIMARY, n=4)
        self.assertTrue(passed, detail)
        # four in-flight requests, one key → the side effect ran exactly once.
        self.assertEqual(self._side_effects(url) - before, 1, detail)

    def test_missing_key_required_passes(self):
        url = self._correct(require_key=True)
        passed, detail = ikt.check_missing_key(url, PRIMARY, "required")
        self.assertTrue(passed, detail)

    def test_missing_key_passthrough_mode(self):
        url = self._correct(require_key=False)
        passed, detail = ikt.check_missing_key(url, PRIMARY, "passthrough")
        self.assertTrue(passed, detail)

    def test_key_scoping_across_endpoints(self):
        # Same key on two different paths → two independent side effects.
        url = self._correct()
        before = self._side_effects(url)
        key = ikt.new_key()
        ikt.post(url, "/charges", ikt.load_fixture(PRIMARY), "application/json", key=key)
        ikt.post(url, "/orders", ikt.load_fixture("order_create"), "application/json", key=key)
        self.assertEqual(self._side_effects(url) - before, 2)

    def test_full_suite_green_against_correct_stub(self):
        url = self._correct()
        failures = ikt.run_suite(url, PRIMARY, VARIANT, "required")
        self.assertEqual(failures, 0)


# --------------------------------------------------------------------------- #
# NAIVE stub — the kit FLAGS the broken behaviour (the value proof)
# --------------------------------------------------------------------------- #
class NaiveStubTests(_ServerCase):
    def test_kit_flags_replay_double_execution(self):
        url = self._naive()
        before = self._side_effects(url)
        passed, detail = ikt.check_replay(url, PRIMARY)
        self.assertFalse(passed, "kit should FLAG a no-dedup replay")
        self.assertIn("TWICE", detail)
        # proof the naive stub really double-executed the retry.
        self.assertEqual(self._side_effects(url) - before, 2)

    def test_kit_flags_mismatch_accepted(self):
        url = self._naive()
        passed, detail = ikt.check_mismatch(url, PRIMARY, VARIANT)
        self.assertFalse(passed, "kit should FLAG same-key/different-body being accepted")
        self.assertIn("ACCEPTED", detail)

    def test_kit_flags_concurrent_double_execution(self):
        url = self._naive()
        before = self._side_effects(url)
        passed, detail = ikt.check_concurrent(url, PRIMARY, n=4)
        self.assertFalse(passed, "kit should FLAG concurrent double-execution")
        self.assertGreaterEqual(self._side_effects(url) - before, 2)

    def test_kit_flags_missing_key_accepted_when_required(self):
        url = self._naive()
        passed, detail = ikt.check_missing_key(url, PRIMARY, "required")
        self.assertFalse(passed, "kit should FLAG a keyless request accepted under `required`")

    def test_distinct_keys_still_passes_on_naive(self):
        # Honest: over-executing trivially satisfies distinct-keys, so this
        # property does NOT distinguish correct from naive. Documented in
        # stub_handler_naive.py and GOTCHAS.md.
        url = self._naive()
        passed, _ = ikt.check_distinct_keys(url, PRIMARY)
        self.assertTrue(passed)

    def test_full_suite_flags_naive_stub(self):
        url = self._naive()
        failures = ikt.run_suite(url, PRIMARY, VARIANT, "required")
        # replay + mismatch + concurrent + missing-key = 4 flagged; distinct-keys passes.
        self.assertEqual(failures, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
