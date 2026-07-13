# 2026-07-13 — Night run: comet-biscuit board-book cut (BOOKS lane)

> **Status:** `complete`

Started 2026-07-13T02:41:47Z · closed 2026-07-13T02:44:51Z (`date -u`).
**Run under ORDER 008** (control/inbox.md, 2026-07-13T00:46:54Z — owner
night-run DIRECT ORDER; seat clause 1: "BOOKS: multiple new book ideas AND
multiple versions of each (different angles, audiences, lengths) — versions
are cheap once the research exists"): this slice extends the merged board-book
convention (PRs #107/#118, `candidates/childrens-books/VERSIONS.md`) to
**comet-biscuit book 1** (*The Great Jam Wobble* / *De Grote Jamwiebel* /
*Der große Marmeladen-Wackler*) as a toddler (0–3) cut in EN/NL/DE under
`candidates/childrens-books/comet-biscuit/versions/board-book/`. Note:
comet-biscuit uses the subdir convention (`{en,nl,de}/` folders, three books
each), unlike the flat-file titles — this cut targets book 1 only.

## Outcome

- **One title × three languages = three board-book manuscripts**, each 12
  spreads (cut from the picture book's 15), standalone toddler read-aloud
  (not a summary), NL/DE as native parallel versions on the same spread grid:
  - `comet-biscuit/versions/board-book/comet-biscuit-1.board.{en,nl,de}.md`
    — story words (`wc -w`, same count command as PR #107/#118 NOTES):
    EN 187 / NL 178 / DE 176, all inside the 150–250 target.
  - Refrain engine: "Wobble, wobble, glug, glug, GLUG!" (jam-out and
    jam-back spreads) + the Ker-CHUNK bracket opening and closing the book
    + Bloop's name-as-sound call-and-response. One core beat kept: the
    littlest, shyest crew member saves the day just by glowing. Dropped:
    the briefing-comedy routine, Barnaby's last-Tuesday gag, the
    plan-logic chain, Bloop's homesickness framing; a goodnight landing
    replaces the series-hook ending.
  - Each edition keeps its own DECISIONS.md sound-set (KE-TSJONK/PLOP/
    WHOESJ/bloep/glok; KA-TSCHUNK/PLOPP/WUSCH/blubb/gluck) and localized
    names (Nootmuskaat/Muskat, Bloep/Blubb, Muffinmaan/Muffinmond), so the
    sound is consistent across a family's shelf; DE keeps Blubb feminine.
- `NOTES.md` in the version dir: honest `wc -w` with the count command
  verbatim, kept/dropped, and the standing gates — price/format ⚑ OWNER;
  **KDP does not print board books**, so fulfillment needs IngramSpark or
  another board-book printer (⚑ OWNER research, deliberately not decided);
  illustration remains parked.
- Premise-checked at HEAD (ca4c8a1) before writing: comet-biscuit/ had no
  versions/ dir; the only live claim covered control/inbox.md. Filenames
  carry the book number (`comet-biscuit-1.board.<lang>.md`) because the
  title is a series — books 2 and 3 have no board cut yet (obvious next
  slices: `comet-biscuit-2.board.*`, `comet-biscuit-3.board.*`, and
  star-pirates if it also uses the subdir convention).

## 💡 Session idea
💡 **Series-aware version naming needs one line in VERSIONS.md.** This is
the first multi-book title to grow a version dir, and the convention file
only specifies `<slug>.<version>.{en,nl,de}.md` — it says nothing about
series, so this session had to invent `comet-biscuit-1.board.en.md` ad hoc.
One sentence in `candidates/childrens-books/VERSIONS.md` ("multi-book
titles: `<slug>-<book-number>.<version>.<lang>.md`, one shared NOTES.md per
version dir with a per-book count table") would keep comet-biscuit books
2–3 and star-pirates from each re-deciding the pattern — and would prevent
a mixed dir where one book's cut is named by slug and the next by title.

## Previous-session review
previous-session review: `.sessions/2026-07-13-kids-board-book-cuts-2.md`
(PR #118, tummel + dormouse) — its NOTES.md format was precise enough to
mirror mechanically (count command, kept/dropped structure, the three
standing ⚑ gates), which is what made this slice cheap. Honest nit: its
close-out claims "all five finished picture-book titles now carry a
board-book version," which silently excludes the subdir-convention series
(comet-biscuit, star-pirates) — that framing reads as track-complete and
could have stranded this very slice; series titles should be named as
remaining work, not defined out of the tally.

## Model
- **📊 Model:** fable-5 · worker · BOOKS lane, night run
