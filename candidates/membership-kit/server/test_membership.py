"""Proves the membership-grant logic. Stdlib only — no network, no Stripe.

Run:  python3 -m unittest test_membership -v
"""
import unittest

from app import MembershipStore, handle_purchase_event, _checkout_event


class MembershipGrantTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = MembershipStore()

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


if __name__ == "__main__":
    unittest.main()
