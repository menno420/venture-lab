#!/usr/bin/env python3
"""Stripe Webhook Test Kit (swtk) — fire REAL-shape signed Stripe events at your
local webhook endpoint and check your handler the way Stripe actually behaves.

Stdlib only. No pip install, no build step. Python 3.8+.

What it checks (see GOTCHAS.md for the why):
  1. fire            — your handler ACCEPTS a correctly-signed real event (2xx).
  2. fire --forge    — your handler REJECTS a forged/badly-signed event (4xx),
                       instead of silently accepting it.
  3. check-email     — the buyer email is read from customer_details.email;
                       top-level customer_email is null on a normal Checkout
                       completion (the #1 gotcha this kit exists for).
  4. lint-url        — your success_url uses ONLY {CHECKOUT_SESSION_ID}; anything
                       else (e.g. {CHECKOUT_EMAIL}) is a placeholder Stripe never
                       expands, so it lands in the buyer's browser verbatim.

The webhook signing secret is read from an environment variable (NAME only — the
value is never stored, logged, or echoed by this tool). Default: SWTK_WEBHOOK_SECRET.
"""
import argparse
import hashlib
import hmac
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_SECRET_ENV = "SWTK_WEBHOOK_SECRET"

# Stripe expands exactly one placeholder in success_url / cancel_url.
# Verified against Stripe's documented Checkout behaviour (see fixtures/PROVENANCE.md).
VALID_URL_PLACEHOLDERS = {"CHECKOUT_SESSION_ID"}
_PLACEHOLDER_RE = re.compile(r"\{([A-Za-z0-9_]+)\}")

# stripe-go webhook/client.go: DefaultTolerance = 300 * time.Second
DEFAULT_TOLERANCE = 300


# --------------------------------------------------------------------------- #
# Signature — the real Stripe-Signature scheme (t=<ts>,v1=<hex hmac-sha256>).
# Scheme verified verbatim against stripe-go webhook/client.go; see PROVENANCE.md.
# --------------------------------------------------------------------------- #
def stripe_signature(payload: bytes, secret: str, timestamp: int) -> str:
    """Build a real Stripe-Signature header for `payload` signed at `timestamp`.

    signed_payload = f"{timestamp}." + raw_body
    v1             = hex( HMAC-SHA256(secret, signed_payload) )
    header         = f"t={timestamp},v1={v1}"
    """
    signed_payload = str(int(timestamp)).encode("utf-8") + b"." + payload
    v1 = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    return f"t={int(timestamp)},v1={v1}"


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def fixture_path(name: str) -> Path:
    return FIXTURES_DIR / (name if name.endswith(".json") else name + ".json")


def load_fixture(name: str) -> bytes:
    p = fixture_path(name)
    if not p.exists():
        raise SystemExit(f"error: fixture not found: {p.name}. Run `swtk list` to see bundled fixtures.")
    return p.read_bytes()


def list_fixtures():
    return sorted(p.name for p in FIXTURES_DIR.glob("*.json"))


# --------------------------------------------------------------------------- #
# The two gotcha checks
# --------------------------------------------------------------------------- #
def resolve_buyer_email(session_obj: dict):
    """Read the buyer email the way a CORRECT handler must:
    prefer customer_details.email, fall back to top-level customer_email.

    Returns (email, source) where source is the field it came from, or (None, None).
    """
    details = session_obj.get("customer_details") or {}
    if details.get("email"):
        return details["email"], "customer_details.email"
    if session_obj.get("customer_email"):
        return session_obj["customer_email"], "customer_email"
    return None, None


def lint_success_url(url: str):
    """Return a list of issues (each {"level": "error"|"warning", "msg": str}).

    Stripe expands ONLY {CHECKOUT_SESSION_ID}. Any other {TOKEN} is an error —
    Stripe passes it through literally, so the buyer's browser lands on a URL with
    a raw `{CHECKOUT_EMAIL}` in it. A missing {CHECKOUT_SESSION_ID} is a warning:
    valid config, but the success page can't resolve the buyer session.
    """
    issues = []
    found = _PLACEHOLDER_RE.findall(url)
    for token in found:
        if token not in VALID_URL_PLACEHOLDERS:
            issues.append({
                "level": "error",
                "msg": (f"invalid placeholder {{{token}}} — Stripe never expands this; "
                        f"it reaches the buyer's browser verbatim. Only {{CHECKOUT_SESSION_ID}} is supported."),
            })
    if "CHECKOUT_SESSION_ID" not in found:
        issues.append({
            "level": "warning",
            "msg": ("no {CHECKOUT_SESSION_ID} placeholder — the success page will not receive the "
                    "session id, so it cannot resolve the buyer (the email is not on the URL)."),
        })
    return issues


# --------------------------------------------------------------------------- #
# HTTP + verdicts (shared by the CLI and the test suite)
# --------------------------------------------------------------------------- #
def post_event(url: str, payload: bytes, sig_header: str, timeout: float = 10.0):
    """POST a signed event to `url`. Returns (status_code, body_text)."""
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Stripe-Signature", sig_header)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def normal_fire_pass(status: int) -> bool:
    """A valid signed event should be ACCEPTED (2xx)."""
    return 200 <= status < 300


def forged_fire_pass(status: int) -> bool:
    """A forged/badly-signed event should be REJECTED (4xx). A 2xx here means the
    handler skipped signature verification — anyone can forge events."""
    return 400 <= status < 500


# --------------------------------------------------------------------------- #
# CLI commands
# --------------------------------------------------------------------------- #
def _require_secret(env_name: str) -> str:
    secret = os.environ.get(env_name)
    if not secret:
        raise SystemExit(
            f"error: environment variable {env_name} is not set. Export your Stripe webhook "
            f"signing secret (whsec_...) into it — the value is read from the env and never stored."
        )
    return secret


def cmd_fire(args) -> int:
    payload = load_fixture(args.fixture)
    secret = _require_secret(args.secret_env)
    ts = args.timestamp if args.timestamp is not None else int(time.time())

    if args.forge:
        # Sign with a deliberately wrong secret: the header is structurally valid
        # (t=...,v1=...) but will not verify. A correct handler must reject this.
        sig = stripe_signature(payload, secret + "__swtk_forged__", ts)
        status, body = post_event(args.url, payload, sig)
        ok = forged_fire_pass(status)
        print(f"[forge] POST {args.url}  ->  HTTP {status}")
        _print_body(body)
        if ok:
            print("PASS: handler rejected the forged event (signature verification is working).")
            return 0
        print("FAIL: handler ACCEPTED a forged event (HTTP 2xx). It is not verifying the")
        print("      Stripe-Signature — anyone who knows your endpoint URL can post fake events.")
        return 1

    sig = stripe_signature(payload, secret, ts)
    status, body = post_event(args.url, payload, sig)
    ok = normal_fire_pass(status)
    print(f"[fire]  POST {args.url}  ->  HTTP {status}")
    _print_body(body)
    if ok:
        print("PASS: handler accepted the correctly-signed event.")
        return 0
    print(f"FAIL: handler did not accept a correctly-signed event (HTTP {status}, expected 2xx).")
    return 1


def _print_body(body: str):
    body = body.strip()
    if not body:
        return
    if len(body) > 600:
        body = body[:600] + " …(truncated)"
    print("        response:", body)


def cmd_check_email(args) -> int:
    event = json.loads(load_fixture(args.fixture))
    obj = event.get("data", {}).get("object", {}) or {}
    top = obj.get("customer_email")
    details_email = (obj.get("customer_details") or {}).get("email")
    email, source = resolve_buyer_email(obj)

    print(f"fixture: {args.fixture}")
    print(f"  event.data.object.customer_email           = {top!r}")
    print(f"  event.data.object.customer_details.email   = {details_email!r}")
    if email is None:
        print("  resolved buyer email                       = <none>")
        print("FAIL: no buyer email resolvable from this event.")
        return 1
    print(f"  resolved buyer email                       = {email!r}  (from {source})")
    if top is None and source == "customer_details.email":
        print("GOTCHA CONFIRMED: top-level customer_email is null on this real completion.")
        print("  A handler that reads only event.data.object.customer_email gets None here")
        print("  and silently drops the sale. Read customer_details.email first.")
    return 0


def cmd_lint_url(args) -> int:
    issues = lint_success_url(args.url)
    errors = [i for i in issues if i["level"] == "error"]
    print(f"success_url: {args.url}")
    if not issues:
        print("OK: uses {CHECKOUT_SESSION_ID}, no invalid placeholders.")
        return 0
    for i in issues:
        print(f"  [{i['level']}] {i['msg']}")
    if errors:
        print("FAIL: invalid placeholder(s) present.")
        return 1
    print("OK (with warnings): no invalid placeholders.")
    return 0


def cmd_list(args) -> int:
    names = list_fixtures()
    if not names:
        print("(no fixtures found)")
        return 1
    print("bundled real-shape fixtures (see fixtures/PROVENANCE.md):")
    for n in names:
        try:
            ev = json.loads((FIXTURES_DIR / n).read_bytes())
            print(f"  {n:44s}  type={ev.get('type')}")
        except Exception:
            print(f"  {n}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="swtk", description="Stripe Webhook Test Kit — test your webhook handler against real event shapes.")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fire", help="sign a fixture and POST it to your local webhook endpoint")
    f.add_argument("--url", required=True, help="your webhook endpoint, e.g. http://localhost:8000/webhook")
    f.add_argument("--fixture", required=True, help="fixture name (see `swtk list`)")
    f.add_argument("--secret-env", default=DEFAULT_SECRET_ENV, dest="secret_env",
                   help=f"env var holding your whsec_ signing secret (default {DEFAULT_SECRET_ENV})")
    f.add_argument("--forge", action="store_true",
                   help="sign with a wrong secret; PASS means your handler rejected it (4xx)")
    f.add_argument("--timestamp", type=int, default=None, help="override the signature timestamp (advanced)")
    f.set_defaults(func=cmd_fire)

    e = sub.add_parser("check-email", help="show where the buyer email actually lives on a fixture")
    e.add_argument("--fixture", required=True)
    e.set_defaults(func=cmd_check_email)

    l = sub.add_parser("lint-url", help="check a success_url for invalid Stripe placeholders")
    l.add_argument("url", help='e.g. "https://x/success?session_id={CHECKOUT_SESSION_ID}"')
    l.set_defaults(func=cmd_lint_url)

    ls = sub.add_parser("list", help="list bundled fixtures")
    ls.set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
