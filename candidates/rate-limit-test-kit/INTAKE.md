# Rate-Limit Test Kit — intake (ORDER 016 build, 2026-07-18)

> A stdlib-only local test harness + docs-derived request templates that lets any
> developer verify their server-side API rate limiter behaves correctly — returns
> 429 at the limit (no off-by-one), emits a valid positive `Retry-After`, keeps
> its `RateLimit-*` headers consistent, and actually resets its window — at the
> HTTP layer, in seconds, with no live API and no account.

## What it is

The webhook-/idempotency-test-kit **packaging pattern** (stdlib harness +
docs-derived fixtures + a correct reference stub + a deliberately naive stub +
HTTP real-path suite + byte-reproducible bundle + §7 owner-gate packet, proven
across the LIVE Stripe kit, the GitHub/Slack/Shopify kits, and the Idempotency
kit) applied to a **third, genuinely different problem class**: **rate-limiting /
throttling correctness**, NOT signature verification and NOT dedup/safe-retry.
Where the webhook kits verify an *inbound* provider signature and the idempotency
kit verifies a buyer's *stateful safe-retry* contract, this kit verifies a
buyer's OWN endpoint's *throttling* contract: 2xx under the limit, **429 + a
valid `Retry-After`** at it, consistent `RateLimit-*` headers, and a window that
resets when advertised. Ships as: a CORRECT reference limiter (thread-safe
fixed-window counter, short configurable window, 429 + `Retry-After` +
`RateLimit-*`/`X-RateLimit-*`), a deliberately NAIVE limiter (off-by-one, a 429
with no `Retry-After`, stuck/stale headers) so the suite can PROVE the harness
catches the bugs, a language-agnostic harness (Python `rltk.py` + Node `rltk.js`)
a buyer points at their own endpoint, two docs-derived request templates +
`PROVENANCE.md`, a 27-test HTTP real-path suite, and `package.sh` →
`dist/rate-limit-test-kit-vX.Y.zip`.

## Provenance of this build

Built under **ORDER 016** (live owner overnight/continued autonomous-build
authorization, reaffirmed by the live owner turn 2026-07-18) as a NEW sellable in
the API-robustness kit family. It **reuses the kit scaffold's structure** (file
set, evidence bar, packaging, listing/vetting grammar — closest template is the
Idempotency kit, PR #233, which has the same correct-stub + naive-stub evidence
pattern) but is **not** an N+1 of any existing line — it is a distinct product in
a distinct problem class, so the scoring below is an analog estimate inherited
from the dev-tool kit line, not a fresh ideation re-score.

## Scoring (kill-rule intake rubric, inherited weights — analog estimate)

| Axis | W | Score (analog to the sibling kits) |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **≈3.60 — BUILD (dev-tool kit line, new problem class)** |

## Kill-rule fields (provisional — bound at this INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on a free "your rate limiter is
  off by one / your 429 has no Retry-After" gotcha article within **30 days of
  publish**, else ledgered negative (same bar as the sibling kits).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting packet
  once the publish click is DONE-flipped):** **T+7** funnel checkpoint · **T+30**
  kill-rule deadline (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode article on the exact "429 done right / your limiter is
  lying about Retry-After" pain ⚑; (2) cross-link from the sibling dev-tool
  listings — the Idempotency kit and the webhook kits (adjacent buyer: a
  developer hardening an API against retries and abuse needs both safe-retry AND
  correct throttling) ⚑; (3) Gumroad Discover ⚑. Distinct angle vs the siblings:
  this is the *server-emitting-429* half of API robustness — the pair to the
  client-honouring-429 concern and the idempotency concern.
- **Max agent-effort budget:** ≤80k tokens to a buildable v0.1 zip.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — the proven sibling (Stripe kit)
  has 0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified until
  first sale.

## Why this might fail

Rate limiting is a well-documented pattern, most API gateways and frameworks ship
a limiter, and the correct 429/`Retry-After` behaviour is a few dozen lines once
you know the contract. The paid delta is the same shape as the sibling kits' delta:
a runnable harness that tests a buyer's OWN endpoint against the properties + the
correct/naive reference pair that demonstrably catches a broken limiter + the docs
discipline. A free blog post substitutes substantially, and the `RateLimit-*`
header spec being a moving IETF draft (not an RFC) means the headers half is a
softer target than the stable 429/`Retry-After` half. The $29 price sits on
catalog precedent (the sibling kits at $29), not measured rate-limit-specific
willingness-to-pay, and distribution is the same owner-gated channel where the
Stripe kit has produced 0 organic sales so far. One honest structural plus: the
off-by-one and the lying-`Retry-After` bugs are invisible in a green unit-test
suite (a single-request test never crosses the boundary or waits out a window),
and this kit proves the boundary and the reset against a live endpoint in seconds.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/rate-limit-test-kit.md` (the
derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the HOW detail
lives in `docs/launch/rate-limit-test-kit/owner-actions.md`. Nothing here is
performed by any agent: no publish, no spend, no accounts — the build ENDS at the
queued owner ⚑ publish click (rail 13 / CONSTITUTION §13).
