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

Persistence (v0.2): membership survives process restart. A pluggable
`MembershipStore` seam (see below) selects the backend via env `STORE_BACKEND`:

  * `json` (default, stdlib-only): `JsonFileStore` persists members to a JSON
    file (atomic writes) so a killed-and-restarted process keeps its members.
  * `supabase`: `SupabaseStore` is a drop-in-ready skeleton — same interface,
    swapping to it later is a config flip + filling the documented REST bodies,
    with NO changes to this file.

Run:  python3 app.py           # mock mode on http://localhost:8000
Test: python3 -m unittest test_membership -v

No third-party dependencies. No network in mock/json mode.
"""
from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# --- config (env-gated; placeholders live in .env.example) ---------------
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
DISCORD_INVITE_URL = os.environ.get("DISCORD_INVITE_URL", "https://discord.gg/your-invite")
PRICE_USD = 49
WEB_DIR = Path(__file__).resolve().parent.parent / "web"

# Persistence config. STORE_BACKEND picks the implementation; MEMBERS_DB_PATH
# is the JSON file the default backend writes (kept out of git via .gitignore).
STORE_BACKEND = os.environ.get("STORE_BACKEND", "json").strip().lower()
DEFAULT_MEMBERS_DB_PATH = Path(__file__).resolve().parent / "members.json"


# --- persistence seam ----------------------------------------------------
class MembershipStore(ABC):
    """Membership persistence interface — one email == one member.

    Implementations back the *same* contract so the HTTP layer never knows or
    cares where members live. Granting is idempotent: granting an existing
    member creates no duplicate and reports ``created=False``.

    Swapping local JSON for hosted Supabase (or anything else) is a matter of
    adding an implementation and flipping ``STORE_BACKEND`` — no app.py rework.
    """

    @abstractmethod
    def grant(self, email: str, source: str = "unknown") -> dict:
        """Grant membership idempotently.

        Returns ``{"email", "created": bool, "source"}`` — ``created`` is False
        when the member already existed. Raises ``ValueError`` on empty email.
        """

    @abstractmethod
    def has_access(self, email: str) -> bool:
        """True when ``email`` is an active member."""

    @abstractmethod
    def all_members(self) -> list:
        """Return every member record (list of dicts)."""

    @abstractmethod
    def count(self) -> int:
        """Number of members."""

    # ---- shared helpers (concrete on the interface) ----
    def is_member(self, email: str) -> bool:
        """Back-compat alias for :meth:`has_access`."""
        return self.has_access(email)

    @staticmethod
    def _normalize(email: str) -> str:
        return (email or "").strip().lower()


class JsonFileStore(MembershipStore):
    """Default backend: persist members to a JSON file with atomic writes.

    This is the real v0.2 win — members survive a process restart. Writes go
    to a temp file in the same directory then ``os.replace`` into place, so a
    crash mid-write never corrupts the live file. Stdlib only; no network.
    """

    def __init__(self, path: str | os.PathLike | None = None) -> None:
        self._path = Path(path) if path else DEFAULT_MEMBERS_DB_PATH
        self._members: dict[str, dict] = self._load()

    def _load(self) -> dict[str, dict]:
        try:
            raw = self._path.read_text(encoding="utf-8")
        except (FileNotFoundError, OSError):
            return {}
        try:
            data = json.loads(raw or "{}")
        except json.JSONDecodeError:
            return {}
        members = data.get("members") if isinstance(data, dict) else None
        return dict(members) if isinstance(members, dict) else {}

    def _save(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps({"members": self._members}, indent=2)
        tmp = self._path.parent / (self._path.name + ".tmp")
        tmp.write_text(payload, encoding="utf-8")
        os.replace(tmp, self._path)  # atomic on POSIX + Windows

    def grant(self, email: str, source: str = "unknown") -> dict:
        key = self._normalize(email)
        if not key:
            raise ValueError("email required to grant membership")
        if key in self._members:
            return {"email": key, "created": False, "source": self._members[key]["source"]}
        self._members[key] = {"email": key, "source": source}
        self._save()
        return {"email": key, "created": True, "source": source}

    def has_access(self, email: str) -> bool:
        return self._normalize(email) in self._members

    def all_members(self) -> list:
        return [dict(rec) for rec in self._members.values()]

    def count(self) -> int:
        return len(self._members)


class SupabaseStore(MembershipStore):
    """Drop-in-ready hosted backend (skeleton).

    Same interface as :class:`JsonFileStore`. The point of v0.2 is that going
    live is a *config flip* (``STORE_BACKEND=supabase`` + keys) and filling the
    documented PostgREST bodies below — with **no** change to app.py.

    Guardrails:
      * No top-level ``supabase`` import — importing this module never crashes
        because a package is missing.
      * The constructor is the single startup gate: selecting this backend
        without ``SUPABASE_URL``/``SUPABASE_KEY`` raises a clear, actionable
        error instead of failing later mid-request.
    """

    TABLE = "members"

    def __init__(self, url: str | None = None, key: str | None = None) -> None:
        self._url = (url if url is not None else os.environ.get("SUPABASE_URL", "")).rstrip("/")
        self._key = key if key is not None else os.environ.get("SUPABASE_KEY", "")
        if not (self._url and self._key):
            raise RuntimeError(
                "STORE_BACKEND=supabase selected but SUPABASE_URL/SUPABASE_KEY "
                "are unset. Set both env vars, or use STORE_BACKEND=json for "
                "local file persistence."
            )

    def _headers(self) -> dict:
        # Shared auth headers for every PostgREST call.
        return {
            "apikey": self._key,
            "Authorization": f"Bearer {self._key}",
            "Content-Type": "application/json",
        }

    def grant(self, email: str, source: str = "unknown") -> dict:
        key = self._normalize(email)
        if not key:
            raise ValueError("email required to grant membership")
        # DROP-IN: idempotent upsert via PostgREST.
        #   POST {self._url}/rest/v1/{self.TABLE}?on_conflict=email
        #   headers: {**self._headers(),
        #             "Prefer": "resolution=merge-duplicates,return=representation"}
        #   body:    json.dumps({"email": key, "source": source})
        #   -> parse response; created = HTTP 201 / row not previously present.
        #   return {"email": key, "created": <bool>, "source": source}
        raise NotImplementedError(
            "SupabaseStore.grant is a drop-in skeleton — fill the PostgREST "
            "upsert (shape documented above). Use STORE_BACKEND=json until then."
        )

    def has_access(self, email: str) -> bool:
        key = self._normalize(email)
        # DROP-IN:
        #   GET {self._url}/rest/v1/{self.TABLE}?email=eq.{key}&select=email&limit=1
        #   headers: self._headers()
        #   -> return bool(response_json)
        _ = key
        raise NotImplementedError(
            "SupabaseStore.has_access is a drop-in skeleton — fill the "
            "PostgREST select (shape documented above)."
        )

    def all_members(self) -> list:
        # DROP-IN:
        #   GET {self._url}/rest/v1/{self.TABLE}?select=email,source
        #   headers: self._headers()  -> return response_json (list of dicts)
        raise NotImplementedError(
            "SupabaseStore.all_members is a drop-in skeleton — fill the "
            "PostgREST select (shape documented above)."
        )

    def count(self) -> int:
        # DROP-IN:
        #   GET {self._url}/rest/v1/{self.TABLE}?select=email
        #   headers: {**self._headers(), "Prefer": "count=exact"}
        #   -> read the Content-Range header count.
        raise NotImplementedError(
            "SupabaseStore.count is a drop-in skeleton — fill the PostgREST "
            "count (shape documented above)."
        )


def make_store() -> MembershipStore:
    """Build the configured store. Called once at startup; raises clearly on
    a bad backend selection so misconfiguration fails fast, not mid-request."""
    if STORE_BACKEND == "json":
        return JsonFileStore(os.environ.get("MEMBERS_DB_PATH") or DEFAULT_MEMBERS_DB_PATH)
    if STORE_BACKEND == "supabase":
        return SupabaseStore()
    raise RuntimeError(
        f"unknown STORE_BACKEND {STORE_BACKEND!r} — use 'json' (default) or 'supabase'."
    )


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
STORE = make_store()


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
            self._json(200, {
                "status": "ok",
                "mode": _mode(),
                "store": STORE_BACKEND,
                "members": STORE.count(),
            })
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
    print(f"membership-kit backend | mode={_mode()} | store={STORE_BACKEND} | http://localhost:{port}")
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
