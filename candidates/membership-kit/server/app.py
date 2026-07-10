#!/usr/bin/env python3
"""Membership-Site Boilerplate Kit — minimal backend (stdlib only).

Two modes, one file:

  * MOCK mode (default): runs with ZERO accounts/keys. `/mock-purchase` grants
    membership exactly like a real Stripe webhook would, so the whole
    purchase -> access flow is demonstrable now.

  * REAL Stripe mode: enabled when STRIPE_SECRET_KEY is set in the environment.
    `/create-checkout-session` and `/webhook` take the real Stripe path. Every
    real Stripe call is guarded by `if STRIPE_SECRET_KEY:` so this file imports
    and runs with NO `stripe` package installed.

Run:  python3 app.py           # mock mode on http://localhost:8000
Test: python3 -m unittest test_membership -v

No third-party dependencies. No network in mock mode.
"""
from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# --- config (env-gated; placeholders live in .env.example) ---------------
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
DISCORD_INVITE_URL = os.environ.get("DISCORD_INVITE_URL", "https://discord.gg/your-invite")
PRICE_USD = 49
WEB_DIR = Path(__file__).resolve().parent.parent / "web"


# --- membership core (the part the tests exercise) -----------------------
class MembershipStore:
    """In-memory membership store. Swap for Supabase in production.

    A member is identified by email. Granting is idempotent: granting an
    existing member does not create a duplicate and is reported as such.
    """

    def __init__(self) -> None:
        self._members: dict[str, dict] = {}

    def is_member(self, email: str) -> bool:
        return self._normalize(email) in self._members

    def grant(self, email: str, source: str = "unknown") -> dict:
        """Grant membership. Idempotent — returns the record + whether it was new."""
        key = self._normalize(email)
        if not key:
            raise ValueError("email required to grant membership")
        if key in self._members:
            return {"email": key, "created": False, "source": self._members[key]["source"]}
        self._members[key] = {"email": key, "source": source}
        return {"email": key, "created": True, "source": source}

    def count(self) -> int:
        return len(self._members)

    @staticmethod
    def _normalize(email: str) -> str:
        return (email or "").strip().lower()


def handle_purchase_event(store: MembershipStore, event: dict) -> dict:
    """Grant membership from a purchase event and (in prod) fire the Discord invite.

    Shared by BOTH the mock route and the real Stripe `/webhook` handler, so the
    exact grant logic under test is the logic that runs in production.

    `event` shape (mirrors the fields we read off a Stripe checkout event):
        {"type": "checkout.session.completed",
         "data": {"object": {"customer_email": "buyer@example.com"}}}
    Returns a result dict including the Discord invite that would be delivered.
    """
    if event.get("type") != "checkout.session.completed":
        return {"granted": False, "reason": f"ignored event type {event.get('type')!r}"}

    email = (
        event.get("data", {})
        .get("object", {})
        .get("customer_email")
    )
    if not email:
        return {"granted": False, "reason": "no customer_email on event"}

    result = store.grant(email, source="stripe" if STRIPE_SECRET_KEY else "mock")
    invite = _deliver_discord_invite(email) if result["created"] else None
    return {
        "granted": True,
        "email": result["email"],
        "new_member": result["created"],
        "discord_invite": invite or DISCORD_INVITE_URL,
    }


def _deliver_discord_invite(email: str) -> str:
    """In production this would POST to the Discord API to mint/send an invite.

    v0.1: returns the configured invite URL. The real API call is an owner-gated
    next step (needs a Discord bot token) and is intentionally not performed.
    """
    return DISCORD_INVITE_URL


# --- HTTP layer ----------------------------------------------------------
STORE = MembershipStore()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args) -> None:  # quieter test/dev output
        pass

    # ---- helpers ----
    def _send(self, code: int, body: bytes, content_type: str = "text/plain; charset=utf-8") -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj: dict) -> None:
        self._send(code, json.dumps(obj, indent=2).encode(), "application/json")

    def _serve_file(self, name: str, code: int = 200) -> None:
        path = WEB_DIR / name
        if not path.exists():
            self._send(404, b"not found")
            return
        ctype = "text/html; charset=utf-8" if name.endswith(".html") else "text/css; charset=utf-8"
        self._send(code, path.read_bytes(), ctype)

    # ---- routing ----
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path
        query = parse_qs(parsed.query)

        if route in ("/", "/index.html"):
            self._serve_file("index.html")
        elif route == "/styles.css":
            self._serve_file("styles.css")
        elif route == "/members":
            email = (query.get("email", [""])[0])
            if STORE.is_member(email):
                # access granted -> serve the gated page
                self._serve_file("members.html")
            else:
                self._json(402, {
                    "error": "payment required",
                    "message": "No active membership for this email. Purchase to unlock.",
                    "checkout": "/create-checkout-session",
                })
        elif route == "/health":
            self._json(200, {"status": "ok", "mode": _mode(), "members": STORE.count()})
        else:
            self._send(404, b"not found")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path
        query = parse_qs(parsed.query)
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b""

        if route == "/mock-purchase":
            # MOCK: grant membership with zero accounts. Mirrors a real webhook.
            email = query.get("email", [""])[0]
            if not email:
                self._json(400, {"error": "email query param required"})
                return
            event = _checkout_event(email)
            result = handle_purchase_event(STORE, event)
            self._json(200, {"mode": "mock", **result})

        elif route == "/create-checkout-session":
            if STRIPE_SECRET_KEY:
                # REAL Stripe path — guarded so the file runs without `stripe`.
                import stripe  # noqa: PLC0415  (deliberately lazy, env-gated)
                stripe.api_key = STRIPE_SECRET_KEY
                session = stripe.checkout.Session.create(
                    mode="payment",
                    line_items=[{
                        "price_data": {
                            "currency": "usd",
                            "unit_amount": PRICE_USD * 100,
                            "product_data": {"name": "Membership-Site Boilerplate Kit"},
                        },
                        "quantity": 1,
                    }],
                    success_url="http://localhost:8000/members?email={CHECKOUT_EMAIL}",
                    cancel_url="http://localhost:8000/",
                )
                self._json(200, {"mode": "stripe", "checkout_url": session.url})
            else:
                self._json(200, {
                    "mode": "mock",
                    "message": "Stripe not configured. Use POST /mock-purchase?email=... to simulate a purchase.",
                })

        elif route == "/webhook":
            # Stripe webhook. In real mode we verify the signature, then grant.
            if STRIPE_SECRET_KEY:
                import stripe  # noqa: PLC0415
                sig = self.headers.get("Stripe-Signature", "")
                try:
                    event = stripe.Webhook.construct_event(raw, sig, STRIPE_WEBHOOK_SECRET)
                except Exception as exc:  # signature failure -> reject
                    self._json(400, {"error": f"invalid signature: {exc}"})
                    return
            else:
                # Mock: accept a raw JSON event body (no signature check).
                try:
                    event = json.loads(raw or b"{}")
                except json.JSONDecodeError:
                    self._json(400, {"error": "invalid JSON body"})
                    return
            result = handle_purchase_event(STORE, event)
            self._json(200, {"mode": _mode(), **result})

        else:
            self._send(404, b"not found")


def _checkout_event(email: str) -> dict:
    """Build a checkout.session.completed event for the given buyer email."""
    return {
        "type": "checkout.session.completed",
        "data": {"object": {"customer_email": email}},
    }


def _mode() -> str:
    return "stripe" if STRIPE_SECRET_KEY else "mock"


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"membership-kit backend | mode={_mode()} | http://localhost:{port}")
    if _mode() == "mock":
        print("  MOCK mode (no keys). Try:")
        print(f"    curl -X POST 'http://localhost:{port}/mock-purchase?email=buyer@example.com'")
        print(f"    curl 'http://localhost:{port}/members?email=buyer@example.com'")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
