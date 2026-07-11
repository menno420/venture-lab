# Stripe Webhook Test Kit — intake (candidate #3)

> A standalone, framework-agnostic harness + vendored REAL Stripe sample payloads that lets any indie dev verify their `checkout.session.completed` handler at the HTTP layer BEFORE they ship and silently lose orders.

## What it is
A digital dev-tool kit packaging the exact real-Stripe-path knowledge this lane already earned the hard way (see the D1 lesson): `checkout.session.completed` events carry `customer_email: null` — the buyer address lives in `customer_details.email`; the success URL supports only `{CHECKOUT_SESSION_ID}` (never `{CHECKOUT_EMAIL}`); signatures must be HMAC-verified natively; and test payloads must be VENDORED from real Stripe samples, never synthesized from memory. Ships as: vendored real sample payloads (JSON), a language-agnostic HTTP-layer test harness (Python + a JS port), a one-page "gotchas checklist", and a `package.sh` → `dist/stripe-webhook-test-kit-vX.Y.zip`. Fully agent-buildable in-repo; reuses zero code from candidates/membership-kit/server (fresh vendored fixtures with their own PROVENANCE).

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 4 | Genuine HIGH-INTENT search pain ("stripe customer_email null", "checkout.session.completed email missing", "stripe webhook signature verify test"). A free technical gotcha article/gist is authentically SEO-discoverable (specific Q&A, not generic AI content). Paid kit still marketplace-gated → not 5. |
| Agent-buildability | 20% | 5 | Pure code + JSON + docs; agents build fully in-repo, zero owner involvement. |
| Owner-click cost | 15% | 4 | One-time marketplace listing click (same as existing); free-article posting is owner-gated but optional. |
| Speed to first dollar | 15% | 3 | Needs owner publish click + a little content seeding before intent traffic converts. |
| WTP / moat | 15% | 4 | Devs pay to avoid a real money-losing bug; the vendored-real-payload discipline is a genuine differentiator vs free snippets. |
| **Weighted total** | | **4.05** | 0.35·4 + 0.20·5 + 0.15·4 + 0.15·3 + 0.15·4 |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 14 days / 3 owner-click steps of a free "Stripe checkout email null" gotcha article going live — ≥1 of: (a) article draws ≥50 organic visits, (b) ≥3 saves/stars on a free gist or repo mirror, (c) first paid sale. No signal by the budget cap = ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) free technical article on the exact `customer_email: null` gotcha on dev.to/Hashnode ⚑; (2) free public gist/GitHub repo mirror of the checklist ⚑ (account plausibly owned); (3) answer the canonical StackOverflow question with the fix + soft link ⚑; (4) Gumroad/Lemon Squeezy listing for the paid kit ⚑; (5) r/stripe, r/SaaS posts ⚑. High-intent, search-driven — a genuinely different surface than the existing candidates' community funnel.
- **Max agent-effort budget (at intake):** 120k tokens to a buildable v0.1 zip. Over budget without the validation signal = ledgered negative.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day: 0–5 sales ($0–$145). Zero distribution = $0.
- **Payback-time estimate:** owner-gated on the publish click; unverified until first sale. At ~100k build tokens, one $29 sale clears return-on-labor only after the free-article seeding lands traffic.
- **Token-cost line:** intake ~this slice (measured post-hoc, see addendum); build est. 80–120k (harness + vendored payloads + docs + zip). Actuals: not measured until built.

## Why this might fail
The fix is a ~5-line snippet once you know it, so a free blog post — even the kit's own free gotcha article — can fully substitute for the paid kit and cap willingness-to-pay near zero. Stripe's own docs and CLI-generated test fixtures are free and official. The addressable buyer is narrow (indie devs hand-rolling raw webhook handlers), and it shrinks as frameworks and Stripe's own libraries bundle this verification. Distribution still depends on owner-gated posting, so with zero seeding the realistic revenue is ~$0.

## Owner actions (six-field grammar) — NOT queued yet
No owner action is queued at intake. Per the D1 lesson and playbook R23, a sell/publish click ships ONLY after v0.1 is built and its real-path HTTP test is green against VENDORED real payloads. The eventual publish click, once earned, will take this shape:
- **WHAT:** publish stripe-webhook-test-kit at $29 on a marketplace.
- **WHERE:** Gumroad/Lemon Squeezy Discover.
- **HOW:** upload `candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-vX.Y.zip`, set price $29, paste LISTING.md copy.
- **WHY:** first-dollar path for the highest-WTP new candidate.
- **UNBLOCKS:** organic search funnel + first revenue.
- **VERIFIED-WHEN:** live listing URL returns 200 and the real-path HTTP test is green in CI on the built head SHA.
