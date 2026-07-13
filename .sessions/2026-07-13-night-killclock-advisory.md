# Session — Night run: kill-clock advisory + TEMPLATE.md evidence upgrades (ORDER 008, closing infra slice)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run infra lane
- **session:** the night run's closing infra slice — three small debts named
  by tonight's session cards, bundled: (1) `scripts/check_kill_clocks.py`
  (PR #128 card's 💡): advisory DUE/OVERDUE checker that IMPORTS
  `derive_owner_queue.parse_packet` + `ParseResult` (no forked parse logic)
  and compares KILL-CHECK ⏲ dates against a required `--today`; (2)
  TEMPLATE.md upgrades validated by two products each: the PROVENANCE-FOOTER
  listing convention (PRODUCT #8 + #9 both hand-rolled it) and the stage-3
  third evidence class **verified-by-production** (merge-wall card's 💡,
  Recipe 2 as the not-production-run exemplar); (3) `docs/current-state.md`
  advisory note + the one genuinely stale night-run line flipped.
- **started (date -u):** Sun Jul 13 03:29:38 UTC 2026
- **closed (date -u):** Sun Jul 13 03:35 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-merge-wall.md`, PRODUCT #9,
merged `3ee25d8` = tonight's HEAD): its central move — citing a production
system (live `auto-merge-enabler.yml` @ sha + real merge event IDs) instead
of faking an in-slice execution — is exactly the evidence class this slice
promoted into TEMPLATE.md stage 3, on the card's own argument that it is
both STRONGER (real event IDs, one API call to verify) and CHEAPER than a
CI harness. Its 💡 was adopted verbatim including the built-in honesty rule
(Recipe 2's not-production-run label cited as the exemplar). Its
previous-session review had already spotted that the PROVENANCE-FOOTER idea
was "two products' worth of validated pattern — that idea is ripe"; this
slice is the ripening. One discipline echoed: that card measured its guide
honestly (~8 pages vs the intake's estimate); this slice kept the same
honesty shape by scoping the current-state flip to the ONE line actually
stale against live main rather than claiming a full ledger refresh.

## 💡 Session idea

`check_kill_clocks.py` computes due-ness but nothing RUNS it on a schedule:
the natural next step is wiring `--today "$(date -u +%F)"` into the
coordinator's wake ritual (and/or the advisory step of `kit-tests.yml`,
where `check_ledger_drift.py` already runs) so "SWTK T+7 DUE today" is a
printed fact on every wake from 2026-07-19 onward. Design note for whoever
wires it: the required-but-advisory `--today` pattern (missing flag → skip
line + exit 0, never argparse's usage-error exit 2) kept the exit-0
contract airtight AND the determinism boundary explicit — worth reusing for
any future checker in the timestamp-free generator family that needs an
impure input.

## Scope

- `scripts/check_kill_clocks.py` — NEW: advisory kill-clock checker,
  stdlib-only, imports the owner-queue parser, `kill-clock:` stdout prefix,
  exit 0 on every path.
- `scripts/test_check_kill_clocks.py` — NEW: 7 stdlib-unittest tests
  (upcoming / due-today / overdue / no-tokens+pending-packet /
  malformed-checkpoint-date / malformed-`--today` / missing-`--today`).
- `docs/products/TEMPLATE.md` — stage-3 cell + new "Verified-by-production
  clause" section; stage-5 cell PROVENANCE-FOOTER convention.
- `docs/current-state.md` — kill-clock advisory bullet (Stability
  baseline); SWTK checkpoint line flipped coordinator-side → packet-side
  (the live state since PR #128).

## Executed evidence (all 2026-07-13, 03:29–03:35Z)

1. **Import-reuse proof:** `check_kill_clocks.py` imports
   `DEFAULT_VETTING_DIR`, `TIMER`, `ParseResult`, `parse_packet` from
   `derive_owner_queue` — zero KILL-CHECK grammar of its own; the
   "kill clock only ticks once live" rule is inherited by reading
   `result.live` only.
2. **Tests:** full scripts suite `Ran 16 tests in 0.011s … OK` (9 existing
   owner-queue + 7 new) at 03:31:25Z; verbose run shows all 7 kill-clock
   tests ok.
3. **Real-packet runs (exit 0 both):** `--today 2026-07-13` → SWTK ⏲
   upcoming 2026-07-19 (in 6 days) + upcoming 2026-07-26 (in 13 days),
   summary `0 overdue, 0 due today, 2 upcoming`; `--today 2026-07-19`
   (SWTK checkpoint day) → `DUE today 2026-07-19 — T+7 funnel checkpoint`
   + upcoming 2026-07-26 (in 7 days) + the ACTION line.
4. **Stale-line verification before flipping:** live main confirmed at
   `3ee25d8` via `git ls-remote` (03:29:38Z); In-flight night-run lines
   (catalog counts, sweep verdicts through PRODUCT #9) already match
   merged state — only the SWTK "coordinator-side" checkpoint claim
   predated PR #128's packet-side KILL-CHECK line and was flipped.

## Honest caveats

- The advisory is not yet wired into any wake ritual or CI step — it only
  prints when invoked (the 💡 above is that follow-up).
- "Recently shipped" in current-state trails the whole night run (newest
  cited #97 vs newest merged #132). Deliberately NOT half-fixed here: the
  wholesale backfill is the morning-tally/heartbeat's job and a parallel
  edit magnet; `check_ledger_drift.py` exists to nag about exactly this.
- TEMPLATE.md's new clauses are distilled from two products' cards, not
  from a third product executing them post-adoption; the first product to
  travel the template WITH these clauses is the real validation.
