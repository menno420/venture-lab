# 2026-07-13 — Night run: kids board-book cuts (BOOKS lane)

> **Status:** `complete`

Started 2026-07-13T01:09:30Z · closed 2026-07-13T01:17:30Z (`date -u`).
**Run under ORDER 008** (control/inbox.md, 2026-07-13T00:46:54Z — owner
night-run DIRECT ORDER; seat clause 1: "BOOKS: multiple new book ideas AND
multiple versions of each (different angles, audiences, lengths) — versions
are cheap once the research exists"): this slice delivers the
multiple-versions half for the kids track — toddler-length (0–3) board-book
cuts of existing picture books, EN/NL/DE, as
`candidates/childrens-books/<title>/versions/board-book/`.

## Outcome

- **Three titles × three languages = nine board-book manuscripts**, each 12
  spreads, standalone toddler read-aloud (not a summary), NL/DE as native
  parallel versions on the same spread grid:
  - `painted-stones/versions/board-book/` — story words (`wc -w`):
    EN 172 / NL 162 / DE 177. Refrains: "Who painted the stone?" +
    "Follow, follow!" Kept the shy-hello-becomes-a-friend beat; dropped the
    notebook/detective apparatus.
  - `the-lantern-door/versions/board-book/` — story words: EN 171 / NL 168 /
    DE 171. Counting engine (one, two, three) + "up, up, up" climb; kept the
    make-the-town-warm-again beat; dropped the peril and bravery thesis;
    ends as a usable bedtime book.
  - `bram-the-yak/versions/board-book/` — story words: EN 154 / NL 161 /
    DE 163. The picture book's own refrain (tiny breath → BRONK) IS the
    board-book engine; kept sad-beat + rescue + hug; dropped the swan
    dinner, weekdays, and medal epilogue.
- Every version dir carries `NOTES.md`: honest `wc -w` (command stated),
  kept/dropped, and the format gates — price/format ⚑ OWNER; **KDP does not
  print board books**, so fulfillment needs IngramSpark or another
  board-book printer (⚑ OWNER research, deliberately not decided);
  illustration remains parked.
- `candidates/childrens-books/VERSIONS.md` seeded (status `reference`): the
  version-subdir convention — required NOTES.md, honest wc, standalone-work
  rule, owner gates carry over.
- Premise-checked at HEAD before writing: no versions/ or board-book files
  existed for any target; only live claim covered control/inbox.md.

## 💡 Session idea
💡 **Spread-grid parity check.** All three languages of a version are
written to the same spread grid, but nothing machine-checks it. A ~20-line
advisory script that greps `^\[Spread` per language file in a version dir
and flags count mismatches (12/12/11 = a dropped spread in one language)
would catch the likeliest co-edition drift for near-zero cost — same
tolerant/exit-0 contract as `derive_owner_queue.py`.

## Previous-session review
previous-session review: `.sessions/2026-07-13-night-book-idea-packets.md`
(PR #105) — strong slice: six genuinely non-overlapping concept packets
with real collision scans, and its close-out explicitly queued
"versions-of-each is the natural next slice", which is exactly what this
session picked up — the handoff worked as designed. Honest nit: its packets
record series/variant shape for NEW concepts, but the versioning that was
actually cheapest tonight was on EXISTING finished manuscripts
(painted-stones etc.), which the card didn't point at — the "start warm"
pointer aimed one shelf too far ahead.

## Model
- **📊 Model:** fable-5 · worker · BOOKS lane, night run
