# 2026-07-13 — Night run: kids board-book cuts 2 (BOOKS lane)

> **Status:** `in-progress`

Started 2026-07-13T01:51:06Z (`date -u`).
**Run under ORDER 008** (control/inbox.md, 2026-07-13T00:46:54Z — owner
night-run DIRECT ORDER; seat clause 1: "BOOKS: multiple new book ideas AND
multiple versions of each (different angles, audiences, lengths) — versions
are cheap once the research exists"): this slice extends merged PR #107's
board-book convention to the two remaining picture books — **tummel** and
**dormouse** — as toddler (0–3) cuts in EN/NL/DE under
`candidates/childrens-books/<title>/versions/board-book/`, mirroring
`candidates/childrens-books/VERSIONS.md` exactly.

## Plan

- Premise checked at HEAD (35e5597): neither `tummel/` nor `dormouse/` has a
  `versions/` dir; only live claim covers control/inbox.md.
- One commit per title: `<slug>.board.{en,nl,de}.md` + `NOTES.md` (honest
  `wc -w`, same count command as PR #107; kept/dropped; standing ⚑s).
- Dormouse keeps slug `dormouse` in filenames and the manuscripts' existing
  title ("Pippa and the Tear in the Night") in text; the folder-slug/title
  rename question is noted as a ⚑ pointer in NOTES.md, not decided.
