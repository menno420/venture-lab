# Session — The Night Kiln, Book 4 (The Winter Wheel)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · long-form fiction drafting

- **started (date -u):** Sun Jul 19 16:39 UTC 2026
- **branch:** `claude/night-kiln-book4`
- **base:** `main@3802bdb`
- **purpose:** write a genuine cozy sequel — **The Night Kiln, Book 4** — as
  landable repo content, fulfilling the book-4 hook planted in Book 3's closing
  pages (Grams Ilsabet's thumb-marked first pot on the private shelf: *"What did
  Grams Ilsabet keep in her own first pot?" / "That's a winter story."*). A
  complete finished manuscript in the series voice/format (close third on Edda,
  past tense, 12 chapters, ~16k band), honouring the "one fired vessel per book"
  engine and the cozy/low-stakes register — no genre shift, no darkness creep.
  Pure repo content; **publishing stays owner-gated** (no publish, no Gumroad/KDP,
  no SKU, no generated-file edits).
- **scope (files):** NEW `candidates/adult-novels/the-night-kiln/en/the-winter-wheel.md`
  (the manuscript); NEW `candidates/adult-novels/the-night-kiln/series-arc.md`
  (outline/series arc + Book-5 hook plant); NEW
  `candidates/adult-novels/the-night-kiln/book-4-cover-brief.md`; NEW
  `candidates/adult-novels/the-night-kiln/book-4-listing-copy.md`; APPEND
  `candidates/adult-novels/the-night-kiln/DECISIONS.md`; NEW
  `control/claims/night-kiln-book4.md`. This card. Property content + prep only;
  no SKU, no publish surface, no OWNER-QUEUE row, no generated file touched.

## Work log

- 2026-07-19 — Isolated clone; branch `claude/night-kiln-book4` from
  `origin/main` (`3802bdb`). Baseline `bootstrap.py check --strict` EXIT 0 (2
  seat-digest + 2 model-line advisories pre-existing, non-gating). Ground: read
  Books 1–3 (`en/*.md`), `DECISIONS.md`, `LENGTH-BAND-PREP.md`, and located the
  planted Book-4 hook (Book 3 ch. 12). Born-red card + claim committed (first
  commit `c41042c`), pushed; PR **#269** opened READY. Build begins.
- 2026-07-19 — Wrote the manuscript: `en/the-winter-wheel.md`, honest `wc -w` =
  **15,580**, 12 chapters, THE END — in the series voice (close third on Edda,
  past tense, byte-identical rule-sentence opening, growing catechism). Spine pays
  the Book-3 hook exactly (Grams Ilsabet's first pot; her orphan-in-the-snow
  backstory and her dead mother's cradle-song, discovered via the ledger and
  re-fired into apprentice Perrin's first pot, making him the fifth witch). Firing
  is a *flitting* (give-back → keep), **not** a fifth temper; the keep/take/give/
  mend set stays closed. New catechism line is a succession/first-pot rule. Added
  `series-arc.md` (arc + hook chain + Book-5 plant — the humming wedding cup),
  `book-4-cover-brief.md`, `book-4-listing-copy.md`, and a dated `DECISIONS.md`
  append (model attributed at family level, "Claude Opus"). Content committed
  (`a71f25c`), pushed. Diff carries only the 5 intended property files (+ card +
  claim); no SKU, no generated file, no publish surface.
- 2026-07-19 — Verified pre-flip: `bootstrap.py check --strict` red on the
  **born-red HOLD only** (in-progress Status + auto-draft slots — the designed
  hold); no guard reds, no other errors; advisories pre-existing/non-gating. CI
  test suites run locally all green (membership-kit 36, stripe-webhook 14,
  github-webhook 18, owner-click-queue 38 — all OK).
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level "Claude Opus"), one 💡 idea, previous-session review, all
  auto-draft slots resolved. Re-ran `bootstrap.py check --strict` EXIT 0 — born-red
  HOLD clears. Did NOT touch `control/status.md` (lead owns the consolidated
  heartbeat); guard-fires ledger left unstaged to keep the diff scoped.

## 💡 Session idea

💡 **A tiny `series-editions-drift` advisory that flags when a property's
`en/*.md` book count outruns the books enumerated in its `versions/*/EDITION-SPEC.md`
files.** The Night Kiln now has **four** EN books, but `versions/omnibus-en/`,
`versions/large-print/`, `versions/audio/`, and the NL editions were all scoped to
Books 1–3 — so the moment a fourth book lands, every derived edition spec is
silently one book stale, and nothing in the substrate notices. The fix mirrors the
existing advisory classes (never exit-affecting): for each property under
`candidates/adult-novels/*`, count the primary-language manuscripts and compare to
the highest "Book N" each `EDITION-SPEC.md`/`NOTES.md` references; emit a
`series-editions-drift` advisory when a manuscript exists with no edition-spec
coverage. It keeps the omnibus/large-print/audio/translation backlog honest
against the actual manuscript count instead of relying on a human to remember,
and it's a natural sibling of the `owner-start-here-stale` freshness checker
(#257 card) — same "derived artifact fell behind its source" shape, applied to the
book catalogue.

## previous-session review

previous-session review: the recent `2026-07-19-owner-steps-refresh.md` card
(#257) built a curated, plain-language one-sitting owner-action list and correctly
refused to hand-edit the GENERATED `OWNER-QUEUE.md`, adding a companion doc that
points *into* the generated source rather than re-transcribing it — the right
instinct for keeping one source of truth. I carried the same "don't touch the
generated/owner-gated surface" discipline here: this slice is pure property
content and prep (manuscript + arc + cover + listing), leaving the vetting
packet's OWNER-GATE checkboxes, the SKU registry, and every generated file
untouched, and storing cover/listing as property-local files rather than editing
the owner-gated `docs/publishing/vetting/` packet. The one thing that card flagged
forward — that hand-maintained artifacts drift against their sources — is exactly
the failure my 💡 above proposes to catch for this property's edition specs.
