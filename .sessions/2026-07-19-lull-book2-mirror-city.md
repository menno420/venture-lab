# Session — Lull Book 2: The Mirror City (complete draft)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model-line]]
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
  files** (`ch01.md`–`ch12.md`, ~25k words total, matching Book 1's chapter
  front-matter and cliff-ended pacing) forming a COMPLETE manuscript, not an
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

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-19 — Branch `claude/lull-book2-mirror-city` from `origin/main`
  (`3802bdb`); clean base confirmed. Grounded in `series-arc.md`, `bible/`
  (names + world), `DECISIONS.md`, all of `book1/` (12 chapters, ~25.7k
  words), `book1/outline.md` + `part2-direction.md`, and the substrate
  card/claim/gate conventions. Born-red card + claim committed as first commit
  ([[fill:card-sha]]), pushed. PR [[fill:pr]] opened READY. Drafting begins.
