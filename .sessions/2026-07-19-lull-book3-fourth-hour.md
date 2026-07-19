# Session — Lull Book 3: The Fourth Hour Comes (complete draft, trilogy finale)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · long-form fiction drafting
- **started (date -u):** Sun Jul 19 17:23 UTC 2026
- **branch:** `claude/lull-book3-fourth-hour`
- **base:** `main@6954e9a`
- **purpose:** Write **Lull · Book Three: The Fourth Hour Comes** as a
  complete, landable manuscript matching Books 1–2's format
  (`candidates/dream-series/`, Percy-Jackson-style MG/YA, confession-frame
  first-person past tense). Owner directive (2026-07-11, via coordinator)
  authorizes autonomous book-building; PUBLISHING stays owner-gated. Book 3 is
  the **finale** — it must RESOLVE the series, not merely deepen it. It executes
  the concluding beats from `series-arc.md` (Book 3 — *The Fourth Hour Comes*):
  the frozen moment of **Pompeii** on the date the nightmare finally names; both
  factions converge in the water; the **Lantern Man's identity** resolved; the
  **confession frame** paid off (who the narrator is confessing to, why it had
  to stay secret, "the thing that made everyone angry"); the **girl who says
  *not yet*** resolved; the **Vigil's exposed forgery** and **Lena's undecided
  allegiance** landed; Sam's lost parent-memories addressed; a genuine ending
  (THE END). No new trilogy-length threads left dangling.
- **deliverable:** a `book3/` dir mirroring `book2/`'s layout — **12 chapter
  files** (`ch01.md`–`ch12.md`, ~23–26k words total, in Books 1–2's chapter
  front-matter and cliff-ended pacing band) forming a COMPLETE manuscript, not
  an outline; a Book-3 outline (`book3/outline.md`); an update to
  `series-arc.md` marking the trilogy **COMPLETE**; a Book-3 cover brief
  (`book3-cover-brief.md`) + listing copy (`book3-listing.md`) matching Book 2's
  formats; a dated `DECISIONS.md` append (D-004: Book 3 title, chapter count,
  word count, how it resolves the arc). No invented sales/reviews.
- **scope (files):** ADD `candidates/dream-series/book3/ch01..ch12.md`,
  `book3/outline.md`, `candidates/dream-series/book3-cover-brief.md`,
  `candidates/dream-series/book3-listing.md`; EDIT
  `candidates/dream-series/series-arc.md` (mark trilogy complete) +
  `candidates/dream-series/DECISIONS.md` (append D-004). Plus this card + the
  claim. Pure repo content: **no SKU registered, no generated file edited, no
  Gumroad/KDP/publish surface, no spend/account action.**
- **guardrails:** born-red card holds substrate-gate red until the completion
  flip. No `derive_owner_queue` run (book content registers no SKU); no
  `docs/publishing/**` or `docs/launch/**` edit; `control/status.md` left to the
  lead's consolidated heartbeat. All new content confined to the
  `candidates/dream-series/` property. `bootstrap.py check --strict` and the
  repo CI (kit-tests + substrate-gate) must pass green (advisories OK) before
  the flip.

## 💡 Session idea

💡 **A `series-manifest` advisory that pins a whole series' aggregate claims to
the sum of its parts.** The Book-2 card floated a `manuscript-manifest` checker
(one book: DECISIONS "N chapters / ~Nk words" vs `ls ch*.md` + `wc -w` vs the
outline's "(drafted)" tags). Landing Book 3 exposes the *next* drift surface up:
`series-arc.md` now asserts a **series total** ("36 chapters, ≈71.8k words") and
carries a per-book status table, while three independent `DECISIONS.md` blocks
(D-002/D-003/D-004) each claim their own book's counts, and each `bookN/outline.md`
header claims a third. Nothing checks that the *series* line equals the *sum of
the books*, or that every book the arc marks "DRAFTED ✅" actually has 12
`chNN.md` on disk. A future session that adds a `book4/`, splits a chapter, or
hand-edits one word-count leaves the series header quietly lying with zero signal.
Recipe: extend the proposed stdlib-only `scripts/check_manuscript_manifest.py`
with a series pass — per `candidates/*/`, (INV-1) re-derive each book's real
chapter count + `wc -w`, (INV-2) sum them, (INV-3) parse the aggregate claim out
of `series-arc.md` and assert `series == Σ books` within a tolerance band, and
(INV-4) assert every book the arc tags DRAFTED resolves to a complete `bookN/`.
Advisory-only (continue-on-error in `kit-tests.yml`, same shape as
`funnel-coverage-advisory`) since a creative property legitimately runs ahead of
its bookkeeping mid-draft; unittest adds a series-sum-mismatch + a
missing-drafted-book catch-case. Anchors: the same new checker + test under
`scripts/`, one added advisory job in `.github/workflows/kit-tests.yml`.

## previous-session review

previous-session review: the direct predecessor in this lane was
`2026-07-19-lull-book2-mirror-city.md` (PR #268, landed today) — it drafted Book 2
*The Mirror City* via the exact born-red card→content→flip recipe this session
reused, and left a clean base: I confirmed `book2/` is present at `origin/main`
(`6954e9a`) before branching, so Book 3 inherited a real, merged middle volume to
build the finale on. Its forward flag (a manuscript-manifest advisory pinning a
book's claims to its files) is still unbuilt and stays live — this card's 💡
extends it one altitude up to the *series* total, which Book 3 is the first slice
to make checkable (the arc now carries a trilogy aggregate). Same lane, same
conventions, opposite of the ENG-3→ENG-9 tooling baton: pure
`candidates/dream-series/` content, no guard added, no footgun removed, riding
green past every storefront guard by construction (they exclude the property).

## Work log

- 2026-07-19 — Branch `claude/lull-book3-fourth-hour` from `origin/main`
  (`6954e9a`, which includes PR #268 / `book2/`); clean base confirmed.
  Grounded in `series-arc.md`, `bible/` (names + world), `DECISIONS.md`, ALL of
  `book1/` (12 ch, ~25.7k words) and ALL of `book2/` (12 ch, ~23.3k words),
  outlines + direction pointers, and the substrate card/claim/gate conventions.
  Born-red card + claim committed as first commit (`51829db`), pushed, PR #271
  opened READY. Drafting begins.
- 2026-07-19 — Content commit (`374d8ce`): complete Book-3 manuscript
  (`book3/ch01.md`–`ch12.md`, 12 chapters, ~22.8k words) + `book3/outline.md` +
  `book3-cover-brief.md` + `book3-listing.md`; `series-arc.md` marked "TRILOGY
  COMPLETE"; `DECISIONS.md` D-004 appended. Finale resolves every open thread
  (the Lantern Man, the girl who says *not yet* / Vibia, the Vigil's forgery,
  Lena's allegiance, Sam's lost parent-memories, the confession frame) and ends
  the trilogy (THE END). Pure `candidates/dream-series/` content — no SKU, no
  generated-file edit, no publish/spend surface, no `control/status.md` touch
  (left to the lead).
- 2026-07-19 — Verify pre-flip: `python3 bootstrap.py check --strict` = the
  born-red HOLD ONLY (2 unresolved `[[fill:]]` slots + in-progress Status on THIS
  card); all other findings are pre-existing non-gating advisories on `main`
  (seat-digest stale/over-budget; model-line class on other cards). Repo CI test
  line green on the live tree: `python3 -m unittest` across membership-kit
  (36 tests OK), stripe-webhook-test-kit (14 OK), github-webhook-test-kit
  (18 OK) = 68 tests OK. A content-only PR under `candidates/dream-series/` is
  out of scope for every storefront guard by construction.
- 2026-07-19 — Flip to `complete` (this commit): Status badge → complete, the two
  `[[fill:]]` slots resolved (one 💡 idea — a series-manifest advisory extending
  Book 2's manuscript-manifest to the trilogy total — + the previous-session
  review of the Book-2 card), `📊 Model:` line already present, guard-fire ledger
  delta committed (do not revert). Born-red HOLD clears; this last commit releases
  auto-merge.
