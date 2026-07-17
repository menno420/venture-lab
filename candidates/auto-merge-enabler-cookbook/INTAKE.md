# The Auto-Merge Enabler Cookbook — intake

> *Land your AI agents' PRs on green with no human clicking merge: the exact
> merge-on-green enabler workflow this repo runs in production, annotated,
> plus the required-check gate and born-red HOLD that make it safe.*

## What it is
A ($19) guide-shaped cookbook for people building AI-agent fleets that open
their own PRs and want them to land on green automatically. It teaches the
merge-on-green ENABLE mechanism specifically: a repo-owned workflow arms
GitHub-native auto-merge at PR open; GitHub squash-merges on green; the
agent never merges or arms (classifier-barred, correctly). Ships the exact
production `auto-merge-enabler.yml` and `substrate-gate.yml` (born-red HOLD)
verbatim, plus a minimal reading variant. Evidence class:
**verified-by-production** — the subject is this repo's own live infra, so
every claim cites `file@sha` + real merge events (the five 2026-07-17
`github-actions[bot]` squashes), not a synthetic HTTP test.

**Product or funnel? PRODUCT.** Standalone $19 cookbook for a narrow,
specific buyer (agent-fleet / autonomous-CI builders). No funnel
dependency.

**Distinct from the Agent Merge-Wall Cookbook ($19).** That product is the
walls a self-merging fleet hits and how to avoid conflict stalls (AVOID);
this is the enabler mechanism itself, deep (ENABLE). Sibling audience,
non-overlapping scope, natural cross-sell — the intake for a "CI/CD for
agent fleets" bundle pairing the two + the Field Manual is a live idea.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3 | High-intent, small TAM (people building self-merging agent fleets); same owner-gated community funnel as the Merge-Wall Cookbook / Field Manual — does not diversify channel risk. |
| Agent-buildability | 20% | 5 | Fully from committed repo (the live workflows + current-state doctrine + API-verifiable merge events). |
| Owner-click cost | 15% | 4 | One publish click. |
| Speed to first dollar | 15% | 4 | Guide + verbatim production YAML already in-repo; no new runtime to author. |
| WTP / moat | 15% | 3 | Narrow but real pain; those who have it have few alternatives — the strongest production-evidence mechanic in the catalog (the subject IS this repo's live infra). |
| **Weighted total** | | **3.75** | 0.35·D + 0.20·AB + 0.15·OC + 0.15·Sp + 0.15·WTP |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 30 days, ≥1 sale OR ≥30 reads from the
  agent-builder audience. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1)
  in-repo README badge — $0; (2) r/ClaudeAI · r/LocalLLaMA · agent-builder
  Discords ⚑ (self-promo risk, saturated); (3) Dev.to article ⚑; (4)
  Gumroad Discover ⚑. NOTE: same community funnel as
  merge-wall-cookbook / Field Manual — concentrated channel risk, not
  diversifying.
- **Max agent-effort budget (at intake):** ~90k tokens to v0.1. CI/polling
  overhead ≤12k — do NOT sleep-poll CI; PR events wake the session. Over
  budget without the signal = ledgered negative.
- **Conservative revenue estimate:** $19 one-time. Conservative first-90-day:
  0–3 sales ($0–$57). Zero distribution = $0.
- **Payback-time estimate:** unverified until first sale; owner-gated
  distribution.
- **Token-cost line:** build est. 70–90k. Actuals: not measured until built.

## Why this might fail
The buyer is extremely narrow — only people building agent fleets that
land their own PRs on green hit this exact need, and most are on the same
platforms reading the same free GitHub docs. GitHub also changes its
API/UI, so the mechanics can rot (required-check arming, the `GITHUB_TOKEN`
recursion guard). And it shares an audience with the Merge-Wall Cookbook —
the honest framing is a cross-sell pair, not two independent TAMs.
