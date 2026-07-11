# The False-Green Test Trap — intake (candidate #7)

> *Why your webhook tests pass and production still drops the order — and the one-page discipline that catches it: test against vendored real payloads, never payloads you wrote from memory.*

## What it is
A focused (~15-page) recipe guide plus copy-paste checklist teaching one hard-won discipline: integration tests that assert against payloads synthesized from memory go green while real provider events (Stripe, GitHub, and others) carry different field shapes — so production breaks with a passing suite. It generalizes the lane's D1 lesson (13 green tests that injected memory-authored events, while real `checkout.session.completed` carries `customer_email: null`) into a provider-agnostic method: vendor a real sample payload, assert at the HTTP layer, diff memory-shape vs real-shape. Ships with a runnable "vendor-a-fixture" script pattern and a pre-merge checklist. Fully writable from committed repo history; no invented cases.

**Product or funnel? PRODUCT (with a soft funnel edge).** It stands alone as a $15 methodology guide for a broad audience (anyone writing webhook/integration tests), and secondarily cross-links the $29 stripe-webhook-test-kit as the Stripe-specific done-for-you tool.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3.5 | "Why do my passing tests lie / webhook works in test but not prod" is broad, high-intent dev search — wider TAM than SWTK — but competes with abundant free blog content, capping the surface. |
| Agent-buildability | 20% | 5 | Fully from committed repo history (D1 lesson, real-path test files). |
| Owner-click cost | 15% | 4 | One publish click. |
| Speed to first dollar | 15% | 4 | Short guide plus one runnable snippet; fast, but the fixture-vendoring pattern needs CI-testing. |
| WTP / moat | 15% | 2 | Real pain, but methodology/advice competes with free substitutes; softer WTP than a tool. |
| **Weighted total** | | **3.73** | 0.35·D + 0.20·AB + 0.15·OC + 0.15·Sp + 0.15·WTP |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 30 days of publish, ≥1 sale OR ≥40 reads with ≥1 SWTK click-through. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) in-repo README badge — $0, agent-doable; (2) Dev.to/Hashnode article on the false-green pattern ⚑; (3) Gumroad/Lemon Squeezy Discover ⚑; (4) r/webdev · r/programming · r/ExperiencedDevs high-intent replies ⚑ (self-promo removal risk); (5) HN comment on any "tests passed, prod broke" thread ⚑.
- **Max agent-effort budget (at intake):** 70k tokens to v0.1. CI/polling overhead budgeted at ≤10k — do NOT sleep-poll CI; PR events wake the session. Over budget without the signal = ledgered negative.
- **Conservative revenue estimate:** $15 one-time. Conservative first-90-day: 0–4 sales ($0–$60). Zero distribution = $0.
- **Payback-time estimate:** unverified until first sale; owner-gated distribution.
- **Token-cost line:** intake ~this slice; build est. 50–70k. CI/polling ≤10k. Actuals: not measured until built.

## Why this might fail
"Write better tests" is advice, and advice has near-infinite free substitutes (blogs, docs, threads) — the guide's only edge is a concrete runnable pattern and the credibility of a specific war story, which may not out-rank free content. The broad audience is also low-intent: people who hit this bug fix it and move on rather than buying a guide. If it cannot rank organically, revenue is $0.

## Owner actions (six-field grammar) — NOT queued yet
No owner action queued at intake; publish click is earned only after v0.1 is built. Eventual shape:
- **WHAT:** publish the $15 guide with its runnable fixture-vendoring snippet.
- **WHERE:** Gumroad/Lemon Squeezy under the owner's store, plus in-repo README badge.
- **HOW:** upload PDF/markdown + snippet, set price $15.
- **WHY:** standalone revenue on a broad high-intent testing pain, soft funnel to SWTK.
- **UNBLOCKS:** organic-search acquisition; SWTK cross-sell.
- **VERIFIED-WHEN:** live listing URL returns 200 and the guide's runnable fixture-vendoring snippet passes in CI on the built head SHA.
