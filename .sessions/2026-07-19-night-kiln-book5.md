# Session — The Night Kiln, Book 5 (The Spring Cup)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · long-form fiction drafting

- **started (date -u):** Sun Jul 19 18:00 UTC 2026
- **branch:** `claude/night-kiln-book5`
- **base:** `main@9b9129c`
- **purpose:** write a genuine cozy sequel — **The Night Kiln, Book 5** — as
  landable repo content, fulfilling the book-5 hook planted in Book 4's closing
  pages (the unclaimed wedding cup that hums on the private shelf; a granddaughter
  who "inherited the not-happening" of a wedding that never was and thinks of it
  every spring — *"could a fire ever fire a thing that never happened at all?" /
  "that's a spring story."*). A complete finished manuscript in the series
  voice/format (close third on Edda, past tense, 12 chapters, ~16k band),
  honouring the "one fired vessel per book" engine and the cozy/low-stakes
  register — no genre shift, no darkness creep, no fifth temper (the
  keep/take/give/mend set stays closed; the new twist is a RULE, not a power).
  Pure repo content; **publishing stays owner-gated** (no publish, no Gumroad/KDP,
  no SKU, no generated-file edits).
- **scope (files):** NEW `candidates/adult-novels/the-night-kiln/en/the-spring-cup.md`
  (the manuscript); UPDATE `candidates/adult-novels/the-night-kiln/series-arc.md`
  (Book-5 entry + hook chain + Book-6 hook plant + continuity anchors); NEW
  `candidates/adult-novels/the-night-kiln/book-5-cover-brief.md`; NEW
  `candidates/adult-novels/the-night-kiln/book-5-listing-copy.md`; APPEND
  `candidates/adult-novels/the-night-kiln/DECISIONS.md`; NEW
  `control/claims/night-kiln-book5.md`. This card. Property content + prep only;
  no SKU, no publish surface, no OWNER-QUEUE row, no generated file touched.

## Work log

- 2026-07-19 — Isolated clone; branch `claude/night-kiln-book5` from
  `origin/main` (`9b9129c`), which carries Book 4 (`en/the-winter-wheel.md`).
  Ground: read Books 1–4 (`en/*.md`), `series-arc.md`, `DECISIONS.md`,
  `bootstrap.py` card/claim mechanics, `docs/conventions.md`. Confirmed the
  planted Book-5 hook in Book 4 ch. 12 (the humming wedding cup; the granddaughter
  who inherited the not-happening; "a spring story"). Born-red card + claim
  committed (first commit), pushed; PR opened READY. Build begins.
- 2026-07-19 — Wrote the manuscript: `en/the-spring-cup.md`, honest `wc -w` =
  **15,568**, 12 chapters, THE END — in the series voice (close third on Edda,
  past tense, byte-identical rule-sentence opening, catechism advanced to "three
  lines more", `⁂` scene breaks). Spine pays the Book-4 hook exactly: Brida of
  Stonebeck crosses the spring flood to ask if the fire can fire a wedding that
  never was; the answer is a gentle no (the fire keeps only the *true*), but the
  humming cup holds a *true love* — Nesta Alder & Elias Wick, sundered thirty years
  ago by a flood and two liars' wrong words, recovered via Ilsabet's seventh ledger
  + Elias's kept letter; given-back (cup stills for good) and paired into a new cup
  the granddaughter carries home. Firing is a **new asking of the closed
  keep/take/give/mend set** (a keep borrowing a give-back's opening + a carry's
  bringing to pair two true halves), **not** a fifth temper. New catechism line is a
  truth/keeping rule, byte-consistent at all three occurrences: *"…the fire keeps
  the love, not the loss."* Added `series-arc.md` update (Book-5 row + spine +
  Book-4→5 marked PAID + Book-5→6 hook planted [the cold far-side Stonebeck kiln; a
  summer story] + refreshed continuity anchors), `book-5-cover-brief.md`,
  `book-5-listing-copy.md`, and a dated `DECISIONS.md` entry (model family-level
  "Claude Opus"). Content committed (`85f19d3`), pushed. Diff carries only the 5
  intended property files (+ card + claim); no SKU, no generated file, no publish
  surface.
- 2026-07-19 — Verified pre-flip: `bootstrap.py check --strict` red on the
  **born-red HOLD only** (in-progress Status + 5 auto-draft `[[fill:]]` slots — the
  designed hold; the checker itself labels it "HOLD (by design)… nothing to
  investigate"); no guard reds, no other errors; advisories pre-existing/non-gating
  (2 seat-digest, 5 model-line). CI test suites run locally in their working-dirs
  all green: membership-kit 36, stripe-webhook 14, github-webhook 18,
  owner-click-queue 38 — all OK.
- 2026-07-19 — Flip to `complete` (this commit): Status badge flipped, 📊 Model
  line kept (family-level "Claude Opus"), one 💡 idea, previous-session review, all
  `[[fill:]]` slots resolved. Re-ran `bootstrap.py check --strict` → EXIT 0; born-red
  HOLD clears. Did NOT touch `control/status.md`; guard-fires ledger left unstaged
  to keep the diff scoped.

## 💡 Session idea

💡 **A `series-hook-chain` advisory that verifies each cozy-series property keeps its
planted-hook chain honest.** The Night Kiln runs on a strict engine — every book
plants the next book's hook, and the next book's DECISIONS/series-arc must mark that
hook **PAID** while planting exactly one new (unwritten) tail hook. This is enforced
entirely by hand right now: I paid the Book-4 hook, flipped its `series-arc.md` entry
from *(Planted; unwritten.)* to *(PAID in Book 5.)*, and planted Book-5→6 — all
manual, all easy to forget or half-do (e.g. ship Book N without marking Book N−1's
hook paid, or plant two tails, or plant none). A tiny advisory (never exit-affecting,
same class as the seat-digest/model-line warnings) could, for each property under
`candidates/adult-novels/*` with a `series-arc.md`, parse the "Hook chain" block and
flag when: (a) the newest book's inbound hook is still marked planted/unwritten
though a manuscript for that book now exists in `en/`, or (b) the chain has zero or
more-than-one unpaid tail hook. It's the natural sibling of Book 4's proposed
`series-editions-drift` advisory (#269 card) — same "a hand-maintained series
invariant silently drifts from the actual manuscript count" shape, applied to the
hook chain instead of the edition specs.

## previous-session review

previous-session review: the immediately-prior card `2026-07-19-night-kiln-book4.md`
(Book 4, same property, same day) modelled the exact discipline this slice needed —
pure property content + prep, storing cover/listing as property-local files and
leaving the vetting packet's OWNER-GATE, the SKU registry, and every generated file
untouched; I carried that discipline forward here (no publish surface, no generated
edit, guard-fires left unstaged, `control/status.md` untouched) and reused its
born-red landing recipe verbatim, so the one thing its own 💡 flagged (hand-maintained
series artifacts drift from their sources) is exactly what my 💡 above extends from
edition specs to the hook chain.
