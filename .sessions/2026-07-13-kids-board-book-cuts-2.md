# 2026-07-13 — Night run: kids board-book cuts 2 (BOOKS lane)

> **Status:** `complete`

Started 2026-07-13T01:51:06Z · closed 2026-07-13T01:55:53Z (`date -u`).
**Run under ORDER 008** (control/inbox.md, 2026-07-13T00:46:54Z — owner
night-run DIRECT ORDER; seat clause 1: "BOOKS: multiple new book ideas AND
multiple versions of each (different angles, audiences, lengths) — versions
are cheap once the research exists"): this slice extends merged PR #107's
board-book convention to the two remaining picture books — **tummel** and
**dormouse** — as toddler (0–3) cuts in EN/NL/DE under
`candidates/childrens-books/<title>/versions/board-book/`, mirroring
`candidates/childrens-books/VERSIONS.md` exactly.

## Outcome

- **Two titles × three languages = six board-book manuscripts**, each 12
  spreads, standalone toddler read-aloud (not a summary), NL/DE as native
  parallel versions on the same spread grid:
  - `tummel/versions/board-book/` — story words (`wc -w`):
    EN 203 / NL 204 / DE 206. Refrain: "I'm coming, little squeak!" (x3 on
    the climb) + the Tick/Creak/Tock sound bracket; kept the
    small-helper-hears-a-small-cry beat and the bedtime landing; dropped
    the simile texture, the sound-taxonomy spread, and the 4–8
    characterization aside.
  - `dormouse/versions/board-book/` — story words: EN 219 / NL 220 /
    DE 218. Double refrain: "one, two, curl" tuck-in bracket + Heron's
    "Gently now. Small and gentle."; kept the small-and-gentle-mends-best
    beat and the in/out stitch chant; dropped Heron's backstory, the
    sleepy-fog exchange, and the closing Mama dialogue.
- Every version dir carries `NOTES.md`: honest `wc -w` (same count command
  PR #107's NOTES document), kept/dropped, and the standing format gates —
  price/format ⚑ OWNER; **KDP does not print board books**, so fulfillment
  needs IngramSpark or another board-book printer (⚑ OWNER research,
  deliberately not decided); illustration remains parked.
- Dormouse title handling per instruction: filenames keep the working slug
  `dormouse`; the text keeps the manuscripts' existing titles ("Pippa and
  the Tear in the Night" etc. per its DECISIONS.md); the folder-slug/title
  rename question is recorded as a ⚑ pointer in that NOTES.md, not decided.
  No DREAMLINE canon terms used — the cut stays in the tot-register the
  picture book chose.
- Premise-checked at HEAD (35e5597) before writing: neither tummel/ nor
  dormouse/ had a versions/ dir; the only live claim covered
  control/inbox.md. With this slice, all five finished picture-book titles
  now carry a board-book version — the PR #107 convention is fully applied.

## 💡 Session idea
💡 **Refrain-consistency ledger.** Each title's refrains and sound-words
now live in FOUR places per language (picture book, board cut, DECISIONS,
NOTES) — e.g. Heron's "Rustig maar. Klein en zachtjes." must match
byte-for-byte across all of them or a co-edition reprint drifts. A tiny
per-title `refrains.md` (one table: refrain x language, quoted verbatim)
would give every future version (early-reader cut, audio script) one
canonical place to copy from instead of re-mining the manuscripts.

## Previous-session review
previous-session review: `.sessions/2026-07-13-kids-board-book-cuts.md`
(PR #107) — excellent template slice: its VERSIONS.md convention +
NOTES.md count command were precise enough that this session could mirror
them mechanically with zero re-derivation, which is exactly what a
convention-seeding card should achieve. Honest nit: its close-out says
"three titles" done but never names the two remaining titles
(tummel/dormouse) as the obvious next slice — the coordinator had to
supply that pointer; a one-line "remaining: tummel, dormouse" would have
made the handoff self-serve.

## Model
- **📊 Model:** fable-5 · worker · BOOKS lane, night run
