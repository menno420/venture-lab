# Session — Ultramarine, Book 3

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · high · Ultramarine Book 3 manuscript

- **started (date -u):** Mon Jul 20 04:12 UTC 2026
- **branch:** `claude/ultramarine-book3`
- **base:** `main@1fdbc4f`
- **purpose:** write the genuine third and final Ultramarine novel as landable
  repo content, grounded strictly in the series `bible/` (style/world/characters
  + `book2-additions.md`) and the ending of Book 2 (*The Blue and the White*).
  A complete finished manuscript in the series voice/format (close third on
  Clara Wijnants, past tense, 12 chapters in three parts, ~20k+ band matching
  Book 2's shape), **paying off the exact hook Book 2 planted in ch. 12 ("The
  Colour That Remains")**: the great VOC order of blue-and-white bound for the
  East — more than Clara and one pottery can grind alone — and Grietje, the
  child who will paint it, standing at the slab with blue to the creases,
  "the bluest hands in Delft, and everywhere the plates go." Book 3 fulfils that
  order: the scale beyond one pottery, the fired-cobalt trade set against the
  lost true ultramarine, Grietje's coming into her own as a painter, the
  East-bound freight, and the human cost and reward of industrialising a colour.
  Closes the second trilogy with earned resolution and a light, organic forward
  note. Pure repo content; **publishing stays owner-gated** (no publish, no
  Gumroad/KDP, no SKU, no generated-file edits).
- **scope (files):** NEW
  `candidates/adult-novels/ultramarine/book3/<title-slug>.md` (the complete
  manuscript, single combined file mirroring Book 2's
  `book2/the-blue-and-the-white.md`); NEW
  `candidates/adult-novels/ultramarine/book3/outline.md` (chapter outline +
  closing/forward hook, written first and drafted to); NEW
  `candidates/adult-novels/ultramarine/book3-cover-brief.md`; NEW
  `candidates/adult-novels/ultramarine/book3-listing.md`; NEW
  `candidates/adult-novels/ultramarine/kdp-ready/book-3/` 3-file package
  (`MANUSCRIPT-KDP.md`, `KDP-METADATA.md`, `SELF-EDIT-PASS.md`) mirroring
  `kdp-ready/book-2/` structure; APPEND
  `candidates/adult-novels/ultramarine/DECISIONS.md` (Book-3 decisions); NEW
  `control/claims/claude-ultramarine-book3.md`. This card. Property content +
  prep only; no SKU, no publish surface, no OWNER-QUEUE row, no generated file
  touched (`.substrate/guard-fires.jsonl` left unstaged to keep the diff scoped).

## Work log

- 2026-07-20 — Isolated worktree; branch `claude/ultramarine-book3` from
  `origin/main` (`1fdbc4f`). Baseline `bootstrap.py check --strict` EXIT 0 (2
  seat-digest + 5 model-line advisories pre-existing, non-gating). Ground: read
  the series `bible/` (style/world/characters + `book2-additions.md`), Book 2's
  `outline.md` and full manuscript ending (the ch. 12 VOC-order hook), the
  `book2-cover-brief.md` / `book2-listing.md`, and the `kdp-ready/book-2/`
  3-file package (format to mirror byte-for-byte). Confirmed the exact hook to
  pay and the continuity fixed by `book2-additions.md` (no true ultramarine
  left in Clara's hands; goldfinch panel held in trust, not owned; Grietje's
  five bright things; cobalt supply outside Doncker's lapis network). Born-red
  card + claim committed (first commit).

## 💡 Session idea

💡 **A `series-close-marker` advisory that flags when a multi-book property's
final volume plants a *forward* hook it never means to pay.** This series runs
on planted hooks (Book 1 → Book 2 → Book 3), and each sequel's job is to pay the
prior book's hook. But the *last* book of a trilogy inverts the rule: it must
*resolve*, and any forward hook it plants is decorative (a "the trade goes on"
gesture), not a promissory note for a Book 4 nobody will write. Today nothing
distinguishes "hook the next book pays" from "closing note that is deliberately
never paid" — a future automated hook-chain checker (see the night-kiln
`series-hook-chain` idea) would wrongly nag a trilogy-closer's organic final
image as an *unpaid tail hook* forever. Recipe: give each series a
`series-arc.md`/DECISIONS marker (`closes-trilogy: true` or a `# Series close`
block) that the hook-chain scan reads to treat the terminal book's forward note
as **intentionally-open**, not owed — the natural complement to the
book-N-pays-book-(N−1) invariant, so a finished series telemeters as *complete*
rather than as one perpetual dangling hook.

## previous-session review

previous-session review: the immediately-prior card for this property,
`2026-07-19-ultramarine-book2.md` (Book 2, *The Blue and the White*), executed
exactly the discipline this slice needs — a genuine bible-grounded literary
sequel (not a reboot) written to a fresh outline drafted first, honest `wc -w`
(22,079), the born-red→complete card ritual, family-level model attribution, and
a scoped diff that left every generated/owner-gated surface untouched
(`control/status.md`, SKU registry, OWNER-QUEUE, `.substrate/guard-fires.jsonl`
all clear). It also logged the Book-2 canon I must honour verbatim in
`bible/book2-additions.md` (goldfinch held in trust; no true ultramarine left;
Grietje's five bright things; cobalt outside Doncker's network) and planted the
precise ch.-12 VOC-order hook this book pays. I carry its landing recipe forward
here (born-red card + claim first, content second, flip last; no
`control/status.md` touch; guard-fires unstaged) and extend its own 💡
(retire the `long-form fiction drafting` model-line friction at the taxonomy
level) with a trilogy-close marker so a *finished* series stops reading as an
unpaid dangling hook.
