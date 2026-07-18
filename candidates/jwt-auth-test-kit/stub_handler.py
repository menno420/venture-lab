#!/usr/bin/env python3
"""Example CORRECT JWT-protected endpoint — stdlib only, ~190 lines.

Reference code you can adapt. It does the things a SECURE JWT verifier must (see
GOTCHAS.md for the why, fixtures/PROVENANCE.md for the sources — RFC 7519 JWT,
RFC 7515 JWS, and RFC 8725 "JWT Best Current Practices", plus the well-known
`alg:none` and RS256->HS256 algorithm-confusion attacks). A protected route
`GET /protected` reads `Authorization: Bearer <jwt>` and returns 200 only for a
token that survives EVERY check; anything else is 401.

The contract this handler honours:

  1. ALGORITHM ALLOWLIST (pinned). The verifier decides the acceptable algorithm
     itself — it does NOT trust the token header's `alg`. Here the allowlist is
     exactly `{"HS256"}`. `"none"` is refused outright (RFC 8725 §3.1), and so is
     any `alg` not on the list. This is the single most important defence: it is
     what stops the RS256->HS256 CONFUSION attack, where a token's header claims a
     symmetric algorithm so a naive verifier HMACs it against key material meant
     for an asymmetric one (RFC 8725 §2.1).
  2. SIGNATURE VERIFY (HS256). The signature is `HMAC-SHA256(secret,
     b64url(header) + "." + b64url(payload))`, compared with `hmac.compare_digest`.
     A tampered payload, a wrong signature, or a token signed with a different key
     fails here. The secret is used for HS256 ONLY — never is any other key
     material (e.g. an RSA/EC public key) accepted as an HMAC secret.
  3. TIME CLAIMS. `exp` must be in the future and `nbf` (and a present `iat`) must
     not be in the future — an expired or not-yet-valid token is rejected
     (RFC 7519 §4.1.3/§4.1.5/§4.1.6). A small leeway is allowed for clock skew.
  4. AUDIENCE + ISSUER. When the verifier is configured with an expected `aud` /
     `iss`, a token whose `aud` / `iss` is wrong or missing is rejected
     (RFC 7519 §4.1.1/§4.1.3). Configure them to `None` to disable that check.
  5. STRUCTURE. A token without exactly three base64url segments, or with a
     segment that is not valid base64url / JSON, is rejected — never coerced.

The reference verifier is deliberately a single, readable function
(`verify_jwt`). Real deployments use a vetted JWT library; the externally-visible
CONTRACT this models — pin the algorithm, verify the signature with the right
key, enforce the time/audience/issuer claims, reject malformed input — is the
same one a library must be configured to enforce.

`jatk` mints a valid token and the attack tokens and fires them at a handler like
this. Run standalone:
    python3 stub_handler.py 8000
Optional env:
    JATK_SECRET=...        # HS256 secret (demo default if unset — a NON-secret)
    JATK_AUD=jatk-demo-api # expected audience  (empty disables the aud check)
    JATK_ISS=jatk-demo-issuer  # expected issuer (empty disables the iss check)
    JATK_PUBKEY_FILE=...   # a "public key" blob, present ONLY so the confusion
                           # attack has key material to forge with; the CORRECT
                           # verifier NEVER uses it (that is the whole point).
"""
import base64
import hashlib
import hmac
import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

# Clearly-labelled NON-secrets: demo defaults so the bundled kit runs with zero
# configuration. A real deployment loads a real secret from its own secret store.
DEFAULT_SECRET = b"jatk-demo-hs256-secret-not-a-real-secret"
DEFAULT_AUD = "jatk-demo-api"
DEFAULT_ISS = "jatk-demo-issuer"
# The confusion attack needs the bytes of a public key the server also holds. A
# real (throwaway) RSA public key ships in fixtures/test_public_key.pem — a PUBLIC
# key is not a secret. The correct verifier below never touches it.
_PUBKEY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "fixtures", "test_public_key.pem")

ALLOWED_ALGS = ("HS256",)   # pinned — the header's alg is NOT trusted
LEEWAY = 60                 # seconds of clock-skew tolerance on time claims


def b64url_decode(seg: str) -> bytes:
    """Decode one base64url segment, tolerating missing padding. Raises
    ValueError (via binascii.Error subclass) on invalid input."""
    pad = "=" * (-len(seg) % 4)
    return base64.urlsafe_b64decode(seg.encode("ascii") + pad.encode("ascii"))


def b64url_encode(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


class JWTError(ValueError):
    """A token failed verification. `.reason` is a short machine tag."""

    def __init__(self, reason: str, detail: str = ""):
        super().__init__(detail or reason)
        self.reason = reason
        self.detail = detail or reason


def verify_jwt(token: str, secret: bytes, expected_aud, expected_iss,
               now=None, allowed_algs=ALLOWED_ALGS, leeway=LEEWAY) -> dict:
    """Verify a compact JWS/JWT. Return the claims dict, or raise JWTError.

    The order matters: structure -> algorithm allowlist -> signature -> time ->
    audience/issuer. Each raise carries a short `.reason` the handler maps to 401.
    """
    now = time.time() if now is None else now

    # (5) structure: exactly three base64url segments.
    parts = token.split(".")
    if len(parts) != 3:
        raise JWTError("malformed", f"expected 3 segments, got {len(parts)}")
    h_b64, p_b64, s_b64 = parts
    try:
        header = json.loads(b64url_decode(h_b64))
    except Exception as e:  # bad base64url or bad JSON
        raise JWTError("malformed", f"header not decodable: {e}")
    if not isinstance(header, dict):
        raise JWTError("malformed", "header is not a JSON object")

    # (1) algorithm allowlist — the header's alg is NOT trusted, only checked
    # against the verifier's pinned list. "none" and anything off-list are out.
    alg = header.get("alg")
    if alg == "none" or alg is None:
        raise JWTError("alg_none", "unsigned/none algorithm refused")
    if alg not in allowed_algs:
        raise JWTError("alg_not_allowed", f"alg {alg!r} not in allowlist {list(allowed_algs)}")

    # (2) signature: HMAC-SHA256 over the signing input, constant-time compare.
    signing_input = (h_b64 + "." + p_b64).encode("ascii")
    try:
        sig = b64url_decode(s_b64)
    except Exception as e:
        raise JWTError("malformed", f"signature not decodable: {e}")
    expected_sig = hmac.new(secret, signing_input, hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected_sig):
        raise JWTError("bad_signature", "signature mismatch (tampered/wrong key)")

    # payload
    try:
        claims = json.loads(b64url_decode(p_b64))
    except Exception as e:
        raise JWTError("malformed", f"payload not decodable: {e}")
    if not isinstance(claims, dict):
        raise JWTError("malformed", "payload is not a JSON object")

    # (3) time claims: exp in the future, nbf/iat not in the future.
    exp = claims.get("exp")
    if exp is not None and now > float(exp) + leeway:
        raise JWTError("expired", f"exp {exp} is in the past")
    nbf = claims.get("nbf")
    if nbf is not None and now + leeway < float(nbf):
        raise JWTError("not_yet_valid", f"nbf {nbf} is in the future")
    iat = claims.get("iat")
    if iat is not None and now + leeway < float(iat):
        raise JWTError("not_yet_valid", f"iat {iat} is in the future")

    # (4) audience + issuer, when configured.
    if expected_aud:
        aud = claims.get("aud")
        aud_ok = (aud == expected_aud) or (isinstance(aud, list) and expected_aud in aud)
        if not aud_ok:
            raise JWTError("bad_audience", f"aud {aud!r} != expected {expected_aud!r}")
    if expected_iss:
        if claims.get("iss") != expected_iss:
            raise JWTError("bad_issuer", f"iss {claims.get('iss')!r} != expected {expected_iss!r}")

    return claims


def _load_pubkey():
    try:
        with open(_PUBKEY_PATH, "rb") as fh:
            return fh.read()
    except OSError:
        return b""


def make_handler(secret: bytes, expected_aud, expected_iss):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            parsed = urlparse(self.path)
            if parsed.path == "/_debug/config":
                # Non-secret introspection: what this verifier enforces. Never
                # exposes the HMAC secret. Lets a harness auto-discover aud/iss.
                self._json(200, {
                    "allowed_algs": list(ALLOWED_ALGS),
                    "expected_aud": expected_aud or None,
                    "expected_iss": expected_iss or None,
                    "checks": ["alg-allowlist", "signature", "exp", "nbf", "aud", "iss"],
                })
                return
            if parsed.path == "/protected":
                token = self._bearer()
                if token is None:
                    self._json(401, {"error": "missing bearer token"})
                    return
                try:
                    claims = verify_jwt(token, secret, expected_aud, expected_iss)
                except JWTError as e:
                    self._json(401, {"error": "invalid token", "reason": e.reason,
                                     "detail": e.detail})
                    return
                self._json(200, {"ok": True, "sub": claims.get("sub"),
                                 "aud": claims.get("aud"), "iss": claims.get("iss")})
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

    return Handler


def serve(port: int, secret: bytes = None, expected_aud=DEFAULT_AUD,
          expected_iss=DEFAULT_ISS) -> ThreadingHTTPServer:
    httpd = ThreadingHTTPServer(("127.0.0.1", port),
                                make_handler(secret or DEFAULT_SECRET,
                                             expected_aud, expected_iss))
    httpd.jatk_secret = secret or DEFAULT_SECRET       # expose for in-process callers
    httpd.jatk_pubkey = _load_pubkey()
    httpd.jatk_aud = expected_aud
    httpd.jatk_iss = expected_iss
    return httpd


if __name__ == "__main__":
    import sys
    _port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    _secret = os.environ.get("JATK_SECRET")
    _sec = _secret.encode("utf-8") if _secret else DEFAULT_SECRET
    _aud = os.environ.get("JATK_AUD", DEFAULT_AUD)
    _iss = os.environ.get("JATK_ISS", DEFAULT_ISS)
    print(f"correct JWT-protected stub on http://127.0.0.1:{_port} "
          f"(GET /protected, alg allowlist {list(ALLOWED_ALGS)}, "
          f"aud={_aud!r}, iss={_iss!r})")
    serve(_port, _sec, _aud, _iss).serve_forever()
