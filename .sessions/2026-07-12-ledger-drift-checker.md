# Session — advisory ledger-drift checker (scripts, non-publishing)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · ledger-drift-checker
- **⚑ Self-initiated:** rung-4 contained reversible increment — sanctioned by
  PR #90's card 💡 idea (`.sessions/2026-07-12-current-state-refresh.md`,
  the ledger-drift checker proposal) and PR #91's card previous-session
  review ("The idea is worth building before the gap grows teeth",
  `.sessions/2026-07-12-slow-word-vetting.md`).
- **session:** build the ADVISORY ledger-drift checker: a stdlib-only
  `scripts/check_ledger_drift.py` that parses the highest PR number cited in
  `docs/current-state.md` § "Recently shipped", asks the GitHub API for the
  newest MERGED PR, and prints one advisory line (in-sync / trailing-by-K
  with the missing PR numbers / graceful skip). Exit 0 on EVERY path — it is
  never a gate. Wired as a non-blocking `continue-on-error` job in the
  host-owned `kit-tests.yml`; documented in `docs/ledger-drift-checker.md`.
- **started (date -u):** Sun Jul 12 21:50:15 UTC 2026

## Scope

- `scripts/check_ledger_drift.py` — new advisory checker (stdlib only).
- `docs/ledger-drift-checker.md` — new doc (badge `reference`), linked from
  `docs/current-state.md` for reachability.
- `.github/workflows/kit-tests.yml` — HOST-OWNED workflow: one new
  advisory job (`continue-on-error: true`; the script also exits 0 always,
  so it structurally cannot red a gate).
- `control/claims/2026-07-12-ledger-drift-checker.md` — claim (born-red
  first commit, deleted at close per `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `docs/publishing/**` (sibling lane in flight there),
  `control/inbox.md`, `control/status.md`, `control/outbox.md`, or any
  trigger. No publish, spend, or account action.

## Work log

- Hard-synced `main`: HEAD `c1214b8` == `git ls-remote origin main`.
- Inbox at HEAD: max ORDER 007, none countermand this slice.
  `control/claims/` at HEAD: README only — no live claim overlaps
  "scripts drift-checker (non-publishing)".
- Drift evidence grounding: `docs/current-state.md` § "Recently shipped"
  tops out at PR #87 while the newest merged PR is #91 (merged
  2026-07-12T21:36:26Z) — live drift of 4 (#88–#91); PR #91's card already
  recorded the ledger 3 PRs behind at #90's own merge.

## Status / outcome

(in progress)
