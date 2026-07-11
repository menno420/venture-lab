# The Kill-Rule Intake Kit — intake (candidate #9)

> *Stop building side projects nobody buys: the fillable intake + scoring rubric this revenue lane uses to kill weak ideas before writing code.*

## What it is
A ($15) fillable decision kit packaging the exact intake discipline this lane runs: a distribution-first weighted scoring rubric (the venture-eval-001 axes), a fillable INTAKE.md template with the kill-rule fields (validation signal + window, first-ten-customers path, max effort budget, conservative revenue, why-this-might-fail), and worked examples redacted from the lane's own real candidate intakes. Aimed at indie devs / solo builders who repeatedly build unsellable projects. Fully agent-writable from the repo's own intake artifacts — the lane is its own case study.

**Product or funnel? PRODUCT.** Standalone $15 template kit. Weakest WTP of the four; a decision framework, adjacent to general advice.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 2.5 | "How do I decide what to build" is broad but LOW purchase-intent — frameworks/templates convert poorly and compete with free content and paid courses; weakest surface of the four. |
| Agent-buildability | 20% | 5 | Fully from repo (the intake discipline is committed). |
| Owner-click cost | 15% | 4 | One publish click. |
| Speed to first dollar | 15% | 4 | Template + rubric + redacted examples; fast. |
| WTP / moat | 15% | 2 | Soft — decision templates are a crowded, free-heavy category. |
| **Weighted total** | | **3.38** | 0.35·D + 0.20·AB + 0.15·OC + 0.15·Sp + 0.15·WTP |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 30 days of publish, ≥1 sale OR ≥50 reads. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) in-repo README badge — $0; (2) Gumroad Discover ⚑; (3) Indie Hackers / r/SaaS · r/Entrepreneur post ⚑ (self-promo risk); (4) Dev.to article ⚑.
- **Max agent-effort budget (at intake):** 60k tokens to v0.1. CI/polling overhead budgeted at ≤10k — do NOT sleep-poll CI; PR events wake the session. Over budget without the signal = ledgered negative.
- **Conservative revenue estimate:** $15 one-time. Conservative first-90-day: 0–3 sales ($0–$45). Zero distribution = $0.
- **Payback-time estimate:** unverified until first sale; owner-gated.
- **Token-cost line:** intake ~this slice; build est. 45–60k. CI/polling ≤10k. Actuals: not measured until built.

## Why this might fail
This is the closest of the four to general advice, which the eval's own finding warns against (high-intent problem-solving beats advice). Decision frameworks have enormous free and paid competition, and buyer intent is low — people browse frameworks, they rarely pay for them. It also risks looking self-referential ("here is how we score ideas") without a track record of profitable outcomes to back it, since the lane has not yet earned a first dollar. Honest expectation: near-$0.

## Owner actions (six-field grammar) — NOT queued yet
No owner action queued at intake; publish click is earned only after v0.1 is built. Eventual shape:
- **WHAT:** publish the $15 fillable intake kit (template + rubric + redacted examples).
- **WHERE:** Gumroad/Lemon Squeezy under the owner's store, plus in-repo README badge.
- **HOW:** upload the fillable template + rubric, set price $15.
- **WHY:** standalone revenue packaging the lane's intake methodology.
- **UNBLOCKS:** indie-builder acquisition.
- **VERIFIED-WHEN:** live listing URL returns 200 and the fillable template renders/validates (schema check) in CI on the built head SHA.
