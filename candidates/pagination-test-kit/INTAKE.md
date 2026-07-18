# Pagination Test Kit — intake (ORDER 016 build, 2026-07-18)

> A stdlib-only local test harness + docs-derived request/response templates that
> lets any developer verify their paginated API is correct — cursor traversal with
> no skipped or duplicated items, **stable under mid-traversal mutation** (where
> naive OFFSET pagination fails), consistent ordering, a page-size limit that is
> honored and clamped, a terminal signal, and a forged cursor rejected — at the
> HTTP layer, in seconds, with no live API and no account.

## What it is

The webhook-/idempotency-/rate-limit-test-kit **packaging pattern** (stdlib
harness + docs-derived fixtures + a correct reference stub + a deliberately naive
stub + HTTP real-path suite + byte-reproducible bundle + §7 owner-gate packet,
proven across the LIVE Stripe kit, the GitHub/Slack/Shopify kits, the Idempotency
kit, and the Rate-Limit kit) applied to a **fourth, genuinely different problem
class**: **pagination / result-set integrity**, NOT signature verification, NOT
dedup/safe-retry, and NOT throttling. Where the webhook kits verify an *inbound*
provider signature, the idempotency kit verifies a buyer's *stateful safe-retry*
contract, and the rate-limit kit verifies a buyer's *throttling* contract, this
kit verifies a buyer's OWN paginated endpoint's *result-set integrity*: that
following the cursor reproduces the ordered set exactly once, **stays stable when
rows are inserted/deleted between page fetches**, orders consistently with a unique
tiebreaker, honors and clamps the page size, signals the terminal page, and
rejects a forged/opaque cursor. Ships as: a CORRECT reference pager (keyset on
`(created_at, id)` with an opaque HMAC-signed cursor, an `X-Page-Size-Max` clamp,
and `/_debug/*` mutation hooks), a deliberately NAIVE pager (OFFSET/LIMIT that
skips under mutation, no clamp, a forged cursor served as page 1) so the suite can
PROVE the harness catches the bugs, a language-agnostic harness (Python `pgtk.py`
+ Node `pgtk.js`) a buyer points at their own endpoint, two docs-derived templates
+ `PROVENANCE.md`, a 31-test HTTP real-path suite, and `package.sh` →
`dist/pagination-test-kit-vX.Y.zip`.

## Provenance of this build

Built under **ORDER 016** (live owner overnight/continued autonomous-build
authorization, reaffirmed by the live owner turn 2026-07-18) as a NEW sellable in
the API-robustness kit family (roadmap R2). It **reuses the kit scaffold's
structure** (file set, evidence bar, packaging, listing/vetting grammar — closest
templates are the Rate-Limit kit, PR #236, and the Idempotency kit, PR #233, which
have the same correct-stub + naive-stub evidence pattern) but is **not** an N+1 of
any existing line — it is a distinct product in a distinct problem class, so the
scoring below is an analog estimate inherited from the dev-tool kit line, not a
fresh ideation re-score.

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

- **Validation signal:** ≥1 sale OR ≥50 reads on a free "your offset pagination
  silently skips rows / your cursor is forgeable" gotcha article within **30 days
  of publish**, else ledgered negative (same bar as the sibling kits).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting packet
  once the publish click is DONE-flipped):** **T+7** funnel checkpoint · **T+30**
  kill-rule deadline (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode article on the exact "offset pagination skips rows
  under writes / keyset fixes it / your cursor is forgeable" pain ⚑; (2)
  cross-link from the sibling dev-tool listings — the Idempotency and Rate-Limit
  kits and the webhook kits (adjacent buyer: a developer hardening an API needs
  correct pagination alongside safe-retry and throttling) ⚑; (3) Gumroad Discover
  ⚑. Distinct angle vs the siblings: this is the *result-set integrity* rung of
  API robustness — the pair to safe-retry (idempotency) and throttling
  (rate-limit).
- **Max agent-effort budget:** ≤80k tokens to a buildable v0.1 zip.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — the proven sibling (Stripe kit)
  has 0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified until
  first sale.

## Why this might fail

Pagination is a well-documented pattern, many ORMs and API frameworks ship a
cursor pager, and correct keyset pagination is a few dozen lines once you know to
use a composite key. The paid delta is the same shape as the sibling kits' delta:
a runnable harness that tests a buyer's OWN endpoint against the properties + the
correct/naive reference pair that demonstrably catches a broken pager + the docs
discipline. A free blog post substitutes substantially, and the absence of a
single RFC (cursor pagination is a pattern, not a standard) means the model must be
stated honestly rather than cited to one authority. The $29 price sits on catalog
precedent (the sibling kits at $29), not measured pagination-specific
willingness-to-pay, and distribution is the same owner-gated channel where the
Stripe kit has produced 0 organic sales so far. One honest structural plus: the
offset-skip-under-mutation bug is **invisible in a green unit-test suite** (a
single static-fixture test never mutates the dataset mid-traversal) and invisible
in a static integration test — this kit reproduces the exact mutation that exposes
it, in seconds, against a live endpoint.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/pagination-test-kit.md` (the
derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the HOW detail
lives in `docs/launch/pagination-test-kit/owner-actions.md`. Nothing here is
performed by any agent: no publish, no spend, no accounts — the build ENDS at the
queued owner ⚑ publish click (rail 13 / CONSTITUTION §13).
