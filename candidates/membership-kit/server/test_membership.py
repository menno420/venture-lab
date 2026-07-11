"""Proves the membership-grant logic AND persistence. Stdlib only — no
network, no Stripe, no Supabase.

Run:  python3 -m unittest test_membership -v
"""
import os
import tempfile
import unittest

from app import (
    JsonFileStore,
    MembershipStore,
    SupabaseStore,
    handle_purchase_event,
    make_store,
    _checkout_event,
)


class MembershipGrantTests(unittest.TestCase):
    """The v0.1 grant contract — now exercised through the real file store."""

    def setUp(self) -> None:
        # Each test gets its own throwaway DB file; the store persists to it.
        fd, self._db_path = tempfile.mkstemp(suffix="-members.json")
        os.close(fd)
        os.unlink(self._db_path)  # start from a clean (non-existent) path
        self.store = JsonFileStore(self._db_path)

    def tearDown(self) -> None:
        for p in (self._db_path, self._db_path + ".tmp"):
            try:
                os.unlink(p)
            except FileNotFoundError:
                pass

    def test_purchase_event_grants_access(self) -> None:
        """A completed-checkout event grants membership + returns a Discord invite."""
        self.assertFalse(self.store.is_member("buyer@example.com"))
        result = handle_purchase_event(self.store, _checkout_event("buyer@example.com"))
        self.assertTrue(result["granted"])
        self.assertTrue(result["new_member"])
        self.assertIn("discord_invite", result)
        self.assertTrue(self.store.is_member("buyer@example.com"))

    def test_unpaid_user_is_denied(self) -> None:
        """An email that never purchased is not a member (gated page would 402)."""
        self.store.grant("paid@example.com", source="mock")
        self.assertTrue(self.store.is_member("paid@example.com"))
        self.assertFalse(self.store.is_member("freeloader@example.com"))

    def test_duplicate_purchase_is_idempotent(self) -> None:
        """Re-processing the same purchase does not create a second membership."""
        event = _checkout_event("buyer@example.com")
        first = handle_purchase_event(self.store, event)
        second = handle_purchase_event(self.store, event)
        self.assertTrue(first["new_member"])
        self.assertFalse(second["new_member"])   # second time: already a member
        self.assertEqual(self.store.count(), 1)  # exactly one membership

    def test_email_is_normalized(self) -> None:
        """Casing/whitespace differences resolve to the same membership."""
        self.store.grant("Buyer@Example.com ")
        self.assertTrue(self.store.is_member("buyer@example.com"))
        self.assertEqual(self.store.count(), 1)

    def test_non_purchase_event_grants_nothing(self) -> None:
        """An unrelated event type is ignored — no membership leaks out."""
        result = handle_purchase_event(self.store, {"type": "invoice.paid", "data": {}})
        self.assertFalse(result["granted"])
        self.assertEqual(self.store.count(), 0)

    def test_grant_requires_email(self) -> None:
        """Granting with an empty email is rejected, not silently accepted."""
        with self.assertRaises(ValueError):
            self.store.grant("")


class JsonFilePersistenceTests(unittest.TestCase):
    """v0.2: membership survives a process restart (re-instantiation)."""

    def setUp(self) -> None:
        fd, self._db_path = tempfile.mkstemp(suffix="-members.json")
        os.close(fd)
        os.unlink(self._db_path)

    def tearDown(self) -> None:
        for p in (self._db_path, self._db_path + ".tmp"):
            try:
                os.unlink(p)
            except FileNotFoundError:
                pass

    def test_fresh_path_starts_empty(self) -> None:
        """A brand-new DB path has no members and writes nothing until a grant."""
        store = JsonFileStore(self._db_path)
        self.assertEqual(store.count(), 0)
        self.assertEqual(store.all_members(), [])
        self.assertFalse(os.path.exists(self._db_path))  # read alone creates no file

    def test_access_survives_restart(self) -> None:
        """Grant, drop the store, re-open the SAME file — access is still there."""
        first = JsonFileStore(self._db_path)
        first.grant("buyer@example.com", source="mock")
        self.assertTrue(first.has_access("buyer@example.com"))

        # Simulate a process restart: a fresh store reading the same file.
        reopened = JsonFileStore(self._db_path)
        self.assertTrue(reopened.has_access("buyer@example.com"))
        self.assertEqual(reopened.count(), 1)
        self.assertEqual(reopened.all_members()[0]["email"], "buyer@example.com")

    def test_grant_idempotent_across_restart(self) -> None:
        """Re-granting after a restart creates no duplicate (created=False)."""
        JsonFileStore(self._db_path).grant("buyer@example.com")

        reopened = JsonFileStore(self._db_path)
        again = reopened.grant("buyer@example.com")
        self.assertFalse(again["created"])   # already persisted before restart
        self.assertEqual(reopened.count(), 1)

    def test_writes_are_atomic_no_temp_left(self) -> None:
        """Atomic write leaves no stray .tmp file behind."""
        store = JsonFileStore(self._db_path)
        store.grant("buyer@example.com")
        self.assertTrue(os.path.exists(self._db_path))
        self.assertFalse(os.path.exists(self._db_path + ".tmp"))

    def test_make_store_defaults_to_json(self) -> None:
        """The factory yields a JsonFileStore for the default backend."""
        os.environ.pop("STORE_BACKEND", None)
        os.environ["MEMBERS_DB_PATH"] = self._db_path
        try:
            store = make_store()
            self.assertIsInstance(store, JsonFileStore)
            self.assertIsInstance(store, MembershipStore)
        finally:
            os.environ.pop("MEMBERS_DB_PATH", None)


class SupabaseStoreConfigTests(unittest.TestCase):
    """The Supabase backend's construction + auth wiring (no network here).

    The HTTP behaviour of the store (insert/select/upsert/count/errors against a
    real PostgREST request/response shape) is proven in test_supabase_store.py,
    which drives it over real HTTP against an in-process stub PostgREST server.
    This suite stays network-free — it only checks construction and the factory.
    """

    def test_missing_keys_raise_actionable_error_at_construction(self) -> None:
        """Direct construction without keys fails fast with a clear message."""
        with self.assertRaises(RuntimeError) as ctx:
            SupabaseStore(url="", key="")
        self.assertIn("STORE_BACKEND=json", str(ctx.exception))

    def test_conforms_to_interface(self) -> None:
        """It implements the same MembershipStore contract as the file store."""
        self.assertTrue(issubclass(SupabaseStore, MembershipStore))
        store = SupabaseStore(url="https://demo.supabase.co", key="fake-key")
        self.assertEqual(store.TABLE, "members")

    def test_auth_headers_use_apikey_and_bearer(self) -> None:
        """Every call carries `apikey` + `Authorization: Bearer <key>` (Supabase
        requires both) — and the key never leaks into anything but headers."""
        store = SupabaseStore(url="https://demo.supabase.co", key="fake-key")
        headers = store._headers()
        self.assertEqual(headers["apikey"], "fake-key")
        self.assertEqual(headers["Authorization"], "Bearer fake-key")

    def test_make_store_supabase_without_keys_falls_back_to_json(self) -> None:
        """STORE_BACKEND=supabase but no keys -> loud fallback to JsonFileStore,
        never a crash and never a silent success (banner goes to stderr)."""
        import app as app_module
        saved_backend = app_module.STORE_BACKEND
        saved_url = os.environ.pop("SUPABASE_URL", None)
        saved_key = os.environ.pop("SUPABASE_KEY", None)
        saved_db = os.environ.get("MEMBERS_DB_PATH")
        app_module.STORE_BACKEND = "supabase"
        os.environ["MEMBERS_DB_PATH"] = self._db_path
        try:
            store = make_store()
            self.assertIsInstance(store, JsonFileStore)
        finally:
            app_module.STORE_BACKEND = saved_backend
            if saved_url is not None:
                os.environ["SUPABASE_URL"] = saved_url
            if saved_key is not None:
                os.environ["SUPABASE_KEY"] = saved_key
            if saved_db is None:
                os.environ.pop("MEMBERS_DB_PATH", None)
            else:
                os.environ["MEMBERS_DB_PATH"] = saved_db

    def setUp(self) -> None:
        fd, self._db_path = tempfile.mkstemp(suffix="-members.json")
        os.close(fd)
        os.unlink(self._db_path)

    def tearDown(self) -> None:
        for p in (self._db_path, self._db_path + ".tmp"):
            try:
                os.unlink(p)
            except FileNotFoundError:
                pass


if __name__ == "__main__":
    unittest.main()
