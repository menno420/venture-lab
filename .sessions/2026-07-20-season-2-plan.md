# Session — Season-2 contingent build plan + heartbeat

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · idea/planning + heartbeat

- **started (date -u):** Mon Jul 20 07:45 UTC 2026
- **branch:** `claude/season-2-plan`
- **base:** `main@d2d49ec`
- **purpose:** land the **season-2 plan** — a prioritized, CONTINGENT-shaped
  post-cutoff build plan (`docs/ideas/2026-07-20-season-2-plan.md`) for the world
  after the 2026-07-21 write-cutoff, structured as ordered branches keyed to which
  owner action fires first (lead magnets posted · vetoes arrive · a book sells ·
  trading data provisioned) plus the standing upkeep cadence — AND carry this
  pass's **session heartbeat** (`control/status.md`, neutral PROSE, pointers only,
  NO trigger/routine/cron state — that class is classifier-walled here) and a
  **current-state restamp** (`docs/current-state.md` HEAD/date to current, noting
  the new plan doc exists). This is the FINAL PR of the pass; a sibling worker
  concurrently QA'd the owner click-surface and its fixes ride a **companion QA
  PR** (branch `claude/owner-surface-qa`). Planning + orientation only;
  **publishing stays owner-gated** (no publish, no Gumroad/KDP, no SKU, no
  generated-file edits — the plan doc is decide-and-flagged, owner-gated items
  marked).
- **scope (files):** NEW `docs/ideas/2026-07-20-season-2-plan.md` (the contingent
  plan; frontmatter + one-line-per-item ordered branches, mirroring the
  `2026-07-19-execution-roadmap.md` house style) + a link from
  `docs/ideas/README.md`; OVERWRITE `control/status.md` (neutral heartbeat, prose
  + pointers, NO routine/trigger state); UPDATE `docs/current-state.md` (restamp
  HEAD/date, note the plan doc exists); NEW `control/claims/season-2-plan.md`.
  This card. The inbox stays its writer's — `control/inbox.md` NOT edited. Docs +
  orientation only; no SKU, no publish surface, no OWNER-QUEUE row, no generated
  file, no scripts/ touched.

## Work log

- 2026-07-20 — Isolated clone `/home/user/venture-lab-s2` (a sibling worker holds
  `/home/user/venture-lab` on `claude/owner-surface-qa`); branch
  `claude/season-2-plan` cut from `origin/main` (`d2d49ec`, PR #281 EOD refresh).
  Read the context set (current-state, OWNER-START-HERE, status, inbox@HEAD, the
  execution-roadmap for house style, CATALOG.md for catalog facts, the QA scan for
  current catalog counts). Grounded the catalog: **2 complete adult trilogies
  (Ultramarine Bk 1–3 · Lull/DREAMLINE Bk 1–3) + a 6-book Night Kiln cozy series
  (Bk 1–6, Bk 7 planted-unwritten)**; 7 KDP-ready packages; **1 LIVE SKU + 19
  READY + 3 hard-gated bundles**; distribution the binding constraint. Trading
  direction doc: **not located** (searched venture cross-refs + the
  trading-strategy references; nearest artifact is a single strategy proposal —
  `trading-strategy docs/proposals/r5c-btc-bollinger-breakout-oos-proposal.md`,
  cited in the EAP closeout walkthrough — which is *a* strategy, not a
  fundamentals-vs-flows direction doc). Born-red card = first commit; PR #283
  opened READY on it.
- 2026-07-20 — Content commits. **Season-2 plan** — NEW
  `docs/ideas/2026-07-20-season-2-plan.md`: frontmatter + Status badge + four
  contingency branches (each an ordered one-line-per-item list) + a standing
  upkeep cadence + provenance, mirroring `2026-07-19-execution-roadmap.md`'s house
  style; linked from `docs/ideas/README.md`; claim file added. **Heartbeat +
  restamp** — overwrote `control/status.md` LAST (neutral PROSE, pointers only, NO
  routine/trigger/cron state — classifier-walled class), stating this pass QA'd
  the owner click-surface (fixes in flight on the companion QA PR, branch
  `claude/owner-surface-qa`), added the season-2 plan, catalog counts unchanged,
  nothing due before Friday's grading; restamped `docs/current-state.md` to HEAD
  `d2d49ec` (#281) noting the plan doc now exists. Pre-flip `bootstrap.py check
  --strict` red on the **born-red HOLD only** (four auto-draft fill slots +
  in-progress Status — the checker labels it "HOLD (by design)… nothing to
  investigate"); no
  guard reds, no D-ref/staleness/catalog-guard fire; advisories (seat-digest
  stale/over-budget + 7 pre-existing model-line notes on OTHER cards) non-gating.
  A **control + docs diff** — the claim rides the control fast lane; no SKU,
  generated file, or scripts touched. Then this flip to `complete`: Status
  flipped, all four auto-draft fill slots resolved, the four byte-markers present;
  re-ran strict → EXIT 0. `.substrate/guard-fires.jsonl` left unstaged to keep the
  diff scoped (sibling cards' convention).

## 💡 Session idea

💡 **A `check_plan_catalog_claims.py` advisory that guards planning docs against
stale hard catalog counts** — the exact drift class this doc *created*. My
season-2 plan asserts load-bearing catalog facts in prose ("a **six-book** Night
Kiln", "**two complete** trilogies", "**1 LIVE + 19 READY + 3** hard-gated
bundles") to make the "IF a book sells" and distribution branches concrete — but
those numbers go stale the moment a Night Kiln Bk 7 lands or a SKU publishes, and
nothing links the plan's assertions back to their source of truth. Cross-refs
INTO `OWNER-QUEUE.md` are already guarded (`check_owner_queue_staleness.py`
INV-1); catalog *count claims in narrative docs* are not. Guard recipe: a new
`scripts/check_plan_catalog_claims.py`, advisory-only, that (1) parses
`docs/current-state.md`'s "Book catalog" + "Products & revenue" sections and
`docs/launch/CATALOG.md`'s comparison table for the canonical counts (series
lengths, LIVE/READY/bundle tallies), (2) regex-scans `docs/ideas/*.md` and
`docs/publishing/*.md` for the same claim shapes (`\b(six|seven|\d+)-book\b`,
`\b(\d+)\s+publish-READY\b`, `\b(two|three)\s+complete\b.*trilog`), and (3) warns
on any mismatch — reusing the allowlist + itemized-findings pattern from
`check_catalog_drefs.py`. Test target: a new fixture in
`scripts/test_check_plan_catalog_claims.py` with a plan doc claiming "5-book Night
Kiln" against a current-state that says six. It is the narrative-prose sibling of
the D-ref guard: structured cross-refs guarded, prose counts still open.

## previous-session review

previous-session review: the newest prior card
`2026-07-20-owner-list-heartbeat-eod.md` (the #281 EOD refresh, final PR of the
prior pass) was the **orientation** slice that surfaced today's #277–#279 to the
owner (the submission-pack quick-win step + the two new books added to
OWNER-START-HERE) and overwrote `control/status.md` LAST as neutral prose — my
slice is its direct successor: I followed the same heartbeat-last discipline
(status.md written before the flip, pointers only, routine/trigger state
excluded) and carry the season-2 plan it did not. Its 💡 (a companion
section/step-numbering self-ref guard) and mine (a plan-doc catalog-count guard)
name the same footgun from adjacent angles — a hand-maintained doc silently
drifting from a source of truth — so both are framed as tiny non-gating siblings
of an existing guard rather than new hard walls.
