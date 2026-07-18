# Marketplace listing copy — JWT Auth Test Kit v0.1

> **Status:** `reference`

**Title:** JWT Auth Test Kit — prove your token verification rejects alg:none and algorithm-confusion

**Short description (≤200 chars, 187):** Point it at your endpoint and prove your
JWT auth rejects alg:none, RS256->HS256 confusion, tampered, expired, and
wrong-aud/iss tokens, catching naive verifiers. Stdlib only. No account.

**Price:** $29 (one-time)

## Description

JWT verification is easy to write and dangerous to get subtly wrong — and when it
is wrong, the failure is not a bug, it is an **auth bypass**. The verifier reads
the algorithm from the token and honours `alg:none`, so anyone mints an admin
token. It also trusts an identity provider's **public** key, and a naive
`verify(token, key)` HMACs an HS256 token against that public key — the RS256→HS256
**algorithm-confusion** attack, and the public key is public. It never checks `exp`,
so a leaked token is valid forever; never checks `aud`/`iss`, so a token minted for
another service is accepted. None of these show up in a green unit-test suite,
because a happy-path test only ever fires a valid token.

The JWT Auth Test Kit points at your own protected endpoint and proves the nine
properties a **secure** JWT verifier must satisfy — runnable in seconds, no vendor
account, no live API, stdlib only. It is **not** a webhook-signature kit, **not**
the Idempotency Key Test Kit, **not** the Rate-Limit Test Kit, and **not** the
Pagination Test Kit; it tests the highest-severity problem class in API robustness:
**auth bypass**. Every property is grounded in **RFC 7519** (JWT), **RFC 7515**
(JWS), and **RFC 8725** ("JWT Best Current Practices"), plus the well-known
`alg:none` and RS256→HS256 attacks.

- **Accepts a valid token.** A correctly-signed, unexpired HS256 token with the
  right claims is accepted (2xx).
- **Rejects `alg:none`.** The classic unsigned-token bypass — the verifier decides
  the algorithm from an allowlist, not the token.
- **Rejects a bad signature.** A tampered payload and a wrong-key token both fail.
- **Rejects algorithm-confusion.** An HS256 token signed with the RSA/EC public-key
  bytes is rejected — the verifier pins its algorithm and never HMACs against a
  public key.
- **Rejects expired and not-yet-valid tokens.** `exp` in the past, `nbf`/`iat` in
  the future — both refused.
- **Enforces `aud` and `iss`.** A wrong or missing audience/issuer is rejected when
  you configure them.
- **Fails closed on malformed input.** A token that is not three valid base64url
  segments is rejected, not coerced or 500'd.

## What makes it a *test* kit, not a blog post

It ships **two reference verifiers**: a correct one (pins an alg allowlist, verifies
the HS256 signature, enforces `exp`/`nbf`/`aud`/`iss`) and a deliberately naive one
(accepts `alg:none`, HMACs a token against a public key it holds, skips the
time/audience/issuer checks). Run `jatk demo` and watch the harness pass all nine
against the correct verifier and *flag* the naive one on `alg-none`,
`alg-confusion`, `expired`, `not-yet-valid`, `audience`, and `issuer`. That
correct/broken pair is the proof the checks actually distinguish a secure verifier
from a bypassable one — and the kit is honest that three of the nine properties
(`valid-accepted`, `signature-rejected`, `malformed-rejected`) don't distinguish the
two, so it never overclaims.

Runs in Python or Node, entirely from the standard library. No `pip install`, no
`npm install`, no account required to run any of it.

## What's inside

- The harness in two languages: `jatk.py` (Python) and `jatk.js` (Node), same
  commands (`check`, the nine single-property checks, `demo`, `list`).
- A **correct** reference verifier (`stub_handler.py`) you can read — a pinned
  `HS256` allowlist, an `hmac.compare_digest` signature check, and
  `exp`/`nbf`/`aud`/`iss` enforcement over `GET /protected`.
- A **naive** verifier (`stub_handler_naive.py`) with the classic bypasses, shipped
  so the suite can prove the harness catches them.
- Endpoint/claim templates + `PROVENANCE.md` grounding every property in its RFC /
  attack source, with a pinned sha256 per vendored fixture, plus a throwaway RSA
  **public** key for the confusion token.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 47 tests) — every
  request fired over real HTTP against a reference verifier; time claims are fixed
  ±1h offsets, so it runs fast.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No account, no dependencies, no build step.
- No secret values live in the kit; `.env.example` names optional config only.

## What it does NOT do (so you know what you're buying)

- It does **not** perform real **RS256 / ES256 (RSA / ECDSA) signature-math
  verification**. Testing that your endpoint correctly verifies a genuinely
  RSA-signed token is **out of the shipped stdlib scope** — it would need an
  asymmetric-crypto dependency. The kit tests the HS256 signature path and every
  auth-bypass class above (none of which needs RSA verify), which are the
  highest-severity bugs. The algorithm-confusion check needs **no** RSA verify — it
  forges an HS256 token over the public-key bytes, which a bypassable verifier
  accepts and a pinned one rejects.
- It does **not** verify webhook signatures / HMAC (the Webhook Test Kits), test
  idempotency (the Idempotency Key Test Kit), test throttling (the Rate-Limit Test
  Kit), or test pagination (the Pagination Test Kit). This is a distinct,
  higher-severity problem class: auth bypass.
- It does **not** talk to any live API, create an account, or move money. The `demo`
  runs entirely in-process.
- It tests the **externally-visible verifier contract** (which tokens are accepted
  vs. rejected), not your token-issuance flow, key rotation, refresh tokens,
  revocation, or transport security (use HTTPS).
- The bundled secret is a clearly-labelled **non-secret** and the bundled key is a
  **public** key; the fixtures are kit-authored TEST material (cited in
  `PROVENANCE.md`), not captures from a live identity provider.

## FAQ

**Doesn't my JWT library handle all this?**
Only if it's *configured* to. The bypasses come from libraries used with defaults
that trust the token's `alg`, or a verify call passed the wrong key, or claims left
unchecked. This kit fires the exact attack tokens (`alg:none`, the confusion token,
expired, wrong-`aud`/`iss`) at *your* running endpoint and proves your
configuration rejects them — the thing a happy-path test never does.

**Why not just read RFC 8725?**
You should — it's the source this kit is built on. What you're paying for is the
harness that proves *your* endpoint honours it, including the algorithm-confusion
and `alg:none` tokens a from-memory test skips, plus the correct/naive reference
pair that demonstrates the checks catch a bypassable verifier. The free substitute
is real; the kit is the done, runnable version.

**Does it test RS256?**
It tests the RS256→HS256 **confusion** attack (which needs no RSA math). It does
**not** do real RSA/ECDSA signature-math verification — that's out of the stdlib
scope, stated plainly above so nothing is overclaimed.

**Refunds / support / license:** [owner-to-set — storefront defaults; suggested:
14-day no-questions refund, single-developer license, email support best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha` at
build time, branch `claude/jwt-auth-test-kit-2026-07-18`):

- `candidates/jwt-auth-test-kit/jatk.py@de98e59cf94472b944bf8c8c70fb8d30f543905b`
  — the harness (nine properties, token minting, demo, list).
- `candidates/jwt-auth-test-kit/jatk.js@5425adee5e5837796afa589ae9e5241f36916176`
  — the Node parity port (same nine properties + demo).
- `candidates/jwt-auth-test-kit/stub_handler.py@1e4ad46ce90d71d481c357d3c82eead43cf5395a`
  — the CORRECT reference verifier (pinned HS256 allowlist, signature verify,
  exp/nbf/aud/iss enforcement).
- `candidates/jwt-auth-test-kit/stub_handler_naive.py@13318862a0bea447e39d8ebd6a372eeaa67a3c60`
  — the deliberately bypassable verifier (alg:none, algorithm-confusion, no
  time/aud/iss checks — the value proof).
- `candidates/jwt-auth-test-kit/test_http_realpath.py@7c21400e5b084f02b27c7e5bf4940f6a987937a7`
  — the 47-test HTTP real-path suite (correct all-pass; naive flagged on 6;
  valid-accepted + signature + malformed honestly non-distinguishing; the aud/iss
  SKIP paths; verify_jwt + mint unit coverage).
- `candidates/jwt-auth-test-kit/GOTCHAS.md@8e2b2cadca09c2ae6e5b7513bb8cbe85da3971a2`
  — the bypass classes, each mapped to a kit command.
- `candidates/jwt-auth-test-kit/fixtures/PROVENANCE.md@a3a998e1596947207b6a877139cff0692a29ce9e`
  — the honest source statement (RFC 7519/7515/8725 + the alg:none and RS256->HS256
  attacks; stdlib-only scope, RS256 signature-math out of band) + per-fixture sha256.
- `candidates/jwt-auth-test-kit/dist/jwt-auth-test-kit-v0.1.zip@f7009ce454c438282009f2110eea75e2a4b3f9a5`
  — the buyer bundle (sha256
  `d772b26e11ac9e7673c3dd4a47fa9c1671384ae3b8805d1068ccc2d55f391a61`, 40,703 bytes,
  13 content files; byte-reproducible via `package.sh`).
