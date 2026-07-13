# venture-lab — fleet cleanup audit, 2026-07-13 (EAP final night)

> **Status:** `audit` — one-shot, point-in-time. This is a complementary
> cleanup/verification pass by a fleet-wide auditor session, run in parallel
> with the owner's own live "ORDER 045" dispatch pass. It does not redispatch
> work and does not touch `control/inbox.md` (manager-written) or
> `control/status.md` (this seat's own coordinator heartbeat) — both are
> read-only inputs here.

## Scope and method

Audited `menno420/venture-lab` at `main` HEAD `991aff1` (PR #168, merged
2026-07-13T22:17:27Z) via a local clone plus the live GitHub MCP (state
re-verified at write time, ~2026-07-13T22:50Z). Checked: open PRs and their
CI/mergeable state, CI workflow definitions, the repo's own advisory
checkers (`bootstrap.py check --strict`, `lint_owner_gates.py`,
`check_kill_clocks.py`), `control/status.md` heartbeat freshness, and a
sample of `docs/` for internal consistency against live GitHub state.

## What the repo is

**venture-lab** is the fleet's "gen-2 born-right" pilot lane (seeded
2026-07-09 by the fleet manager from `menno420/fleet-manager`'s gen-2
blueprint). Mission (`README.md`): *"Find and validate the cheapest credible
path to first revenue."* An autonomous Claude Code coordinator seat
generates, scores, and builds small sellable digital products (Gumroad-style
kits, guides, template packs) and short-form fiction/books, and separately
runs trading-strategy backtests — always stopping at the owner-gated click
(no spend, no account creation, no publishing, no payment flows without an
explicit owner action; `README.md` "Hard rails"). Coordination with the
fleet manager runs through `control/inbox.md` (manager-written, append-only
orders) and `control/status.md` (lane-written heartbeat), per
`control/README.md`.

## Structure

- `control/` — manager↔lane protocol (`inbox.md`, `status.md`, `outbox.md`,
  `claims/`).
- `candidates/` — 20 venture-candidate directories (one-writer build trees:
  `membership-kit`, `template-packs`, `stripe-webhook-test-kit`,
  `github-webhook-test-kit`, `owner-click-queue-kit`,
  `multi-agent-control-plane-pack`, `agent-fleet-field-manual`,
  `kill-rule-intake-kit`, `false-green-test-trap`, `merge-wall-cookbook`,
  book categories `adult-novels`/`ya-novels`/`middle-grade`/
  `childrens-books`, plus `photo-packs`, `cc-cost-lens` (killed at intake
  this session, see below), `market-state-dashboard`,
  `stripe-webhook-gotchas`, `bababoefoe`, `dream-series`).
- `docs/` — `current-state.md` (living ledger), `conventions.md` (binding,
  overrides harness defaults), `publishing/` (31 vetting packets +
  generated `OWNER-QUEUE.md` + `keyword-map.md`), `products/` (ideation
  batches), `research/`, `retro/`, `review-queue.md`, `PLATFORM-LIMITS.md`,
  `CAPABILITIES.md`.
- `scripts/` — `derive_owner_queue.py` (generates `OWNER-QUEUE.md`),
  `lint_owner_gates.py`, `check_kill_clocks.py`, `check_ledger_drift.py`
  (each stdlib-only, advisory, exits 0 on nothing-to-report).
- `.sessions/` — 140 per-session log files (dated, newest-first convention).
- `bootstrap.py` (828 KB, vendored substrate-kit v1.15.0) + `.substrate/`
  — the enforcement/adoption tooling.
- `claims/` and `control/claims/` — both exist; `control/claims/README.md`
  documents `control/claims/` as the current home with `claims/` as an
  auto-detected legacy location during a migration window.

## CI setup and health

Four workflows: `substrate-gate.yml` (kit-owned merge gate — session-log
hygiene, claims, badge tokens), `kit-tests.yml` (host-owned — real HTTP-layer
tests for the shipped Stripe/GitHub webhook kits + owner-click-queue-kit +
the owner-gate lint and ledger-drift advisory steps), `photo-samples-validate.yml`
(scoped to `candidates/photo-packs/**`), `auto-merge-enabler.yml` (arms
native GitHub auto-merge on `claude/*`-headed PRs at open).

Locally at HEAD `991aff1`:
- `python3 bootstrap.py check --strict` → **exit 0**, "all checks passed."
- `python3 scripts/lint_owner_gates.py` → **OK — 33 input(s) clean.**
- `python3 scripts/check_kill_clocks.py --today 2026-07-13` → 0 overdue,
  0 due today, 2 upcoming (Stripe Webhook Test Kit T+7 2026-07-19, T+14
  2026-07-26).
- `python3 scripts/check_ledger_drift.py` → could not run from this sandbox
  (`HTTP Error 403: Forbidden` reaching the GitHub API directly — the
  sandbox's outbound network wall, not a repo defect); cross-checked the
  same fact manually via the GitHub MCP instead (see Inconsistencies below).

The one open PR at audit time (#169) shows CI green on every substantive
check — `owner-gate-lint-advisory`, `ledger-drift-advisory`,
`owner-click-queue-kit-tests`, `stripe-webhook-test-kit-tests`,
`membership-kit-tests`, `github-webhook-test-kit-tests` all `success` — with
`substrate-gate` `failure` by design (the repo's documented "born-red hold":
a session card left at `in-progress` intentionally reds the gate until the
session's final "flip" commit). This is the convention working as
documented, not a CI health problem.

## Doc quality

Strong points: `docs/conventions.md` is a short, binding, numbered rule set
explicitly stated to override harness defaults; `docs/current-state.md`
is dense and mostly well-cited (PR numbers + squash SHAs throughout);
`docs/publishing/OWNER-QUEUE.md` is machine-generated from the vetting
packets (never hand-edited) and is lint-checked; kill-clock and owner-gate
discipline is genuinely enforced by advisory CI, not just described.

Gaps found:
- **`.session-journal.md` is still template-empty.** After 168 PRs and 140
  session-log files, every section of the cross-session "guidebook" —
  Quick reference, Environment & boot runbook, Recurring problems + fixes,
  Past mistakes to avoid, Candidate rules — is an unfilled placeholder
  (`(Boot / run-checks / common-recovery commands for venture-lab.)` etc.,
  verbatim, all five sections). All institutional memory currently lives
  only in per-session `.sessions/*.md` files, which are not indexed or
  grep-guided for a fresh session the way the journal is designed to be.
- **`docs/review-queue.md` has a stale row.** See Inconsistencies below —
  PR #9 is listed as unmerged three days and ~160 PRs after it merged.
- **`docs/current-state.md` "Recently shipped" trails live HEAD by 7
  merged PRs** (#162–#168) at audit time — see Inconsistencies below. The
  repo's own `check_ledger_drift.py` is designed to catch exactly this but
  is advisory (never blocks) and could not be run from this sandbox to
  confirm it currently fires; the drift is real regardless, confirmed
  independently via the GitHub MCP.

## Open PRs — verification and disposition

**Live count at audit time: 1 open PR** (`state=open` via
`mcp__github__list_pull_requests`, single result, no pagination needed).

### PR #169 — left untouched (verified active, in-flight work)

`ORDER 011 item 1: cc-cost-lens intake KILL + fresh ideation batch (night slice)`
— branch `claude/night-product-slice`, base `991aff1`, opened
**2026-07-13T22:45:50Z** (created_at, per `pull_request_read`), i.e.
**minutes before this audit ran**, not hours. Session card
(`.sessions/2026-07-13-night-product-slice.md`) states `Status: in-progress`,
`started (date -u): Sun Jul 13 22:39:25 UTC 2026`, `completed: (at flip)`,
and every terminal section is a literal `(at flip)` placeholder. The PR body
itself says explicitly: *"the top BUILD's packet ... lands on this same
branch in the next commits — the born-red card holds this PR red by design
until the flip. **Do not merge before the flip.**"* `substrate-gate` is
`failure` by the repo's own documented born-red convention (see CI section);
every other check is green. `mergeable_state: blocked`.

This is squarely covered by global safety rule 1 (PR created/updated in the
last 2–3 hours = likely live work — here, in the last **five minutes**) —
**not touched, not merged, not commented on.** It is the visible, concrete
evidence that this repo's coordinator seat is doing real work *right now*,
independent of and concurrent with this audit.

**No PRs were merged, closed, or fixed by this audit.** There was nothing
else in the open-PR queue to disposition.

## Heartbeat verification

`control/status.md` (`updated: 2026-07-13T16:26:34Z`) was **~6h23m stale**
at the moment this audit checked it (2026-07-13T22:50Z UTC, `date -u`
verified). This matches and extends the dispatch-time observation of
"~5h04m stale" — the gap has grown by roughly the time between dispatch and
this audit, which is expected since no new heartbeat write has landed since
PR #167 (the 16:26Z heartbeat itself). Two PRs merged since that heartbeat
touched `control/inbox.md` only (append-only orders, PR #168) or are
in-flight product work not yet at its heartbeat-writing "flip" step
(PR #169, open) — **neither is a `control/status.md` heartbeat refresh**,
so the staleness is real, not a false reading from a partial clone.

**Read against the fleet context's "not flagged active-right-now"
assessment: that assessment is now stale.** PR #169's session card shows
work starting at 22:39:25Z and the PR opening at 22:45:50Z — inside the
same ~10-minute window this audit began (~22:45–22:50Z). The heartbeat file
being stale and the seat being actively mid-session are not contradictory:
this lane's convention is to write the heartbeat only at session close
("LAST: overwrite `control/status.md`", `control/README.md`), so an
in-progress session legitimately shows a stale heartbeat file right up
until its flip commit. **Verdict: this repo is ACTIVE right now** (evidence:
PR #169, opened ~5 minutes before this audit, still `in-progress`), even
though its heartbeat *file* reads 6+ hours old — the two facts describe
different things (last completed session vs. current session), and this
audit deliberately treated the live PR signal as authoritative over the
stale file, per the global safety rules.

## Inconsistencies found

1. **`docs/review-queue.md` PR #9 row is stale by ~3.5 days / ~160 PRs.**
   The table's only row says PR #9's zips are "not yet landed" pending "the
   owner merge," citing an agent self-merge wall from 2026-07-10. PR #9 in
   fact merged **2026-07-10T05:11:50Z** (verified live via
   `mcp__github__pull_request_read`: `"merged": true, "merged_at":
   "2026-07-10T05:11:50Z"`; also independently recorded in this lane's own
   ORDER 004 inbox text at the time: *"PR #9 IS merged (`95b755b`,
   05:11:50Z)"*). The review-queue row was never updated or cleared after
   the merge-then-flag re-check happened (or never happened) — the repo's
   own convention states *"An empty queue with all PRs merged is the
   healthy state,"* which this file has not reflected for three days.
2. **`docs/current-state.md` "Recently shipped" ledger trails live main by
   7 merged PRs.** The file's own header states it was "Refreshed
   2026-07-13 at the coordinator boot-refresh pass (HEAD `84d4bcb`, PR
   #161)" and its shipped-list stops at PR #161 (squash `84d4bcb`). Live
   main is at PR #168 (squash on `991aff1`) at audit time — PRs #162
   (boot-refresh follow-on heartbeat), #163 (ORDER 010 verdicts), #164
   (Multi-Agent Control-Plane Pack), #165 (NEXT-SESSION rewrite), #166
   (counts-sync), #167 (heartbeat), #168 (ORDER 011 inbox append) are
   merged but not listed. The repo's own `check_ledger_drift.py` exists
   specifically to catch this and is wired as an advisory (non-blocking)
   CI step — this is exactly the class of drift it is designed to nag
   about, confirming the checker's purpose is sound even though this
   audit's sandbox could not execute it directly against the live API.
3. **`candidates/` has more directories than `docs/current-state.md`'s
   product catalog narrative accounts for.** `market-state-dashboard` and
   `stripe-webhook-gotchas` exist as candidate directories on disk but are
   not named in the "Products" section of `current-state.md` (which lists
   1 live + 9 publish-READY + 2 hard-gated + "remaining unpacketed
   candidate: `cc-cost-lens`"). This audit did not investigate their
   contents/intent — flagging only that the catalog narrative and the
   directory listing don't fully match; it may be pre-intake scratch work
   rather than a real gap.

## Suggestions

1. **Centralize the "stale ledger row" pattern as a fleet-wide advisory
   check, not just a per-repo script.** `check_ledger_drift.py` here and
   the analogous checkers in sibling repos are independently reinvented;
   a shared substrate-kit-level ledger-drift checker (compare a doc's
   "as of PR #N" citation against the live default-branch PR count) would
   travel to every lane for free on `bootstrap.py upgrade`, the way
   `substrate-gate.yml` already does.
2. **A born-red PR that predates a heartbeat write is, by convention, an
   ambiguous "is this repo active" signal from the outside.** This audit
   had to cross-reference PR creation/session-card timestamps against the
   stale `control/status.md` to correctly conclude the repo was live. A
   cheap fix: have the born-red *first* commit also touch a single
   well-known low-conflict file (e.g. append one line to
   `control/status.md` or a separate `control/activity.md`) so "is a
   session in flight right now" is answerable from one file without
   needing to enumerate open PRs first.
3. **Populate `.session-journal.md` from the existing `.sessions/` corpus.**
   140 session logs contain real recurring friction (the #778-style
   auto-merge/enabler classes referenced elsewhere in the fleet, the
   #157 dead-mid-turn recovery case cited inside PR #169 itself, the
   inbox-grammar substrate-gate rejections logged in the 2026-07-13 night
   report) that would cost a fresh session real time to rediscover by
   reading session logs one at a time. A single grooming pass extracting
   3–5 "recurring problems + fixes" entries would make the journal earn
   its designed role.
4. **`docs/review-queue.md`'s single stale row suggests the "merge-then-flag,
   veto=revert" post-merge review loop isn't actually being walked** —
   worth a one-line addition to a future session's standing-ritual checklist
   ("check `review-queue.md` for rows older than N merged PRs and clear or
   re-flag them") so the queue doesn't silently stop functioning as a real
   review mechanism.

## Notes

- No commits were made to `main`, `control/inbox.md`, or `control/status.md`
  by this audit. This report is the only change, on a new branch, via a
  new PR that this audit does **not** self-merge.
- `claims/` vs `control/claims/`: both directories are recognized by the
  repo's own tooling as a migration-window duplicate (documented in
  `control/README.md`); not treated as an inconsistency here since it is
  explicitly called out as intentional and temporary in the repo's own
  docs.
