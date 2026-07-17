# Session — Auto-Merge Enabler Cookbook $19 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Fri Jul 17 23:09:05 UTC 2026
- **branch:** `claude/auto-merge-enabler-cookbook-2026-07-17` (PR TBD)
- **base:** `main@f0511ae`
- **purpose:** build **The Auto-Merge Enabler Cookbook ($19)** to owner-click-ready
  and land it as ONE PR — a guide-shaped sellable teaching how to run merge-on-green
  auto-merge for agent-opened PRs, distilled from the workflow THIS fleet runs in
  production (`.github/workflows/auto-merge-enabler.yml`). Ships the annotated
  enabler workflow line-by-line, the required-checks gating model, the born-red HOLD
  pattern (`substrate-gate.yml`), the `do-not-automerge` opt-out, the
  seats-can't-self-arm classifier caveat, a troubleshooting chapter (MCP-opened PRs
  fire no workflows at open → push once; GraphQL-quota walls), and a copy-paste
  recipe set (the real enabler yml + a minimal variant). Evidence class =
  **verified-by-production**: the subject IS this repo's own live infra, so the
  guide cites `file@sha` + REAL squash-merge event IDs (tonight's #219→389ab6e,
  #220→4e0a37c, #221→12498f4, #222→37cf9fd, #223→f0511ae, all github-actions[bot]
  auto-merge on green), not an HTTP test. Build ENDS at a queued owner ⚑ publish
  click (rail 13 / CONSTITUTION §13) — no publish, no spend, no accounts.
- **distinct-from:** the already-built `candidates/merge-wall-cookbook/` ($19) is
  conflict AVOIDANCE (the walls a self-merging fleet hits + fallbacks); THIS is the
  merge-on-green ENABLE mechanism specifically — the enabler workflow that arms
  GitHub-native auto-merge so a born-red session PR lands itself the moment
  substrate-gate goes green. Sibling audience, non-overlapping deep-dive.
- **session:** Mirrors the proven guide-shaped scaffold exactly
  (merge-wall-cookbook / false-green-test-trap file set, evidence bar, packaging,
  listing/vetting shape). Born-red card holds substrate-gate red until the
  deliberate completion flip.

## 💡 Session idea

💡 [[fill:idea]]

## previous-session review

previous-session review: [[fill:prev-review]]
