#!/usr/bin/env python3
"""GitHub Webhook Test Kit (gwtk) — fire REAL-shape signed GitHub webhook
deliveries at your local endpoint and check your handler the way GitHub
actually behaves. No GitHub App, no live webhook, no tunnel needed.

Stdlib only. No pip install, no build step. Python 3.8+.

What it checks (see GOTCHAS.md for the why):
  1. fire              — your handler ACCEPTS a correctly-signed real delivery (2xx).
  2. fire --forge      — your handler REJECTS a delivery signed with the wrong
                         secret (4xx) instead of silently accepting it.
  3. fire --unsigned   — your handler REJECTS an UNSIGNED delivery (4xx):
                         "no signature header" must fail closed, not skip
                         verification.
  4. fire --sha1-only  — your handler REJECTS a delivery carrying only the
                         legacy SHA-1 header (4xx): accepting a stripped-down
                         SHA-1-only request is a downgrade path.
  5. fire --form       — same checks with content type
                         application/x-www-form-urlencoded (payload=<json>);
                         the signature covers the RAW FORM BODY, not the JSON
                         inside — the #1 "my signature never validates" cause.
  6. fire --replay     — fires the SAME delivery (same X-GitHub-Delivery GUID)
                         twice: GitHub's scheme has NO timestamp, so replayed
                         deliveries verify forever; dedupe on the GUID.
  7. check-event       — shows that the event NAME lives ONLY in the
                         X-GitHub-Event header — payload "action" alone is
                         ambiguous across event types.
  8. vector            — proves this kit's HMAC implementation against
                         GitHub's OWN published test vector, offline.

The webhook secret is read from an environment variable (NAME only — the
value is never stored, logged, or echoed by this tool). Default:
GWTK_WEBHOOK_SECRET.
"""
import argparse
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_SECRET_ENV = "GWTK_WEBHOOK_SECRET"

# GitHub's official known-answer test (docs source: github/docs
# content/webhooks/using-webhooks/validating-webhook-deliveries.md — see
# fixtures/PROVENANCE.md). Public documentation values, not a real secret.
VECTOR_SECRET = "It's a Secret to Everybody"
VECTOR_PAYLOAD = b"Hello, World!"
VECTOR_SIG_256 = "sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17"


# --------------------------------------------------------------------------- #
# Signatures — the real X-Hub-Signature-256 / X-Hub-Signature schemes.
# HMAC hex digest of the RAW request body, keyed with the webhook secret;
# scheme verified against GitHub's docs source (fixtures/PROVENANCE.md).
# Note there is NO timestamp component — unlike Stripe's t=,v1= scheme.
# --------------------------------------------------------------------------- #
def hub_signature_256(payload: bytes, secret: str) -> str:
    """The X-Hub-Signature-256 header value for `payload`: sha256=<hex hmac>."""
    digest = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def hub_signature_sha1(payload: bytes, secret: str) -> str:
    """The legacy X-Hub-Signature header value: sha1=<hex hmac>."""
    digest = hmac.new(secret.encode("utf-8"), payload, hashlib.sha1).hexdigest()
    return f"sha1={digest}"


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def fixture_path(name: str) -> Path:
    return FIXTURES_DIR / (name if name.endswith(".json") else name + ".json")


def load_fixture(name: str) -> bytes:
    p = fixture_path(name)
    if not p.exists():
        raise SystemExit(f"error: fixture not found: {p.name}. Run `gwtk list` to see bundled fixtures.")
    return p.read_bytes()


def load_events() -> dict:
    """fixture name -> X-GitHub-Event header value (fixtures/EVENTS.json)."""
    events = json.loads((FIXTURES_DIR / "EVENTS.json").read_text(encoding="utf-8"))
    events.pop("_comment", None)
    return events


def event_for_fixture(name: str) -> str:
    stem = name[:-5] if name.endswith(".json") else name
    events = load_events()
    if stem not in events:
        raise SystemExit(
            f"error: fixture {stem!r} has no X-GitHub-Event mapping in fixtures/EVENTS.json — "
            f"add one (the event name travels only in the header, never in the payload)."
        )
    return events[stem]


def list_fixtures():
    return sorted(p.name for p in FIXTURES_DIR.glob("*.json") if p.name != "EVENTS.json")


# --------------------------------------------------------------------------- #
# HTTP + verdicts (shared by the CLI and the test suite)
# --------------------------------------------------------------------------- #
def build_request(url: str, payload: bytes, event: str, delivery: str,
                  secret: str = None, form: bool = False, sha1_only: bool = False):
    """(body_bytes, headers) exactly as `fire` would send them.

    When form=True the body is `payload=<urlencoded json>` with content type
    application/x-www-form-urlencoded — and the signature is computed over
    THOSE raw form bytes, exactly as GitHub signs form deliveries.
    """
    if form:
        body = ("payload=" + urllib.parse.quote_plus(payload.decode("utf-8"))).encode("utf-8")
        content_type = "application/x-www-form-urlencoded"
    else:
        body = payload
        content_type = "application/json"
    headers = {
        "Content-Type": content_type,
        "User-Agent": "GitHub-Hookshot/gwtk",
        "X-GitHub-Event": event,
        "X-GitHub-Delivery": delivery,
    }
    if secret is not None:
        if not sha1_only:
            headers["X-Hub-Signature-256"] = hub_signature_256(body, secret)
        headers["X-Hub-Signature"] = hub_signature_sha1(body, secret)
    return body, headers


def post_delivery(url: str, body: bytes, headers: dict, timeout: float = 10.0):
    """POST a delivery to `url`. Returns (status_code, body_text)."""
    req = urllib.request.Request(url, data=body, method="POST")
    for k, v in headers.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def normal_fire_pass(status: int) -> bool:
    """A correctly-signed delivery should be ACCEPTED (2xx)."""
    return 200 <= status < 300


def rejected_fire_pass(status: int) -> bool:
    """A forged / unsigned / sha1-only delivery should be REJECTED (4xx).
    A 2xx means the handler is not verifying X-Hub-Signature-256 properly —
    anyone who knows the endpoint URL can post fake events."""
    return 400 <= status < 500


# --------------------------------------------------------------------------- #
# CLI commands
# --------------------------------------------------------------------------- #
def _require_secret(env_name: str) -> str:
    secret = os.environ.get(env_name)
    if not secret:
        raise SystemExit(
            f"error: environment variable {env_name} is not set. Export your webhook "
            f"secret token into it — the value is read from the env and never stored."
        )
    return secret


def _print_body(body: str):
    body = body.strip()
    if not body:
        return
    if len(body) > 600:
        body = body[:600] + " …(truncated)"
    print("        response:", body)


def cmd_fire(args) -> int:
    payload = load_fixture(args.fixture)
    secret = _require_secret(args.secret_env)
    event = event_for_fixture(args.fixture)
    delivery = args.delivery or str(uuid.uuid4())
    modes = [bool(args.forge), bool(args.unsigned), bool(args.sha1_only), bool(args.replay)]
    if sum(modes) > 1:
        raise SystemExit("error: --forge / --unsigned / --sha1-only / --replay are mutually exclusive.")

    if args.forge:
        # Sign with a deliberately wrong secret: headers are structurally valid
        # but will not verify. A correct handler must reject this.
        body, headers = build_request(args.url, payload, event, delivery,
                                      secret=secret + "__gwtk_forged__", form=args.form)
        status, resp = post_delivery(args.url, body, headers)
        print(f"[forge]     POST {args.url}  ({event})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the forged delivery (signature verification is working).")
            return 0
        print("FAIL: handler ACCEPTED a forged delivery (HTTP 2xx). It is not verifying")
        print("      X-Hub-Signature-256 — anyone who knows your endpoint URL can post fake events.")
        return 1

    if args.unsigned:
        body, headers = build_request(args.url, payload, event, delivery, secret=None, form=args.form)
        status, resp = post_delivery(args.url, body, headers)
        print(f"[unsigned]  POST {args.url}  ({event})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the unsigned delivery (missing signature fails closed).")
            return 0
        print("FAIL: handler ACCEPTED a delivery with NO signature header. If your webhook has a")
        print("      secret configured, a missing X-Hub-Signature-256 must be rejected, not skipped.")
        return 1

    if args.sha1_only:
        body, headers = build_request(args.url, payload, event, delivery,
                                      secret=secret, form=args.form, sha1_only=True)
        status, resp = post_delivery(args.url, body, headers)
        print(f"[sha1-only] POST {args.url}  ({event})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the SHA-1-only delivery (no downgrade path).")
            return 0
        print("FAIL: handler ACCEPTED a delivery carrying only the legacy X-Hub-Signature (SHA-1).")
        print("      GitHub always sends X-Hub-Signature-256 when a secret is set — an attacker who")
        print("      strips the sha256 header should not be able to route you onto the weaker check.")
        return 1

    if args.replay:
        body, headers = build_request(args.url, payload, event, delivery, secret=secret, form=args.form)
        status1, resp1 = post_delivery(args.url, body, headers)
        status2, resp2 = post_delivery(args.url, body, headers)
        print(f"[replay]    POST {args.url}  ({event})  delivery {delivery}")
        print(f"        1st -> HTTP {status1}")
        _print_body(resp1)
        print(f"        2nd -> HTTP {status2} (identical bytes, identical GUID)")
        _print_body(resp2)
        print("NOTE: GitHub's signature scheme has NO timestamp — a replayed delivery verifies")
        print("      forever. HTTP alone cannot show whether you PROCESSED it twice: dedupe on")
        print("      X-GitHub-Delivery (redeliveries reuse the original GUID) and check your own")
        print("      side effects. The bundled stub_handler.py shows the dedupe pattern.")
        if normal_fire_pass(status1) and status2 < 500:
            print("PASS (transport): both deliveries handled without a 5xx. Idempotency is on you.")
            return 0
        print("FAIL: a correctly-signed (re)delivery crashed or was mis-rejected "
              f"(HTTP {status1} then {status2}).")
        return 1

    body, headers = build_request(args.url, payload, event, delivery, secret=secret, form=args.form)
    status, resp = post_delivery(args.url, body, headers)
    mode = "form" if args.form else "json"
    print(f"[fire/{mode}] POST {args.url}  ({event})  ->  HTTP {status}")
    _print_body(resp)
    if normal_fire_pass(status):
        print("PASS: handler accepted the correctly-signed delivery.")
        return 0
    print(f"FAIL: handler did not accept a correctly-signed delivery (HTTP {status}, expected 2xx).")
    if args.form:
        print("      (--form signs the RAW urlencoded body, exactly as GitHub does. If you verify")
        print("      the decoded JSON instead of the raw request bytes, this is the failure you see.)")
    return 1


def cmd_check_event(args) -> int:
    payload = json.loads(load_fixture(args.fixture))
    event = event_for_fixture(args.fixture)
    action = payload.get("action")
    print(f"fixture: {args.fixture}")
    print(f"  X-GitHub-Event header (the ONLY place the event name travels) = {event!r}")
    print(f"  payload top-level \"action\"                                    = {action!r}")
    if event == "ping":
        print(f"  payload \"zen\"                                                 = {payload.get('zen')!r}")
        print("GOTCHA: ping is the FIRST delivery every new webhook receives (sent on creation).")
        print("  It has no \"action\" and no event-specific resource — a handler that assumes")
        print("  e.g. payload[\"pull_request\"] exists will 500 before your webhook ever works.")
        print("  Return 2xx on ping.")
        return 0
    if action is None:
        print(f"GOTCHA: {event!r} deliveries have NO \"action\" field at all. Routing on")
        print("  payload[\"action\"] alone breaks here — route on the X-GitHub-Event header first.")
        return 0
    print(f"GOTCHA: \"action\": {action!r} is NOT unique to {event!r} — many event types share")
    print("  action values (e.g. \"created\", \"completed\"). Route on the X-GitHub-Event header")
    print("  first, THEN on action; a handler switching on action alone conflates event types.")
    return 0


def cmd_vector(args) -> int:
    computed = hub_signature_256(VECTOR_PAYLOAD, VECTOR_SECRET)
    print("GitHub's published test vector (validating-webhook-deliveries docs):")
    print(f"  secret   = {VECTOR_SECRET!r}")
    print(f"  payload  = {VECTOR_PAYLOAD!r}")
    print(f"  expected = {VECTOR_SIG_256}")
    print(f"  computed = {computed}")
    if hmac.compare_digest(computed, VECTOR_SIG_256):
        print("PASS: this kit's HMAC-SHA256 implementation matches GitHub's own published constant.")
        return 0
    print("FAIL: computed signature does not match GitHub's published vector — do not trust")
    print("      this copy of the kit; re-download it.")
    return 1


def cmd_list(args) -> int:
    names = list_fixtures()
    if not names:
        print("(no fixtures found)")
        return 1
    events = load_events()
    print("bundled real-shape fixtures (vendored from GitHub's own example set —")
    print("see fixtures/PROVENANCE.md):")
    for n in names:
        stem = n[:-5]
        try:
            payload = json.loads((FIXTURES_DIR / n).read_bytes())
            action = payload.get("action")
            suffix = f' action={action}' if action is not None else " (no action field)"
            print(f"  {n:36s}  X-GitHub-Event={events.get(stem, '?')}{suffix}")
        except Exception:
            print(f"  {n}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="gwtk",
        description="GitHub Webhook Test Kit — test your webhook handler against real delivery shapes.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fire", help="sign a fixture and POST it to your local webhook endpoint")
    f.add_argument("--url", required=True, help="your webhook endpoint, e.g. http://localhost:8000/webhook")
    f.add_argument("--fixture", required=True, help="fixture name (see `gwtk list`)")
    f.add_argument("--secret-env", default=DEFAULT_SECRET_ENV, dest="secret_env",
                   help=f"env var holding your webhook secret (default {DEFAULT_SECRET_ENV})")
    f.add_argument("--forge", action="store_true",
                   help="sign with a wrong secret; PASS means your handler rejected it (4xx)")
    f.add_argument("--unsigned", action="store_true",
                   help="send NO signature headers; PASS means your handler rejected it (4xx)")
    f.add_argument("--sha1-only", action="store_true", dest="sha1_only",
                   help="send only the legacy SHA-1 header; PASS means your handler rejected it (4xx)")
    f.add_argument("--replay", action="store_true",
                   help="fire the same delivery (same X-GitHub-Delivery GUID) twice")
    f.add_argument("--form", action="store_true",
                   help="deliver as application/x-www-form-urlencoded (payload=<json>), signed over the raw form body")
    f.add_argument("--delivery", default=None,
                   help="override the X-GitHub-Delivery GUID (default: a random UUID)")
    f.set_defaults(func=cmd_fire)

    e = sub.add_parser("check-event", help="show where the event name actually travels (header, not payload)")
    e.add_argument("--fixture", required=True)
    e.set_defaults(func=cmd_check_event)

    v = sub.add_parser("vector", help="prove the kit's HMAC against GitHub's published test vector (offline)")
    v.set_defaults(func=cmd_vector)

    ls = sub.add_parser("list", help="list bundled fixtures")
    ls.set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
