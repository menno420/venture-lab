# GitHub Webhook Test Kit — intake (ideation batch 2026-07-13, BUILD #1)

> A stdlib-only local test harness + vendored real-shape GitHub event payloads
> that lets any developer verify their webhook handler's `X-Hub-Signature-256`
> handling, routing, and replay hygiene at the HTTP layer — before (and
> without) wiring a live GitHub App or webhook.

## What it is

The SWTK pattern (the lane's one LIVE product, $29 on Gumroad since
2026-07-12) applied to GitHub webhooks. Ships as: five vendored real-shape
payloads (byte-for-byte from GitHub's own `octokit/webhooks` example set,
with `fixtures/PROVENANCE.md` citing every scheme/header fact to the docs
sources), a language-agnostic HTTP-layer harness (Python + a Node port), a
correct example handler, a one-page `GOTCHAS.md`, an HTTP-layer real-path
test suite, and `package.sh` → `dist/github-webhook-test-kit-vX.Y.zip`.
Fully agent-buildable in-repo; reuses the committed SWTK template
(`candidates/stripe-webhook-test-kit/` — harness/fixtures/tests/package
structure) with fresh GitHub-specific checks: unsigned/sha1-downgrade
fail-closed, form-encoded raw-body signing, no-timestamp replay + GUID
dedupe, header-vs-payload event routing, and GitHub's own published HMAC
test vector as an offline known-answer check.

## Scoring (kill-rule intake rubric, fixed weights)

Scored at ideation — `docs/products/ideas-2026-07-13.md` §1 (PR #142,
squash `49fcf1e`), arithmetic shown there:

| Axis | W | Score |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **3.60 — BUILD (#1)** |

## Kill-rule fields (binding — provisional fields from the ideation entry, bound here at INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on the free gotcha article
  within **30 days of publish**, else ledgered negative.
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting
  packet once the publish click is DONE-flipped, per
  `docs/products/TEMPLATE.md` stage 8):** **T+7** funnel checkpoint (any
  organic traffic/reads at all?) · **T+30** kill-rule deadline (signal above,
  else ledger ⚑ NEGATIVE + pause/delist, SWTK-style).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode gotcha article on the exact "verify
  X-Hub-Signature-256" pain ⚑; (2) cross-link from the LIVE SWTK listing +
  its gotcha article (same buyer, sibling product) ⚑; (3) Gumroad Discover ⚑.
- **Max agent-effort budget (bound at ideation):** ≤70k tokens to a
  buildable v0.1 zip. Over budget without the validation signal = ledgered
  negative. Actual: one build session 2026-07-13 (this slice — the SWTK
  template did make N+1 measurably cheaper; ideation had estimated 80–120k
  for SWTK itself).
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — SWTK, the proven sibling,
  has 0 organic sales as of 2026-07-13; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified
  until first sale.

## Why this might fail

The verification snippet is ~10 lines once you know it, and GitHub's own
docs publish it free in six languages — the paid delta is the harness +
vendored fixtures + hostile modes, which a free blog post can substantially
substitute. `gh webhook forward` and smee.io cover the "test locally"
story for anyone willing to wire a real repo webhook. The buyer (devs
hand-rolling webhook handlers outside big frameworks) is narrow, the $29
price sits on catalog precedent rather than measured GitHub-specific
willingness-to-pay, and distribution is the same owner-gated channel where
SWTK has produced 0 organic sales so far.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/github-webhook-test-kit.md`
(the derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the
six-field HOW detail lives in
`docs/launch/github-webhook-test-kit/owner-actions.md`. Nothing here is
performed by any agent: no publish, no spend, no accounts.
