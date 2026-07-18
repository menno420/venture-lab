#!/usr/bin/env python3
"""HTTP-layer real-path tests for the Rate-Limit Test Kit.

Discipline (carried over from the webhook + idempotency kits): every request is
fired over actual HTTP to a handler running on an ephemeral port — never an
in-process shortcut. Two reference stubs are exercised:

  - the CORRECT stub (stub_handler.py, a real fixed-window limiter): the harness
    reports all six properties PASS.
  - the NAIVE stub (stub_handler_naive.py: off-by-one, no Retry-After, stale
    headers): the harness correctly FLAGS over-limit / retry-after / headers /
    retry-after-honored, and (honestly) does NOT flag under-limit / window-reset
    — those two properties don't distinguish the stubs, and the kit says so. This
    is the kit's value proof — it distinguishes a correct limiter from a broken
    one.

A short window (800 ms) keeps the timed properties (window-reset,
retry-after-honored) fast; the whole suite runs in a few seconds.

Run:  python3 -m unittest -v   (from this directory)
"""
import json
import threading
import unittest
from http.server import ThreadingHTTPServer

import rltk
import stub_handler
import stub_handler_naive

FIXTURE = "api_ping"
LIMIT = 5
WINDOW_MS = 800
WINDOW_S = WINDOW_MS / 1000.0


class _ServerCase(unittest.TestCase):
    def _start(self, httpd: ThreadingHTTPServer) -> str:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _correct(self, header_style="both"):
        return self._start(stub_handler.serve(0, limit=LIMIT, window_ms=WINDOW_MS, header_style=header_style))

    def _naive(self):
        return self._start(stub_handler_naive.serve(0, limit=LIMIT, window_ms=WINDOW_MS))

    def _state(self, base_url) -> dict:
        status, _h, body = rltk.fire(base_url, "GET", "/_debug/state")
        self.assertEqual(status, 200, body)
        return json.loads(body)


# --------------------------------------------------------------------------- #
# Fixtures + manifest real-shape assertions
# --------------------------------------------------------------------------- #
class FixtureTests(_ServerCase):
    def test_manifest_covers_every_fixture(self):
        from pathlib import Path
        fix = Path(__file__).resolve().parent / "fixtures"
        manifest_stems = set(rltk.load_manifest().keys())
        on_disk = {p.stem for p in fix.glob("*.json")}
        on_disk.discard("MANIFEST")
        self.assertEqual(manifest_stems, on_disk)
        self.assertEqual(len(manifest_stems), 2)

    def test_fixtures_have_method_and_path(self):
        for stem in rltk.list_fixtures():
            self.assertIn(rltk.method_for(stem), ("GET", "POST", "PUT", "PATCH", "DELETE"))
            self.assertTrue(rltk.path_for(stem).startswith("/"))
            json.loads(rltk.load_fixture(stem))  # parses

    def test_default_fixture_is_a_get_probe(self):
        self.assertEqual(rltk.method_for("api_ping"), "GET")
        self.assertEqual(rltk.path_for("api_ping"), "/api/ping")


# --------------------------------------------------------------------------- #
# CORRECT stub — every property passes
# --------------------------------------------------------------------------- #
class CorrectStubTests(_ServerCase):
    def test_under_limit_passes(self):
        url = self._correct()
        passed, detail = rltk.check_under_limit(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_over_limit_passes_and_429_at_boundary(self):
        url = self._correct()
        passed, detail = rltk.check_over_limit(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)
        # direct confirmation: after a reset, request LIMIT+1 is a 429.
        rltk.reset(url)
        statuses = [rltk.fire(url, "GET", "/api/ping")[0] for _ in range(LIMIT + 1)]
        self.assertTrue(all(200 <= s < 300 for s in statuses[:LIMIT]), statuses)
        self.assertEqual(statuses[LIMIT], 429, statuses)

    def test_retry_after_present_and_sane(self):
        url = self._correct()
        passed, detail = rltk.check_retry_after(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_the_429_carries_a_positive_retry_after_header(self):
        url = self._correct()
        rltk.reset(url)
        hdrs = None
        for _ in range(LIMIT + 2):
            s, h, _b = rltk.fire(url, "GET", "/api/ping")
            if s == 429:
                hdrs = h
                break
        self.assertIsNotNone(hdrs)
        self.assertIn("retry-after", hdrs)
        self.assertGreater(int(hdrs["retry-after"]), 0)

    def test_headers_consistent(self):
        url = self._correct()
        passed, detail = rltk.check_headers(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_remaining_decrements_to_zero(self):
        url = self._correct()
        rltk.reset(url)
        remaining = []
        for _ in range(LIMIT):
            _s, h, _b = rltk.fire(url, "GET", "/api/ping")
            remaining.append(int(h["ratelimit-remaining"]))
        self.assertEqual(remaining, [4, 3, 2, 1, 0], remaining)

    def test_legacy_header_style_also_consistent(self):
        url = self._correct(header_style="legacy")
        passed, detail = rltk.check_headers(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)
        # and the harness reads the X-RateLimit-* aliases
        rltk.reset(url)
        _s, h, _b = rltk.fire(url, "GET", "/api/ping")
        self.assertIn("x-ratelimit-remaining", h)
        self.assertNotIn("ratelimit-remaining", h)

    def test_window_reset_passes(self):
        url = self._correct()
        passed, detail = rltk.check_window_reset(url, FIXTURE, limit=LIMIT, window=WINDOW_S)
        self.assertTrue(passed, detail)

    def test_retry_after_honored_passes(self):
        url = self._correct()
        passed, detail = rltk.check_retry_after_honored(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_full_suite_green_against_correct_stub(self):
        url = self._correct()
        failures = rltk.run_suite(url, FIXTURE, LIMIT, 0.0, WINDOW_S, rltk.DEFAULT_MAX_DELAY)
        self.assertEqual(failures, 0)


# --------------------------------------------------------------------------- #
# NAIVE stub — the kit FLAGS the broken behaviour (the value proof)
# --------------------------------------------------------------------------- #
class NaiveStubTests(_ServerCase):
    def test_kit_flags_off_by_one_over_limit(self):
        url = self._naive()
        passed, detail = rltk.check_over_limit(url, FIXTURE, limit=LIMIT)
        self.assertFalse(passed, "kit should FLAG the off-by-one quota leak")
        self.assertIn("off-by-one", detail)

    def test_kit_flags_missing_retry_after(self):
        url = self._naive()
        passed, detail = rltk.check_retry_after(url, FIXTURE, limit=LIMIT)
        self.assertFalse(passed, "kit should FLAG a 429 with no Retry-After")
        self.assertIn("Retry-After", detail)

    def test_kit_flags_inconsistent_headers(self):
        url = self._naive()
        passed, detail = rltk.check_headers(url, FIXTURE, limit=LIMIT)
        self.assertFalse(passed, "kit should FLAG stuck Remaining / stale Reset")

    def test_kit_flags_retry_after_not_honored(self):
        url = self._naive()
        passed, detail = rltk.check_retry_after_honored(url, FIXTURE, limit=LIMIT)
        self.assertFalse(passed, "kit should FLAG a Retry-After it can't honour")

    def test_under_limit_still_passes_on_naive(self):
        # Honest: the off-by-one still serves the first `limit` requests, so
        # under-limit does NOT distinguish correct from naive. Documented in
        # stub_handler_naive.py and GOTCHAS.md.
        url = self._naive()
        passed, _ = rltk.check_under_limit(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed)

    def test_window_reset_still_passes_on_naive(self):
        # The naive stub resets its window on time; window-reset doesn't
        # distinguish either. Documented honestly.
        url = self._naive()
        passed, _ = rltk.check_window_reset(url, FIXTURE, limit=LIMIT, window=WINDOW_S)
        self.assertTrue(passed)

    def test_full_suite_flags_naive_stub(self):
        url = self._naive()
        failures = rltk.run_suite(url, FIXTURE, LIMIT, 0.0, WINDOW_S, rltk.DEFAULT_MAX_DELAY)
        # over-limit + retry-after + headers + retry-after-honored = 4 flagged;
        # under-limit + window-reset pass.
        self.assertEqual(failures, 4)


# --------------------------------------------------------------------------- #
# Retry-After parsing unit coverage (delay-seconds + HTTP-date forms)
# --------------------------------------------------------------------------- #
class RetryAfterParseTests(unittest.TestCase):
    def test_positive_delay_seconds_ok(self):
        ok, _d, secs = rltk._parse_retry_after({"retry-after": "30"}, 3600)
        self.assertTrue(ok)
        self.assertEqual(secs, 30)

    def test_zero_and_negative_rejected(self):
        self.assertFalse(rltk._parse_retry_after({"retry-after": "0"}, 3600)[0])
        self.assertFalse(rltk._parse_retry_after({"retry-after": "-5"}, 3600)[0])

    def test_absurd_delay_rejected(self):
        self.assertFalse(rltk._parse_retry_after({"retry-after": "999999"}, 3600)[0])

    def test_missing_rejected(self):
        self.assertFalse(rltk._parse_retry_after({}, 3600)[0])

    def test_future_http_date_ok(self):
        from email.utils import format_datetime
        import datetime as dt
        future = dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=45)
        ok, _d, secs = rltk._parse_retry_after({"retry-after": format_datetime(future)}, 3600)
        self.assertTrue(ok)
        self.assertGreater(secs, 0)

    def test_past_http_date_rejected(self):
        self.assertFalse(rltk._parse_retry_after({"retry-after": "Wed, 21 Oct 2015 07:28:00 GMT"}, 3600)[0])

    def test_reset_heuristic_past_epoch_flagged(self):
        self.assertIsNotNone(rltk._reset_not_future(1_600_000_000))  # 2020, past
        self.assertIsNone(rltk._reset_not_future(5))                 # delta-seconds, future


if __name__ == "__main__":
    unittest.main(verbosity=2)
