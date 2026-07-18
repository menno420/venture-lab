# JWT auth gotchas — the one-page checklist

The bypass classes that repeatedly break hand-rolled (and mis-configured) JWT
verifiers. Each maps to a `jatk` command that proves your endpoint is not making
the mistake. Sources cited in `fixtures/PROVENANCE.md` (RFC 7519 JWT, RFC 7515 JWS,
RFC 8725 "JWT BCP").

## 1. `alg:none` — the unsigned-token bypass

A JWT header carries an `alg` field. If your verifier **reads the algorithm from
the token** and honours `"none"`, an attacker sends `{"alg":"none"}` with any
payload and **no signature**, and is let in as anyone — full auth bypass. The fix:
the **verifier** decides the algorithm, from an allowlist it controls; `"none"` is
never on it (RFC 8725 §3.1).

**Check it:** `jatk alg-none-rejected` — fires an unsigned `alg:none` token and
asserts a 4xx.

## 2. Algorithm confusion (RS256 → HS256)

The most subtle one. Your service verifies RS256 tokens from an identity provider,
so it has the IdP's **public** key on hand. A naive `verify(token, key)` that reads
the algorithm from the token will, for an **HS256** token, treat `key` as an HMAC
secret. But the public key is **public** — so an attacker forges an HS256 token,
HMAC-signs it with the public-key bytes, and the verifier accepts it. The fix: **pin
the expected algorithm** and use each key only with its intended algorithm — never
feed a public key to an HMAC verify (RFC 8725 §2.1).

**Check it:** `jatk alg-confusion-rejected` — mints an HS256 token signed with the
public-key bytes and asserts a 4xx. (Needs `--pubkey`; the bundled one is used by
default. SKIPs if no public key is available.)

## 3. Not actually verifying the signature

A tampered payload or a token signed with a different key must fail. Two failure
modes: decoding the payload **without** checking the signature at all (some
libraries have a `decode` that does not verify), or comparing signatures with `==`
in a way that leaks timing. Verify with the right key using a constant-time compare
(`hmac.compare_digest`).

**Check it:** `jatk signature-rejected` — fires a tampered token and a wrong-key
token and asserts both are rejected.

## 4. No expiry / not-before checks

A token with `exp` in the past must be rejected; a token with `nbf` (or `iat`) in
the future is not valid yet. Skipping these means a leaked token is valid **forever**
(RFC 7519 §4.1.4/§4.1.5/§4.1.6). Allow a small clock-skew leeway, but do check.

**Check it:** `jatk expired-rejected` and `jatk not-yet-valid-rejected` — fire an
expired token and a future-`nbf`/`iat` token and assert each is rejected.

## 5. No audience / issuer checks (token reuse / confused deputy)

`aud` says *which service* the token is for; `iss` says *who minted it*. If you skip
them, a token minted for a **different** service (or by a **different** issuer) is
accepted by yours — a token-reuse / confused-deputy bypass (RFC 7519 §4.1.1/§4.1.3).
Configure the expected `aud`/`iss` and reject anything else, including a **missing**
one.

**Check it:** `jatk audience-enforced` and `jatk issuer-enforced` — fire wrong and
missing `aud`/`iss` and assert each is rejected. (SKIPs if you don't configure an
expected value.)

## 6. Not failing closed on malformed input

A token that is not three base64url segments, or whose header/payload is not valid
base64url/JSON, must be **rejected** — never coerced, and never a 500 that reveals a
stack trace. The parser should fail closed.

**Check it:** `jatk malformed-rejected` — fires several malformed tokens (bad
base64url, wrong segment count) and asserts each is rejected.

## 7. Two honest non-signals (and the scope of the test)

- **`valid-accepted`, `signature-rejected`, and `malformed-rejected` don't
  distinguish a bypassable verifier from a secure one on their own.** Even the
  naive reference verifier accepts a valid token, rejects a token whose HMAC matches
  neither key it holds, and rejects an unparseable token — so those three pass on
  both stubs. The distinguishing failures are `alg-none`, `alg-confusion`,
  `expired`, `not-yet-valid`, `audience`, and `issuer`. The kit says this out loud
  rather than overclaiming (`stub_handler_naive.py` documents which bypasses each
  property does and doesn't catch).
- **Scope.** This kit tests the externally-visible **verifier** contract: which
  tokens a protected endpoint accepts vs. rejects. It does **not** test your
  token-issuance flow, key rotation, refresh tokens, revocation, or transport
  security (use HTTPS), and it does **not** perform real RS256/ES256 signature-math
  verification (out of the stdlib scope — see `fixtures/PROVENANCE.md`). It checks
  that whatever verifier you built pins its algorithm, verifies the signature,
  enforces the time/audience/issuer claims, and fails closed on garbage.

---

Run all nine at once with `jatk check --url … --secret …`, and see them distinguish
a secure verifier from a bypassable one with `jatk demo`.
