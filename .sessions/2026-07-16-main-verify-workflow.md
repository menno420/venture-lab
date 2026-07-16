# Session — main-verification workflow (close the GITHUB_TOKEN post-merge CI gap)

> **Status:** `in-progress`

- **📊 Model:** Fable · medium · feature build (CI-workflow authoring)
- **started (date -u):** Thu Jul 16 01:09:31 UTC 2026
- **closed (date -u):** [[fill: date -u at flip]]
- **branch:** `claude/main-verify-workflow` (PR [[fill: number at open]])
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

[[fill: results at flip]]

## ⟲ Previous-session review

[[fill: prev-session review at flip]]

## 💡 Session idea

[[fill: idea at flip]]
