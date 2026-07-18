#!/usr/bin/env python3
"""JWT Auth Test Kit (jatk) — point it at your own JWT-protected endpoint and
prove your token verification is SECURE: it ACCEPTS a valid, correctly-signed,
unexpired token with the right claims, and REJECTS the critical auth-bypass
classes — an `alg:none` unsigned token, a tampered/wrong-signature/wrong-key
token, the RS256->HS256 ALGORITHM-CONFUSION attack, an EXPIRED token, a
NOT-YET-VALID (`nbf`/`iat` in the future) token, a wrong/missing `aud`, a
wrong/missing `iss`, and a structurally-malformed token.

Stdlib only (hmac, hashlib, base64, json, urllib). No pip install, no build step.
Python 3.8+. No account, no vendor, no live third-party call.

This is NOT a webhook signature kit, NOT the idempotency kit, NOT the rate-limit
kit, and NOT the pagination kit — it tests JWT VERIFIER SECURITY (auth bypass),
the highest-severity rung of API robustness. The properties are grounded in
RFC 7519 (JWT), RFC 7515 (JWS), and RFC 8725 ("JWT Best Current Practices"), plus
the well-known `alg:none` and RS256->HS256 algorithm-confusion attacks — cited in
fixtures/PROVENANCE.md.

HONEST SCOPE: the shipped tests exercise the HS256 signature path and every
attack class above using the Python standard library only. Real RS256/ES256
*signature-math* verification (RSA/ECDSA) is out of the stdlib scope of this kit
(see the listing's "what it does NOT do" + PROVENANCE.md). The algorithm-confusion
check does NOT need RSA verify — it forges an HS256 token over the public-key
bytes, which a naive verifier accepts and a pinned verifier rejects.

Properties checked (each PASS/FAIL/SKIP against YOUR endpoint):

  1. valid-accepted        A valid HS256 token (correct signature, unexpired,
                           correct aud/iss) is ACCEPTED (2xx).
  2. alg-none-rejected     An `alg:none` unsigned token is REJECTED. (RFC 8725 §3.1)
  3. signature-rejected    A tampered payload AND a wrong-key token are REJECTED.
  4. alg-confusion-rejected  An HS256 token signed with the RSA/EC PUBLIC key
                           bytes as the HMAC secret is REJECTED. (RFC 8725 §2.1)
  5. expired-rejected      A token with `exp` in the past is REJECTED. (RFC 7519 §4.1.4)
  6. not-yet-valid-rejected  A token with `nbf`/`iat` in the future is REJECTED.
  7. audience-enforced     A wrong `aud` AND a missing `aud` are REJECTED. (SKIP if
                           no expected audience is configured.)
  8. issuer-enforced       A wrong `iss` AND a missing `iss` are REJECTED. (SKIP if
                           no expected issuer is configured.)
  9. malformed-rejected    Structurally malformed tokens (bad base64url, wrong
                           segment count) are REJECTED.

`jatk demo` runs all nine against the bundled reference stubs — the CORRECT one
(accepts the valid token, rejects every attack) and the deliberately NAIVE one
(accepts alg:none, algorithm-confusion, expired, not-yet-valid, wrong aud/iss) —
with ZERO accounts and a loud banner, so you can see the checks working before you
point them at your app.
"""
import argparse
import base64
import hashlib
import hmac
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_FIXTURE = "hs256_bearer"
DEFAULT_SECRET = b"jatk-demo-hs256-secret-not-a-real-secret"   # a NON-secret demo default
WRONG_KEY = b"jatk-attacker-guessed-wrong-key"                 # for the wrong-key token


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def load_manifest() -> dict:
    manifest = json.loads((FIXTURES_DIR / "MANIFEST.json").read_text(encoding="utf-8"))
    manifest.pop("_comment", None)
    return manifest


def _entry_for(stem: str) -> dict:
    stem = stem[:-5] if stem.endswith(".json") else stem
    manifest = load_manifest()
    if stem not in manifest:
        raise SystemExit(
            f"error: fixture {stem!r} has no entry in fixtures/MANIFEST.json — "
            f"run `jatk list` to see bundled fixtures."
        )
    return manifest[stem]


def list_fixtures():
    return sorted(load_manifest().keys())


class AuthSpec:
    """The request shape of a JWT-protected endpoint, read from a fixture so a
    buyer can point it at their own route, header, and expected claims."""

    def __init__(self, entry: dict):
        self.path = entry.get("path", "/protected")
        self.auth_header = entry.get("auth_header", "Authorization")
        self.auth_scheme = entry.get("auth_scheme", "Bearer")
        self.expected_aud = entry.get("expected_aud") or None
        self.expected_iss = entry.get("expected_iss") or None
        self.subject = entry.get("subject", "jatk-demo-user-001")

    @classmethod
    def from_fixture(cls, stem: str):
        return cls(_entry_for(stem))


def load_pubkey() -> bytes:
    p = FIXTURES_DIR / "test_public_key.pem"
    return p.read_bytes() if p.exists() else b""


# --------------------------------------------------------------------------- #
# JWT primitives (stdlib) — mint the valid token and every attack token
# --------------------------------------------------------------------------- #
def b64url_encode(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def _seg(obj) -> str:
    return b64url_encode(json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("utf-8"))


def mint(claims: dict, key: bytes, alg: str = "HS256", typ: str = "JWT") -> str:
    """Compact-serialize + HS256-sign a JWT. alg='none' emits an empty signature."""
    header = {"alg": alg, "typ": typ}
    h, p = _seg(header), _seg(claims)
    signing_input = (h + "." + p).encode("ascii")
    if alg == "none":
        sig = ""
    else:
        sig = b64url_encode(hmac.new(key, signing_input, hashlib.sha256).digest())
    return f"{h}.{p}.{sig}"


def base_claims(spec: AuthSpec, now: float) -> dict:
    claims = {"sub": spec.subject, "iat": int(now - 60), "nbf": int(now - 60),
              "exp": int(now + 3600)}
    if spec.expected_aud:
        claims["aud"] = spec.expected_aud
    if spec.expected_iss:
        claims["iss"] = spec.expected_iss
    return claims


def attack_tokens(spec: AuthSpec, secret: bytes, pubkey: bytes, now: float) -> dict:
    """Every token the suite fires, keyed by scenario. All time claims are fixed
    offsets from `now` (±1h), so there is no real waiting and no flakiness."""
    valid = base_claims(spec, now)

    # tampered: a valid token with one payload character altered (signature no
    # longer matches the payload).
    v = mint(valid, secret)
    h, p, s = v.split(".")
    p_tampered = (p[:-1] + ("A" if p[-1] != "A" else "B"))
    tampered = f"{h}.{p_tampered}.{s}"

    expired = dict(valid, iat=int(now - 7200), nbf=int(now - 7200), exp=int(now - 3600))
    future = dict(valid, iat=int(now + 3600), nbf=int(now + 3600), exp=int(now + 7200))
    wrong_aud = dict(valid, aud="jatk-attacker-different-audience")
    missing_aud = {k: v2 for k, v2 in valid.items() if k != "aud"}
    wrong_iss = dict(valid, iss="https://attacker.example/")
    missing_iss = {k: v2 for k, v2 in valid.items() if k != "iss"}

    # malformed: not three base64url/JSON segments.
    two_seg = ".".join(mint(valid, secret).split(".")[:2])          # header.payload
    four_seg = mint(valid, secret) + ".extra"                        # four segments
    bad_b64 = "@@@bad@@@." + p + "." + s                             # header not base64url

    return {
        "valid":         mint(valid, secret),
        "alg_none":      mint(valid, b"", alg="none"),
        "tampered":      tampered,
        "wrong_key":     mint(valid, WRONG_KEY),
        "confusion":     mint(valid, pubkey),        # HS256 over the PUBLIC key bytes
        "expired":       mint(expired, secret),
        "not_yet_valid": mint(future, secret),
        "wrong_aud":     mint(wrong_aud, secret),
        "missing_aud":   mint(missing_aud, secret),
        "wrong_iss":     mint(wrong_iss, secret),
        "missing_iss":   mint(missing_iss, secret),
        "malformed_notjwt":  "this-is-not-a-jwt",
        "malformed_twoseg":  two_seg,
        "malformed_fourseg": four_seg,
        "malformed_badb64":  bad_b64,
    }


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def fire(base_url, method, path, headers=None, timeout=10.0):
    """Fire one request. Returns (status, body_text). A dropped connection yields
    status 0 so a crashing endpoint is a FAIL, not an exception."""
    url = base_url.rstrip("/") + path
    req = urllib.request.Request(url, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except OSError as e:
        return 0, f"<no HTTP response: {e}>"


def is_2xx(s):
    return 200 <= s < 300


def fire_token(base_url, spec: AuthSpec, token: str):
    headers = {spec.auth_header: f"{spec.auth_scheme} {token}"}
    return fire(base_url, "GET", spec.path, headers=headers)


# --------------------------------------------------------------------------- #
# Suite plumbing
# --------------------------------------------------------------------------- #
def _mk_tokens(base_url, spec, secret, pubkey, now):
    return attack_tokens(spec, secret, pubkey, now if now is not None else time.time())


def _reject_check(base_url, spec, tokens, keys, ok_msg, bypass_word):
    """Assert every token named in `keys` is REJECTED (non-2xx). Returns
    (passed, detail); an accepted attack token is a FAIL naming the bypass."""
    accepted = []
    for k in keys:
        status, _body = fire_token(base_url, spec, tokens[k])
        if is_2xx(status):
            accepted.append((k, status))
    if accepted:
        pairs = ", ".join(f"{k} (HTTP {s})" for k, s in accepted)
        return False, (f"the endpoint ACCEPTED {bypass_word}: {pairs} — it must reject "
                       f"these with 401/403, not serve the protected resource.")
    return True, ok_msg


# --------------------------------------------------------------------------- #
# Properties — each returns (passed: bool|None, detail: str). None == SKIP.
# --------------------------------------------------------------------------- #
def check_valid_accepted(base_url, spec, secret, pubkey, now=None):
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    status, body = fire_token(base_url, spec, tokens["valid"])
    if not is_2xx(status):
        return False, (f"the endpoint REJECTED a valid, correctly-signed, unexpired token "
                       f"(HTTP {status}) — check that --secret matches your server's HS256 key "
                       f"and that --aud/--iss match what it expects. Body: {body[:160]}")
    return True, f"a valid HS256 token with correct claims was accepted (HTTP {status})"


def check_alg_none_rejected(base_url, spec, secret, pubkey, now=None):
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["alg_none"],
                         "an `alg:none` unsigned token was rejected — the classic bypass is closed",
                         "an `alg:none` unsigned token")


def check_signature_rejected(base_url, spec, secret, pubkey, now=None):
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["tampered", "wrong_key"],
                         "a tampered token and a wrong-key token were both rejected — the "
                         "signature is actually verified",
                         "a token with an invalid signature")


def check_alg_confusion_rejected(base_url, spec, secret, pubkey, now=None):
    if not pubkey:
        return None, ("SKIP: no public-key blob available to craft the confusion token "
                      "(pass --pubkey <file>). Against the bundled stubs it is present.")
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["confusion"],
                         "an HS256 token signed with the public-key bytes was rejected — the "
                         "verifier pins its algorithm and key (no RS256->HS256 confusion)",
                         "an algorithm-confusion token (HS256 signed with the RSA/EC public key)")


def check_expired_rejected(base_url, spec, secret, pubkey, now=None):
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["expired"],
                         "an expired token (exp in the past) was rejected",
                         "an expired token (exp in the past)")


def check_not_yet_valid_rejected(base_url, spec, secret, pubkey, now=None):
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["not_yet_valid"],
                         "a not-yet-valid token (nbf/iat in the future) was rejected",
                         "a not-yet-valid token (nbf/iat in the future)")


def check_audience_enforced(base_url, spec, secret, pubkey, now=None):
    if not spec.expected_aud:
        return None, ("SKIP: no expected audience configured (fixture `expected_aud` empty / "
                      "--aud unset), so the aud check cannot be exercised — set it to your API's "
                      "audience to run this property.")
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["wrong_aud", "missing_aud"],
                         f"a wrong `aud` and a missing `aud` were both rejected — the audience "
                         f"{spec.expected_aud!r} is enforced",
                         "a token with the wrong/missing audience")


def check_issuer_enforced(base_url, spec, secret, pubkey, now=None):
    if not spec.expected_iss:
        return None, ("SKIP: no expected issuer configured (fixture `expected_iss` empty / "
                      "--iss unset), so the iss check cannot be exercised — set it to your API's "
                      "issuer to run this property.")
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    return _reject_check(base_url, spec, tokens, ["wrong_iss", "missing_iss"],
                         f"a wrong `iss` and a missing `iss` were both rejected — the issuer "
                         f"{spec.expected_iss!r} is enforced",
                         "a token with the wrong/missing issuer")


def check_malformed_rejected(base_url, spec, secret, pubkey, now=None):
    tokens = _mk_tokens(base_url, spec, secret, pubkey, now)
    keys = [k for k in tokens if k.startswith("malformed_")]
    return _reject_check(base_url, spec, tokens, keys,
                         f"all {len(keys)} structurally-malformed tokens (bad base64url, wrong "
                         f"segment count) were rejected — the parser fails closed",
                         "a structurally-malformed token")


CHECKS = [
    ("valid-accepted", check_valid_accepted),
    ("alg-none-rejected", check_alg_none_rejected),
    ("signature-rejected", check_signature_rejected),
    ("alg-confusion-rejected", check_alg_confusion_rejected),
    ("expired-rejected", check_expired_rejected),
    ("not-yet-valid-rejected", check_not_yet_valid_rejected),
    ("audience-enforced", check_audience_enforced),
    ("issuer-enforced", check_issuer_enforced),
    ("malformed-rejected", check_malformed_rejected),
]
CHECKS_BY_NAME = dict(CHECKS)


# --------------------------------------------------------------------------- #
# Runner / reporting
# --------------------------------------------------------------------------- #
def _label(passed):
    return "SKIP" if passed is None else ("PASS" if passed else "FAIL")


def _print_result(name, passed, detail):
    print(f"[{_label(passed)}] {name:24s} {detail}")


def run_suite(base_url, spec, secret, pubkey, now=None):
    failures = 0
    for name, fn in CHECKS:
        passed, detail = fn(base_url, spec, secret, pubkey, now)
        _print_result(name, passed, detail)
        if passed is False:
            failures += 1
    return failures


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _resolve(args):
    spec = AuthSpec.from_fixture(args.fixture)
    if getattr(args, "path", None):
        spec.path = args.path
    if getattr(args, "aud", None) is not None:
        spec.expected_aud = args.aud or None
    if getattr(args, "iss", None) is not None:
        spec.expected_iss = args.iss or None
    secret = args.secret.encode("utf-8") if args.secret else DEFAULT_SECRET
    if getattr(args, "pubkey", None):
        pubkey = Path(args.pubkey).read_bytes()
    else:
        pubkey = load_pubkey()
    return spec, secret, pubkey


def cmd_check(args) -> int:
    spec, secret, pubkey = _resolve(args)
    print(f"JWT Auth Test Kit — checking {args.url}")
    print(f"  {spec.auth_scheme} token at GET {spec.path}   aud={spec.expected_aud!r} "
          f"iss={spec.expected_iss!r}")
    print(f"  (set --secret to your server's HS256 key so the kit can mint a valid token +\n"
          f"   otherwise-valid attack tokens; --aud/--iss to what your server enforces)\n")
    failures = run_suite(args.url, spec, secret, pubkey, args.now)
    print()
    if failures == 0:
        print("ALL PROPERTIES PASS/SKIP — this endpoint accepts a valid token and rejects the "
              "attack classes tested.")
        return 0
    print(f"{failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.")
    return 1


def _single(args, name) -> int:
    spec, secret, pubkey = _resolve(args)
    passed, detail = CHECKS_BY_NAME[name](args.url, spec, secret, pubkey, args.now)
    _print_result(name, passed, detail)
    return 1 if passed is False else 0


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled fixtures (endpoint/claim templates — see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        e = manifest[stem]
        print(f"  {stem:16s}  {e.get('auth_scheme','Bearer')} @ GET {e.get('path','/protected'):12s}  "
              f"aud={e.get('expected_aud') or '-'} iss={e.get('expected_iss') or '-'}  "
              f"— {e.get('note','')}")
    return 0


def cmd_demo(args) -> int:
    """Run the whole suite against the bundled reference stubs — zero accounts."""
    import stub_handler
    import stub_handler_naive
    import threading

    print("=" * 74)
    print("  JATK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.")
    print("  NO real endpoint, NO accounts, NO money. This proves the kit works")
    print("  before you point `jatk check --url` at your own app.")
    print("=" * 74)

    spec = AuthSpec.from_fixture(DEFAULT_FIXTURE)
    correct = stub_handler.serve(0, expected_aud=spec.expected_aud, expected_iss=spec.expected_iss)
    naive = stub_handler_naive.serve(0)
    secret = correct.jatk_secret
    pubkey = correct.jatk_pubkey
    cport = correct.server_address[1]
    nport = naive.server_address[1]
    threading.Thread(target=correct.serve_forever, daemon=True).start()
    threading.Thread(target=naive.serve_forever, daemon=True).start()
    try:
        print(f"\n--- CORRECT stub (alg allowlist [HS256], exp/nbf/aud/iss enforced) — expect ALL PASS ---")
        cf = run_suite(f"http://127.0.0.1:{cport}", spec, secret, pubkey)
        print(f"\n--- NAIVE stub (accepts alg:none, confusion, expired, future, wrong aud/iss) — expect the kit to FLAG it ---")
        nf = run_suite(f"http://127.0.0.1:{nport}", spec, secret, pubkey)
    finally:
        correct.shutdown()
        naive.shutdown()

    print("\n" + "=" * 74)
    if cf == 0 and nf > 0:
        print(f"  DEMO OK: correct stub passed all properties; naive stub flagged on {nf} property(ies).")
        print("  The kit distinguishes a secure JWT verifier from a bypassable one.")
        print("=" * 74)
        return 0
    print(f"  DEMO UNEXPECTED: correct failures={cf}, naive failures={nf} (expected 0 and >0).")
    print("=" * 74)
    return 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="jatk",
        description="JWT Auth Test Kit — prove your endpoint's JWT verification is secure.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--url", required=True, help="your endpoint base, e.g. http://localhost:8000")
        sp.add_argument("--fixture", default=DEFAULT_FIXTURE, help=f"fixture name (default {DEFAULT_FIXTURE})")
        sp.add_argument("--secret", default=None, help="your server's HS256 secret (so the kit can mint tokens)")
        sp.add_argument("--pubkey", default=None, help="path to the RSA/EC public-key blob for the confusion token")
        sp.add_argument("--path", default=None, help="override the protected path (default from the fixture)")
        sp.add_argument("--aud", default=None, help="expected audience your server enforces (empty string disables)")
        sp.add_argument("--iss", default=None, help="expected issuer your server enforces (empty string disables)")
        sp.add_argument("--now", type=float, default=None, help="fixed unix time for token exp/nbf (default: real clock)")

    c = sub.add_parser("check", help="run all nine properties against your endpoint")
    common(c)
    c.set_defaults(func=cmd_check)

    for name, _fn in CHECKS:
        sp = sub.add_parser(name, help=f"run just the {name} property")
        common(sp)
        sp.set_defaults(func=lambda a, n=name: _single(a, n))

    sub.add_parser("demo", help="run all nine against the bundled stubs (zero accounts)").set_defaults(func=cmd_demo)
    sub.add_parser("list", help="list bundled fixtures").set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
