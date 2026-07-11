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

import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

# --- config (env-gated; placeholders live in .env.example) ---------------
# NOTE: the request handlers read the Stripe env vars *live* (see the
# `_stripe_secret_key()` / `_webhook_secret()` helpers) rather than these
# import-time snapshots, so the same process can be flipped between mock and
# real mode (and so the HTTP tests can exercise both). These module constants
# are the import-time view, kept for documentation/back-compat.
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
DISCORD_INVITE_URL = os.environ.get("DISCORD_INVITE_URL", "https://discord.gg/your-invite")
PRICE_USD = 49
WEB_DIR = Path(__file__).resolve().parent.parent / "web"

# D3: never a silent success. When running without real keys the server is in
# MOCK mode (no real payments) and says so LOUDLY — a startup banner on stderr
# and this warning field in every /webhook and /create-checkout-session reply.
MOCK_WARNING = (
    "MOCK MODE — no real payments. Set STRIPE_SECRET_KEY and "
    "STRIPE_WEBHOOK_SECRET to take the real Stripe path."
)

# Same "never a silent success" posture for the storage layer: selecting the
# hosted Supabase backend without its env vars must never quietly break the
# server. `make_store()` warns LOUDLY (this text, via `_loud_banner`) and falls
# back to the local file store — mirroring the MOCK-mode banner style.
SUPABASE_FALLBACK_WARNING = (
    "SUPABASE FALLBACK — STORE_BACKEND=supabase but SUPABASE_URL/SUPABASE_KEY "
    "are unset. Falling back to local JSON file persistence. Set BOTH env vars "
    "(NAMES only — never paste a key value into the repo) to use the hosted "
    "Supabase store."
)


def _loud_banner(message: str) -> None:
    """Print an unmissable ``!!!``-barred banner to stderr (never a silent state)."""
    bar = "!" * len(message)
    print(f"\n{bar}\n{message}\n{bar}\n", file=sys.stderr, flush=True)

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

    def record_session(self, session_id: str, email: str) -> None:
        """Remember which buyer a Checkout Session id belongs to.

        Stripe's `success_url` can only interpolate `{CHECKOUT_SESSION_ID}`, so
        the success page arrives knowing the *session id*, not the email. The
        webhook records the id→email link here at grant time; the `/members`
        route resolves the buyer back from it. Kept in-process (the redirect
        follows the webhook within seconds); no-op on empty inputs.
        """
        if not session_id or not email:
            return
        sessions = getattr(self, "_sessions", None)
        if sessions is None:
            sessions = {}
            self._sessions = sessions
        sessions[session_id] = self._normalize(email)

    def email_for_session(self, session_id: str) -> str | None:
        """Return the buyer email for a recorded Checkout Session id, or None."""
        if not session_id:
            return None
        return getattr(self, "_sessions", {}).get(session_id)

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
    """Hosted backend — persists members in Supabase via its PostgREST REST API.

    Same interface as :class:`JsonFileStore`, so going hosted is a *config flip*
    (``STORE_BACKEND=supabase`` + ``SUPABASE_URL``/``SUPABASE_KEY``) with **no**
    change to app.py. Talks to Supabase over its REST endpoint
    ``{SUPABASE_URL}/rest/v1/{TABLE}`` using **stdlib ``urllib`` only** — no
    ``supabase`` package, no third-party HTTP client (matching the kit's
    zero-dependency posture). Auth on every call is the pair Supabase requires:
    an ``apikey`` header and an ``Authorization: Bearer <key>`` header.

    ``SUPABASE_KEY`` should be the project's **service_role** key: the store
    performs server-side reads and writes to the members table, so it needs a
    key that bypasses row-level security. The key is read from the environment,
    sent only as request headers, and **never logged or echoed** — error
    messages carry the HTTP status and response body, never the key.

    Requires a ``members`` table (``email`` unique/PK, ``source`` text) in the
    owner's Supabase project — see the OWNER-ACTION in ``server/README.md``.

    Guardrails:
      * No top-level ``supabase`` import — importing this module never crashes
        because a package is missing.
      * Direct construction without keys raises a clear, actionable error. The
        server never crashes on this, though: ``make_store()`` catches it, warns
        loudly, and falls back to the local JSON store (see ``make_store``).
    """

    TABLE = "members"
    TIMEOUT = 10  # seconds per PostgREST call

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
        # Shared auth headers for every PostgREST call. Supabase requires BOTH
        # `apikey` and `Authorization: Bearer <key>` (verified against the
        # Supabase REST docs — see server/README.md provenance).
        return {
            "apikey": self._key,
            "Authorization": f"Bearer {self._key}",
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        *,
        query: str = "",
        body: object | None = None,
        extra_headers: dict | None = None,
    ) -> tuple[int, object, object]:
        """Make one PostgREST call and return ``(status, headers, parsed_body)``.

        Raises ``RuntimeError`` on any non-2xx response or transport failure.
        The raised message includes the HTTP status and (truncated) response
        body for debuggability but **never** the ``SUPABASE_KEY`` value — the
        key lives only in request headers, which are not echoed here.
        """
        url = f"{self._url}/rest/v1/{self.TABLE}"
        if query:
            url = f"{url}?{query}"
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.TIMEOUT) as resp:
                status = resp.status
                resp_headers = resp.headers
                raw = resp.read()
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:500]
            # Note: exc carries the request URL (never the key) — safe to omit.
            raise RuntimeError(
                f"Supabase {method} {self.TABLE} failed: HTTP {exc.code} {detail}"
            ) from None
        except urllib.error.URLError as exc:
            raise RuntimeError(
                f"Supabase {method} {self.TABLE} unreachable: {exc.reason}"
            ) from None
        parsed = json.loads(raw) if raw else None
        return status, resp_headers, parsed

    def _select_one(self, key: str) -> dict | None:
        """Return the stored row for ``key`` (email/source) or ``None``."""
        _, _, rows = self._request(
            "GET",
            query=f"email=eq.{quote(key, safe='')}&select=email,source&limit=1",
        )
        if isinstance(rows, list) and rows:
            return rows[0]
        return None

    def grant(self, email: str, source: str = "unknown") -> dict:
        key = self._normalize(email)
        if not key:
            raise ValueError("email required to grant membership")
        # Idempotent like JsonFileStore: an already-present member keeps its
        # ORIGINAL source and reports created=False. Check-then-insert so we
        # never clobber an existing source.
        existing = self._select_one(key)
        if existing is not None:
            return {"email": key, "created": False, "source": existing.get("source", source)}
        # Insert the new member. `Prefer: return=representation` sends the stored
        # row back (201); `resolution=merge-duplicates` + `on_conflict=email`
        # makes this an UPSERT, so a concurrent grant that raced us in between
        # the select above and here merges instead of erroring on the unique
        # constraint. (PostgREST upsert shape — see server/README.md provenance.)
        _, _, rows = self._request(
            "POST",
            query="on_conflict=email",
            body=[{"email": key, "source": source}],
            extra_headers={"Prefer": "resolution=merge-duplicates,return=representation"},
        )
        stored = rows[0] if isinstance(rows, list) and rows else {}
        return {
            "email": stored.get("email", key),
            "created": True,
            "source": stored.get("source", source),
        }

    def has_access(self, email: str) -> bool:
        key = self._normalize(email)
        if not key:
            return False
        # GET {url}/rest/v1/members?email=eq.<key>&select=email&limit=1 -> [] or [row].
        _, _, rows = self._request(
            "GET",
            query=f"email=eq.{quote(key, safe='')}&select=email&limit=1",
        )
        return bool(rows)

    def all_members(self) -> list:
        # GET {url}/rest/v1/members?select=email,source -> list of dicts.
        _, _, rows = self._request("GET", query="select=email,source")
        return rows if isinstance(rows, list) else []

    def count(self) -> int:
        # `Prefer: count=exact` returns the total in the Content-Range response
        # header ("start-end/total", e.g. "0-0/42"; "*/0" when empty). `Range:
        # 0-0` fetches zero rows but still reports the count, so we never pull
        # the whole table just to size it. (PostgREST count shape — provenance
        # in server/README.md.)
        _, resp_headers, _ = self._request(
            "GET",
            query="select=email",
            extra_headers={"Prefer": "count=exact", "Range-Unit": "items", "Range": "0-0"},
        )
        content_range = resp_headers.get("Content-Range", "") if resp_headers else ""
        total = content_range.rsplit("/", 1)[-1] if "/" in content_range else ""
        try:
            return int(total)
        except (TypeError, ValueError):
            return 0


def _json_store() -> JsonFileStore:
    return JsonFileStore(os.environ.get("MEMBERS_DB_PATH") or DEFAULT_MEMBERS_DB_PATH)


def make_store() -> MembershipStore:
    """Build the configured store. Called once at startup.

    Local file persistence (``STORE_BACKEND=json``) is the DEFAULT. Selecting
    ``STORE_BACKEND=supabase`` without ``SUPABASE_URL``/``SUPABASE_KEY`` does not
    crash the server: it warns LOUDLY (MOCK-banner style) and falls back to the
    local file store — never a silent success, never a hard stop on a
    misconfigured hosted backend. An unknown backend name still fails fast."""
    if STORE_BACKEND == "json":
        return _json_store()
    if STORE_BACKEND == "supabase":
        try:
            return SupabaseStore()
        except RuntimeError:
            _loud_banner(SUPABASE_FALLBACK_WARNING)
            return _json_store()
    raise RuntimeError(
        f"unknown STORE_BACKEND {STORE_BACKEND!r} — use 'json' (default) or 'supabase'."
    )


def handle_purchase_event(store: MembershipStore, event: dict) -> dict:
    """Grant membership from a purchase event and (in prod) fire the Discord invite.

    Shared by BOTH the mock route and the real Stripe `/webhook` handler, so the
    exact grant logic under test is the logic that runs in production.

    `event` shape (the REAL live Stripe checkout event):
        {"type": "checkout.session.completed",
         "data": {"object": {"id": "cs_...",
                             "customer_email": null,
                             "customer_details": {"email": "buyer@example.com"}}}}
    The buyer email is read PREFERRING `customer_details.email` (the real live
    shape — top-level `customer_email` is `null` on a normal completion) and
    FALLING BACK to top-level `customer_email` (legacy / guest-prefill case).
    Returns a result dict including the Discord invite that would be delivered.
    """
    if event.get("type") != "checkout.session.completed":
        return {"granted": False, "reason": f"ignored event type {event.get('type')!r}"}

    obj = event.get("data", {}).get("object", {}) or {}
    details = obj.get("customer_details") or {}
    email = details.get("email") or obj.get("customer_email")
    session_id = obj.get("id")
    if not email:
        return {"granted": False, "reason": "no customer email on event"}

    result = store.grant(email, source="stripe" if _stripe_secret_key() else "mock")
    # Record session_id -> email so the {CHECKOUT_SESSION_ID} success page can
    # resolve the buyer back to their membership.
    if session_id:
        store.record_session(session_id, result["email"])
    invite = _deliver_discord_invite(result["email"]) if result["created"] else None
    return {
        "granted": True,
        "email": result["email"],
        "new_member": result["created"],
        "session_id": session_id,
        "discord_invite": invite or DISCORD_INVITE_URL,
    }


def _deliver_discord_invite(email: str) -> str:
    """In production this would POST to the Discord API to mint/send an invite.

    v0.1: returns the configured invite URL. The real API call is an owner-gated
    next step (needs a Discord bot token) and is intentionally not performed.
    """
    return DISCORD_INVITE_URL


# --- live env-gating helpers ---------------------------------------------
# Read at REQUEST time (not import time) so one running process can be flipped
# between mock and real mode, and so the HTTP tests can drive both paths.
def _stripe_secret_key() -> str:
    return os.environ.get("STRIPE_SECRET_KEY", "")


def _webhook_secret() -> str:
    return os.environ.get("STRIPE_WEBHOOK_SECRET", "")


def _is_mock() -> bool:
    """Mock mode = running WITHOUT any real Stripe key. Never a silent success."""
    return not (_stripe_secret_key() or _webhook_secret())


# --- native Stripe webhook signature verification ------------------------
def verify_stripe_signature(raw: bytes, sig_header: str, secret: str, tolerance: int = 300) -> None:
    """Verify a Stripe `Stripe-Signature` header over the RAW request body.

    Re-implements Stripe's scheme with stdlib only (no `stripe` package, no live
    keys), so the real signature path is testable:

      * Header shape: ``t=<unix_ts>,v1=<hex>`` (there may be multiple ``v1=``).
      * ``<hex>`` = hex HMAC-SHA256 of the bytes ``f"{t}.".encode() + raw``,
        keyed by the ``whsec_...`` secret.
      * Constant-time compare against any provided ``v1``.
      * Enforce ``|now - t| <= tolerance`` (default 300s).

    Raises ``ValueError`` on any failure (missing header, no timestamp, no
    signature, no match, or a stale timestamp). Returns ``None`` on success.
    (Source of scheme: stripe-go webhook/client.go.)
    """
    if not sig_header:
        raise ValueError("missing Stripe-Signature header")

    timestamp: str | None = None
    signatures: list[str] = []
    for part in sig_header.split(","):
        key, sep, value = part.partition("=")
        if not sep:
            continue
        key = key.strip()
        value = value.strip()
        if key == "t":
            timestamp = value
        elif key == "v1":
            signatures.append(value)

    if timestamp is None:
        raise ValueError("no timestamp (t=) in Stripe-Signature header")
    if not signatures:
        raise ValueError("no v1 signature in Stripe-Signature header")
    try:
        ts = int(timestamp)
    except ValueError:
        raise ValueError("malformed timestamp in Stripe-Signature header")

    signed_payload = f"{ts}.".encode("utf-8") + raw
    expected = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    if not any(hmac.compare_digest(expected, sig) for sig in signatures):
        raise ValueError("no matching v1 signature")
    if abs(int(time.time()) - ts) > tolerance:
        raise ValueError(f"timestamp outside tolerance ({tolerance}s)")
    return None


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
            # Resolve the buyer. Preferred: ?session_id= (what Stripe's
            # {CHECKOUT_SESSION_ID} success_url lands with) -> look up the email
            # recorded at grant time. Fallback: ?email= (legacy).
            session_id = query.get("session_id", [""])[0]
            email = query.get("email", [""])[0]
            if session_id:
                resolved = STORE.email_for_session(session_id)
                if resolved:
                    email = resolved
            if email and STORE.is_member(email):
                # access granted -> serve the gated page
                self._serve_file("members.html")
            else:
                self._json(402, {
                    "error": "payment required",
                    "message": "No active membership for this session/email. Purchase to unlock.",
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
            # Accept the buyer email from the query string or a JSON POST body.
            # Passing it to Stripe as customer_email makes the webhook deterministic.
            email = query.get("email", [""])[0]
            if not email and raw:
                try:
                    body = json.loads(raw)
                    if isinstance(body, dict):
                        email = body.get("email", "") or ""
                except json.JSONDecodeError:
                    pass

            if _stripe_secret_key():
                # REAL Stripe path — guarded so the file runs without `stripe`.
                import stripe  # noqa: PLC0415  (deliberately lazy, env-gated)
                stripe.api_key = _stripe_secret_key()
                params = {
                    "mode": "payment",
                    "line_items": [{
                        "price_data": {
                            "currency": "usd",
                            "unit_amount": PRICE_USD * 100,
                            "product_data": {"name": "Membership-Site Boilerplate Kit"},
                        },
                        "quantity": 1,
                    }],
                    # Stripe expands {CHECKOUT_SESSION_ID} ONLY (not {CHECKOUT_EMAIL}).
                    "success_url": "http://localhost:8000/members?session_id={CHECKOUT_SESSION_ID}",
                    "cancel_url": "http://localhost:8000/",
                }
                if email:
                    params["customer_email"] = email
                session = stripe.checkout.Session.create(**params)
                self._json(200, {"mode": "stripe", "checkout_url": session.url})
            else:
                self._json(200, {
                    "mode": "mock",
                    "warning": MOCK_WARNING,
                    "message": "Stripe not configured. Use POST /mock-purchase?email=... to simulate a purchase.",
                })

        elif route == "/webhook":
            # Stripe webhook. When STRIPE_WEBHOOK_SECRET is set we verify the
            # signature natively over the RAW body BEFORE parsing/granting, and
            # reject with HTTP 400 on any failure. No `stripe` package required.
            # When it is NOT set we split by mode: FULL mock (no keys at all)
            # accepts an unsigned body with a loud warning; a PARTIAL/misconfigured
            # deploy (real key set, webhook secret missing) FAILS CLOSED — it must
            # never grant from an unsigned webhook while real checkout is live.
            secret = _webhook_secret()
            if secret:
                sig = self.headers.get("Stripe-Signature", "")
                try:
                    verify_stripe_signature(raw, sig, secret)
                except ValueError as exc:  # signature/timestamp failure -> reject
                    self._json(400, {"error": f"invalid signature: {exc}"})
                    return
                try:
                    event = json.loads(raw or b"{}")
                except json.JSONDecodeError:
                    self._json(400, {"error": "invalid JSON body"})
                    return
                result = handle_purchase_event(STORE, event)
                self._json(200, {"mode": "stripe", **result})
            elif not _is_mock():
                # FAIL CLOSED on a partial / misconfigured deploy: STRIPE_SECRET_KEY
                # is set (real checkout is live) but STRIPE_WEBHOOK_SECRET is missing,
                # so signatures CANNOT be verified. Never grant membership from an
                # unsigned webhook body in a money-live deploy — a buyer who forgets
                # the webhook secret would otherwise let anyone POST unsigned JSON and
                # mint free memberships. Reject loudly instead of falling open.
                self._json(400, {
                    "error": (
                        "misconfigured: STRIPE_WEBHOOK_SECRET is required when "
                        "STRIPE_SECRET_KEY is set. Refusing to grant membership "
                        "from an unsigned webhook. Set STRIPE_WEBHOOK_SECRET "
                        "(whsec_...), or unset STRIPE_SECRET_KEY to run in mock mode."
                    ),
                })
                return
            else:
                # FULL MOCK (no Stripe keys at all): accept a raw JSON event body
                # (no signature check) but NEVER a silent success — loud warning.
                try:
                    event = json.loads(raw or b"{}")
                except json.JSONDecodeError:
                    self._json(400, {"error": "invalid JSON body"})
                    return
                result = handle_purchase_event(STORE, event)
                self._json(200, {"mode": "mock", "warning": MOCK_WARNING, **result})

        else:
            self._send(404, b"not found")


def _checkout_event(email: str) -> dict:
    """Build a checkout.session.completed event for the given buyer email."""
    return {
        "type": "checkout.session.completed",
        "data": {"object": {"customer_email": email}},
    }


def _mode() -> str:
    return "mock" if _is_mock() else "stripe"


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    if _is_mock():
        # D3: loud, unmissable — no real payments happen in this mode.
        _loud_banner(
            "!!! MOCK MODE: no real payments — set STRIPE_SECRET_KEY and "
            "STRIPE_WEBHOOK_SECRET for real Stripe !!!"
        )
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
