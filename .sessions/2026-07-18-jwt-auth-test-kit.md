# Session — JWT Auth Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Sat Jul 18 18:49 UTC 2026
- **branch:** `claude/jwt-auth-test-kit-2026-07-18`
- **base:** `main@1b19e71`
- **purpose:** build the **JWT Auth Test Kit ($29)** to owner-click-ready and land
  it as ONE PR — a NEW sellable in the API-robustness kit family, and the
  HIGHEST-SEVERITY problem class in it (auth bypass), distinct from the webhook
  signature kits, the idempotency kit, the rate-limit kit, and the pagination kit.
  Where the webhook kits verify an inbound provider *signature*, the idempotency
  kit verifies a *safe-retry / exactly-once* contract, the rate-limit kit verifies
  a *throttling* contract, and the pagination kit verifies *result-set integrity*,
  this kit verifies a buyer's OWN JWT verifier is SECURE: that a protected endpoint
  ACCEPTS a valid, correctly-signed, unexpired token with correct claims, and
  REJECTS the critical auth-bypass classes — an `alg:none` unsigned token (the
  classic bypass, RFC 8725 §3.1); a tampered payload / wrong signature / wrong key;
  the RS256→HS256 ALGORITHM-CONFUSION attack (a token signed HS256 using the RSA/EC
  PUBLIC key bytes as the HMAC secret, RFC 8725 §2.1/§3.1); an EXPIRED (`exp` past)
  token; a NOT-YET-VALID (`nbf`/`iat` future) token; a wrong/missing `aud` and a
  wrong/missing `iss` when configured; and a structurally-malformed token (bad
  base64url / wrong segment count). Stdlib-only (HS256 via `hmac`/`hashlib`/`base64`
  /`json`), account-free, runs with a loud DEMO banner against bundled reference
  stubs. Ships: a CORRECT reference stub (pins an alg allowlist, verifies the HS256
  signature, and checks `exp`/`nbf`/`aud`/`iss`), a deliberately NAIVE/broken stub
  (accepts `alg:none`, is vulnerable to algorithm-confusion, and skips
  `exp`/`nbf`/`aud`/`iss`) so the suite can PROVE it catches the bugs, a `jatk.py`
  harness (+ `jatk.js` Node parity) that mints the attack tokens and a valid token
  and fires each at the endpoint, an HTTP-layer real-path test suite (deterministic
  — fixed exp/nbf offsets, no real waiting), real docs-derived fixtures + PROVENANCE
  (cited to RFC 7519 / RFC 7515 / RFC 8725 + the well-known alg:none and RS256→HS256
  attacks; honest that RS256/ES256 signature-math verify is out of the shipped
  stdlib scope), a byte-reproducible buyer bundle, and a §7 owner-gate publish
  packet. The build ENDS at a queued owner ⚑ publish click (rail 13 / CONSTITUTION
  §13) — no publish, no spend, no accounts by the seat.
- **session:** Mirrors the proven pagination- / rate-limit- / idempotency-key-test-kit
  scaffold (the closest templates — same correct-stub + naive-stub evidence pattern)
  but is a genuinely DIFFERENT and higher-severity product: JWT auth-bypass, not
  throttling, result-set integrity, dedup, or inbound signature verification. The
  value proof is built in — the CORRECT stub accepts the valid token and rejects
  every attack, while the NAIVE stub is FLAGGED on the alg:none / algorithm-confusion
  / expired / not-yet-valid / audience / issuer bypasses, so the kit demonstrably
  distinguishes a secure verifier from a bypassable one. Honest scope carried in
  PROVENANCE + the listing: the shipped tests fully cover HS256 + the attack classes
  above (which need no RSA verify) with stdlib only; real RS256/ES256 signature-math
  verification is scoped OUT-OF-BAND and the listing's "what it does NOT do" section
  states that truthfully — no overclaimed RS256 coverage. Born-red card holds the
  substrate-gate red until the deliberate completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]
