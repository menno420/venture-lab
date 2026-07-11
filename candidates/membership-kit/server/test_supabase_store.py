"""HTTP-layer tests for SupabaseStore against a STUB PostgREST server.

Like test_http_realpath.py drives the real Stripe path against vendored real
payloads, this drives the real Supabase persistence path against an in-process
stub PostgREST server whose request/response shapes mirror REAL PostgREST — the
shapes were verified against the PostgREST + Supabase docs (URLs in the module
docstring below), NOT invented from memory.

What is PROVEN here (over real HTTP, no third-party deps):
  * insert  — POST with `Prefer: return=representation` (201 + the stored row)
  * select  — GET with a `email=eq.<value>` filter + `select=` projection
  * upsert  — POST with `Prefer: resolution=merge-duplicates` + `on_conflict=email`
  * count   — GET with `Prefer: count=exact` -> total in the `Content-Range` header
  * auth    — every call carries `apikey` + `Authorization: Bearer <key>`
  * errors  — a non-2xx response raises RuntimeError and never leaks the key
  * idempotency + email normalization/URL-encoding of the filter value

What is NOT proven here (OWNER-GATED, explicitly UNVERIFIED): a live round-trip
against a real Supabase project. That needs the owner to create a project + the
`members` table and supply SUPABASE_URL/SUPABASE_KEY (see server/README.md
OWNER-ACTION). This stub proves the wire contract; only the owner's keys prove
the live integration.

Vendored PostgREST/Supabase shape sources (fetched, not memory):
  * PostgREST tables/views (filter `col=eq.`, `select=`, insert
    `Prefer: return=representation`, upsert `Prefer: resolution=merge-duplicates`
    + `on_conflict=`):
    https://raw.githubusercontent.com/PostgREST/postgrest-docs/main/docs/references/api/tables_views.rst
  * PostgREST exact count (`Prefer: count=exact`, `Content-Range: start-end/total`,
    `Range: 0-0`):
    https://raw.githubusercontent.com/PostgREST/postgrest-docs/main/docs/references/api/pagination_count.rst
  * Supabase REST base path `/rest/v1/` + `apikey` and `Authorization: Bearer`
    headers:
    https://raw.githubusercontent.com/supabase/supabase/master/apps/docs/content/guides/api/creating-routes.mdx

Run:  python3 -m unittest test_supabase_store -v
"""
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

from app import SupabaseStore

FAKE_KEY = "fake-service-role-key"  # a TEST placeholder — never a real key


class _StubPostgREST(ThreadingHTTPServer):
    """A PostgREST-shaped stub. Holds an in-memory `members` table + a request
    log, and can be told to force a non-2xx error for the error-path test."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.table: dict[str, dict] = {}   # email -> {"email", "source"}
        self.requests: list[dict] = []     # captured request records
        self.force_status: int | None = None
        self.force_body: bytes = b'{"code":"PGRST","message":"forced error"}'


class _Handler(BaseHTTPRequestHandler):
    PATH = "/rest/v1/members"

    def log_message(self, *args) -> None:  # keep test output quiet
        pass

    # ---- low-level send helpers ----
    def _send(self, code: int, body: bytes, headers: dict | None = None) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, code: int, obj, headers: dict | None = None) -> None:
        self._send(code, json.dumps(obj).encode(), headers)

    def _record(self, method: str, raw: bytes) -> dict:
        parsed = urlparse(self.path)
        rec = {
            "method": method,
            "path": parsed.path,
            "raw_query": parsed.query,
            "query": parse_qs(parsed.query),
            # lowercased keys: urllib capitalizes header names on the wire
            # (apikey -> Apikey), so normalize for case-insensitive assertions.
            "headers": {k.lower(): v for k, v in self.headers.items()},
            "body": raw.decode("utf-8") if raw else "",
        }
        self.server.requests.append(rec)
        return rec

    # ---- routes ----
    def do_GET(self) -> None:
        self._record("GET", b"")
        srv = self.server
        if srv.force_status:
            self._send(srv.force_status, srv.force_body)
            return
        parsed = urlparse(self.path)
        if parsed.path != self.PATH:
            self._send(404, b'{"message":"not found"}')
            return
        q = parse_qs(parsed.query)
        prefer = self.headers.get("prefer", "")

        # count path: Prefer: count=exact -> total in Content-Range (start-end/total)
        if "count=exact" in prefer:
            total = len(srv.table)
            content_range = f"0-0/{total}" if total else "*/0"
            # Range: 0-0 returns at most one row; body is ignored by the store.
            body = json.dumps(list(srv.table.values())[:1]).encode()
            self.send_response(206)
            self.send_header("Content-Type", "application/json")
            self.send_header("Range-Unit", "items")
            self.send_header("Content-Range", content_range)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        # horizontal filter: email=eq.<value>
        email_filter = None
        for raw_val in q.get("email", []):
            if raw_val.startswith("eq."):
                email_filter = unquote(raw_val[3:])
        if email_filter is not None:
            rows = [srv.table[email_filter]] if email_filter in srv.table else []
        else:
            rows = list(srv.table.values())
        self._send_json(200, rows)

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b""
        self._record("POST", raw)
        srv = self.server
        if srv.force_status:
            self._send(srv.force_status, srv.force_body)
            return
        parsed = urlparse(self.path)
        if parsed.path != self.PATH:
            self._send(404, b'{"message":"not found"}')
            return
        try:
            payload = json.loads(raw or b"[]")
        except json.JSONDecodeError:
            self._send(400, b'{"message":"invalid json"}')
            return
        records = payload if isinstance(payload, list) else [payload]
        prefer = self.headers.get("prefer", "")
        merge = "merge-duplicates" in prefer
        stored = []
        for r in records:
            email = r.get("email")
            if email in srv.table and not merge:
                # Real PostgREST: a plain insert on a duplicate key -> 409.
                self._send(409, b'{"code":"23505","message":"duplicate key value"}')
                return
            srv.table[email] = {"email": email, "source": r.get("source", "unknown")}
            stored.append(srv.table[email])
        if "return=representation" in prefer:
            self._send_json(201, stored)
        else:
            self._send(201, b"")


class SupabaseStoreHTTPTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = _StubPostgREST(("127.0.0.1", 0), _Handler)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.store = SupabaseStore(url=f"http://127.0.0.1:{self.port}", key=FAKE_KEY)

    def tearDown(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)

    # ---- helpers ----
    def _last(self, method: str) -> dict:
        for rec in reversed(self.server.requests):
            if rec["method"] == method:
                return rec
        raise AssertionError(f"no {method} request captured")

    def _assert_auth(self, rec: dict) -> None:
        self.assertEqual(rec["headers"].get("apikey"), FAKE_KEY)
        self.assertEqual(rec["headers"].get("authorization"), f"Bearer {FAKE_KEY}")

    # ---- insert (POST + return=representation) ----
    def test_grant_new_member_inserts_and_returns_created(self) -> None:
        result = self.store.grant("buyer@example.com", source="stripe")
        self.assertEqual(result, {"email": "buyer@example.com", "created": True, "source": "stripe"})
        self.assertIn("buyer@example.com", self.server.table)

        post = self._last("POST")
        self.assertEqual(post["path"], "/rest/v1/members")
        self._assert_auth(post)
        self.assertIn("return=representation", post["headers"].get("prefer", ""))
        self.assertEqual(json.loads(post["body"]), [{"email": "buyer@example.com", "source": "stripe"}])

    # ---- upsert (Prefer: resolution=merge-duplicates + on_conflict=email) ----
    def test_grant_uses_upsert_shape(self) -> None:
        self.store.grant("buyer@example.com", source="stripe")
        post = self._last("POST")
        self.assertIn("on_conflict=email", post["raw_query"])
        self.assertIn("resolution=merge-duplicates", post["headers"].get("prefer", ""))

    # ---- select (GET with eq. filter) + idempotency (created=False, source kept) ----
    def test_grant_existing_member_is_idempotent(self) -> None:
        self.server.table["buyer@example.com"] = {"email": "buyer@example.com", "source": "stripe"}
        result = self.store.grant("buyer@example.com", source="mock")
        # created False, and the ORIGINAL source is preserved (not overwritten).
        self.assertEqual(result, {"email": "buyer@example.com", "created": False, "source": "stripe"})
        # It resolved this via a SELECT with an eq. filter, no POST issued.
        get = self._last("GET")
        self.assertIn("email=eq.", get["raw_query"])
        self.assertNotIn("POST", [r["method"] for r in self.server.requests])

    # ---- has_access (GET with eq. filter + select=email) ----
    def test_has_access_true_and_false(self) -> None:
        self.server.table["member@example.com"] = {"email": "member@example.com", "source": "stripe"}
        self.assertTrue(self.store.has_access("member@example.com"))
        self.assertFalse(self.store.has_access("nobody@example.com"))
        get = self._last("GET")
        self._assert_auth(get)
        self.assertIn("select=email", get["raw_query"])

    def test_has_access_empty_email_is_false_without_call(self) -> None:
        before = len(self.server.requests)
        self.assertFalse(self.store.has_access(""))
        self.assertEqual(len(self.server.requests), before)  # no network for empty email

    # ---- email normalization + URL-encoding of the filter value ----
    def test_email_is_normalized_and_url_encoded_in_filter(self) -> None:
        self.assertFalse(self.store.has_access("  Buyer+Tag@Example.COM "))
        get = self._last("GET")
        # normalized to lowercase/trimmed, and @/+ are percent-encoded in the query
        self.assertIn("email=eq.buyer%2Btag%40example.com", get["raw_query"])

    # ---- all_members (GET select=email,source) ----
    def test_all_members_returns_rows(self) -> None:
        self.server.table["a@example.com"] = {"email": "a@example.com", "source": "stripe"}
        self.server.table["b@example.com"] = {"email": "b@example.com", "source": "mock"}
        members = self.store.all_members()
        self.assertEqual(len(members), 2)
        self.assertEqual({m["email"] for m in members}, {"a@example.com", "b@example.com"})
        get = self._last("GET")
        self.assertIn("select=email,source", get["raw_query"])

    # ---- count (Prefer: count=exact -> Content-Range total) ----
    def test_count_reads_content_range_total(self) -> None:
        for e in ("a@example.com", "b@example.com", "c@example.com"):
            self.server.table[e] = {"email": e, "source": "stripe"}
        self.assertEqual(self.store.count(), 3)
        get = self._last("GET")
        self.assertIn("count=exact", get["headers"].get("prefer", ""))

    def test_count_zero_when_empty(self) -> None:
        self.assertEqual(self.store.count(), 0)

    # ---- round-trip: grant then observe via the same store ----
    def test_grant_then_has_access_and_count(self) -> None:
        self.store.grant("buyer@example.com", source="stripe")
        self.assertTrue(self.store.has_access("buyer@example.com"))
        self.assertEqual(self.store.count(), 1)
        self.assertEqual(self.store.all_members()[0]["email"], "buyer@example.com")

    # ---- error handling (non-2xx) ----
    def test_non_2xx_raises_runtimeerror_without_leaking_key(self) -> None:
        self.server.force_status = 500
        with self.assertRaises(RuntimeError) as ctx:
            self.store.has_access("buyer@example.com")
        msg = str(ctx.exception)
        self.assertIn("500", msg)
        self.assertNotIn(FAKE_KEY, msg)  # the key must never appear in errors

    def test_grant_error_raises_without_leaking_key(self) -> None:
        self.server.force_status = 401
        with self.assertRaises(RuntimeError) as ctx:
            self.store.grant("buyer@example.com")
        self.assertNotIn(FAKE_KEY, str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
