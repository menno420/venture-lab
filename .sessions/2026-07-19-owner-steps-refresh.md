# Session — Owner-steps refresh (single plain-language one-sitting list)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only

- **started (date -u):** Sun Jul 19 07:32 UTC 2026
- **branch:** `claude/owner-steps-refresh`
- **base:** `main@5d439bf`
- **purpose:** the owner (a non-technical human) needs ONE refreshed,
  plain-language "do these in one sitting" action list — every entry a genuine
  owner click or owner choice, nothing technical, nothing the seat can do
  itself. The canonical owner home `docs/publishing/OWNER-QUEUE.md` is a
  GENERATED file (by `scripts/derive_owner_queue.py`) and must not be
  hand-edited, so this slice adds a curated companion
  `docs/publishing/OWNER-START-HERE.md` that links back to it. Time-sensitive:
  the Stripe kit T+7 checkpoint is DUE TODAY 2026-07-19, and the Claude Code
  Projects EAP goes read-only 2026-07-21 (~2 days of write access left).
- **scope (files):** NEW `docs/publishing/OWNER-START-HERE.md`; EDIT
  `docs/publishing/README.md` (one index-table link so the docs reachability
  gate reaches the new doc); NEW `control/claims/owner-steps-refresh.md`. This
  card. Docs-only, reversible; no SKU, no publish surface, no OWNER-QUEUE row;
  the seat performs no publish/spend/account action.

## Work log

- 2026-07-19 — Branch `claude/owner-steps-refresh` from `origin/main`
  (`5d439bf`, #257 HEAD); clean base confirmed, `bootstrap.py check --strict`
  EXIT 0. Born-red card committed (first commit `c534ffd`), pushed. Build begins.
- 2026-07-19 — Decide-and-flag: `OWNER-QUEUE.md` header says GENERATED and a
  generator exists (`scripts/derive_owner_queue.py`), so hand-editing it would be
  overwritten on the next re-run — created a curated companion instead of
  extending it. No curated one-sitting home existed (OWNER-LAUNCH-HOUR is a
  single-product runbook; PUBLISHING-PLAN is book-catalog-only), so the companion
  is a new focused doc, `docs/publishing/OWNER-START-HERE.md`. A curated
  quickest-wins digest is NOT a duplicate of the exhaustive generated queue — it
  links back into `OWNER-QUEUE.md` §1/§2 for the full menu.
- 2026-07-19 — Built the payload: `docs/publishing/OWNER-START-HERE.md` (6 owner
  steps in one-sitting order — Stripe T+7 read due today; webhook trio → $79
  bundle; API four → $79 bundle; Membership+Template → $59 bundle with the ⚑A
  live-purchase caveat; the rest; the veto-menu skim — each with What/Where/Why/
  How-you'll-know and a bolded rec) + one `docs/publishing/README.md` index row
  (docs reachability gate) + `control/claims/owner-steps-refresh.md`. Sourced real
  links (live Stripe kit URL, per-kit owner-actions scripts, `gumroad.com → New
  product → Digital product`) from OWNER-QUEUE §2/§4 and the launch owner-actions
  docs; no invented URLs. Committed (`df4142a`), pushed. Diff carries only the 3
  intended files (+ card).
- 2026-07-19 — Pre-flip `bootstrap.py check --strict` = the born-red HOLD only
  (in-progress Status + missing markers); the new doc cleared all docs-hygiene
  gates (badge `owner-guidance`, links resolve, reachable via the README row);
  seat-digest + model-line advisories are pre-existing and non-gating.
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8` — no exact version id), one 💡 idea, previous-session
  review, all markers resolved. Re-ran `bootstrap.py check --strict` EXIT 0;
  born-red HOLD clears. Guard-fires ledger append reverted to keep the diff scoped
  to docs/publishing/ + .sessions/ + control/claims/.

## 💡 Session idea

💡 **A tiny `scripts/derive_owner_start_here.py` advisory that flags when
`OWNER-START-HERE.md`'s time-sensitive rows go stale against their source dates.**
This curated digest hard-codes two live clocks — the Stripe kit **T+7 (2026-07-19)
/ T+14 (2026-07-26)** checkpoint and the **EAP read-only cutover (2026-07-21)** —
that already live as structured facts elsewhere: the kill-clock dates in
`stripe-webhook-test-kit/LAUNCH-LOG.md` (the same source `scripts/check_kill_clocks.py`
already parses) and the cutover date in `control/inbox.md` ORDER 015. A curated
one-sitting list is only useful while its "do this TODAY" framing is true; the day
after T+14 passes, "DUE TODAY 2026-07-19" is actively misleading to a
non-technical owner. The fix mirrors the existing `check_kill_clocks.py` advisory
class (never exit-affecting): parse the dates this doc cites, compare against
`date -u`, and emit a `owner-start-here-stale` advisory when a cited checkpoint is
in the past — so the digest either gets refreshed or the stale urgency line gets
pulled, instead of silently rotting. Natural sibling of the `bundle-unlock-order`
advisory idea (#255 card) and the funnel-coverage checker: those check *ordering*
and *coverage*; this checks *freshness of owner-facing time claims*.

## previous-session review

previous-session review: the immediately prior distribution-lane card
(`2026-07-19-dist-9-pre-eap-sprint-plan.md`, #255) built the AGENT-LANDS-THESE vs
OWNER-CLICKS-THESE split for the pre-EAP window; this slice is its owner-facing
consumer — it takes that plan's hand-derived click sequence (webhook trio → bundle,
API four → bundle, membership+template → Ship-It) and the funnel diagnostic's
T+7/T+14 read (#252) and renders them as a single plain-language one-sitting list a
non-technical owner can act on without opening any of the ~30-section generated
queue. The lesson I carried forward from the #255 card's own flagged risk: those
click sequences are hand-copied across CATALOG, OWNER-QUEUE §2, and the sprint
plan, so they drift on every OWNER-QUEUE renumber — I kept this digest's per-step
detail *pointing into* `OWNER-QUEUE.md` §2 (never re-transcribing the paste-ready
values) so the one place a value can go stale stays the generated file, not this
curated page. The freeze/gate honesty bar #255 set (reconcile the append-only
ORDER 003 "frozen" text against the repo's real "UNFROZEN 2026-07-11" state) is
honored here as the ⚑A caveat on Step 4. One thing I'd flag forward: this doc's
own time-sensitive header dates are the new hand-maintained drift risk — see the
💡 above for the mechanical fix.
