# Session — The Night Kiln, Book 6 (The Summer Ember)

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · high · Night Kiln Book 6 novella

- **started (date -u):** Mon Jul 20 04:19 UTC 2026
- **branch:** `claude/night-kiln-book6`
- **base:** `main@1fdbc4f`
- **purpose:** write a genuine cozy sequel — **The Night Kiln, Book 6** — as
  landable, upload-ready repo content, fulfilling the book-6 hook planted in
  Book 5's closing pages (the cold far-side kiln: Stonebeck once had a fire of
  its own, fallen and dead thirty years and more, and a single pot come down in
  Brida's family that "holds something" but has had no witch to hear it in a
  lifetime — *"could a fire on this side ever hear what a dead fire on that side
  kept — can a keeping wait longer than the witch who made it?" / "that's a
  summer story."* — flagged as a **young witch's crossing, Perrin's**, over the
  water the other way). A complete finished manuscript in the series
  voice/format (close third on Edda, past tense, byte-identical rule-sentence
  opening, catechism byte-identical near the close, `⁂` scene breaks, 12
  chapters / 3 implicit acts, ~16k band), honouring the "one fired vessel per
  book" engine and the cozy/low-stakes register — no genre shift, no darkness
  creep, **no fifth temper** (keep/take/give/mend stays closed; the new twist is
  a RULE, not a power). Pure repo content; **publishing stays owner-gated** (no
  publish, no Gumroad/KDP action, no SKU, no generated-file edits).
- **scope (files):** NEW `candidates/adult-novels/the-night-kiln/en/the-summer-ember.md`
  (the manuscript); UPDATE `candidates/adult-novels/the-night-kiln/series-arc.md`
  (Book-6 entry + hook chain [Book-5→6 marked WRITTEN] + Book-6→7 hook plant +
  continuity anchors); NEW `candidates/adult-novels/the-night-kiln/book-6-cover-brief.md`;
  NEW `candidates/adult-novels/the-night-kiln/book-6-listing.md`; NEW
  `candidates/adult-novels/the-night-kiln/kdp-ready/book-6/` 3-file package
  (`MANUSCRIPT-KDP.md`, `KDP-METADATA.md`, `SELF-EDIT-PASS.md`); APPEND
  `candidates/adult-novels/the-night-kiln/DECISIONS.md`; NEW
  `control/claims/night-kiln-book6.md`. This card. Property content + prep only;
  no SKU, no publish surface, no OWNER-QUEUE row, no generated file touched.

## Work log

- 2026-07-20 — Isolated worktree; branch `claude/night-kiln-book6` from
  `origin/main` (`1fdbc4f`), which carries Books 1–5 and the five KDP-ready
  packages. Ground: read Book 5 (`en/the-spring-cup.md`) whole + skimmed Books
  1–4 for voice; `series-arc.md` (Hook chain + Book-5→6 hook), `DECISIONS.md`,
  `LENGTH-BAND-PREP.md`, the `book-5-*` cover/listing files, the
  `kdp-ready/book-5/` package, and the Book-5 session card. Confirmed the planted
  Book-6 hook in Book 5 ch. 12 (the cold far Stonebeck kiln; the single unheard
  Alder pot; "a summer story"; a young witch's crossing the other way). Copied
  the five inherited catechism lines **byte-for-byte** from `the-spring-cup.md`
  (L325–333) rather than retyping; house style verified (straight ASCII quotes
  U+0027/U+0022, em-dash U+2014, `⁂` breaks). Born-red card + claim = first
  commit. Build begins.

## 💡 Session idea

💡 **A `catechism-drift` advisory that verifies the series' byte-locked refrain
stays byte-identical across every `en/*.md` in a Night-Kiln-shaped property.**
The whole engine leans on one hard invariant — the catechism recital must be
**byte-identical** book to book, each new book appending exactly one line — and
that invariant is currently defended entirely by the writer's discipline of
grepping the previous book and copying verbatim (which is exactly what I did:
`sed -n '325,333p' the-spring-cup.md`). It is one fat-fingered em-dash (U+2014 →
hyphen) or one curly apostrophe away from a silent, permanent divergence that no
reader-facing check would ever catch. A tiny advisory (never exit-affecting,
same class as seat-digest/model-line) could, for each property under
`candidates/adult-novels/*` with ≥2 `en/*.md`, extract each book's closing
italic recital block, normalise nothing, and flag when book N's first *k* lines
are not byte-equal to book N−1's — catching drift the instant it lands. It is the
natural third sibling of Book 4's proposed `series-editions-drift` and Book 5's
proposed `series-hook-chain` advisories: same "a hand-maintained series
invariant silently drifts from its own prior text" shape, applied to the refrain
that the whole property is built on.

## previous-session review

previous-session review: the immediately-prior same-property card
`2026-07-19-night-kiln-book5.md` (Book 5, *The Spring Cup*) is the natural
predecessor and the template I mirrored end to end — same born-red landing
recipe, same "pure property content + prep, publishing owner-gated" discipline
(cover/listing stored as property-local files; SKU registry, vetting packet
OWNER-GATE, and every generated file left untouched; guard-fires ledger left
unstaged to keep the diff scoped; `control/status.md` untouched). It paid the
Book-4 hook and planted the exact Book-6 hook this slice pays, so its close-out
is my spec: the cup stilled on the shelf, the two witches now at the kiln, the
young-witch's-crossing flagged for a summer story. Its 💡 (a `series-hook-chain`
advisory) and Book 4's 💡 (`series-editions-drift`) both name the same footgun —
hand-maintained series invariants drift from the manuscripts — which my own 💡
above extends from the hook chain to the byte-locked catechism itself.
