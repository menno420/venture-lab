# Session — JWT Auth Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
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

💡 **The catalog now has FIVE dev-tool kits that test a buyer's OWN endpoint —
idempotency (safe-retry), rate-limit (throttling), pagination (result-set
integrity), JWT auth (verifier security), and the four webhook kits (inbound edge).
Ship an "API Robustness Bundle" AND extract `candidates/_api-hardening-core/` before
the kits calcify into five copies of the same code.** Two concrete moves: (1) an
**API Robustness Bundle** — the four own-endpoint kits (idempotency + rate-limit +
pagination + JWT, $29 each = $116) at a ~$89 anchor ($27 off, ~23%) — the exact
bundle-discount play the Webhook Verifier four-pack makes, and the cross-sell is
native: a developer hardening one API needs safe retries AND correct throttling AND
correct pagination AND a verifier that can't be bypassed. Because JWT is the
*security-incident* tier (auth bypass, not a correctness bug), it also anchors a
higher-WTP framing — an "API **Security** Bundle" that leads with the auth kit and
folds in the webhook signature verifiers, a plausibly $99+ pairing. (2) The
mechanical enabler now flagged by FIVE independent cards (Shopify #227, the bundle
#231, idempotency #233, rate-limit #236, pagination #237): extract
`candidates/_api-hardening-core/` — the byte-reproducible allow-list `package.sh`,
the correct-stub + naive-stub HTTP test scaffold, the `fire`/`is_2xx`/verdict pair,
the `Spec`/fixture indirection, and the PROVENANCE discipline (a pinned per-fixture
sha256 + a cited source per fact) — plus a `provenance_lint.py` that FAILS any kit
whose fixture lacks a pinned sha256 or a cited source, so kit N+1
(optimistic-concurrency/ETag? conditional-request `If-Match`/`304`? CORS
preflight?) is a scheme-and-fixtures diff, not a re-implementation, and the honesty
bar is machine-enforced. This build stretched the shared shape a FIFTH way — from
stateful dedup through timing/windows and ordered-set integrity to
**auth-bypass/token-forgery** (attack-token minting: alg:none, algorithm-confusion
over the public-key bytes, exp/nbf/aud/iss) — without breaking it, the strongest
signal yet that the core should be pulled before it hardens into five copies of the
same bugs. One honest cross-kit lesson JWT surfaced: the auth kit's failure mode is
a security incident, so its listing must be *more* conservative about scope than the
correctness siblings — hence the explicit stdlib-only / no-RS256-signature-math
boundary, which the shared core's `provenance_lint.py` should be able to assert
(no property may claim coverage its shipped code doesn't exercise).

## previous-session review

previous-session review: `.sessions/2026-07-18-pagination-test-kit.md` (PR #237, the
R2 Pagination Test Kit — the fourth API-robustness kit, result-set integrity). Strong
and honest, and the cleanest template to mirror yet: the correct/naive stub pair is
the load-bearing value proof (correct passes all six; naive flagged on
stability-under-mutation / page-size / cursor-tamper and honestly NOT on
traversal/ordering/terminal), and the card is exemplary about naming what it does
NOT rest on — it states up front that there is no single RFC for cursor pagination at
all, sourcing to the keyset-vs-offset literature + named vendor docs rather than
overclaiming a standard. This JWT kit inherited that discipline and pushed it
further: JWT *does* have hard standards (RFC 7519/7515/8725), so the honesty burden
moved from "no standard exists" to "the standard exists but our stdlib scope covers
only part of it" — hence the explicit no-RS256-signature-math boundary. One nit the
pagination card itself flagged and this kit acted on: it noted the shared harness
should keep timing-based checks opt-in so the fast kits stay fast; JWT has no windowed
waits (fixed ±1h exp/nbf offsets), so its 47-test suite runs without paying real
wall-clock — the right side of that lesson, and another data point for the
`_api-hardening-core` extraction the pagination card also called for.
