# Stripe Webhook Gotchas — the real-payload field guide — intake (candidate #6)

> *The five Stripe webhook gotchas that pass every test and still lose you the sale — free, and it hands you the $29 kit that fixes them for you.*

## What it is
A short (~10-page) PWYW guide documenting the exact, real-payload Stripe checkout gotchas the lane hit and solved: `checkout.session.completed` carries `customer_email: null` (the buyer address lives in `customer_details.email`); the success-URL `{CHECKOUT_EMAIL}` placeholder is invalid (Stripe supports `{CHECKOUT_SESSION_ID}` only); and why tests built from memory go green while production silently drops the fulfillment email. Every claim is drawn from the lane's own D1 lesson and the stripe-webhook-test-kit build — no invented case studies. Fully agent-writable from committed repo history. It is the top-of-funnel FREE/PWYW guide whose "done-for-you" CTA is the $29 stripe-webhook-test-kit.

**Product or funnel? FUNNEL.** Direct revenue is ~$0 by design (PWYW); its job is to rank on the exact high-intent dev search the eval already named the lane's most defensible surface and convert readers into $29 kit buyers. It is not a standalone revenue product and is not scored as one.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3.5 | Rides the same high-intent dev search as SWTK (the eval's #1 surface); free/PWYW removes purchase friction — but as a funnel its own first-ten-*paying*-customers path is indirect (feeds SWTK, does not close paying buyers itself). Below SWTK's 4 for that indirection. |
| Agent-buildability | 20% | 5 | Fully writable from committed repo history (D1 lesson, GOTCHAS.md, test-kit fixtures). Zero owner involvement to build. |
| Owner-click cost | 15% | 4 | One publish click (Gumroad PWYW or in-repo README link); funnel only pays off once SWTK is also live. |
| Speed to first dollar | 15% | 5 | Shortest build of any candidate — prose + code snippets from existing repo artifacts. |
| WTP / moat | 15% | 1 | PWYW/free by design; near-zero direct willingness-to-pay. Moat is gotcha specificity, monetized downstream via SWTK. |
| **Weighted total** | | **3.73** | 0.35·D + 0.20·AB + 0.15·OC + 0.15·Sp + 0.15·WTP (funnel score not comparable to standalone-product scores). |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 21 days of the guide AND SWTK both being live, ≥1 of: (a) a click-through from the guide's CTA to the SWTK listing, or (b) ≥25 guide reads. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) in-repo README badge linking the guide — $0, agent-doable once URL exists; (2) Gumroad/Lemon Squeezy Discover as a $0 PWYW listing ⚑; (3) Dev.to / Hashnode article seeding the guide ⚑; (4) r/stripe · r/webdev high-intent thread reply ⚑ (self-promo removal risk). The guide's "customers" are SWTK buyers — its conversion, not direct sales, is the metric.
- **Max agent-effort budget (at intake):** 45k tokens to v0.1 (short guide; content already exists in-repo). CI/polling overhead budgeted at ≤8k of that — do NOT sleep-poll CI; PR events wake the session (the test-kit build overran ~2.3×, partly on polling). Over budget without the signal = ledgered negative.
- **Conservative revenue estimate:** $0 direct (PWYW; expect ~$0 tips). Value = incremental SWTK conversions; conservative first-90-day incremental: 0–2 extra $29 sales ($0–$58). Zero distribution = $0.
- **Payback-time estimate:** owner-gated / unverified until SWTK's first sale; funnel payback cannot precede the paid product's payback.
- **Token-cost line:** intake ~this slice; build est. 30–45k. CI/polling ≤8k budgeted. Actuals: not measured until built.

## Why this might fail
A free guide with no paying product behind it is worthless, so it is strictly gated on SWTK shipping first — if SWTK slips, this has no destination. PWYW guides attract readers, not buyers; the conversion assumption (reads → $29 kit) is unmeasured and could be ~0%. And Stripe's own docs already document these fields for free, so the guide's edge is packaging and search-timing, not secret knowledge — thin if it does not rank.

## Owner actions (six-field grammar) — NOT queued yet
No owner action queued at intake; publish click is earned only after v0.1 is built AND SWTK is live. Eventual shape:
- **WHAT:** publish the PWYW guide (free, tip-optional) linking the SWTK listing.
- **WHERE:** Gumroad/Lemon Squeezy under the owner's store, plus in-repo README badge.
- **HOW:** upload PDF/markdown, set PWYW $0+, paste the SWTK product URL as the CTA.
- **WHY:** top-of-funnel for the lane's highest-scoring paid product.
- **UNBLOCKS:** organic-search acquisition into SWTK.
- **VERIFIED-WHEN:** live guide URL returns 200, the CTA resolves to a live SWTK listing, and the SWTK real-path HTTP test is green in CI on the built head SHA.
