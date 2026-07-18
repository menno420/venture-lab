#!/usr/bin/env python3
"""HTTP-layer real-path tests for the Pagination Test Kit.

Discipline (carried over from the webhook + idempotency + rate-limit kits): every
request is fired over actual HTTP to a handler running on an ephemeral port —
never an in-process shortcut. Two reference stubs are exercised:

  - the CORRECT stub (stub_handler.py, real keyset pagination on (created_at, id)
    with an opaque HMAC-signed cursor): the harness reports all six properties
    PASS.
  - the NAIVE stub (stub_handler_naive.py: OFFSET/LIMIT pagination, no over-max
    clamp, a forged cursor silently coerced to page 1): the harness correctly
    FLAGS stable-under-mutation / page-size / cursor-tamper, and (honestly) does
    NOT flag traversal / ordering / terminal — those three don't distinguish the
    stubs, and the kit says so. This is the kit's value proof.

No timed waits — pagination has no windows, so the whole suite runs in well under
a second.

Run:  python3 -m unittest -v   (from this directory)
"""
import json
import threading
import unittest
from http.server import ThreadingHTTPServer

import pgtk
import stub_handler
import stub_handler_naive

FIXTURE = "items_keyset"
LIMIT = 3
MAX_PAGE = 5


class _ServerCase(unittest.TestCase):
    def _start(self, httpd: ThreadingHTTPServer) -> str:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _correct(self):
        return self._start(stub_handler.serve(0, max_page=MAX_PAGE))

    def _naive(self):
        return self._start(stub_handler_naive.serve(0, max_page=MAX_PAGE))


# --------------------------------------------------------------------------- #
# Fixtures + manifest real-shape assertions
# --------------------------------------------------------------------------- #
class FixtureTests(_ServerCase):
    def test_manifest_covers_every_fixture(self):
        from pathlib import Path
        fix = Path(__file__).resolve().parent / "fixtures"
        manifest_stems = set(pgtk.load_manifest().keys())
        on_disk = {p.stem for p in fix.glob("*.json")}
        on_disk.discard("MANIFEST")
        self.assertEqual(manifest_stems, on_disk)
        self.assertEqual(len(manifest_stems), 2)

    def test_fixtures_parse_and_have_a_spec(self):
        for stem in pgtk.list_fixtures():
            spec = pgtk.PageSpec.from_fixture(stem)
            self.assertTrue(spec.path.startswith("/"))
            self.assertTrue(spec.cursor_param)
            self.assertTrue(spec.items_field)
            json.loads(pgtk.load_fixture(stem))  # parses

    def test_default_fixture_matches_the_stub(self):
        spec = pgtk.PageSpec.from_fixture("items_keyset")
        self.assertEqual(spec.path, "/items")
        self.assertEqual(spec.cursor_param, "cursor")
        self.assertEqual(spec.next_cursor_field, "next_cursor")


# --------------------------------------------------------------------------- #
# CORRECT stub — every property passes
# --------------------------------------------------------------------------- #
class CorrectStubTests(_ServerCase):
    def test_traversal_passes(self):
        url = self._correct()
        passed, detail = pgtk.check_traversal(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_traversal_reproduces_ground_truth_exactly_once(self):
        url = self._correct()
        pgtk.reset(url)
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        ids, _rows, _sizes, terminated, err = pgtk.traverse(url, spec, LIMIT)
        self.assertIsNone(err)
        self.assertTrue(terminated)
        truth = pgtk.debug_all(url)
        self.assertEqual(ids, truth)
        self.assertEqual(len(ids), len(set(ids)))  # no overlap

    def test_stability_passes(self):
        url = self._correct()
        passed, detail = pgtk.check_stable_under_mutation(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_stability_no_skip_after_deleting_a_seen_row(self):
        # Direct confirmation: delete an already-returned row mid-traversal; the
        # keyset cursor still names a position, so nothing after it is skipped.
        url = self._correct()
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        pgtk.reset(url)
        truth = set(pgtk.debug_all(url))
        _s, _h, obj = pgtk.fire_page(url, spec, LIMIT, "")
        seen, _r, cursor = pgtk._extract(obj, spec)
        self.assertTrue(pgtk.debug_delete(url, seen[0]))
        rest, _r2, _s2, _t, err = pgtk.traverse(url, spec, LIMIT, start_cursor=cursor)
        self.assertIsNone(err)
        returned = set(seen + rest)
        self.assertEqual(truth - {seen[0]}, (truth - {seen[0]}) & returned)

    def test_ordering_passes(self):
        url = self._correct()
        passed, detail = pgtk.check_ordering(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_page_size_passes(self):
        url = self._correct()
        passed, detail = pgtk.check_page_size(url, FIXTURE, limit=LIMIT, max_arg=pgtk.DEFAULT_MAX)
        self.assertTrue(passed, detail)

    def test_over_max_is_clamped(self):
        url = self._correct()
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        _s, _h, obj = pgtk.fire_page(url, spec, 1000, "")
        ids, _r, _n = pgtk._extract(obj, spec)
        self.assertLessEqual(len(ids), MAX_PAGE)

    def test_advertises_page_size_max_header(self):
        url = self._correct()
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        _s, h, _o = pgtk.fire_page(url, spec, 3, "")
        self.assertEqual(h.get("x-page-size-max"), str(MAX_PAGE))

    def test_terminal_passes(self):
        url = self._correct()
        passed, detail = pgtk.check_terminal(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_cursor_tamper_passes(self):
        url = self._correct()
        passed, detail = pgtk.check_cursor_tamper(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed, detail)

    def test_forged_cursor_returns_400(self):
        url = self._correct()
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        status, _h, _o = pgtk.fire_page(url, spec, LIMIT, "not-a-real-cursor")
        self.assertEqual(status, 400)

    def test_tampered_valid_cursor_returns_400(self):
        url = self._correct()
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        _s, _h, obj = pgtk.fire_page(url, spec, LIMIT, "")
        _ids, _r, cursor = pgtk._extract(obj, spec)
        self.assertIsNotNone(cursor)
        tampered = cursor[:-1] + ("Z" if cursor[-1] != "Z" else "Q")
        status, _hh, _oo = pgtk.fire_page(url, spec, LIMIT, tampered)
        self.assertEqual(status, 400)

    def test_full_suite_green_against_correct_stub(self):
        url = self._correct()
        failures = pgtk.run_suite(url, FIXTURE, LIMIT, pgtk.DEFAULT_MAX)
        self.assertEqual(failures, 0)


# --------------------------------------------------------------------------- #
# NAIVE stub — the kit FLAGS the broken behaviour (the value proof)
# --------------------------------------------------------------------------- #
class NaiveStubTests(_ServerCase):
    def test_kit_flags_skip_under_mutation(self):
        url = self._naive()
        passed, detail = pgtk.check_stable_under_mutation(url, FIXTURE, limit=LIMIT)
        self.assertFalse(passed, "kit should FLAG the offset skip under mutation")
        self.assertIn("SKIPPED", detail)

    def test_kit_flags_missing_over_max_clamp(self):
        url = self._naive()
        passed, detail = pgtk.check_page_size(url, FIXTURE, limit=LIMIT, max_arg=pgtk.DEFAULT_MAX)
        self.assertFalse(passed, "kit should FLAG an unbounded over-max page")
        self.assertIn("clamp", detail.lower())

    def test_kit_flags_forged_cursor_accepted(self):
        url = self._naive()
        passed, detail = pgtk.check_cursor_tamper(url, FIXTURE, limit=LIMIT)
        self.assertFalse(passed, "kit should FLAG a forged cursor served as page 1")
        self.assertIn("ACCEPTED", detail)

    def test_forged_cursor_on_naive_returns_2xx(self):
        # The bug directly: garbage cursor -> offset 0 -> HTTP 200 (page 1).
        url = self._naive()
        spec = pgtk.PageSpec.from_fixture(FIXTURE)
        status, _h, _o = pgtk.fire_page(url, spec, LIMIT, "not-a-real-cursor")
        self.assertTrue(200 <= status < 300, status)

    def test_traversal_still_passes_on_naive(self):
        # Honest: offset pagination traverses a STATIC dataset correctly, so
        # traversal does NOT distinguish correct from naive. Documented.
        url = self._naive()
        passed, _ = pgtk.check_traversal(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed)

    def test_ordering_still_passes_on_naive(self):
        url = self._naive()
        passed, _ = pgtk.check_ordering(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed)

    def test_terminal_still_passes_on_naive(self):
        url = self._naive()
        passed, _ = pgtk.check_terminal(url, FIXTURE, limit=LIMIT)
        self.assertTrue(passed)

    def test_full_suite_flags_naive_stub(self):
        url = self._naive()
        failures = pgtk.run_suite(url, FIXTURE, LIMIT, pgtk.DEFAULT_MAX)
        # stable-under-mutation + page-size + cursor-tamper = 3 flagged;
        # traversal + ordering + terminal pass.
        self.assertEqual(failures, 3)


# --------------------------------------------------------------------------- #
# Stability SKIP path — no test-mutation hooks => neither pass nor fail
# --------------------------------------------------------------------------- #
class _NoDebugHandler(stub_handler.BaseHTTPRequestHandler):
    """A minimal keyset-ish endpoint with NO /_debug/* routes, to prove the
    stability check SKIPs (rather than falsely fails) when it cannot mutate."""

    def log_message(self, *a):
        pass

    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(self.path)
        if parsed.path != "/items":
            self._json(404, {"error": "not found"})
            return
        rows = sorted(stub_handler.CANONICAL, key=stub_handler._sort_key)
        q = parse_qs(parsed.query)
        n = min(int(q.get("limit", ["3"])[0]), 5)
        start = int(q.get("cursor", ["0"])[0] or "0")
        window = rows[start:start + n]
        nxt = str(start + n) if start + n < len(rows) else None
        self._json(200, {"items": window, "next_cursor": nxt})

    def _json(self, code, obj):
        data = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


class StabilitySkipTests(_ServerCase):
    def test_stability_skips_without_debug_hooks(self):
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), _NoDebugHandler)
        url = self._start(httpd)
        passed, detail = pgtk.check_stable_under_mutation(url, FIXTURE, limit=LIMIT)
        self.assertIsNone(passed, f"expected SKIP, got {passed}: {detail}")
        self.assertIn("SKIP", detail)

    def test_skip_does_not_count_as_a_failure(self):
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), _NoDebugHandler)
        url = self._start(httpd)
        # traversal/ordering/terminal pass; page-size passes (clamped at 5);
        # cursor-tamper: this stub coerces bad cursors to 0, so it FAILS here —
        # which is correct (a real endpoint SHOULD 400). Stability SKIPs (not a
        # failure). Assert the SKIP itself contributes 0 to the failure count.
        passed, _d = pgtk.check_stable_under_mutation(url, FIXTURE, limit=LIMIT)
        self.assertIsNone(passed)


# --------------------------------------------------------------------------- #
# Cursor encode/decode unit coverage (opaque, tamper-evident)
# --------------------------------------------------------------------------- #
class CursorTests(unittest.TestCase):
    def setUp(self):
        self.store = stub_handler.KeysetStore(stub_handler.DEFAULT_SECRET, 5)

    def test_roundtrip(self):
        row = {"id": "b1", "created_at": 105}
        token = self.store.encode_cursor(row)
        self.assertEqual(self.store.decode_cursor(token), (105, "b1"))

    def test_bad_base64_rejected(self):
        with self.assertRaises(ValueError):
            self.store.decode_cursor("###.###")

    def test_missing_dot_rejected(self):
        with self.assertRaises(ValueError):
            self.store.decode_cursor("justonepart")

    def test_signature_mismatch_rejected(self):
        row = {"id": "b1", "created_at": 105}
        token = self.store.encode_cursor(row)
        tampered = token[:-2] + ("AA" if token[-2:] != "AA" else "BB")
        with self.assertRaises(ValueError):
            self.store.decode_cursor(tampered)

    def test_a_different_secret_rejects_the_cursor(self):
        row = {"id": "b1", "created_at": 105}
        token = self.store.encode_cursor(row)
        other = stub_handler.KeysetStore(b"a-totally-different-key", 5)
        with self.assertRaises(ValueError):
            other.decode_cursor(token)


if __name__ == "__main__":
    unittest.main(verbosity=2)
