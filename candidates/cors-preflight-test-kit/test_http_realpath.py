#!/usr/bin/env python3
"""HTTP-layer real-path tests for the CORS Preflight Test Kit.

Discipline (carried over from the webhook + idempotency + rate-limit + pagination
+ JWT kits): every request is fired over actual HTTP to a handler running on an
ephemeral port — never an in-process shortcut. Three kinds of stub are exercised:

  - the CORRECT stub (stub_handler.py, a real allowlist-based CORS handler): the
    harness reports all six properties PASS.
  - the NAIVE stub (stub_handler_naive.py: reflects any origin, no Vary, no
    Allow-Methods/Allow-Headers on the preflight): the harness correctly FLAGS
    allow-origin / allow-methods / allow-headers / reflect-guard, and (honestly)
    does NOT flag preflight-status / credentials — those two properties don't
    distinguish the stubs, and the kit says so. This is the kit's value proof — it
    distinguishes a correct CORS config from a broken one.
  - small EDGE-CASE stubs defined inline, to prove two Fetch-spec footguns are
    caught: `Access-Control-Allow-Headers: *` does NOT cover Authorization, and
    `Access-Control-Allow-Origin: *` + credentials is rejected.

No timed waits — the whole suite runs in well under a second.

Run:  python3 -m unittest -v   (from this directory)
"""
import json
import threading
import unittest
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import cptk
import stub_handler
import stub_handler_naive

FIXTURE = "api_json_post"
ALLOWED = "https://app.example.com"
BAD = "https://evil.example"


class _ServerCase(unittest.TestCase):
    def _start(self, httpd: ThreadingHTTPServer) -> str:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)
        return f"http://127.0.0.1:{port}"

    def _correct(self, allowed=(ALLOWED,)):
        return self._start(stub_handler.serve(0, allowed_origins=list(allowed)))

    def _naive(self):
        return self._start(stub_handler_naive.serve(0))


# --------------------------------------------------------------------------- #
# Fixtures + manifest real-shape assertions
# --------------------------------------------------------------------------- #
class FixtureTests(_ServerCase):
    def test_manifest_covers_every_fixture(self):
        from pathlib import Path
        fix = Path(__file__).resolve().parent / "fixtures"
        manifest_stems = set(cptk.load_manifest().keys())
        on_disk = {p.stem for p in fix.glob("*.json")}
        on_disk.discard("MANIFEST")
        self.assertEqual(manifest_stems, on_disk)
        self.assertEqual(len(manifest_stems), 2)

    def test_fixtures_have_method_path_and_headers(self):
        for stem in cptk.list_fixtures():
            self.assertIn(cptk.method_for(stem), ("GET", "POST", "PUT", "PATCH", "DELETE"))
            self.assertTrue(cptk.path_for(stem).startswith("/"))
            # every bundled fixture triggers a preflight (non-empty request headers)
            self.assertTrue(cptk.request_headers_for(stem).strip())
            json.loads(cptk.load_fixture(stem))  # parses

    def test_default_fixture_is_the_json_post(self):
        self.assertEqual(cptk.method_for("api_json_post"), "POST")
        self.assertEqual(cptk.path_for("api_json_post"), "/api/data")
        self.assertIn("authorization", cptk.request_headers_for("api_json_post").lower())


# --------------------------------------------------------------------------- #
# CORRECT stub — every property passes
# --------------------------------------------------------------------------- #
class CorrectStubTests(_ServerCase):
    def test_preflight_status_passes(self):
        url = self._correct()
        passed, detail = cptk.check_preflight_status(url, FIXTURE, ALLOWED)
        self.assertTrue(passed, detail)

    def test_preflight_returns_204(self):
        url = self._correct()
        status, h, _b = cptk.preflight(url, "/api/data", ALLOWED, "POST", "content-type, authorization")
        self.assertEqual(status, 204, h)

    def test_allow_origin_passes(self):
        url = self._correct()
        passed, detail = cptk.check_allow_origin(url, FIXTURE, ALLOWED)
        self.assertTrue(passed, detail)

    def test_allow_origin_echoes_specific_origin_with_vary(self):
        url = self._correct()
        _s, h, _b = cptk.preflight(url, "/api/data", ALLOWED, "POST", "content-type, authorization")
        self.assertEqual(h.get("access-control-allow-origin"), ALLOWED)
        self.assertTrue(cptk._vary_has_origin(h), h.get("vary"))
        # and on the actual response too
        _s2, h2, _b2 = cptk.actual(url, "POST", "/api/data", ALLOWED, cptk.load_fixture(FIXTURE))
        self.assertEqual(h2.get("access-control-allow-origin"), ALLOWED)
        self.assertTrue(cptk._vary_has_origin(h2))

    def test_allow_methods_passes(self):
        url = self._correct()
        passed, detail = cptk.check_allow_methods(url, FIXTURE, ALLOWED)
        self.assertTrue(passed, detail)

    def test_allow_methods_lists_the_requested_method(self):
        url = self._correct()
        _s, h, _b = cptk.preflight(url, "/api/data", ALLOWED, "POST", "content-type, authorization")
        methods = {m.strip().upper() for m in h["access-control-allow-methods"].split(",")}
        self.assertIn("POST", methods)

    def test_allow_headers_passes(self):
        url = self._correct()
        passed, detail = cptk.check_allow_headers(url, FIXTURE, ALLOWED)
        self.assertTrue(passed, detail)

    def test_allow_headers_covers_authorization_explicitly(self):
        url = self._correct()
        _s, h, _b = cptk.preflight(url, "/api/data", ALLOWED, "POST", "content-type, authorization")
        acah = {x.strip().lower() for x in h["access-control-allow-headers"].split(",")}
        self.assertIn("authorization", acah)
        self.assertNotIn("*", acah)  # named explicitly, not a wildcard

    def test_credentials_passes(self):
        url = self._correct()
        passed, detail = cptk.check_credentials(url, FIXTURE, ALLOWED)
        self.assertTrue(passed, detail)

    def test_credentials_is_specific_origin_not_star(self):
        url = self._correct()
        _s, h, _b = cptk.preflight(url, "/api/data", ALLOWED, "POST", "content-type, authorization")
        self.assertEqual(h.get("access-control-allow-credentials"), "true")
        self.assertNotEqual(h.get("access-control-allow-origin"), "*")

    def test_reflect_guard_passes(self):
        url = self._correct()
        passed, detail = cptk.check_reflect_guard(url, FIXTURE, ALLOWED, BAD)
        self.assertTrue(passed, detail)

    def test_disallowed_origin_gets_no_allow_origin(self):
        url = self._correct()
        _s, h, _b = cptk.preflight(url, "/api/data", BAD, "POST", "content-type, authorization")
        self.assertIsNone(h.get("access-control-allow-origin"))
        _s2, h2, _b2 = cptk.actual(url, "POST", "/api/data", BAD, cptk.load_fixture(FIXTURE))
        self.assertIsNone(h2.get("access-control-allow-origin"))

    def test_get_authed_fixture_also_passes(self):
        url = self._correct()
        failures = cptk.run_suite(url, "api_get_authed", ALLOWED, BAD)
        self.assertEqual(failures, 0)

    def test_second_allowed_origin_also_works(self):
        other = "https://admin.example.com"
        url = self._correct(allowed=(ALLOWED, other))
        failures = cptk.run_suite(url, FIXTURE, other, BAD)
        self.assertEqual(failures, 0)

    def test_full_suite_green_against_correct_stub(self):
        url = self._correct()
        failures = cptk.run_suite(url, FIXTURE, ALLOWED, BAD)
        self.assertEqual(failures, 0)


# --------------------------------------------------------------------------- #
# NAIVE stub — the kit FLAGS the broken behaviour (the value proof)
# --------------------------------------------------------------------------- #
class NaiveStubTests(_ServerCase):
    def test_kit_flags_missing_vary_on_allow_origin(self):
        url = self._naive()
        passed, detail = cptk.check_allow_origin(url, FIXTURE, ALLOWED)
        self.assertFalse(passed, "kit should FLAG an echoed origin with no Vary: Origin")
        self.assertIn("Vary: Origin", detail)

    def test_kit_flags_missing_allow_methods(self):
        url = self._naive()
        passed, detail = cptk.check_allow_methods(url, FIXTURE, ALLOWED)
        self.assertFalse(passed, "kit should FLAG a preflight with no Access-Control-Allow-Methods")
        self.assertIn("Access-Control-Allow-Methods", detail)

    def test_kit_flags_missing_allow_headers(self):
        url = self._naive()
        passed, detail = cptk.check_allow_headers(url, FIXTURE, ALLOWED)
        self.assertFalse(passed, "kit should FLAG a preflight with no Access-Control-Allow-Headers")
        self.assertIn("Access-Control-Allow-Headers", detail)

    def test_kit_flags_arbitrary_origin_reflection(self):
        url = self._naive()
        passed, detail = cptk.check_reflect_guard(url, FIXTURE, ALLOWED, BAD)
        self.assertFalse(passed, "kit should FLAG an arbitrary reflected origin (open CORS)")
        self.assertIn("REFLECTS", detail)

    def test_preflight_status_still_passes_on_naive(self):
        # Honest: the naive stub still returns a 204 preflight, so preflight-status
        # does NOT distinguish correct from naive. Documented in the stub + GOTCHAS.
        url = self._naive()
        passed, _ = cptk.check_preflight_status(url, FIXTURE, ALLOWED)
        self.assertTrue(passed)

    def test_credentials_still_passes_on_naive(self):
        # The naive stub reflects the SPECIFIC origin (not `*`) with credentials,
        # which is a valid pairing — so credentials does NOT distinguish either.
        url = self._naive()
        passed, _ = cptk.check_credentials(url, FIXTURE, ALLOWED)
        self.assertTrue(passed)

    def test_full_suite_flags_naive_stub(self):
        url = self._naive()
        failures = cptk.run_suite(url, FIXTURE, ALLOWED, BAD)
        # allow-origin + allow-methods + allow-headers + reflect-guard = 4 flagged;
        # preflight-status + credentials pass.
        self.assertEqual(failures, 4)


# --------------------------------------------------------------------------- #
# Edge-case stubs — the two Fetch-spec footguns, over real HTTP
# --------------------------------------------------------------------------- #
def _edge_handler(policy):
    """policy: dict of the CORS headers to emit on EVERY response (preflight +
    actual), verbatim. Missing keys are simply not sent."""
    class Edge(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _emit(self, code, body=b""):
            self.send_response(code)
            for k, v in policy.items():
                self.send_header(k, v)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if body:
                self.wfile.write(body)

        def do_OPTIONS(self):
            self._emit(204)

        def do_GET(self):
            self._emit(200, json.dumps({"id": "res_" + uuid.uuid4().hex}).encode())

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            if length:
                self.rfile.read(length)
            self._emit(200, json.dumps({"id": "res_" + uuid.uuid4().hex}).encode())

    return Edge


class EdgeCaseTests(_ServerCase):
    def _edge(self, policy):
        return self._start(ThreadingHTTPServer(("127.0.0.1", 0), _edge_handler(policy)))

    def test_star_allow_headers_does_not_cover_authorization(self):
        # ACAO echoes origin (+ Vary + methods), but ACAH is the literal `*`.
        url = self._edge({
            "Access-Control-Allow-Origin": ALLOWED,
            "Vary": "Origin",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        })
        passed, detail = cptk.check_allow_headers(url, FIXTURE, ALLOWED)
        self.assertFalse(passed, "`*` must NOT be accepted as covering Authorization")
        self.assertIn("Authorization", detail)

    def test_star_allow_headers_covers_content_type(self):
        # A request that only asks for Content-Type is covered by `*` (only
        # Authorization is special-cased out of the `*` wildcard by Fetch).
        url = self._edge({
            "Access-Control-Allow-Origin": ALLOWED,
            "Vary": "Origin",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        })
        # a direct preflight requesting only content-type
        _s, h, _b = cptk.preflight(url, "/api/data", ALLOWED, "POST", "content-type")
        acah = [x.strip().lower() for x in h["access-control-allow-headers"].split(",")]
        self.assertIn("*", acah)

    def test_star_origin_with_credentials_flagged(self):
        url = self._edge({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
            "Access-Control-Allow-Credentials": "true",
        })
        passed, detail = cptk.check_credentials(url, FIXTURE, ALLOWED)
        self.assertFalse(passed, "`*` origin + credentials: true must be flagged")
        self.assertIn("*", detail)

    def test_public_star_origin_without_credentials_passes_reflect_guard(self):
        # A public, non-credentialed API legitimately uses `*` — not open-CORS.
        url = self._edge({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
        })
        passed, detail = cptk.check_reflect_guard(url, FIXTURE, ALLOWED, BAD)
        self.assertTrue(passed, detail)

    def test_missing_allow_origin_flagged(self):
        # A preflight that returns 204 but no CORS headers at all.
        url = self._edge({})
        passed, detail = cptk.check_allow_origin(url, FIXTURE, ALLOWED)
        self.assertFalse(passed)
        self.assertIn("Access-Control-Allow-Origin", detail)


# --------------------------------------------------------------------------- #
# Helper unit coverage
# --------------------------------------------------------------------------- #
class HelperTests(unittest.TestCase):
    def test_split_list(self):
        self.assertEqual(cptk._split_list("GET, POST ,PUT"), ["GET", "POST", "PUT"])
        self.assertEqual(cptk._split_list(None), [])
        self.assertEqual(cptk._split_list(""), [])

    def test_vary_has_origin_case_insensitive(self):
        self.assertTrue(cptk._vary_has_origin({"vary": "origin"}))
        self.assertTrue(cptk._vary_has_origin({"vary": "Accept-Encoding, Origin"}))
        self.assertFalse(cptk._vary_has_origin({"vary": "Accept-Encoding"}))
        self.assertFalse(cptk._vary_has_origin({}))

    def test_acao_star_ok(self):
        ok, _d = cptk._acao_ok({"access-control-allow-origin": "*"}, ALLOWED, "preflight")
        self.assertTrue(ok)

    def test_acao_specific_without_vary_flagged(self):
        ok, detail = cptk._acao_ok({"access-control-allow-origin": ALLOWED}, ALLOWED, "preflight")
        self.assertFalse(ok)
        self.assertIn("Vary: Origin", detail)

    def test_acao_specific_with_vary_ok(self):
        ok, _d = cptk._acao_ok(
            {"access-control-allow-origin": ALLOWED, "vary": "Origin"}, ALLOWED, "preflight")
        self.assertTrue(ok)

    def test_acao_missing_flagged(self):
        ok, detail = cptk._acao_ok({}, ALLOWED, "actual response")
        self.assertFalse(ok)
        self.assertIn("NO Access-Control-Allow-Origin", detail)

    def test_acao_wrong_origin_flagged(self):
        ok, _d = cptk._acao_ok(
            {"access-control-allow-origin": "https://other.example"}, ALLOWED, "preflight")
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main(verbosity=2)
