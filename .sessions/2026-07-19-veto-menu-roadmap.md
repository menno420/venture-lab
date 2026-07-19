# Session — Groom veto menu into prioritized execution roadmap

> **Status:** `in-progress`

- **📊 Model:** [[fill: family-level model · effort · task-class at close]]
- **started (date -u):** Sun Jul 19 07:31 UTC 2026
- **closed (date -u):** [[fill: at close]]
- **PR:** [[fill: PR # + URL at close]]
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

💡 [[fill: one genuine next-step idea at close]]

## previous-session review

previous-session review: [[fill: one-line review of the previous session's card at close]]

## Work log

- 2026-07-19 — Branch `claude/veto-menu-roadmap` from `origin/main` (`5d439bf`,
  includes the full #242–#257 wave). Read the veto menu (#247), the next-wave
  roadmap (#248-era), `docs/ideas/README.md`, `docs/current-state.md`, the
  OWNER-QUEUE, `.sessions/README.md`, and the most recent card
  (`2026-07-18-misc-3-kill-clock-packet.md`) as the template. Verified the 9 DONE
  veto items against git log. Born-red card committed FIRST; build begins.
