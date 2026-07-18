# Fixture provenance

**Honest statement up front:** the material in this directory is **kit-authored
TEST material**, not captures from a live identity provider. A JWT-auth test is
about **verifier security** — which tokens a verifier accepts and rejects — so the
harness *mints* every token it fires, live, at run time (see `../jatk.py`
`attack_tokens`). The `sample_tokens.json` bundle here is **illustrative only** (a
frozen snapshot for eyeballing); nothing in it is load-bearing. No account was
created, no real key was used, and no third-party service was called to build this
kit (this repo's no-new-accounts rule). Every security behaviour this kit checks is
grounded in the public standards and attacks below, so a buyer can audit each claim.

> Reconstructed 2026-07-18 (UTC). The signing secret and the RSA public key here
> are **clearly-labelled TEST material** generated for this kit — never a real
> credential. The private key that pairs with `test_public_key.pem` was generated,
> used to derive the public key, and **immediately discarded**; this kit never
> signs RS256 and never needs it.

## The standards this kit tests against

- **RFC 7519 — JSON Web Token (JWT).** Defines the token structure
  (`header.payload.signature`, each base64url) and the registered claims the kit
  checks: `exp` (§4.1.4, expiration), `nbf` (§4.1.5, not-before), `iat` (§4.1.6,
  issued-at), `aud` (§4.1.3, audience), and `iss` (§4.1.1, issuer). The
  `expired-rejected`, `not-yet-valid-rejected`, `audience-enforced`, and
  `issuer-enforced` properties assert these.
- **RFC 7515 — JSON Web Signature (JWS).** Defines the compact serialization and
  the signature over `ASCII(BASE64URL(header) || '.' || BASE64URL(payload))`. The
  `signature-rejected` property asserts the HS256 (`HMAC-SHA256`) signature is
  actually verified — a tampered payload or a wrong key fails.
- **RFC 8725 — JSON Web Token Best Current Practices.** The security core:
  - **§3.1 — do not trust the token's `alg`; reject `"none"`.** The
    `alg-none-rejected` property fires an unsigned `{"alg":"none"}` token; a secure
    verifier refuses it. Accepting it is the classic full-auth-bypass (anyone mints
    any token).
  - **§2.1 / §3.1 — algorithm-confusion / key-material confusion.** A verifier that
    also holds an asymmetric (RSA/EC) **public** key must not let an attacker
    present an **HS256** token and have the verifier HMAC it against that public
    key — the public key is public, so the attacker can forge a valid HMAC. The fix
    is to **pin the expected algorithm** and use each key only with its intended
    algorithm. The `alg-confusion-rejected` property fires exactly this token: an
    HS256 JWT signed with the bytes of `test_public_key.pem` as the HMAC secret. A
    pinned verifier rejects it (it uses its real HS256 secret); the bundled naive
    verifier accepts it (it HMACs against the public key) — the demonstrated bypass.

## Honest scope: HS256 + the attack classes, stdlib only

This kit is **stdlib-only** (Python `hmac`/`hashlib`/`base64`/`json`; Node
`crypto`). That fully covers the HS256 signature path and **every attack class the
kit tests** — valid-accept, `alg:none`, tampered / wrong-key, algorithm-confusion,
expired, not-yet-valid, wrong/missing `aud` and `iss`, and malformed — because none
of those needs RSA/ECDSA signature math to demonstrate. In particular, the
algorithm-confusion check needs **no RSA verify**: it forges an HS256 token over the
public-key bytes, which a bypassable verifier accepts and a pinned verifier rejects.

**What this kit does NOT do (stated so no coverage is overclaimed):** it does not
perform real **RS256 / ES256 (RSA / ECDSA) signature-math verification**. Testing
that an endpoint *correctly verifies a genuinely RSA-signed token* is out of the
shipped stdlib scope — it would require an asymmetric-crypto dependency. The kit
tests the verifier-security properties that do not need it (the highest-value
bugs), and the listing's "what it does NOT do" section says so plainly.

## The properties this kit checks (and their basis)

| Property | What the kit asserts | Basis |
|---|---|---|
| **valid-accepted** | a valid, correctly-signed, unexpired HS256 token with correct claims is accepted (2xx) | RFC 7515/7519 (a conforming token must be accepted) |
| **alg-none-rejected** | an `{"alg":"none"}` unsigned token is rejected | RFC 8725 §3.1 (the classic bypass) |
| **signature-rejected** | a tampered payload AND a wrong-key token are rejected | RFC 7515 (the signature is actually verified) |
| **alg-confusion-rejected** | an HS256 token signed with the RSA/EC public-key bytes is rejected | RFC 8725 §2.1/§3.1 (key-material / algorithm confusion) |
| **expired-rejected** | a token with `exp` in the past is rejected | RFC 7519 §4.1.4 |
| **not-yet-valid-rejected** | a token with `nbf`/`iat` in the future is rejected | RFC 7519 §4.1.5/§4.1.6 |
| **audience-enforced** | a wrong/missing `aud` is rejected when an audience is configured | RFC 7519 §4.1.3 |
| **issuer-enforced** | a wrong/missing `iss` is rejected when an issuer is configured | RFC 7519 §4.1.1 |
| **malformed-rejected** | a token without three valid base64url/JSON segments is rejected | RFC 7515/7519 (structure) |

**What the kit asserts vs. what is a modelling choice.** The behaviours are all
*externally visible*: which tokens the endpoint accepts (2xx) vs. rejects (4xx). The
reference verifier's *implementation* (a pinned HS256 allowlist + `hmac` +
`exp`/`nbf`/`aud`/`iss` checks in `../stub_handler.py`) is one honest way to satisfy
them; a buyer's API may satisfy the same contract with a vetted JWT library
configured to pin the algorithm and enforce the claims. The kit tests the contract,
not the implementation.

## The vendored fixtures

| File | Role | sha256 |
|---|---|---|
| `test_public_key.pem` | a throwaway RSA-2048 **public** key (a public key is not a secret); its bytes are the HMAC secret the algorithm-confusion attack token is forged with | `7690e8edc9accc5bbff8221c7b66eb3bb24eba23d4e8fa1ebc5bdaea63b1907f` |
| `sample_tokens.json` | ILLUSTRATIVE frozen snapshot of the minted token set (reference `now=1800000000`), for eyeballing only — the harness re-mints live | `b0371103a6f94b2212c4600cfd2503a51627e82cf45412d62f6795c83fdc4b7e` |

`MANIFEST.json` (kit-authored, sha256
`e45e0b0cdde637d592dfca6dbc34e94078745178fd08eae8b03ad295b19fd7e4`) maps each
fixture stem to the endpoint's protected path, the auth header + scheme, the
expected `aud`/`iss`, and the subject — so `--fixture` (or an edited manifest) can
point the harness at your own API's route and expected claims.

## What is TEST material, not a real credential

The HS256 secret is the clearly-labelled non-secret string
`jatk-demo-hs256-secret-not-a-real-secret` (a default in `../jatk.py` and
`../stub_handler.py`; also nameable via `JATK_SECRET`). The `test_public_key.pem`
is a **public** key — safe to ship by definition — whose private half was discarded
at generation time. The reference stubs (`../stub_handler.py` /
`../stub_handler_naive.py` and the Node equivalents inside `../jatk.js`'s `demo`)
are the kit's own code, not vendor code; the naive stub exists specifically so the
test suite can prove the harness catches a bypassable verifier (it accepts
`alg:none`, the confusion token, expired, not-yet-valid, and wrong/missing
`aud`/`iss`). The `../.env.example` names optional configuration only; **no real
secret ships in this kit**.
