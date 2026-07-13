# Worked example 1 — "Platform-Walls Cookbook" (borderline build, 3.55)

> Adapted (redacted and genericized) from a real intake in the lane that
> produced this kit. The scores, the arithmetic, and the unflattering
> self-assessment are as-filed; names and identifying details are changed.
> Read it for the SHAPE: honest low scores and a named shelf-life risk
> surviving on the same page as a "build" verdict.

---

# Platform-Walls Cookbook — intake (candidate #8)

> *Ship with automation without getting stuck: the exact platform-API
> walls an automated release pipeline hits, and the runnable workarounds.*

## What it is

A $19 recipe cookbook for people building automated release pipelines that
open and land their own changes. Documents the concrete platform walls the
author's own pipeline hit and their tested workarounds, shipped as
runnable config plus prose — every recipe drawn from committed history and
real incidents, no invented cases. v0.1 scope: the six walls actually hit,
one runnable artifact each. Out of scope: speculative walls, other
platforms.

**Product or funnel?** PRODUCT. Standalone cookbook for a narrow, specific
buyer. No funnel dependency.

## Scoring (weighted 0–5)

| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3 | High-intent but small audience; rides the same gated community channels as my two previous products — does not diversify channel risk. |
| Buildability | 20% | 5 | Fully writable from committed history and configs I already have. |
| Launch-effort cost | 15% | 4 | One publish click on an existing storefront. |
| Speed to first dollar | 15% | 3 | The runnable config needs authoring and verification — more than a prose guide. |
| WTP / moat | 15% | 3 | Narrow but real pain; those who have it have few alternatives. |
| **Weighted total** | | **3.55** | 0.35·3 + 0.20·5 + 0.15·4 + 0.15·3 + 0.15·3 = 1.05+1.00+0.60+0.45+0.45 |

## Kill-rule fields (binding)

- **Validation signal:** within 30 days of publish, ≥1 sale OR ≥30 reads
  from the target audience. Else ledgered negative.
- **First-ten-customers path:** (1) README badge on my public repos — $0,
  self-serve; (2) two niche community posts (gated — self-promo rules,
  saturated); (3) one long-form article on a dev-blogging platform
  (gated); (4) storefront's own discovery feed (gated). NOTE: same
  community funnel as my last two products — concentrated channel risk,
  not diversifying.
- **Max effort budget (at intake):** 3 focused build days to v0.1. Over
  budget without the signal = ledgered negative.
- **Conservative revenue estimate:** $19 one-time. Conservative
  first-90-day: 0–3 sales ($0–$57). Zero distribution = $0.
- **Payback-time estimate:** unverified until first sale; distribution is
  gated, so honestly unknowable at intake.

## Why this might fail

The buyer is extremely narrow — only people running self-landing automated
pipelines hit these exact walls, and most of them read the same free docs
I did. The platform also changes its API and UI, so the workarounds can
rot; a cookbook of platform-specific workarounds has a short shelf life
and a tiny market. My distribution path is the same saturated community
funnel that produced near-zero sales for the previous two products, and
nothing in this plan fixes that.

## Launch actions — NOT queued yet

No launch action queued at intake; the publish click is earned only after
v0.1 is built within budget.

---

## Why this one earned a build (kit commentary)

Not because 3.55 is "good" — because it was the best available candidate
that week, its budget was tight (3 days), its kill conditions were
concrete, and its "Why this might fail" would survive a hostile reader.
Note what the intake does NOT do: it does not round distribution up to 4
because the pain is real, and it does not hide that the channel is the
same one that already failed twice. That is the bar.
