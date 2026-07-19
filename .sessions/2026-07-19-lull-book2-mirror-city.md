# Session — Lull Book 2: The Mirror City (complete draft)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · long-form fiction drafting
- **started (date -u):** Sun Jul 19 16:40 UTC 2026
- **branch:** `claude/lull-book2-mirror-city`
- **base:** `main@3802bdb`
- **purpose:** Write **Lull · Book Two: The Mirror City** as a complete,
  landable manuscript matching Book 1's format (`candidates/dream-series/`,
  Percy-Jackson-style MG/YA, confession-frame first-person past tense). Owner
  directive (2026-07-11, via coordinator) authorizes autonomous
  book-building; PUBLISHING stays owner-gated. Book 2 executes the
  middle-volume beats from `series-arc.md`: train with the Vigil in Venice (a
  mirror-city where the seam never closes), hunt the *place* in Sam's
  nightmare, learn **Anchoring**, discover the Vigil buried a bleed of its own
  ("forged for the greater good" — the crack the Palimpsest exploits), Lena
  returns as half-ally, a betrayal, and — to save someone — Sam makes a bigger
  change than he should, which STICKS (confirms arc-level). Ends on the
  Book-2→Book-3 hook: the nightmare's place is **Pompeii**, and both factions
  stop recruiting him and start fighting *over* him. Middle book = deepen,
  complicate, raise stakes; the series is NOT resolved.
- **deliverable:** a `book2/` dir mirroring `book1/`'s layout — **12 chapter
  files** (`ch01.md`–`ch12.md`, ~23.3k words total, in Book 1's chapter
  front-matter and cliff-ended pacing band) forming a COMPLETE manuscript, not an
  outline; a Book-2 outline (`book2/outline.md`) + a Part-3 direction pointer;
  an update to `series-arc.md` marking Book 2 drafted + confirming the Book-3
  setup; a Book-2 cover brief (`book2-cover-brief.md`); listing copy
  (`book2-listing.md` — blurb + back-cover + keywords + age-range +
  categories); a dated `DECISIONS.md` append (D-003: Book 2 title, chapter
  count, word count, spine, hook into Book 3).
- **scope (files):** ADD `candidates/dream-series/book2/ch01..ch12.md`,
  `book2/outline.md`, `book2/part3-direction.md`,
  `candidates/dream-series/book2-cover-brief.md`,
  `candidates/dream-series/book2-listing.md`; EDIT
  `candidates/dream-series/series-arc.md` (mark Book 2 drafted) +
  `candidates/dream-series/DECISIONS.md` (append D-003). Plus this card + the
  claim. Pure repo content: **no SKU registered, no generated file edited, no
  Gumroad/KDP/publish surface, no spend/account action.**
- **guardrails:** born-red card holds substrate-gate red until the completion
  flip. No `derive_owner_queue` run (book content registers no SKU); no
  `docs/publishing/**` or `docs/launch/**` edit; `control/status.md` left to
  the lead's consolidated heartbeat. All new content confined to the
  `candidates/dream-series/` property. `bootstrap.py check --strict` and the
  repo CI (kit-tests + substrate-gate) must pass green (advisories OK) before
  the flip.

## 💡 Session idea

💡 **A `manuscript-manifest` advisory that pins a drafted book's DECISIONS/outline
claims to the files on disk.** This slice makes three independent claims about the
same manuscript that can silently drift apart: `DECISIONS.md` D-003 states "12
chapters, ~23.3k words"; `book2/outline.md` tags each chapter "(drafted)"; and the
actual truth is `ls candidates/dream-series/book2/ch*.md` + `wc -w`. Nothing checks
that they agree — a future session that adds `ch13.md`, or trims a chapter, or
edits the word count in DECISIONS by hand, leaves the other two lying with zero
signal (exactly the DECISIONS-vs-reality drift class the owner-queue guards catch
for the storefront, but for creative property). Recipe: a stdlib-only
`scripts/check_manuscript_manifest.py` that, per `candidates/*/book*/`, (INV-1)
counts `ch*.md` files and re-derives `wc -w`, (INV-2) parses the "N chapters,
~Nk words" claim out of the sibling `DECISIONS.md` decision block and the
`outline.md` header, and (INV-3) asserts every chapter the outline tags
"(drafted)" resolves to an existing `chNN.md` — advisory-only (continue-on-error
in `kit-tests.yml`, same shape as `funnel-coverage-advisory`), since a creative
draft in flight legitimately runs ahead of its bookkeeping; unittest adds a
count-mismatch + a missing-chapter catch-case. Anchors: new checker + test under
`scripts/`, wired as an advisory job in `.github/workflows/kit-tests.yml`.

## previous-session review

previous-session review: the newest sibling cards on 2026-07-19 were a
tooling/hygiene baton (ENG-3→ENG-9 — funnel/owner-queue guards, and ENG-9 retiring
the legacy root `claims/` dir to collapse the two-claim-home ambiguity). Every one
of those either ADDED an enforcement surface or REMOVED a footgun in the substrate
itself. This slice is the opposite lane entirely — it adds no code and no guard,
only creative property under `candidates/dream-series/`, and leans on the born-red
card + one-file-per-claim conventions those very sessions hardened. Confirmed I
inherited a clean base: the ENG-9 delete means there is exactly one claim home
(`control/claims/`), which is where this session's claim landed; and none of the
ENG-4→ENG-8 required guards touch `candidates/dream-series/`, so a pure-content PR
rides green past all of them (verified live, below). One forward flag echoing the
💡: the guards those sessions built pin the *storefront's* claims to reality but
nothing yet pins a *manuscript's* claims to its files — the natural next hygiene
surface if creative property keeps accruing.

## Work log

- 2026-07-19 — Branch `claude/lull-book2-mirror-city` from `origin/main`
  (`3802bdb`); clean base confirmed. Grounded in `series-arc.md`, `bible/`
  (names + world), `DECISIONS.md`, all of `book1/` (12 chapters, ~25.7k
  words), `book1/outline.md` + `part2-direction.md`, and the substrate
  card/claim/gate conventions. Born-red card + claim committed as first commit
  (`62f9c43`), pushed. PR #268 opened READY. Drafting begins.
- 2026-07-19 — Content commit (`c0cedd2`): complete Book-2 manuscript
  (`book2/ch01.md`–`ch12.md`, 12 chapters, ~23.3k words) + `book2/outline.md` +
  `book2/part3-direction.md` + `book2-cover-brief.md` + `book2-listing.md`;
  `series-arc.md` marked "Book 2 drafted"; `DECISIONS.md` D-003 appended. Pure
  `candidates/dream-series/` content — no SKU, no generated-file edit, no
  publish/spend surface, no `control/status.md` touch (left to the lead).
- 2026-07-19 — Verify pre-flip: all six REQUIRED guard checkers PASS on the live
  tree (catalog-dref, owner-queue-idempotence, built-registered, funnel-assets,
  owner-queue-staleness, docs-links); `scripts/` guard + `sku_registry` unittest
  suites = 97 tests OK; `python3 bootstrap.py check --strict` = the born-red HOLD
  ONLY (5 auto-draft slots + in-progress Status), remaining advisories (seat-digest,
  model-line on OTHER cards) pre-exist on `main` and are non-gating. A
  content-only PR is out of scope for every storefront guard by construction
  (they exclude `candidates/dream-series/`).
- 2026-07-19 — Flip to `complete` (this commit): Status badge → complete,
  `📊 Model:` line, one 💡 idea (manuscript-manifest advisory) + guard recipe,
  previous-session review (the ENG-3→ENG-9 tooling baton), all 5 auto-draft
  slots resolved, guard-fire ledger delta committed. Born-red HOLD clears; this
  last commit releases auto-merge.
