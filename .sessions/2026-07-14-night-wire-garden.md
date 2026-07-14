# Session — Night write-slice: The Wire Garden (concept #2), two-writer manuscript

> **Status:** `in-progress`

- **📊 Model:** fable-5 · BOOKS-lane night session · night run 2026-07-14
- **session:** night worker, coordinator-dispatched write-slice (concept #2 of
  the 2026-07-14 shortlist, `docs/ideas/2026-07-14-adult-title-concepts.md`):
  The Wire Garden as a complete 12-chapter novella, split across two writers
  — this seat lands front matter + chapters 1–6 + DECISIONS.md; a second
  writer lands chapters 7–12, the shortlist-doc marking, and the flip.
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-14T03:02Z

## Outcome
- IN PROGRESS — this card is born-red and holds substrate-gate red by design
  until the second writer's completion flip.
- First-half deliverables (this seat): claim + this card as the first
  commit; READY PR opened immediately;
  `candidates/adult-novels/the-wire-garden/DECISIONS.md`
  (verified-vs-invented Dodendraad ledger, title-collision finding recorded
  honestly); front matter + chapters 1–6 of
  `candidates/adult-novels/the-wire-garden/en/the-wire-garden.md`, committed
  in 3-chapter chunks per house drafting convention.
- Second-half deliverables (second writer): chapters 7–12, honest `wc -w`
  re-measure into DECISIONS.md, shortlist-doc marking, claim deletion, card
  flip to `complete`.

## Work log
- 2026-07-14T03:02Z — Branch `claude/night-wire-garden` from origin/main
  (`0375099`). Claims scan clean (`control/claims/` README-only); no
  `candidates/adult-novels/the-wire-garden` at HEAD; no open PR touching it.
  Born-red card + claim committed as the first commit (`0e608b6` at
  03:02Z) and pushed; READY PR #187 opened immediately; PR activity
  subscribed. Auto-merge left to the enabler workflow, untouched by this
  seat.
- 2026-07-14T03:03Z — `candidates/adult-novels/the-wire-garden/DECISIONS.md`
  committed (`6e3018d`): verified-vs-invented Dodendraad ledger, the
  disputed-length and contested-death-toll handling, the title-collision
  finding (W. D. Marcum 2025 thriller; subtitle mandatory), the *De
  draadtuin* NL pre-naming.
- 2026-07-14T03:12Z–03:18Z — Manuscript first half committed in 3-chapter
  chunks per house drafting convention: `2640455` (03:12Z, front matter +
  ch. 1–3), `28ff3d8` (03:18Z, ch. 4–6). Per-chapter `wc`-region counts at
  `28ff3d8`: ch1 1449 · ch2 1364 · ch3 1353 · ch4 1208 · ch5 1167 ·
  ch6 1378; file total (front matter included) `wc -w` = 7994 — inside the
  first-half band 7,600–8,000. Handoff state for the second writer: ch 7–12
  per the outline, honest re-measure at the flip.
