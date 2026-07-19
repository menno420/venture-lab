# Session — KDP-ready packages, 5 new book sequels (kdp-ready-5-books)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · feature build

- **started (date -u):** Sun Jul 19 20:44 UTC 2026
- **branch:** `claude/kdp-ready-5-books`
- **base:** `main@2be4065`
- **purpose:** Ship KDP-ready packages for the 5 new book sequels (#268–#272):
  compiled upload-ready manuscript + paste-ready KDP metadata + logged self-edit
  pass per book. Turns five just-merged sequels (which shipped with only
  listing-copy + cover briefs, and — for the two Lull books — 12 separate chapter
  files) into folders an owner can actually upload from. **Publishing stays
  owner-gated:** no publish, no SKU, no generated-file edits, no touch to the
  canonical manuscript sources.
- **scope (files):** NEW, all under new nested `kdp-ready/` folders (guard-neutral —
  not `dist/`):
  `candidates/adult-novels/the-night-kiln/kdp-ready/book-4/` (Winter Wheel),
  `candidates/adult-novels/the-night-kiln/kdp-ready/book-5/` (Spring Cup),
  `candidates/adult-novels/ultramarine/kdp-ready/book-2/` (The Blue and the White),
  `candidates/dream-series/kdp-ready/book-2/` (Lull — The Mirror City),
  `candidates/dream-series/kdp-ready/book-3/` (Lull — The Fourth Hour Comes) —
  each with `MANUSCRIPT-KDP.md` + `KDP-METADATA.md` + `SELF-EDIT-PASS.md` (15 files).
  This card. No SKU, no publish surface, no OWNER-QUEUE row, no generated file,
  no canonical-source edit.

## Work log

- 2026-07-19 — Born-red card committed first on branch `claude/kdp-ready-5-books`
  from `main@2be4065` (this commit). Ground: read the prep worker's `source-pack.md`
  (landing toolchain §0/§10, KDP exemplar, per-book packages, guard analysis), the
  `.sessions/README.md` born-red rules, and the Book-4/Book-5 exemplar cards. Baseline
  `bootstrap.py check --strict` established green (guards clean; only pre-existing
  seat-digest + model-line advisories). PR to be opened READY next; then per-book
  package commits.
- 2026-07-19 — Landed the 5 KDP-ready packages, one commit per book, bodies
  preserved **byte-for-byte** from the canonical sources (verified via
  `git hash-object` blob-SHA equality on every pushed file, not a re-typed copy):
  - **Bk4 The Winter Wheel** (Night Kiln) — compiled manuscript **16,024w**.
  - **Bk5 The Spring Cup** (Night Kiln) — compiled manuscript **16,101w**.
  - **Ultramarine Bk2 The Blue and the White** — compiled manuscript **22,617w**.
  - **Lull Bk2 The Mirror City** — 12 chapter files (`ch01`–`ch12`) assembled into
    one upload-ready file with prepended front matter, **24,001w**.
  - **Lull Bk3 The Fourth Hour Comes** — 12 chapter files assembled likewise,
    **23,431w**.
  Each package pairs the manuscript with a paste-ready `KDP-METADATA.md` (title/
  subtitle/series, blurb, 7 keywords, categories, KU/price band, author placeholder)
  and a logged `SELF-EDIT-PASS.md`. Self-edits found **near-zero mechanical typos**
  across all five and flagged continuity items for the owner's native-speaker
  proofread rather than silently "fixing" prose — e.g. a Night Kiln Bk5
  glaze-chemistry contradiction, and a Lull keyword-map §3 genre mis-scope (the
  reserved "quiet literary novella" niche does not match the actual MG portal-fantasy
  books). This pass explicitly does **not** replace that professional proofread.
- 2026-07-19 — **Decide-and-flag choices logged:** (1) output folder named
  `kdp-ready/` (nested, guard-neutral — deliberately **not** `dist/`, which would trip
  `check_built_registered.py` by marking the parent a built SKU); (2) keyword-map §3
  reservations + reconciliation and the five missing vetting packets are **deferred to
  an owner follow-up** — not created here, so `derive_owner_queue.py` / OWNER-QUEUE.md
  stay untouched and idempotent; (3) canonical manuscript sources
  (`en/*.md`, `book2/*.md`, `dream-series/book{2,3}/ch*.md`) left **untouched** — the
  compiled files are additive copies.
- 2026-07-19 — **CLOSE (closer worker).** Resumed a partially-landed branch: the
  Night Kiln Bk4/Bk5 + Ultramarine Bk2 packages (9 files) were already committed,
  but the two Lull packages (`dream-series/kdp-ready/book-2` + `book-3`, 6 files)
  were not yet on the branch. Committed the 6 missing files (one commit per book,
  raw UTF-8 via `push_files`) and confirmed **all 15** KDP-ready package files are
  now present, each verified **byte-for-byte** by `git hash-object` blob-SHA equality
  against the canonical working-tree sources (Lull Bk2 manuscript `4f9c7f6`, Bk3
  `52955bc`, etc.). Cleared the "behind" stall with GitHub's **Update branch**
  (clean merge of latest `main` into the branch — no conflict; #275's
  `docs/publishing/*` + `.sessions/*` changes are disjoint from `candidates/`).
  Guards green; only pre-existing advisories. Flip to `complete`: Status badge,
  📊 Model line, one 💡 idea, previous-session review all present — born-red hold
  released as the final commit.

## 💡 Session idea

💡 **A reusable `kdp-ready/` compile convention + a small `make-kdp-ready` generator
that assembles chapter-split manuscripts into upload-ready single files.** This
session had to do the Lull assembly by hand: concatenate `dream-series/book2/ch01.md`
… `ch12.md` in order, drop the per-chapter `*Lull, Book N · draft*` sublines, and
prepend an exemplar-style front-matter block (CAPS title → italic subtitle → logline
blockquote → `---` → **Content note:** → `---`). That is a deterministic transform
begging for a script. A `scripts/make_kdp_ready.py <property> [--book N]` could, for
any property, read either a single `en/*.md` manuscript or an ordered `chNN.md` set,
strip draft sublines, splice in front/back matter (pulled from the property's
`*-cover-brief.md` / `*-listing-copy.md`), and emit
`candidates/<prop>/kdp-ready/book-N/MANUSCRIPT-KDP.md` byte-deterministically — so the
whole catalog can be made KDP-ready on demand and re-generated when a source changes,
instead of five workers hand-compiling. It is the natural sibling of the Night Kiln
cards' `series-editions-drift` / `series-hook-chain` advisories (#269/#272): same
"derived artifact should be generated from, and stay honest against, its source" shape
— here applied to the upload build rather than a drift check. Guard-neutral by
construction (writes only under nested `kdp-ready/`, never `dist/`).

## previous-session review

previous-session review: the immediately-prior card `2026-07-19-night-kiln-book5.md`
(The Spring Cup, #272) was an honest, disciplined close-out — it paid the Book-4 hook
exactly, kept the keep/take/give/mend engine closed (a new *rule*, not a fifth
temper), reported a truthful `wc -w`, and correctly left the SKU registry, the vetting
packet's OWNER-GATE, and every generated file untouched, storing cover/listing as
property-local files. I carried that same discipline into the landing here: additive
`kdp-ready/` copies only, canonical sources and every owner-gated/generated surface
untouched, and the keyword-map reservation + vetting packets it deliberately deferred
are the same follow-ups I flag rather than force.
