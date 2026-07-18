# Idempotency Key Test Kit — intake (ORDER 016 build, 2026-07-18)

> A stdlib-only local test harness + docs-derived request fixtures that lets any
> developer verify their API's `Idempotency-Key` handling — safe-retry /
> exactly-once, same-key-different-body rejection, per-key scoping, concurrency
> in-flight locking, and a documented missing-key policy — at the HTTP layer,
> before (and without) wiring a live payment API or account.

## What it is

The webhook-test-kit **packaging pattern** (stdlib harness + real-shape fixtures
+ correct example handler + HTTP real-path suite + byte-reproducible bundle +
§7 owner-gate packet, proven across the LIVE Stripe kit and the built
GitHub/Slack/Shopify kits) applied to a **genuinely different problem class**:
**idempotency / safe-retry dedup**, NOT signature verification. Where the four
webhook kits verify an *inbound* provider signature (one request → accept/reject
on an HMAC), this kit verifies a buyer's OWN endpoint's *stateful* behaviour
across multiple requests: that a retried `POST /charges` triggers the side effect
exactly once. Ships as: a CORRECT reference stub (in-memory store keyed on
`(method, path, Idempotency-Key)` with a request-fingerprint + stored response +
per-key in-flight lock), a deliberately NAIVE (no-dedup) stub so the suite can
PROVE the harness catches the double-charge bug, a language-agnostic harness
(Python `ikt.py` + Node `ikt.js`) a buyer points at their own endpoint, three
docs-derived fixtures + `PROVENANCE.md`, a 20-test HTTP real-path suite with a
side-effect counter, and `package.sh` → `dist/idempotency-key-test-kit-vX.Y.zip`.

## Provenance of this build

Built under **ORDER 016** (live owner overnight/continued autonomous-build
authorization, reaffirmed by the live owner turn 2026-07-18) as a NEW, non-webhook
sellable. It **reuses the webhook-kit scaffold's structure** (file set, evidence
bar, packaging, listing/vetting grammar) but is **not** an N+1 of the webhook
line — it is a distinct product in a distinct problem class, so the scoring below
is an analog estimate inherited from the dev-tool kit line, not a fresh ideation
re-score.

## Scoring (kill-rule intake rubric, inherited weights — analog estimate)

| Axis | W | Score (analog to the webhook kits) |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **≈3.60 — BUILD (dev-tool kit line, new problem class)** |

## Kill-rule fields (provisional — bound at this INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on a free "double-charge on retry"
  gotcha article within **30 days of publish**, else ledgered negative (same bar
  as the webhook kits).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting packet
  once the publish click is DONE-flipped):** **T+7** funnel checkpoint · **T+30**
  kill-rule deadline (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode article on the exact "your retry double-charged the
  customer / idempotency keys done right" pain ⚑; (2) cross-link from the LIVE
  Stripe Webhook Test Kit listing + the sibling dev-tool listings (adjacent
  buyer — a developer wiring Stripe Checkout also needs safe retries) ⚑;
  (3) Gumroad Discover ⚑. Distinct angle vs the webhook kits: this is the
  *outbound* half of a payments integration (making your own writes safe), the
  natural companion to the *inbound* webhook-verification kits.
- **Max agent-effort budget:** ≤80k tokens to a buildable v0.1 zip.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — the proven sibling (Stripe kit)
  has 0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified until
  first sale.

## Why this might fail

Idempotency is a well-documented pattern and the correct implementation is a
few dozen lines once you know the contract — Stripe's docs describe it for free,
and mature frameworks/libraries increasingly ship idempotency middleware. The
paid delta is the same shape as the webhook kits' delta: a runnable harness that
tests a buyer's OWN endpoint against the five properties + the correct/naive
reference pair that demonstrably catches a broken implementation + the docs
discipline. A free blog post substitutes substantially. The $29 price sits on
catalog precedent (the webhook kits at $29), not measured idempotency-specific
willingness-to-pay, and distribution is the same owner-gated channel where the
Stripe kit has produced 0 organic sales so far. One honest structural plus: the
double-charge-on-retry bug is expensive and invisible in a green unit-test suite
(the unit test never fires two concurrent same-key requests), and this kit proves
the property against a live endpoint in seconds — including the concurrency case
a from-memory test almost never covers.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/idempotency-key-test-kit.md`
(the derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the HOW
detail lives in `docs/launch/idempotency-key-test-kit/owner-actions.md`. Nothing
here is performed by any agent: no publish, no spend, no accounts — the build
ENDS at the queued owner ⚑ publish click (rail 13 / CONSTITUTION §13).
