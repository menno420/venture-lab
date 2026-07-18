# The Paper Orange — versions/

> **Status:** `active` — index created 2026-07-13 (night run, ORDER 011
> item 2, relaying ORDER 008 item 1: "multiple versions of each — different
> angles, audiences, lengths; versions are cheap once the research exists").
> The `nl/` edition predates this index (PR #150 lane, 2026-07-13).

Alternate cuts/angles/formats of the same title live here, one subdirectory
per version. The EN master (`../en/the-paper-orange.md`, **15,811 words**
measured by `wc -w`) stays the canonical text; a version NEVER edits the
master — fixes propagate EN → NL, never the reverse.

## Convention

- **One subdir per version**, named for the version's angle. Each holds the
  version's complete manuscript file(s) — or, for production specs, a spec
  doc — plus notes (`NOTES.md` for manuscript versions).
- **Specs/notes carry honest `wc -w` counts** (command shown), what was
  added/cut vs the base manuscript, and the version's market position —
  including every ⚑ owner gate.
- A version must not contradict the title's vetted positioning
  (`../DECISIONS.md`, `docs/publishing/vetting/the-paper-orange.md`).
- **No version publishes anything.** Publishing stays owner-gated
  (`docs/publishing/CHECKLIST.md` §7).

## Versions

| dir | angle | length (wc -w) | status |
|-----|-------|----------------|--------|
| `nl/` | complete literary Dutch (NL) edition, *De papieren sinaasappel* — see `nl/NOTES.md` and `docs/publishing/vetting/de-papieren-sinaasappel.md` | 16,203 (measured; EN source 15,811) | complete |
| `large-print/` | EN large-print paperback production spec (6×9, 16pt+, page estimate, KDP cost/royalty math) — spec only, no new manuscript | 15,811 (EN source, measured) | spec complete |
| `audio/` | EN audiobook/narration production spec (script order, Dutch pronunciation guide, per-chapter `wc -w` runtime @~150 wpm, tone/voice notes) — spec only, no recording | 15,811 (EN source, measured) | spec complete |

## Apparatus (back-matter & sellability — not a version)

Back-matter and launch/marketing assets are **not alternate cuts of the text**
— they add no manuscript and edit none — so they live under `../apparatus/`
rather than here, and are indexed below for reachability. Each carries a
provenance footer citing the EN master manuscript `file@sha`. Purely additive;
author's prose untouched. Publishing stays owner-gated
(`docs/publishing/CHECKLIST.md` §7).

| file (`../apparatus/`) | what it is | status |
|-----|-------|--------|
| `HISTORICAL-NOTE.md` | reader's/author's historical-context note on the 1944–45 Dutch Hunger Winter + Liberation, marking record vs. fiction, with a public-history further-reading list | complete |
| `BOOK-CLUB-GUIDE.md` | reading-group discussion guide — thematic overview, ~12 chapter-anchored questions, topics-to-research | complete |
| `MARKETING-COPY.md` | reusable listing/sellability assets — one-line hook, short + long blurb, 3 comp-positioning lines, keyword + BISAC suggestions, book-club/educator pitch (grounded, no fabricated reviews/metrics) | complete |
