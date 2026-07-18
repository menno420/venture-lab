#!/usr/bin/env python3
"""Example NAIVE / INSECURE JWT-protected endpoint — the bypasses this kit catches.

This handler *looks* like it checks a token, but it ships the mistakes a
from-scratch verifier usually has before the author reads RFC 8725 ("JWT Best
Current Practices"). Each is a real, published auth-bypass class:

  - `alg:none` ACCEPTED. It reads the algorithm from the TOKEN header and, for
    `"none"`, treats the token as valid with no signature at all — the classic
    unsigned-token bypass (RFC 8725 §3.1). Anyone can mint an admin token.
  - ALGORITHM CONFUSION. It is an endpoint that also trusts tokens from an
    identity provider, so it has the IdP's RSA/EC PUBLIC key on hand. Instead of
    pinning the algorithm, it accepts an HS256 token whose HMAC verifies against
    EITHER the local secret OR the public-key bytes — so an attacker who knows the
    public key (it is public!) forges a valid HMAC and is let in. This is the
    RS256->HS256 confusion mistake: using key material meant for one algorithm
    with another (RFC 8725 §2.1). (The kit crafts the attack token with stdlib
    HMAC over the public-key bytes — no RSA math needed to demonstrate the accept.)
  - NO TIME CHECKS. It never looks at `exp` or `nbf`/`iat`, so a token that
    expired last year — or one that is not valid until next year — is accepted
    (RFC 7519 §4.1).
  - NO AUDIENCE / ISSUER CHECKS. It never looks at `aud` or `iss`, so a token
    minted for a different service (or by a different issuer) is accepted
    (RFC 7519 §4.1.1/§4.1.3) — a token-reuse / confused-deputy bypass.

It DOES reject a token whose HMAC matches NEITHER the secret nor the public key
(a genuinely tampered or wrong-key token), and it DOES reject a structurally
malformed token (it cannot parse it) — so `signature-rejected` and
`malformed-rejected` PASS on both this stub and the correct one, and
`valid-accepted` passes on both too. Those three properties do NOT distinguish a
secure verifier from a bypassable one, and the kit says so honestly (mirrors how
the Pagination kit's `traversal`/`ordering`/`terminal` and the Rate-Limit kit's
`under-limit`/`window-reset` don't distinguish their stubs).

It ships in the kit ON PURPOSE so the test suite (test_http_realpath.py) can
DEMONSTRATE that the harness FLAGS the bypasses, not only that it passes a secure
verifier. Against this stub the kit correctly FLAGS:

  - alg-none-rejected        : an `alg:none` token is accepted (200).
  - alg-confusion-rejected   : an HS256 token signed with the public-key bytes is
                               accepted (the confusion bypass).
  - expired-rejected         : an expired token is accepted.
  - not-yet-valid-rejected   : a not-yet-valid (future nbf/iat) token is accepted.
  - audience-enforced        : a wrong/missing `aud` token is accepted.
  - issuer-enforced          : a wrong/missing `iss` token is accepted.

Run standalone:  python3 stub_handler_naive.py 8000
"""
import hashlib
import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from stub_handler import (DEFAULT_AUD, DEFAULT_ISS, DEFAULT_SECRET, _load_pubkey,
                          b64url_decode)


def naive_verify(token: str, secret: bytes, pubkey: bytes):
    """Return the claims dict if this INSECURE verifier accepts the token, else
    raise ValueError. It trusts the token's `alg`, accepts `none`, HMACs against
    the public key too (confusion), and checks NO time/aud/iss claims."""
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("not three segments")
    h_b64, p_b64, s_b64 = parts
    header = json.loads(b64url_decode(h_b64))       # may raise -> reject (malformed)
    claims = json.loads(b64url_decode(p_b64))       # may raise -> reject (malformed)
    alg = header.get("alg")

    # BUG 1: trusts the header's alg, and accepts "none" with no signature.
    if alg == "none" or alg is None:
        return claims

    signing_input = (h_b64 + "." + p_b64).encode("ascii")
    sig = b64url_decode(s_b64)
    # BUG 2 (confusion): accept if the HMAC matches the local secret OR the
    # RSA/EC PUBLIC key bytes — key material meant for a different algorithm.
    for key in (secret, pubkey):
        if key and hmac.compare_digest(sig, hmac.new(key, signing_input,
                                                     hashlib.sha256).digest()):
            # BUG 3+4: no exp/nbf/iat check, no aud/iss check — just let it in.
            return claims
    raise ValueError("signature did not match secret or public key")


def make_handler(secret: bytes, pubkey: bytes):
    class Naive(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            parsed = urlparse(self.path)
            if parsed.path == "/_debug/config":
                self._json(200, {
                    "allowed_algs": "ANY (reads token header — the bug)",
                    "expected_aud": None, "expected_iss": None,
                    "checks": ["signature-or-pubkey-only (no alg pin, no time/aud/iss)"],
                })
                return
            if parsed.path == "/protected":
                token = self._bearer()
                if token is None:
                    self._json(401, {"error": "missing bearer token"})
                    return
                try:
                    claims = naive_verify(token, secret, pubkey)
                except Exception as e:
                    self._json(401, {"error": "invalid token", "detail": str(e)})
                    return
                self._json(200, {"ok": True, "sub": claims.get("sub")})
                return
            self._json(404, {"error": "not found"})

        def _bearer(self):
            raw = self.headers.get("Authorization", "")
            if not raw:
                return None
            parts = raw.split(" ", 1)
            if len(parts) != 2 or parts[0].lower() != "bearer" or not parts[1].strip():
                return None
            return parts[1].strip()

        def _json(self, code, obj):
            data = json.dumps(obj).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Naive


def serve(port: int, secret: bytes = None, pubkey: bytes = None) -> ThreadingHTTPServer:
    sec = secret or DEFAULT_SECRET
    pk = pubkey if pubkey is not None else _load_pubkey()
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(sec, pk))
    httpd.jatk_secret = sec
    httpd.jatk_pubkey = pk
    httpd.jatk_aud = DEFAULT_AUD     # what a CORRECT verifier would enforce (for the harness)
    httpd.jatk_iss = DEFAULT_ISS
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _secret = os.environ.get("JATK_SECRET")
    _sec = _secret.encode("utf-8") if _secret else DEFAULT_SECRET
    print(f"NAIVE (insecure) JWT stub on http://127.0.0.1:{_port} — the kit should "
          f"FLAG this one (accepts alg:none, algorithm-confusion, expired, "
          f"not-yet-valid, wrong aud/iss)")
    serve(_port, _sec).serve_forever()
