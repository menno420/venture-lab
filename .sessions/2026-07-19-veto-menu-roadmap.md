# Session — Groom veto menu into prioritized execution roadmap

> **Status:** `complete`

- **📊 Model:** Claude Opus (4.x family) · medium · idea/planning
- **started (date -u):** Sun Jul 19 07:31 UTC 2026
- **closed (date -u):** Sun Jul 19 07:37 UTC 2026
- **PR:** #259 — <https://github.com/menno420/venture-lab/pull/259>
- **branch:** `claude/veto-menu-roadmap`
- **base:** `main@5d439bf`
- **purpose:** Groom the 64-item veto-ready planning menu
  (`docs/ideas/2026-07-18-veto-ready-menu.md`, #247) into a **prioritized,
  sequenced execution roadmap** that reflects reality after the overnight
  #242–#257 wave — not the pre-wave snapshot. Each roadmap entry is ONE line:
  item id/name · autonomous-safe OR owner-gated · its single unblock condition.
  Autonomous-safe slices (landable without owner clicks) are sequenced first,
  then owner-gated items grouped by the gate they wait on. Sequencing is tied to
  the three real standing constraints: (1) distribution — new SKUs/books don't
  move revenue without an owner-gated publish+distribution path; (2) the EAP
  read-only cutover **2026-07-21**; (3) the live-SWTK Stripe kill clock (T+7
  **2026-07-19**, T+14 **2026-07-26**). Planning doc only — NO code, NO publish
  surface, NO OWNER-QUEUE regen, fully reversible.
- **decide-and-flag (extend vs new doc):** **NEW doc**
  `docs/ideas/2026-07-19-execution-roadmap.md`, not an edit of
  `2026-07-18-next-wave-roadmap.md`. Rationale in the PR body; one line: the
  next-wave doc is a *value-ranked SKU pipeline* in the R1–R10 namespace, whereas
  this grooms the veto menu's cross-area SKU/BND/LM/ENG/DIST/BOOK/MISC namespace
  into an *execution sequence*; a fresh dated cohort doc is the `docs/ideas/`
  "conveyor" convention (the veto menu itself was a new doc, not an edit).
- **DONE items marked (shipped in the #242–#257 wave, verified via git log +
  current-state.md):** ENG-2 #248 · DIST-1 #249 · LM-1 #250 · LM-2 #251 ·
  DIST-3 #252 · MISC-3 #253 · DIST-9 #255 · ENG-3 #256 · ENG-9/OPS-1 #257.
- **honesty bar (repo TRUTH rule):** NO invented metrics, NO fabricated demand.
  Owner-gate status and unblock conditions are copied from the veto menu's own
  per-line `owner-gate` fields, not re-guessed. Shipped items are marked DONE only
  where a merged PR # is verified in git log.
- **scope (files):** NEW `docs/ideas/2026-07-19-execution-roadmap.md`; EDIT
  `docs/ideas/README.md` (one backlog index link so the doc is reachable); NEW
  `control/claims/veto-menu-roadmap.md`; this born-red card. No other paths.
  Born-red card holds the substrate-gate red until the completion flip.

## 💡 Session idea

💡 **A `scripts/check_planning_conveyor.py` — mechanize the DONE-reconciliation
this roadmap did by hand.** There are now **four** standing planning docs
(overnight menu · next-wave roadmap · veto menu · this execution roadmap), and
grooming the field into a DONE-marked sequence meant reading git log for each of
nine `#NNN → item` claims and cross-checking that a menu item marked DONE here
isn't still silently listed as open in the source menu. That is exactly the
manual "conveyor, not a graveyard" sweep MISC-5 proposes, and it's a tiny,
exit-0-preserving advisory checker: parse the DONE table(s) in each `docs/ideas/*`
cohort doc, assert every cited `#NNN` is actually a merged PR (via `git log
--grep`), and advisory-warn when an item marked DONE in a downstream roadmap is
not marked DONE (or is still an active `###` block) in the upstream menu it grooms
— so the next wave can't leave a stale "still open" line the way this wave's
pre-groom snapshot did. Guard recipe: new `scripts/check_planning_conveyor.py`
(mirror the advisory shape of `scripts/check_ledger_drift.py`), a
`test_check_planning_conveyor.py` with a fixture pair (one reconciled cohort doc,
one with a DONE-but-upstream-open drift), wired as advisory (never gating) beside
`check_ledger_drift.py` in the non-gating advisory set.

## previous-session review

previous-session review: the previous card
(`.sessions/2026-07-18-misc-3-kill-clock-packet.md`, MISC-3 #253) closed the
#249–#253 distribution-first baton at its *terminal* node — the pre-written T+14
keep/iterate/delist packet the clock→diagnostic→decision chain was aiming at —
and modelled two disciplines this session reused: a tight single-payload diff
with one reachable index link (no publish surface, no OWNER-QUEUE renumber), and
the honesty bar held hard (it *quoted* the kill rule verbatim and marked every
absent datum "not measured" rather than guessing). This roadmap carries the same
one-writer discipline — it *references* the veto menu's line detail instead of
re-deriving it — and extends that card's own forward-pointer: its 💡 asked to wire
the checker so the clock→diagnostic→decision chain is reachable on the day it
fires, and this session's 💡 proposes the sibling conveyor checker that keeps the
*planning* chain (menu→roadmap→DONE) self-reconciling. One nit inherited and
avoided: MISC-3's model line read `opus-4.8` (a version-specific token); per the
ORDER 012 family-level bar this card records `Claude Opus (4.x family)` instead.

## Work log

- 2026-07-19 — Branch `claude/veto-menu-roadmap` from `origin/main` (`5d439bf`,
  includes the full #242–#257 wave). Read the veto menu (#247), the next-wave
  roadmap (#248-era), `docs/ideas/README.md`, `docs/current-state.md`, the
  OWNER-QUEUE, `.sessions/README.md`, and the most recent card
  (`2026-07-18-misc-3-kill-clock-packet.md`) as the template. Verified the 9 DONE
  veto items against git log. Born-red card committed FIRST (`3599fb3`); pushed;
  pre-flip `python3 bootstrap.py check --strict` was EXIT 1 = the expected
  born-red HOLD (in-progress card only; no docs-gate/dref failure). Build begins.
- 2026-07-19 — Built the payload: `docs/ideas/2026-07-19-execution-roadmap.md`
  (Lane A autonomous-safe, five tiers → Lane B owner-gated, five gates → DONE
  table for the nine #242–#257 items → provenance); linked from
  `docs/ideas/README.md` (backlog index, newest-first); claim
  `control/claims/veto-menu-roadmap.md`. Committed `16ac0a9`, pushed. PR #259
  opened READY.
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `Claude Opus (4.x family)`, no version id per ORDER 012), one
  genuine 💡 idea (`check_planning_conveyor.py` with a guard recipe),
  previous-session review of the MISC-3 #253 card, every auto-draft slot
  resolved. This flip clears the born-red HOLD — last commit, releasing the
  merge-on-green workflow.
