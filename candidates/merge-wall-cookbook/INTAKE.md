# The Agent Merge-Wall Cookbook — intake (candidate #8)

> *Ship code with AI agents without getting stuck: the exact GitHub-automation walls a self-merging agent fleet hits, and the runnable workarounds — REST merge-on-green, a GITHUB_TOKEN merge workflow, and why auto-merge will not arm.*

## What it is
A ($19) recipe cookbook for people building AI-agent fleets that open and land their own PRs. Documents the concrete GitHub-platform walls the lane hit and their workarounds: auto-merge cannot arm when the gate check is not a *required* check (no checks-pending window); REST merge-on-green as the primary self-merge path; a GITHUB_TOKEN merge-on-green workflow (shipped as runnable YAML); and how a self-approval / merge-without-review classifier denial behaves (first denial terminal, do not retry). Every recipe is drawn from the lane's committed PLATFORM-LIMITS.md and real PR history — no invented cases. Ships runnable artifacts, not just prose.

**Product or funnel? PRODUCT.** Standalone $19 cookbook for a narrow, specific buyer (agent-fleet / autonomous-CI builders). No funnel dependency.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3 | High-intent but small TAM (people building self-merging agent fleets); rides the same owner-gated r/ClaudeAI-type community funnel as the Field Manual — does not diversify channel risk. |
| Agent-buildability | 20% | 5 | Fully from committed repo (PLATFORM-LIMITS.md, PR #9, workflow precedent). |
| Owner-click cost | 15% | 4 | One publish click. |
| Speed to first dollar | 15% | 3 | Needs the runnable merge-on-green workflow authored and CI-verified — more than a prose guide. |
| WTP / moat | 15% | 3 | Narrow but real pain; those who have it have few alternatives, so moderate WTP + some moat. |
| **Weighted total** | | **3.55** | 0.35·D + 0.20·AB + 0.15·OC + 0.15·Sp + 0.15·WTP |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 30 days, ≥1 sale OR ≥30 reads from the agent-builder audience. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) in-repo README badge — $0; (2) r/ClaudeAI · r/LocalLLaMA · agent-builder Discords ⚑ (self-promo risk, saturated); (3) Dev.to article ⚑; (4) Gumroad Discover ⚑. NOTE: same community funnel as membership-kit / template-packs / Field Manual — concentrated channel risk, not diversifying.
- **Max agent-effort budget (at intake):** 90k tokens to v0.1 (runnable YAML + recipes). CI/polling overhead budgeted at ≤12k — do NOT sleep-poll CI; PR events wake the session. Over budget without the signal = ledgered negative.
- **Conservative revenue estimate:** $19 one-time. Conservative first-90-day: 0–3 sales ($0–$57). Zero distribution = $0.
- **Payback-time estimate:** unverified until first sale; owner-gated distribution.
- **Token-cost line:** intake ~this slice; build est. 70–90k. CI/polling ≤12k. Actuals: not measured until built.

## Why this might fail
The buyer is extremely narrow — only people building agent fleets that self-merge hit these exact walls, and most of them are on the same platforms the lane is, reading the same free docs. GitHub also changes its API/UI, so the workarounds can rot (the lane's own PLATFORM-LIMITS already carries a "re-verify the wall" note where the owner is changing branch protection). A cookbook of platform-specific workarounds has a short shelf life and a tiny market.

## Owner actions (six-field grammar) — NOT queued yet
No owner action queued at intake; publish click is earned only after v0.1 is built. Eventual shape:
- **WHAT:** publish the $19 cookbook with its packaged merge-on-green workflow YAML.
- **WHERE:** Gumroad/Lemon Squeezy under the owner's store, plus in-repo README badge.
- **HOW:** upload PDF/markdown + YAML, set price $19.
- **WHY:** standalone revenue on a narrow but real agent-automation pain.
- **UNBLOCKS:** agent-builder community acquisition.
- **VERIFIED-WHEN:** live listing URL returns 200 and the packaged merge-on-green workflow YAML passes a lint/dry-run check in CI on the built head SHA.
