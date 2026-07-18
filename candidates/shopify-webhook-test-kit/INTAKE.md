# Shopify Webhook Test Kit — intake (ORDER 016 overnight build, 2026-07-17)

> A stdlib-only local test harness + real-shape Shopify webhook fixtures that
> lets any developer verify their Shopify webhook signing
> (`X-Shopify-Hmac-Sha256` = base64 HMAC-SHA256 of the raw body), raw-body
> handling, malformed-input safety, and topic routing at the HTTP layer —
> before (and without) wiring a live Shopify store, app, or tunnel.

## What it is

The webhook-test-kit pattern (SWTK, the lane's one LIVE product at $29 on
Gumroad since 2026-07-12; plus the built GitHub and Slack Webhook Test Kits)
applied to **Shopify webhook signing**. Ships as: three real-shape webhook
fixtures (reconstructed from Shopify's official docs, with
`fixtures/PROVENANCE.md` citing every scheme/header/payload fact to the docs
page it came from and pinning each fixture's sha256), a language-agnostic
HTTP-layer harness (Python `shwtk.py` + a Node port `shwtk.js`), a correct
example handler (`stub_handler.py`), a one-page `GOTCHAS.md`, an HTTP-layer
real-path test suite, and `package.sh` → `dist/shopify-webhook-test-kit-vX.Y.zip`.
Fully agent-buildable in-repo; reuses the committed webhook-kit template
(harness / fixtures / tests / package structure) with fresh **Shopify-specific**
checks: base64 (not hex) digest verification, raw-body tamper (`--tamper`),
wrong-secret (`--forge`), missing-header fail-closed (`--unsigned`), and the
malformed-base64 safety check (`--malformed` — a non-base64 header must be a
clean 4xx, never a 5xx crash), plus topic routing over the real
`X-Shopify-Topic` header. Deliberately has **no** `--stale`/replay mode and
**no** challenge command, because Shopify's HMAC covers the raw body with no
timestamp and Shopify webhooks have no handshake — the honest structural
difference from the Slack kit.

## Provenance of this build

Built under **ORDER 016** (live owner overnight-work order, 2026-07-17,
authorizing autonomous sellable-building). It is the **N+1** of the proven
webhook-kit line — NOT a fresh ideation-batch entry, so the scoring below is
inherited-by-analogy from the GitHub/Slack Webhook Test Kit intakes
(`candidates/github-webhook-test-kit/INTAKE.md` /
`candidates/slack-webhook-test-kit/INTAKE.md`, ideation
`docs/products/ideas-2026-07-13.md` §1), which used the same kill-rule rubric
and the same weights. Treat the numbers as an analog estimate, not a re-scored
ideation ruling.

## Scoring (kill-rule intake rubric, inherited weights — analog estimate)

| Axis | W | Score (analog to SWTK/GWTK) |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **≈3.60 — BUILD (webhook-kit line, N+1)** |

## Kill-rule fields (provisional — bound at this INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on a free gotcha article within
  **30 days of publish**, else ledgered negative (same bar as SWTK/GWTK/Slack).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting
  packet once the publish click is DONE-flipped, per
  `docs/products/TEMPLATE.md` stage 8):** **T+7** funnel checkpoint (any
  organic traffic/reads at all?) · **T+30** kill-rule deadline (signal above,
  else ledger ⚑ NEGATIVE + pause/delist, SWTK-style).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode gotcha article on the exact "verify
  X-Shopify-Hmac-Sha256 / base64 not hex / hash the raw body" pain ⚑;
  (2) cross-link from the LIVE SWTK listing + the GWTK/Slack listings (adjacent
  buyer, sibling products) ⚑; (3) Gumroad Discover ⚑. Shopify-specific angle:
  the Shopify app-dev + custom-storefront community (r/shopify, Shopify
  community forums, the app-devs building outside `@shopify/shopify-api`).
- **Max agent-effort budget:** ≤70k tokens to a buildable v0.1 zip (the
  webhook-kit template makes each N+1 cheaper). Over budget without the
  validation signal = ledgered negative.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — SWTK, the proven sibling, has
  0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified
  until first sale.

## Why this might fail

The verification snippet is ~10 lines once you know it, and Shopify's own docs
publish it free in several languages — the paid delta is the harness + real-shape
fixtures + hostile modes (`--forge`, `--unsigned`, `--tamper`, `--malformed`) +
the topic-routing model, which a free blog post can substantially substitute.
Shopify's CLI (`app dev`) forwards real webhooks to localhost for anyone willing
to run it, and Shopify's official libraries (`@shopify/shopify-api`, the
`shopify_api` gem) verify the HMAC for you — so the addressable audience is
specifically hand-rolled / non-library integrators and custom stacks. The $29
price sits on catalog precedent (SWTK/GWTK/Slack), not measured
Shopify-specific willingness-to-pay, and distribution is the same owner-gated
channel where SWTK has produced 0 organic sales so far. One honest structural
plus vs the free blog post: the `--malformed` DoS check and the base64-not-hex
trap are exactly the two things a from-memory implementation gets wrong, and the
kit proves both against your own endpoint in seconds.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/shopify-webhook-test-kit.md`
(the derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the
HOW detail lives in `docs/launch/shopify-webhook-test-kit/owner-actions.md`.
Nothing here is performed by any agent: no publish, no spend, no accounts —
the build ENDS at the queued owner ⚑ publish click (rail 13 / CONSTITUTION
§13).
