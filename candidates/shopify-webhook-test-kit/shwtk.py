#!/usr/bin/env python3
"""Shopify Webhook Test Kit (shwtk) — fire REAL-shape signed Shopify webhooks at
your local webhook endpoint and check your handler the way Shopify actually
behaves. No Shopify store, no app install, no tunnel needed.

Stdlib only. No pip install, no build step. Python 3.8+.

What it checks (see GOTCHAS.md for the why):
  1. fire              — your handler ACCEPTS a correctly-signed real webhook (2xx).
  2. fire --forge      — your handler REJECTS a webhook signed with the WRONG
                         secret (4xx) instead of silently accepting it.
  3. fire --unsigned   — your handler REJECTS a webhook with NO
                         X-Shopify-Hmac-Sha256 header (4xx): a missing signature
                         must fail closed.
  4. fire --tamper     — signs the real body, then mutates the body before
                         sending: your handler REJECTS it (4xx) because the HMAC
                         covers the RAW bytes, not a re-parsed / re-serialised copy.
  5. fire --malformed  — sends a syntactically INVALID base64 HMAC header: your
                         handler REJECTS it (4xx) without crashing (a bare
                         base64-decode with no error handling 500s here).
  6. vector            — proves this kit's HMAC-SHA256 + base64 implementation
                         against a documented kit-internal known-answer, offline,
                         and (with swtk.js) cross-language. NOTE: Shopify does not
                         publish a fixed known-answer constant, so this vector is
                         the kit's own (honestly labelled) — not a vendor value.

The Shopify webhook secret is read from an environment variable (NAME only — the
value is never stored, logged, or echoed by this tool). Default:
SHOPIFY_WEBHOOK_SECRET.

Shopify signs DIFFERENTLY from Slack/Stripe: the header X-Shopify-Hmac-Sha256 is
the BASE64 (not hex) HMAC-SHA256 of the RAW request body DIRECTLY — there is NO
timestamp basestring and NO replay window baked into the signature (so this kit
has no --stale mode and no challenge handshake; see fixtures/PROVENANCE.md).
"""
import argparse
import base64
import binascii
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_SECRET_ENV = "SHOPIFY_WEBHOOK_SECRET"

# The HMAC header Shopify sends. HTTP header names are case-insensitive
# (RFC 7230 §3.2); Shopify documents it as X-Shopify-Hmac-SHA256.
HMAC_HEADER = "X-Shopify-Hmac-Sha256"
TOPIC_HEADER = "X-Shopify-Topic"
SHOP_DOMAIN_HEADER = "X-Shopify-Shop-Domain"
WEBHOOK_ID_HEADER = "X-Shopify-Webhook-Id"
API_VERSION_HEADER = "X-Shopify-Api-Version"

# Modelled request metadata a real Shopify delivery carries (values are
# illustrative — see fixtures/PROVENANCE.md). Shopify does not send a
# distinctive product User-Agent the way Slack does.
DEMO_SHOP_DOMAIN = "example-store.myshopify.com"
DEMO_WEBHOOK_ID = "b54557e4-bcc0-4f8b-a1f0-6f0b3a1d2c3e"
DEMO_API_VERSION = "2026-07"

# A documented KIT-INTERNAL known-answer vector. Shopify's docs publish the
# verification METHOD (code) but NOT a fixed secret+body+expected-digest
# constant, so — unlike the Slack kit, which reproduces Slack's OWN published
# example — this vector is the kit's own, honestly labelled. It still proves the
# HMAC-SHA256 + base64 path end to end and (against shwtk.js) cross-language.
VECTOR_SECRET = "shwtk_test_client_secret_v0_1_not_a_real_secret"
VECTOR_BODY = b'{"id":123456789,"topic":"orders/create","note":"shwtk known-answer vector"}'
VECTOR_HMAC = "uhRiDuW3C3+o+mLcijsFK2jv0FwIloa+C4O5MQzK6w0="


# --------------------------------------------------------------------------- #
# Signature — the real X-Shopify-Hmac-Sha256 scheme.
# header = base64( HMAC-SHA256(secret, RAW request body) )
# Scheme verified against Shopify's docs; see fixtures/PROVENANCE.md. Note there
# is NO timestamp basestring (unlike Slack's v0:{ts}:{body}) and the digest is
# BASE64, not hex (unlike Slack/GitHub). The secret is the app's client secret
# (API-created webhooks) or the shared secret shown in the admin.
# --------------------------------------------------------------------------- #
def shopify_hmac(raw_body: bytes, secret: str) -> str:
    """The X-Shopify-Hmac-Sha256 header value for `raw_body`."""
    digest = hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).digest()
    return base64.b64encode(digest).decode("ascii")


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def load_manifest() -> dict:
    """fixture stem -> {"content_type": ..., "topic": ...} (fixtures/MANIFEST.json)."""
    manifest = json.loads((FIXTURES_DIR / "MANIFEST.json").read_text(encoding="utf-8"))
    manifest.pop("_comment", None)
    return manifest


def _entry_for(stem: str) -> dict:
    manifest = load_manifest()
    stem = stem[:-5] if stem.endswith(".json") else stem
    if stem not in manifest:
        raise SystemExit(
            f"error: fixture {stem!r} has no entry in fixtures/MANIFEST.json — "
            f"add its Content-Type and X-Shopify-Topic (Shopify puts the topic in "
            f"a header, not the body)."
        )
    return manifest[stem]


def fixture_file(stem: str) -> Path:
    """The on-disk file for a fixture stem (.json)."""
    stem = stem[:-5] if stem.endswith(".json") else stem
    p = FIXTURES_DIR / (stem + ".json")
    if p.exists():
        return p
    raise SystemExit(f"error: fixture not found: {stem}. Run `shwtk list` to see bundled fixtures.")


def load_fixture(stem: str) -> bytes:
    """The RAW request body bytes for a fixture (exactly as Shopify would send)."""
    return fixture_file(stem).read_bytes()


def content_type_for(stem: str) -> str:
    return _entry_for(stem)["content_type"]


def topic_for(stem: str) -> str:
    return _entry_for(stem)["topic"]


def list_fixtures():
    return sorted(load_manifest().keys())


# --------------------------------------------------------------------------- #
# HTTP + verdicts (shared by the CLI and the test suite)
# --------------------------------------------------------------------------- #
def build_request(raw_body: bytes, content_type: str, topic: str, secret=None,
                  sign_body=None, forge=False, malformed=False):
    """(body_bytes, headers) exactly as `fire` would send them.

    The signature is computed over `sign_body` (default: the body being sent).
    To simulate a TAMPERED request — a valid signature over one body but a
    DIFFERENT body on the wire — pass the pre-tamper bytes as `sign_body` and
    the mutated bytes as `raw_body`. `forge=True` signs with a deliberately
    wrong secret so the header is structurally valid but will not verify.
    `malformed=True` sends a header that is NOT valid base64 (a decode-time
    failure, distinct from a valid-but-wrong digest).
    """
    headers = {
        "Content-Type": content_type,
        TOPIC_HEADER: topic,
        SHOP_DOMAIN_HEADER: DEMO_SHOP_DOMAIN,
        WEBHOOK_ID_HEADER: DEMO_WEBHOOK_ID,
        API_VERSION_HEADER: DEMO_API_VERSION,
    }
    if malformed:
        # A syntactically invalid base64 value (contains '!', wrong padding).
        headers[HMAC_HEADER] = "!!!not-valid-base64!!!"
    elif secret is not None:
        signing_secret = secret + "__shwtk_forged__" if forge else secret
        to_sign = raw_body if sign_body is None else sign_body
        headers[HMAC_HEADER] = shopify_hmac(to_sign, signing_secret)
    return raw_body, headers


def post_request(url: str, body: bytes, headers: dict, timeout: float = 10.0):
    """POST a request to `url`. Returns (status_code, body_text).

    A handler that DROPS the connection (e.g. an unhandled exception on bad
    input) yields status 0 — treated as neither a 2xx accept nor a clean 4xx
    reject, so both verdicts correctly mark it a FAIL instead of raising."""
    req = urllib.request.Request(url, data=body, method="POST")
    for k, v in headers.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except OSError as e:
        # URLError, RemoteDisconnected, ConnectionReset, timeouts — no HTTP
        # response was produced.
        return 0, f"<no HTTP response: {e}>"


def normal_fire_pass(status: int) -> bool:
    """A correctly-signed webhook should be ACCEPTED (2xx)."""
    return 200 <= status < 300


def rejected_fire_pass(status: int) -> bool:
    """A forged / unsigned / tampered / malformed webhook should be REJECTED
    (4xx). A 2xx here means the handler is not verifying X-Shopify-Hmac-Sha256 —
    anyone who knows the URL can post fake webhooks. A 5xx on --malformed means
    the handler crashed on bad base64 instead of rejecting cleanly."""
    return 400 <= status < 500


# --------------------------------------------------------------------------- #
# CLI commands
# --------------------------------------------------------------------------- #
def _require_secret(env_name: str) -> str:
    secret = os.environ.get(env_name)
    if not secret:
        raise SystemExit(
            f"error: environment variable {env_name} is not set. Export your Shopify "
            f"webhook secret into it — the value is read from the env and never stored."
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
    content_type = content_type_for(args.fixture)
    topic = topic_for(args.fixture)
    modes = [bool(args.forge), bool(args.unsigned), bool(args.tamper), bool(args.malformed)]
    if sum(modes) > 1:
        raise SystemExit("error: --forge / --unsigned / --tamper / --malformed are mutually exclusive.")

    if args.unsigned:
        body, headers = build_request(payload, content_type, topic, secret=None)
        status, resp = post_request(args.url, body, headers)
        print(f"[unsigned]  POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the unsigned webhook (missing signature fails closed).")
            return 0
        print("FAIL: handler ACCEPTED a webhook with NO X-Shopify-Hmac-Sha256 header. A missing")
        print("      signature must be rejected, not skipped.")
        return 1

    if args.malformed:
        body, headers = build_request(payload, content_type, topic, malformed=True)
        status, resp = post_request(args.url, body, headers)
        print(f"[malformed] POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the malformed-base64 signature cleanly (4xx, no crash).")
            return 0
        if status == 0 or 500 <= status < 600:
            print(f"FAIL: handler CRASHED (HTTP {status or 'connection dropped'}) on a non-base64 signature")
            print("      header. Decode the header defensively and return 401/400 — never let bad input")
            print("      500 you or drop the connection.")
        else:
            print("FAIL: handler ACCEPTED a webhook whose X-Shopify-Hmac-Sha256 header is not even")
            print("      valid base64. It is not verifying the signature at all.")
        return 1

    secret = _require_secret(args.secret_env)

    if args.forge:
        body, headers = build_request(payload, content_type, topic, secret=secret, forge=True)
        status, resp = post_request(args.url, body, headers)
        print(f"[forge]     POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the wrong-secret webhook (signature verification is working).")
            return 0
        print("FAIL: handler ACCEPTED a webhook signed with the wrong secret (HTTP 2xx). It is not")
        print("      verifying X-Shopify-Hmac-Sha256 — anyone who knows your URL can post fake webhooks.")
        return 1

    if args.tamper:
        tampered = payload + b" "  # one byte the signature never covered
        body, headers = build_request(tampered, content_type, topic, secret=secret, sign_body=payload)
        status, resp = post_request(args.url, body, headers)
        print(f"[tamper]    POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the tampered body (it hashes the RAW bytes it received).")
            return 0
        print("FAIL: handler ACCEPTED a body that differs from the one the signature covers. It is")
        print("      verifying a re-parsed/re-serialised copy, not the raw request bytes.")
        return 1

    body, headers = build_request(payload, content_type, topic, secret=secret)
    status, resp = post_request(args.url, body, headers)
    print(f"[fire]      POST {args.url}  ({args.fixture}, topic={topic})  ->  HTTP {status}")
    _print_body(resp)
    if normal_fire_pass(status):
        print("PASS: handler accepted the correctly-signed webhook.")
        return 0
    print(f"FAIL: handler did not accept a correctly-signed webhook (HTTP {status}, expected 2xx).")
    return 1


def cmd_vector(args) -> int:
    computed = shopify_hmac(VECTOR_BODY, VECTOR_SECRET)
    print("Kit-internal known-answer vector (see fixtures/PROVENANCE.md — Shopify")
    print("publishes the verification METHOD but NOT a fixed known-answer constant,")
    print("so this vector is the kit's own, honestly labelled):")
    print(f"  secret   = {VECTOR_SECRET!r}")
    print(f"  body     = {VECTOR_BODY.decode('ascii')!r}")
    print(f"  expected = {VECTOR_HMAC}")
    print(f"  computed = {computed}")
    if hmac.compare_digest(computed, VECTOR_HMAC):
        print("PASS: this kit's HMAC-SHA256 + base64 implementation matches the pinned known-answer")
        print("      (and matches shwtk.js — run `node shwtk.js vector` to confirm cross-language).")
        return 0
    print("FAIL: computed signature does not match the pinned known-answer — do not trust this copy")
    print("      of the kit; re-download it.")
    return 1


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled real-shape fixtures (reconstructed from Shopify's docs —")
    print("see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        entry = manifest[stem]
        ct = entry.get("content_type", "?")
        topic = entry.get("topic", "?")
        print(f"  {stem:20s}  topic={topic:20s}  {ct}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="shwtk",
        description="Shopify Webhook Test Kit — test your Shopify webhook handler against real webhook shapes.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fire", help="sign a fixture and POST it to your local Shopify webhook endpoint")
    f.add_argument("--url", required=True, help="your endpoint, e.g. http://localhost:8000/webhooks/shopify")
    f.add_argument("--fixture", required=True, help="fixture name (see `shwtk list`)")
    f.add_argument("--secret-env", default=DEFAULT_SECRET_ENV, dest="secret_env",
                   help=f"env var holding your Shopify webhook secret (default {DEFAULT_SECRET_ENV})")
    f.add_argument("--forge", action="store_true",
                   help="sign with a wrong secret; PASS means your handler rejected it (4xx)")
    f.add_argument("--unsigned", action="store_true",
                   help="send NO signature header; PASS means your handler rejected it (4xx)")
    f.add_argument("--tamper", action="store_true",
                   help="sign the real body then mutate it; PASS means your handler rejected it (4xx)")
    f.add_argument("--malformed", action="store_true",
                   help="send an invalid-base64 signature header; PASS means rejected cleanly (4xx, no 5xx crash)")
    f.set_defaults(func=cmd_fire)

    v = sub.add_parser("vector", help="prove the kit's HMAC+base64 against a pinned known-answer (offline)")
    v.set_defaults(func=cmd_vector)

    ls = sub.add_parser("list", help="list bundled fixtures")
    ls.set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
