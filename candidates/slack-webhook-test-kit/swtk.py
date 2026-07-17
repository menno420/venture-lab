#!/usr/bin/env python3
"""Slack Webhook Test Kit (swtk) — fire REAL-shape signed Slack requests at your
local request endpoint and check your handler the way Slack actually behaves.
No Slack app, no live workspace, no tunnel needed.

Stdlib only. No pip install, no build step. Python 3.8+.

What it checks (see GOTCHAS.md for the why):
  1. fire              — your handler ACCEPTS a correctly-signed real request (2xx).
  2. fire --forge      — your handler REJECTS a request signed with the WRONG
                         signing secret (4xx) instead of silently accepting it.
  3. fire --unsigned   — your handler REJECTS a request with NO signature
                         headers (4xx): "no X-Slack-Signature" must fail closed.
  4. fire --stale      — your handler REJECTS a request whose
                         X-Slack-Request-Timestamp is outside the ±300s window
                         (4xx), even though its signature is otherwise VALID —
                         this is Slack's replay defence, and it is on you.
  5. fire --tamper     — signs the real body, then mutates the body before
                         sending: your handler REJECTS it (4xx) because the
                         HMAC covers the RAW bytes, not a re-parsed copy.
  6. check-challenge   — shows that a url_verification request must be answered
                         by ECHOING BACK its `challenge` value — the very first
                         thing Slack sends when you save an Events API URL.
  7. vector            — proves this kit's HMAC implementation against Slack's
                         OWN published worked example, offline.

The Slack signing secret is read from an environment variable (NAME only — the
value is never stored, logged, or echoed by this tool). Default:
SLACK_SIGNING_SECRET.
"""
import argparse
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_SECRET_ENV = "SLACK_SIGNING_SECRET"

# Slack rejects any request whose timestamp is more than 5 minutes from now.
# Source: api.slack.com "Verifying requests from Slack" (see fixtures/PROVENANCE.md).
REPLAY_WINDOW_SECONDS = 300

# A real Slack request User-Agent (docs: api.slack.com/robots). Sent so the
# kit's test traffic is honest about its origin in your logs.
SLACK_UA = "Slackbot 1.0 (+https://api.slack.com/robots)"

# Slack's OWN published worked example (api.slack.com "Verifying requests from
# Slack"). Public documentation values — NOT a real secret.
VECTOR_SECRET = "8f742231b10e8888abcd99yyyzzz85a5"
VECTOR_TIMESTAMP = 1531420618
VECTOR_BODY = (
    b"token=xyzz0WbapA4vBCDEFasx0q6G&team_id=T1DC2JH3J&team_domain=testteamnow"
    b"&channel_id=G8PSS9T3V&channel_name=foobar&user_id=U2CERLKJA&user_name=roadrunner"
    b"&command=%2Fwebhook-collect&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands"
    b"%2FT1DC2JH3J%2F397700885554%2F96rGlfmibIGlgcZRskXaIFfN"
    b"&trigger_id=398738663015.47445629121.803a0bc887a14d10d2c447fce8b6703c"
)
VECTOR_SIGNATURE = "v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503"


# --------------------------------------------------------------------------- #
# Signature — the real X-Slack-Signature v0 scheme.
# basestring = "v0:" + timestamp + ":" + RAW request body
# signature  = "v0=" + hex( HMAC-SHA256(signing_secret, basestring) )
# Scheme verified against Slack's docs; see fixtures/PROVENANCE.md. Note the
# timestamp is PART of the signed string (unlike GitHub) AND is independently
# range-checked (unlike GitHub, which has no timestamp at all).
# --------------------------------------------------------------------------- #
def slack_signature(raw_body: bytes, secret: str, timestamp: int) -> str:
    """The X-Slack-Signature header value for `raw_body` at `timestamp`."""
    basestring = b"v0:" + str(int(timestamp)).encode("utf-8") + b":" + raw_body
    digest = hmac.new(secret.encode("utf-8"), basestring, hashlib.sha256).hexdigest()
    return "v0=" + digest


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def load_manifest() -> dict:
    """fixture stem -> Content-Type header (fixtures/MANIFEST.json)."""
    manifest = json.loads((FIXTURES_DIR / "MANIFEST.json").read_text(encoding="utf-8"))
    manifest.pop("_comment", None)
    return manifest


def fixture_file(stem: str) -> Path:
    """The on-disk file for a fixture stem (.json or .txt)."""
    stem = stem[:-5] if stem.endswith(".json") else stem
    stem = stem[:-4] if stem.endswith(".txt") else stem
    for ext in (".json", ".txt"):
        p = FIXTURES_DIR / (stem + ext)
        if p.exists():
            return p
    raise SystemExit(f"error: fixture not found: {stem}. Run `swtk list` to see bundled fixtures.")


def load_fixture(stem: str) -> bytes:
    """The RAW request body bytes for a fixture (exactly as Slack would send)."""
    return fixture_file(stem).read_bytes()


def content_type_for(stem: str) -> str:
    manifest = load_manifest()
    stem = stem[:-5] if stem.endswith(".json") else stem
    stem = stem[:-4] if stem.endswith(".txt") else stem
    if stem not in manifest:
        raise SystemExit(
            f"error: fixture {stem!r} has no Content-Type in fixtures/MANIFEST.json — "
            f"add one (Slack does not put the content type in the body)."
        )
    return manifest[stem]


def list_fixtures():
    return sorted(load_manifest().keys())


# --------------------------------------------------------------------------- #
# HTTP + verdicts (shared by the CLI and the test suite)
# --------------------------------------------------------------------------- #
def build_request(raw_body: bytes, content_type: str, secret=None,
                  timestamp=None, sign_body=None, forge=False):
    """(body_bytes, headers) exactly as `fire` would send them.

    The signature is computed over `sign_body` (default: the body being sent).
    To simulate a TAMPERED request — a valid signature over one body but a
    DIFFERENT body on the wire — pass the pre-tamper bytes as `sign_body` and
    the mutated bytes as `raw_body`. `forge=True` signs with a deliberately
    wrong secret so the header is structurally valid but will not verify.
    """
    ts = int(timestamp) if timestamp is not None else int(time.time())
    headers = {"Content-Type": content_type, "User-Agent": SLACK_UA}
    if secret is not None:
        signing_secret = secret + "__swtk_forged__" if forge else secret
        to_sign = raw_body if sign_body is None else sign_body
        headers["X-Slack-Request-Timestamp"] = str(ts)
        headers["X-Slack-Signature"] = slack_signature(to_sign, signing_secret, ts)
    return raw_body, headers


def post_request(url: str, body: bytes, headers: dict, timeout: float = 10.0):
    """POST a request to `url`. Returns (status_code, body_text)."""
    req = urllib.request.Request(url, data=body, method="POST")
    for k, v in headers.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def normal_fire_pass(status: int) -> bool:
    """A correctly-signed request should be ACCEPTED (2xx)."""
    return 200 <= status < 300


def rejected_fire_pass(status: int) -> bool:
    """A forged / unsigned / stale / tampered request should be REJECTED (4xx).
    A 2xx here means the handler is not verifying X-Slack-Signature (or not
    enforcing the timestamp window) — anyone who knows the URL can post fake
    requests, or replay a captured one forever."""
    return 400 <= status < 500


# --------------------------------------------------------------------------- #
# CLI commands
# --------------------------------------------------------------------------- #
def _require_secret(env_name: str) -> str:
    secret = os.environ.get(env_name)
    if not secret:
        raise SystemExit(
            f"error: environment variable {env_name} is not set. Export your Slack "
            f"signing secret into it — the value is read from the env and never stored."
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
    secret = _require_secret(args.secret_env)
    modes = [bool(args.forge), bool(args.unsigned), bool(args.stale), bool(args.tamper)]
    if sum(modes) > 1:
        raise SystemExit("error: --forge / --unsigned / --stale / --tamper are mutually exclusive.")

    if args.forge:
        body, headers = build_request(payload, content_type, secret=secret, forge=True)
        status, resp = post_request(args.url, body, headers)
        print(f"[forge]    POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the wrong-secret request (signature verification is working).")
            return 0
        print("FAIL: handler ACCEPTED a request signed with the wrong secret (HTTP 2xx). It is not")
        print("      verifying X-Slack-Signature — anyone who knows your URL can post fake requests.")
        return 1

    if args.unsigned:
        body, headers = build_request(payload, content_type, secret=None)
        status, resp = post_request(args.url, body, headers)
        print(f"[unsigned] POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the unsigned request (missing signature fails closed).")
            return 0
        print("FAIL: handler ACCEPTED a request with NO X-Slack-Signature header. A missing")
        print("      signature must be rejected, not skipped.")
        return 1

    if args.stale:
        old_ts = int(time.time()) - (REPLAY_WINDOW_SECONDS + 300)  # well outside the window
        body, headers = build_request(payload, content_type, secret=secret, timestamp=old_ts)
        status, resp = post_request(args.url, body, headers)
        print(f"[stale]    POST {args.url}  ({args.fixture})  ts={old_ts}  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the stale-timestamp request (replay window is enforced).")
            return 0
        print("FAIL: handler ACCEPTED a request whose X-Slack-Request-Timestamp is outside the")
        print(f"      ±{REPLAY_WINDOW_SECONDS}s window. Its signature is VALID — so a captured request replays")
        print("      forever. Reject anything older than 5 minutes BEFORE trusting the signature.")
        return 1

    if args.tamper:
        tampered = payload + b" "  # one byte the signature never covered
        body, headers = build_request(tampered, content_type, secret=secret, sign_body=payload)
        status, resp = post_request(args.url, body, headers)
        print(f"[tamper]   POST {args.url}  ({args.fixture})  ->  HTTP {status}")
        _print_body(resp)
        if rejected_fire_pass(status):
            print("PASS: handler rejected the tampered body (it hashes the RAW bytes it received).")
            return 0
        print("FAIL: handler ACCEPTED a body that differs from the one the signature covers. It is")
        print("      verifying a re-parsed/re-serialised copy, not the raw request bytes.")
        return 1

    body, headers = build_request(payload, content_type, secret=secret)
    status, resp = post_request(args.url, body, headers)
    print(f"[fire]     POST {args.url}  ({args.fixture}, {content_type})  ->  HTTP {status}")
    _print_body(resp)
    if normal_fire_pass(status):
        print("PASS: handler accepted the correctly-signed request.")
        return 0
    print(f"FAIL: handler did not accept a correctly-signed request (HTTP {status}, expected 2xx).")
    return 1


def cmd_check_challenge(args) -> int:
    payload = json.loads(load_fixture("url_verification"))
    challenge = payload.get("challenge")
    print("fixture: url_verification")
    print(f"  payload \"type\"      = {payload.get('type')!r}")
    print(f"  payload \"challenge\" = {challenge!r}")
    print("GOTCHA: when you save an Events API Request URL, Slack immediately POSTs a")
    print("  url_verification request. Your endpoint MUST answer 200 and echo the")
    print("  `challenge` value back (as text/plain, or as JSON {\"challenge\": ...}).")
    print("  If you don't, Slack marks the URL unverified and NO events are ever delivered.")
    if args.url:
        secret = _require_secret(args.secret_env)
        body, headers = build_request(load_fixture("url_verification"),
                                      content_type_for("url_verification"), secret=secret)
        status, resp = post_request(args.url, body, headers)
        print(f"\n[challenge] POST {args.url}  ->  HTTP {status}")
        _print_body(resp)
        echoed = challenge is not None and challenge in resp
        if normal_fire_pass(status) and echoed:
            print("PASS: handler answered 2xx AND echoed the challenge value.")
            return 0
        if not normal_fire_pass(status):
            print(f"FAIL: handler did not answer 2xx (HTTP {status}).")
        else:
            print("FAIL: handler answered 2xx but did NOT echo the challenge — Slack will not verify the URL.")
        return 1
    return 0


def cmd_vector(args) -> int:
    computed = slack_signature(VECTOR_BODY, VECTOR_SECRET, VECTOR_TIMESTAMP)
    print("Slack's published worked example (Verifying requests from Slack docs):")
    print(f"  signing secret = {VECTOR_SECRET!r}")
    print(f"  timestamp      = {VECTOR_TIMESTAMP}")
    print(f"  body           = {VECTOR_BODY[:48]!r}…")
    print(f"  expected       = {VECTOR_SIGNATURE}")
    print(f"  computed       = {computed}")
    if hmac.compare_digest(computed, VECTOR_SIGNATURE):
        print("PASS: this kit's HMAC-SHA256 implementation matches Slack's own published example.")
        return 0
    print("FAIL: computed signature does not match Slack's published example — do not trust")
    print("      this copy of the kit; re-download it.")
    return 1


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled real-shape fixtures (reconstructed from Slack's docs —")
    print("see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        ct = manifest[stem]
        try:
            raw = load_fixture(stem)
            if ct == "application/json":
                kind = json.loads(raw).get("type", "?")
                hint = f'type={kind}'
            elif raw.startswith(b"payload="):
                hint = "interactivity (payload=<json>)"
            else:
                hint = "slash command (form fields)"
        except Exception:
            hint = ""
        print(f"  {stem:32s}  {ct:35s}  {hint}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="swtk",
        description="Slack Webhook Test Kit — test your Slack request handler against real request shapes.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fire", help="sign a fixture and POST it to your local Slack request endpoint")
    f.add_argument("--url", required=True, help="your endpoint, e.g. http://localhost:8000/slack/events")
    f.add_argument("--fixture", required=True, help="fixture name (see `swtk list`)")
    f.add_argument("--secret-env", default=DEFAULT_SECRET_ENV, dest="secret_env",
                   help=f"env var holding your Slack signing secret (default {DEFAULT_SECRET_ENV})")
    f.add_argument("--forge", action="store_true",
                   help="sign with a wrong secret; PASS means your handler rejected it (4xx)")
    f.add_argument("--unsigned", action="store_true",
                   help="send NO signature headers; PASS means your handler rejected it (4xx)")
    f.add_argument("--stale", action="store_true",
                   help="send a VALID signature but an out-of-window timestamp; PASS means rejected (4xx)")
    f.add_argument("--tamper", action="store_true",
                   help="sign the real body then mutate it; PASS means your handler rejected it (4xx)")
    f.set_defaults(func=cmd_fire)

    c = sub.add_parser("check-challenge",
                       help="show the url_verification challenge-echo handshake (optionally test it live)")
    c.add_argument("--url", default=None,
                   help="optional: POST the url_verification fixture here and check the challenge is echoed")
    c.add_argument("--secret-env", default=DEFAULT_SECRET_ENV, dest="secret_env")
    c.set_defaults(func=cmd_check_challenge)

    v = sub.add_parser("vector", help="prove the kit's HMAC against Slack's published worked example (offline)")
    v.set_defaults(func=cmd_vector)

    ls = sub.add_parser("list", help="list bundled fixtures")
    ls.set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
