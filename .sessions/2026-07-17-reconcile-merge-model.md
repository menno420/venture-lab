# Session — reconcile merge-model + cutoff-source in current-state

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · docs-only
- **started (date -u):** Fri Jul 17 20:05:07 UTC 2026
- **branch:** `claude/reconcile-merge-model-2026-07-17` (PR TBD)
- **base:** `main@389ab6e`
- **purpose:** correct `docs/current-state.md`'s merge-model description +
  clarify the 2026-07-21 read-only cutoff source.
- **session:** `docs/current-state.md` still describes the landing model as
  "agent opens a PR READY and leaves it green; the owner merges" and calls
  `auto-merge-enabler.yml` "slated for retirement." Observed reality today
  contradicts both: the enabler is ACTIVE and squash-merged PR #219
  (`github-actions[bot]`, 19:55:33Z) the moment CI went green — automatic
  land-on-green, not owner-merge. This slice reconciles the doc to that
  observed path (enabler active; agent opens READY, workflow squash-merges
  `claude/*` on green; agent seats stay classifier-restricted from
  self-enabling — the workflow is the sanctioned merger; `do-not-automerge`
  opts out, as PR #218 used). Second edit: the "2026-07-21 read-only cutoff"
  mention gets a cited source (`control/inbox.md` ORDER 015, 2026-07-15).
  Born-red card holds substrate-gate red until the deliberate completion flip.

## 💡 Session idea

💡 Have `main-verify.yml` assert `docs/current-state.md`'s stated merge-model
matches the actually-enabled workflows (fail if the doc says "owner-merge" while
`auto-merge-enabler.yml` is active) — turns model-vs-reality drift into a CI
signal.

## previous-session review

previous-session review: `.sessions/2026-07-17-restamp-current-state.md`
(PR #219) — it correctly restamped the HEAD field and proved land-on-green live,
but its heartbeat described the path as "awaiting owner merge," which #219's own
auto-merge immediately contradicted; this slice corrects that framing at the
source doc.
