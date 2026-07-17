# Session — Auto-Merge Enabler Cookbook $19 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
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

💡 The two agent-CI cookbooks now bracket the whole landing problem — the
Merge-Wall Cookbook ($19) is conflict AVOIDANCE + fallbacks, this one ($19)
is the merge-on-green ENABLE mechanism — and the Field Manual ($39) is the
fleet-operations layer above both. Package them as a **"CI/CD for Agent
Fleets" bundle** (~$59 vs $77 buying all three): one storefront page, three
zips, the exact cross-sell the intakes already name as their shared channel.
The honest framing the collision scans keep surfacing (same narrow
agent-builder audience, concentrated funnel) is not a weakness to hide but a
bundle to sell — a buyer setting up a self-merging fleet wants all three, and
a single higher-AOV listing beats three $19 pages competing for the same
click. Bundle-listing precedent already exists (`candidates/BUNDLE-LISTING.md`,
the Ship-It bundle) — this is a second bundle on a tighter, more coherent
theme.

## previous-session review

previous-session review: `.sessions/2026-07-17-slack-webhook-test-kit.md`
(PR #223, slice-1 of ORDER 016) — a clean N+1 build of the proven webhook-kit
scaffold (stdlib-only Slack HMAC verifier, real-path HTTP tests, byte-repro
bundle, §7 packet) and the ideal proof-of-model for THIS card: its own PR was
the fifth of tonight's five `github-actions[bot]` auto-merges (#223 → `f0511ae`,
opened READY and landed 48s later), so the sellable I built is the exact
mechanism that shipped the sellable before it. Its 💡 (extract a shared
`_webhook-kit-core/` + a `provenance_lint.py` that FAILS an unpinned fixture)
is the right instinct — machine-enforce the honesty bar rather than
reviewer-trust it; the same anti-rot principle is why this build regenerates
OWNER-QUEUE.md from the packet instead of hand-editing it.
