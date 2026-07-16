# Session — main-verification workflow (close the GITHUB_TOKEN post-merge CI gap)

> **Status:** `complete`

- **📊 Model:** Fable · medium · feature build (CI-workflow authoring)
- **started (date -u):** Thu Jul 16 01:09:31 UTC 2026
- **closed (date -u):** Thu Jul 16 01:13:09 UTC 2026
- **branch:** `claude/main-verify-workflow` (PR #207)
- **session:** Dispatched worker slice. What/why: the enabler merges every
  `claude/*` PR with `GITHUB_TOKEN` (github-actions[bot]), and GitHub
  suppresses `on: push` workflows for events created by that token — so
  every squash merged onto `main` since `374e8d1` (2026-07-13T09:12Z)
  produced ZERO post-merge CI on main; PR-head green is the only evidence,
  and a bad merge-skew squash would land undetected. This was flagged (not
  fixed) by the previous session's 💡 line
  (`.sessions/2026-07-16-state-restamp.md`). This slice closes the gap from
  the repo side with a scheduled main-verification workflow.
- **scope:** ONE new workflow file `.github/workflows/main-verify.yml` —
  `on: schedule` (cron `17 */6 * * *`, every 6h off the top of the hour) +
  `workflow_dispatch`, `permissions: contents: read`, no secrets, no PATs.
  Jobs mirror `kit-tests.yml`'s test steps verbatim (same checkout /
  setup-python / unittest commands) plus the repo's own
  `bootstrap.py check --strict` gate; schedule runs execute on the default
  branch by definition, so every run re-verifies main. Plus this card,
  claim, and a heartbeat re-stamp. No edits to existing workflows (kit-owned
  files stay untouched; host customizations belong in a separate file per
  their headers).
- **walls:** no publish, spend, or external action; no edits to
  `control/inbox.md`; no merge or auto-merge action from this seat; no
  secrets; family-level model names only.
- **verify plan:** YAML-parse the new workflow
  (`python3 -c "import yaml; yaml.safe_load(...)"`); run
  `python3 bootstrap.py check --strict` pre-push; run the mirrored unittest
  suites locally once and record the verdict lines; after merge, the first
  scheduled or dispatched run on main is the end-to-end proof.

## Results (as landed)

- **`.github/workflows/main-verify.yml` added** (commit `8b25c12`):
  HOST-OWNED lane, `schedule` cron `17 */6 * * *` + `workflow_dispatch`,
  `permissions: contents: read`, five jobs — the four kit-tests.yml test
  jobs mirrored verbatim (membership-kit 3-suite unittest, SWTK / GWTK
  `test_http_realpath`, OCQK `test_ocq`) plus `substrate-strict-check`
  running `python3 bootstrap.py check --strict` on a plain main checkout.
  The kit-tests advisory jobs (owner-gate lint, ledger drift) were NOT
  mirrored: both are continue-on-error/never-red by design, so they add no
  verification signal to a scheduled lane.
- **Local verification pre-push:** YAML parse OK; all four mirrored suites
  green on this branch — membership-kit `Ran 36 tests in 10.593s / OK`,
  SWTK `Ran 14 tests in 3.031s / OK`, GWTK `Ran 18 tests in 4.551s / OK`,
  OCQK `Ran 38 tests in 0.033s / OK`; `bootstrap.py check --strict` green
  except this card's own designed born-red HOLD.
- **Enabler carve-out checked** (`.github/workflows/auto-merge-enabler.yml`
  @ `a00df9b`, job `if:` lines 40–44): exclusions are fork-head, draft,
  non-`claude/` head, and the `do-not-automerge` label only — there is NO
  `.github/workflows/**` path carve-out, so #207 lands on green like any
  other slice.
- **Heartbeat re-stamped** (`control/status.md`, commit `6263858`) with the
  slice facts, #207 disposition, carried ⚑ owner items, and a next-2 baton
  (Friday grading executor; post-merge manual `main-verify` dispatch).
- Claim `control/claims/2026-07-16-main-verify-workflow.md` released in
  this flip commit per convention.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-16-state-restamp.md` (PR #206)
— its claims held under re-verification this session: main HEAD at boot was
its squash `a00df9b`, the live open-PR list was empty before this slice's
#207 (matching its "0 open PRs + #206 only" disposition), and its central
finding — both CI workflows declare `on: push: branches: [main]` yet
enabler merges fire nothing — checks out mechanically: the enabler merges
with `GH_TOKEN: ${{ secrets.ROUTINE_PAT || secrets.GITHUB_TOKEN }}` and the
merges attribute to github-actions[bot], which is exactly the
GITHUB_TOKEN-suppression case. Its 💡 line proposed the cron verification
lane this slice built, correctly scoped it as out-of-bounds for its own
docs-only slice, and left an accurate, actionable baton — a model handoff.

## 💡 Session idea

💡 **A red scheduled run on main is currently invisible — wire the
failsafe to read it.** `main-verify` closes the *execution* gap but not the
*attention* gap: nobody merges anything when a cron run reds, so no PR
surfaces the failure and it sits unseen in the Actions tab. Cheap fix: the
coordinator's failsafe/pacemaker wake reads the latest `main-verify` run
conclusion (one `gh api` / MCP `actions_list` call) and ⚑-flags a red one
on the heartbeat — turning the scheduled lane into a monitored one.
Deduped against prior `.sessions/*.md` 💡 lines: the state-restamp idea
created this lane; advisory-visibility ideas cover advisory *steps inside
PR CI*, not unattended scheduled runs on main.
