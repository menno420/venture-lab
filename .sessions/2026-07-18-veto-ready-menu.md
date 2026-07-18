# Session — Veto-ready planning menu (owner morning deliverable, planning-only)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · idea/planning
- **started (date -u):** Sat Jul 18 22:48 UTC 2026
- **branch:** `claude/veto-ready-menu`
- **base:** `main@661ffce`
- **purpose:** the owner's live overnight directive (2026-07-18) is: "if your
  executable work is done, move over to planning... plan excessively... tomorrow
  morning I will skim the whole menu and VETO what I don't want; my veto is the
  filter, so don't pre-filter down to a few safe picks." The fleet has already
  LANDED the highest-leverage contained executable sellables work tonight (venture
  #242–#246; trading #152). So this slice produces the veto-ready MENU: a single
  comprehensive planning doc the owner can skim and veto line-by-line, deliberately
  EXCESSIVE in quantity, grouped by venture area (new SKUs, bundles, lead magnets,
  engineering leverage, distribution/ops, book/writing path), each proposal carrying
  a pitch · effort (S/M/L) · risk & reversibility · what it unblocks · owner-gate
  status. It REFERENCES and EXTENDS the two standing planning docs
  (`docs/ideas/2026-07-18-next-wave-roadmap.md` R1–R10 and
  `docs/ideas/2026-07-17-overnight-menu.md` P/PUB/REV/OPS) rather than duplicating
  them, retiring what has since shipped.
- **scope (files):** NEW `docs/ideas/2026-07-18-veto-ready-menu.md` (the menu);
  EDIT `docs/ideas/README.md` (link the new file into the backlog per the
  conveyor convention); plus the control scaffolding
  (`control/claims/veto-ready-menu.md`, this card, a `control/status.md`
  heartbeat). Planning-only: NOTHING ambitious is built, no SKU, no publish
  surface, no OWNER-QUEUE row. Born-red card holds substrate-gate red until the
  completion flip.
- **honesty bar (repo rule):** NO fabricated metrics, NO invented demand numbers,
  NO "N companies want this." Mark speculative items as speculative, name every
  dependency and owner gate honestly (especially the owner-only native-speaker NL
  proofread gate and the spend/publish gates), and include an explicit "what I
  deliberately did NOT build tonight and why" note. Quantity is the deliverable;
  the owner's veto is the filter, not mine.

## 💡 Session idea

💡 **A `scripts/reconcile_ideas_backlog.py` that machine-maintains the
`docs/ideas/` conveyor — marks a proposal SHIPPED when its slug lands, so no
planning doc ever re-derives a false "backlog dry" line.** Building this menu, the
single most error-prone manual step was the "how this relates to the existing
menus" reconciliation — by hand cross-checking which of the roadmap's R1–R10 and
the overnight menu's P/PUB/REV/OPS items had SHIPPED since they were written
(R1–R4/R7 had; I had to read `control/status.md`'s merge list to know). That
cross-check is exactly the drift the `docs/ideas/README.md` "conveyor, not a
graveyard" rule warns about, and it's re-done from scratch every planning session.
The fix is a small stdlib deriver that reads each idea doc's proposal ids +
slugs, resolves them against the merged-PR / candidates-tree evidence, and emits a
`backlog-item-shipped` advisory (same never-exit-affecting class as the claims and
kill-clock linters) for any still-listed-as-open item whose artifact is now in the
tree — turning the manual "which lines are stale" pass into a standing greppable
signal, and giving the next planning doc a mechanical "already-shipped, do not
re-propose" list instead of a hand-read one. This is MISC-5 in the menu itself,
promoted here as the session's own highest-leverage takeaway. Guard recipe: new
`scripts/reconcile_ideas_backlog.py` (parse `docs/ideas/*.md` proposal headings for
an id + a `candidates/<slug>/`-or-PR-number reference, resolve each against the
git log / candidates tree, advisory-warn on an "open" item whose artifact exists),
wired into `bootstrap.py check` beside `check_kill_clocks.py`; test target a
fixture pair of idea docs — one with a shipped-but-still-listed item, one clean —
asserting the one advisory fires. (Natural sibling of the funnel-coverage checkers
ENG-3/ENG-4 already logged on the lead-magnet cards: those track distribution
coverage, this tracks backlog freshness.)

## previous-session review

previous-session review: `.sessions/2026-07-18-agent-ops-lead-magnet.md` (PR #246
— the last distribution-first slice before the fleet flipped to planning mode).
It set two things this slice leaned on directly: (1) its hard-won discipline of
running in an ISOLATED fresh clone from the first command (parallel sessions race
on a shared git HEAD) — this slice did the same and hit no collision; and (2) its
closing 💡 (a per-cluster funnel-coverage checker) is one of the concrete
engineering-leverage lines I carried forward into the menu as ENG-3, alongside its
api-robustness-card sibling as ENG-4 — the menu is in part a place those stranded
card-💡s finally get a veto-able home. The one thing I'd flag forward: that slice
(and #243 before it) each shipped one lead magnet per session; the menu's LM-1/LM-2
name the two clusters still uncovered (membership, AI-Novella), so the natural next
distribution slice is pre-teed-up and shouldn't need re-derivation.

## Work log

- 2026-07-18 — Branch `claude/veto-ready-menu` from `origin/main` (`661ffce`);
  collision check clean (no existing `control/claims/` entry for a veto-ready
  menu, no open PR covering it). Claim + born-red card committed (first commit),
  pushed. Menu build begins.
- 2026-07-18 — Built the payload: `docs/ideas/2026-07-18-veto-ready-menu.md` (~55
  proposals across seven areas, referencing/extending R1–R10 and P/PUB/REV/OPS)
  and the `docs/ideas/README.md` backlog link. `git diff --stat origin/main`
  verified to carry ONLY the menu doc + README + claim + card. Committed, pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #247 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed,
  pushed.
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level, `idea/planning` PL-004 class), one 💡 idea, previous-session
  review, all `[[fill:]]` slots resolved. `python3 bootstrap.py check --strict`
  EXIT 0 (advisories only). Born-red HOLD clears; the PR is landable on green.
