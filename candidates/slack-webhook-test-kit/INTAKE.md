# Slack Webhook Test Kit — intake (ORDER 016 overnight build, 2026-07-17)

> A stdlib-only local test harness + real-shape Slack request fixtures that
> lets any developer verify their Slack request-signing (`X-Slack-Signature`
> `v0=` HMAC), timestamp-replay window, and challenge handshake at the HTTP
> layer — before (and without) wiring a live Slack app or workspace.

## What it is

The webhook-test-kit pattern (SWTK, the lane's one LIVE product at $29 on
Gumroad since 2026-07-12; and the built GitHub Webhook Test Kit) applied to
**Slack request signing**. Ships as: four real-shape request fixtures
(reconstructed from Slack's official docs, with `fixtures/PROVENANCE.md`
citing every scheme/header/payload fact to the docs page it came from and
pinning each fixture's sha256), a language-agnostic HTTP-layer harness
(Python `swtk.py` + a Node port `swtk.js`), a correct example handler
(`stub_handler.py`), a one-page `GOTCHAS.md`, an HTTP-layer real-path test
suite, and `package.sh` → `dist/slack-webhook-test-kit-vX.Y.zip`. Fully
agent-buildable in-repo; reuses the committed SWTK/GWTK template
(harness / fixtures / tests / package structure) with fresh **Slack-specific**
checks: the timestamp-replay window (`--stale` — a VALID signature on an
out-of-window timestamp, rejected), raw-body tamper (`--tamper`), the
form-body signing surfaces (slash command flat fields + interactivity
`payload=<json>`), the `url_verification` challenge-echo handshake, and
Slack's own published worked example as an offline known-answer check.

## Provenance of this build

Built under **ORDER 016** (live owner overnight-work order, 2026-07-17T22:39Z,
recorded in the inbox) authorizing autonomous sellable-building. It is the
**N+1** of the proven webhook-kit line — NOT a fresh ideation-batch entry, so
the scoring below is inherited-by-analogy from the GitHub Webhook Test Kit
intake (`candidates/github-webhook-test-kit/INTAKE.md`, ideation
`docs/products/ideas-2026-07-13.md` §1), which used the same kill-rule rubric
and the same weights. Treat the numbers as an analog estimate, not a
re-scored ideation ruling.

## Scoring (kill-rule intake rubric, inherited weights — analog estimate)

| Axis | W | Score (analog to GWTK) |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **≈3.60 — BUILD (webhook-kit line, N+1)** |

## Kill-rule fields (provisional — bound at this INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on a free gotcha article within
  **30 days of publish**, else ledgered negative (same bar as SWTK/GWTK).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting
  packet once the publish click is DONE-flipped, per
  `docs/products/TEMPLATE.md` stage 8):** **T+7** funnel checkpoint (any
  organic traffic/reads at all?) · **T+30** kill-rule deadline (signal above,
  else ledger ⚑ NEGATIVE + pause/delist, SWTK-style).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode gotcha article on the exact "verify
  X-Slack-Signature / the timestamp is on you" pain ⚑; (2) cross-link from the
  LIVE SWTK listing + the GWTK listing (same buyer, sibling products) ⚑;
  (3) Gumroad Discover ⚑.
- **Max agent-effort budget:** ≤70k tokens to a buildable v0.1 zip (SWTK
  template makes each N+1 cheaper). Over budget without the validation signal
  = ledgered negative.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — SWTK, the proven sibling, has
  0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified
  until first sale.

## Why this might fail

The verification snippet is ~15 lines once you know it, and Slack's own docs
publish it free in several languages with a full worked example — the paid
delta is the harness + real-shape fixtures + hostile modes (`--stale`,
`--tamper`, `--forge`, `--unsigned`) + the challenge-echo check, which a free
blog post can substantially substitute. Slack's request-URL tester and Socket
Mode cover the "test locally" story for anyone willing to wire a real app. The
buyer (devs hand-rolling Slack request handlers outside Bolt) is narrow —
Slack's official **Bolt** SDK verifies signatures for you, so the addressable
audience is specifically non-Bolt / custom-stack integrators. The $29 price
sits on catalog precedent (SWTK/GWTK), not measured Slack-specific
willingness-to-pay, and distribution is the same owner-gated channel where
SWTK has produced 0 organic sales so far.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/slack-webhook-test-kit.md`
(the derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the
HOW detail lives in `docs/launch/slack-webhook-test-kit/owner-actions.md`.
Nothing here is performed by any agent: no publish, no spend, no accounts —
the build ENDS at the queued owner ⚑ publish click (rail 13 / CONSTITUTION
§13).
