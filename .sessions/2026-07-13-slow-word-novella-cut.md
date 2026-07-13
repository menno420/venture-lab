# 2026-07-13 — The Slow Word: novella cut + large-print edition spec

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · BOOKS lane, 2026-07-13 night run
- **Started:** 2026-07-13T00:50:40Z (`date -u`)
- **Closed:** 2026-07-13T01:37Z (`date -u`)
- **⚑ Order basis:** run under **ORDER 008** (owner night-run DIRECT ORDER, landed verbatim in `control/inbox.md` at `c99caa4`, re-verified present and unchanged at origin/main `1e90721` before this flip) — BOOKS clause: "multiple versions of each … versions are cheap once the research exists." Not self-initiated.

**What landed:** two derived versions of the finished novel `candidates/adult-novels/the-slow-word/` (~29,400 words, 12 chapters), under a new `versions/` convention:

1. `versions/novella-cut/the-slow-word-novella.md` — a COMPLETE abridged manuscript, all 12 chapters, real self-contained arc, finished prose throughout (no summary placeholders). Honest `wc -w`: **18986** (64.6% of the canonical chapter text). Scene-level cut list in `versions/novella-cut/NOTES.md`, plus market position (novella ebook, $3.99–$5.99 band per CHECKLIST §4) and the ⚑ owner-gate restated.
2. `versions/large-print/EDITION-SPEC.md` — production spec only (no new manuscript) for a large-print paperback of the FULL novel: 6×9 trim, 16pt+ typography norms, estimated 160–200 pages, KDP print cost verified ($1.00 + $0.012/page, [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340) accessed 2026-07-13), royalty math at $12.99/$14.99/$16.99 (60% of list − print cost), accessibility notes; unverified figures marked "not measured".
3. `versions/README.md` — the versions convention (one subdir per version; mandatory honest NOTES.md with real `wc -w`; `en/` stays master; publishing stays owner-gated).

**Publishing remains owner-gated** for both versions via the existing the-slow-word vetting path — this slice adds shelf inventory, not a publish click.

## previous-session review

Previous session (`.sessions/2026-07-13-night-field-manual.md`, PR #110): its checkout step of executing the artifact's own README instructions from inside the extracted bundle caught a real parity defect (tooling missing from the zip whose README invokes it) — the same "verify the artifact against its own claims" discipline this session applied as an honest `wc -w` in NOTES.md rather than a rounded aspirational count.

## 💡 Session idea

Budget-first abridgment: cutting chapter-by-chapter without per-chapter word budgets produced a first draft 26% over target and forced a five-pass line-level trim (expensive in edits and risk to voice). The cheap version: compute each chapter's target as `total_target × (chapter_words / book_words)` BEFORE writing, and `wc -w` after every chapter — the deviation is caught one chapter deep instead of twelve. Worth writing into the versions/README.md convention if a second abridgment (e.g. Ultramarine) is attempted.

## Work log

1. Born-red card + claim (`c98b573`), pushed before content work.
2. Read all 12 `en/` chapters in full before cutting.
3. `versions/README.md` + `large-print/EDITION-SPEC.md` (`e44fce3`; KDP print-cost page fetched and cited same-day).
4. Novella manuscript chapters 1–4 (`59b0e7b`), 5–8 (`287312e`), 9–12 + trim pass (`1329e8c`; note: that commit message says 18,997 — the true count after one further trim is 18,986, recorded verbatim in NOTES.md and the follow-up commit `d558bd3`).
5. NOTES.md with scene-level cut list, market band, ⚑ owner-gate (`d558bd3`).
6. `python3 bootstrap.py check --strict`: only findings are this card's designed born-red hold + its missing close-out markers — both resolved by this flip commit. Claim file deleted in this same commit.
