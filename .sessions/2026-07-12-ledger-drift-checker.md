# Session — advisory ledger-drift checker (scripts, non-publishing)

> **Status:** `complete`

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
- **completed (date -u):** Sun Jul 12 21:56:18 UTC 2026

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
- Built `scripts/check_ledger_drift.py` (stdlib only, exit 0 on every
  path), `docs/ledger-drift-checker.md` (badge `reference`, linked from
  `docs/current-state.md`), and the `ledger-drift-advisory` job in the
  host-owned `kit-tests.yml` (`continue-on-error: true`).
- Tested ALL paths locally with captured output (exit 0 each):
  trailing (`ledger-drift: trailing by 4 — missing PRs: #88, #89, #90,
  #91` against the real ledger + the real merged-PR set learned via the
  github MCP, since `api.github.com` is walled from this environment),
  in-sync (`ledger-drift: in-sync (ledger cites #91, newest merged #91)`
  on a doctored copy), no-token, API-unreachable, and empty-ledger skip
  lines. Full transcripts in PR #92's body.
- Opened PR #92 READY (non-draft), base `main`; the enabler lands it on
  green — this lane never arms or merges.
- CI at head `413f947`: kit-tests run 29210456912 SUCCESS (all 3 jobs,
  incl. the new advisory job, which printed the trailing-by-4 line LIVE
  with the CI token — the real-API path verified end to end);
  substrate-gate run 29210456886 = the designed born-red hold pre-flip.
- `python3 bootstrap.py check --strict` pre-flip: only red was the
  designed born-red hold on this card; clean at flip. Final inbox +
  claims re-read at HEAD `c1214b8` before this close: unchanged.

## Status / outcome

**Complete.** The ledger now has an automatic nag: every kit-tests run
prints one advisory ledger-drift line, and it can never gate a merge
(script exits 0 on every path AND the step is `continue-on-error` AND the
job is not a required context). First live run already earns its keep:
`trailing by 4 — missing PRs: #88, #89, #90, #91`. Claim deleted at close
per `control/claims/README.md`.

## 💡 Session idea

💡 An advisory line that only lives in CI logs is a nag nobody reads: the
`ledger-drift-advisory` job should also append its one line to
`$GITHUB_STEP_SUMMARY` (and, when trailing, the checker doc's suggested
action) so the drift verdict shows on the run's summary page instead of
being buried in a log fold. Same always-green contract, one extra `echo` —
and the pattern generalizes to any future advisory (claims-stale could
surface the same way). (Distinct from the drift checker itself, from the
§7 owner-queue derivation idea, and from any existing card's 💡.)

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-12-slow-word-vetting.md`
(PR #91) is grounded work done right — the collision verdict re-checked
same-day instead of trusted, the novella band measured (29,662 words via
`wc`) instead of guessed, and §7 left strictly owner-gated. Its review of
#90 also supplied this session's mandate verbatim. One honest nit: its
`📊 Model:` line reads `Claude (Fable family)` while sibling cards use the
compact family token (`fable-5`) — both are family-level and compliant,
but two spellings of the same fact make model attribution needlessly
harder to machine-scan across cards; one canonical token form would be
cheaper.
