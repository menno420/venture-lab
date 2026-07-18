# JWT Auth Test Kit — intake (ORDER 016 build, 2026-07-18)

> A stdlib-only local test harness + reference verifiers that lets any developer
> verify their JWT authentication is SECURE — a protected endpoint ACCEPTS a valid,
> correctly-signed, unexpired token with the right claims and REJECTS the critical
> auth-bypass classes (alg:none, tampered/wrong-key, RS256→HS256 algorithm-confusion,
> expired, not-yet-valid, wrong/missing aud/iss, malformed) — at the HTTP layer, in
> seconds, with no live API and no account.

## What it is

The webhook-/idempotency-/rate-limit-/pagination-test-kit **packaging pattern**
(stdlib harness + docs-derived fixtures + a correct reference stub + a deliberately
naive stub + HTTP real-path suite + byte-reproducible bundle + §7 owner-gate packet,
proven across the LIVE Stripe kit, the GitHub/Slack/Shopify kits, the Idempotency
kit, the Rate-Limit kit, and the Pagination kit) applied to the **highest-severity
problem class in the family**: **JWT verifier security — auth bypass**, NOT signature
verification of an inbound provider, NOT dedup/safe-retry, NOT throttling, and NOT
pagination. Where the webhook kits verify an *inbound* provider signature, the
idempotency kit verifies a buyer's *safe-retry* contract, the rate-limit kit
verifies a *throttling* contract, and the pagination kit verifies *result-set
integrity*, this kit verifies a buyer's OWN JWT verifier's *security*: it accepts a
valid token and rejects every bypass class. Ships as: a CORRECT reference verifier
(pins an `HS256` allowlist, `hmac.compare_digest` signature check, `exp`/`nbf`/`aud`
/`iss` enforcement over `GET /protected`), a deliberately NAIVE verifier (accepts
`alg:none`, HMACs a token against a public key it holds → algorithm-confusion, skips
the time/audience/issuer checks) so the suite can PROVE the harness catches the
bypasses, a language-agnostic harness (Python `jatk.py` + Node `jatk.js`) that mints
the attack tokens and fires them, endpoint/claim templates + `PROVENANCE.md` + a
throwaway RSA **public** key for the confusion token, a 47-test HTTP real-path suite,
and `package.sh` → `dist/jwt-auth-test-kit-vX.Y.zip`.

## Provenance of this build

Built under **ORDER 016** (live owner overnight/continued autonomous-build
authorization, reaffirmed by the live owner turn 2026-07-18) as a NEW sellable in
the API-robustness kit family (roadmap R3). It **reuses the kit scaffold's
structure** (file set, evidence bar, packaging, listing/vetting grammar — closest
templates are the Pagination kit, PR #237, the Rate-Limit kit, PR #236, and the
Idempotency kit, PR #233, which have the same correct-stub + naive-stub evidence
pattern) but is **not** an N+1 of any existing line — it is a distinct product in a
distinct, HIGHER-severity problem class (auth bypass), so the scoring below is an
analog estimate inherited from the dev-tool kit line, not a fresh ideation re-score.

## Dependency / scope decision (honest)

Built **stdlib-only** (option b of the build brief): HS256 via `hmac`/`hashlib`/
`base64`/`json`, which fully covers valid-accept + every attack class (alg:none,
tampered/wrong-key, algorithm-confusion, exp/nbf, aud/iss, malformed) — the
highest-value bugs, none of which needs RSA verify. Real RS256/ES256
signature-math verification is HONESTLY scoped OUT-OF-BAND (it would require an
asymmetric-crypto dependency); the listing's "what it does NOT do" section states
that plainly. The algorithm-confusion attack is demonstrated with stdlib HMAC over
the public-key bytes — no RSA verify needed to show the naive verifier accepting it.

## Scoring (kill-rule intake rubric, inherited weights — analog estimate)

| Axis | W | Score (analog to the sibling kits) |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3.5 |
| **Weighted total** | | **≈3.68 — BUILD (dev-tool kit line, highest-severity problem class)** |

## Kill-rule fields (provisional — bound at this INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on a free "your JWT verifier probably
  accepts alg:none / is vulnerable to algorithm confusion" gotcha article within
  **30 days of publish**, else ledgered negative (same bar as the sibling kits).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting packet
  once the publish click is DONE-flipped):** **T+7** funnel checkpoint · **T+30**
  kill-rule deadline (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode article on the exact "alg:none + RS256→HS256 confusion
  are still bypassing hand-rolled JWT auth" pain ⚑; (2) cross-link from the sibling
  dev-tool listings — the Idempotency, Rate-Limit, and Pagination kits and the
  webhook kits (adjacent buyer: a developer hardening an API needs a secure JWT
  verifier alongside safe-retry, throttling, and correct pagination) ⚑; (3) Gumroad
  Discover ⚑. Distinct angle vs the siblings: this is the *auth-bypass* rung — the
  highest-severity of API robustness, the one that is a security incident when it
  fails, not just a correctness bug.
- **Max agent-effort budget:** ≤80k tokens to a buildable v0.1 zip.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — the proven sibling (Stripe kit)
  has 0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified until
  first sale.

## Why this might fail

JWT auth is a well-documented area, every major language has a vetted JWT library,
and the correct configuration (pin the algorithm, enforce the claims) is a few lines
once you know it. The paid delta is the same shape as the sibling kits' delta: a
runnable harness that tests a buyer's OWN endpoint against the bypass classes + the
correct/naive reference pair that demonstrably catches a bypassable verifier + the
docs discipline. A free blog post or the RFC 8725 BCP substitutes substantially. The
$29 price sits on catalog precedent (the sibling kits at $29), not measured
JWT-specific willingness-to-pay, and distribution is the same owner-gated channel
where the Stripe kit has produced 0 organic sales so far. Two honest structural
pluses: (1) the failure mode is a **security incident** (auth bypass), which raises
willingness-to-pay above the correctness-bug siblings; (2) `alg:none` and the
RS256→HS256 confusion are **invisible in a green unit-test suite** (a happy-path
test only ever fires a valid token) — this kit fires the exact attack tokens that
expose them, in seconds, against a live endpoint. One honest scope caveat: the kit
does not do real RS256/ES256 signature-math verification (stdlib-only), stated
plainly in the listing so no coverage is overclaimed.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/jwt-auth-test-kit.md` (the derive
script compiles it into `docs/publishing/OWNER-QUEUE.md`); the HOW detail lives in
`docs/launch/jwt-auth-test-kit/owner-actions.md`. Nothing here is performed by any
agent: no publish, no spend, no accounts — the build ENDS at the queued owner ⚑
publish click (rail 13 / CONSTITUTION §13).
