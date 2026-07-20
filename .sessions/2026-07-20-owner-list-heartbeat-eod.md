# Session — Owner list + heartbeat end-of-day refresh (2026-07-20)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · owner-list + heartbeat refresh

- **started (date -u):** Mon Jul 20 04:54 UTC 2026
- **branch:** `claude/owner-list-heartbeat-eod`
- **base:** `main@3bb962b`
- **purpose:** land the end-of-day owner-facing refresh reflecting today's
  landed work (#277 distribution submission pack, #278 Ultramarine Book 3 *The
  Common Blue*, #279 Night Kiln Book 6 *The Summer Ember*). Three neutral,
  hand-maintained surfaces move: **(1)** `docs/publishing/OWNER-START-HERE.md`
  gains the **one-paste distribution submission pack** as a new zero-cost
  quick-win step (the direct answer to the funnel diagnostic's "traffic is the
  binding constraint" read) and adds the two new books to the existing KDP-upload
  book step, keeping its proofread gate; **(2)** `docs/current-state.md` is
  restamped to the new HEAD with the corrected product/book counts (Ultramarine
  now a **complete 3-book trilogy**, Night Kiln now **6 books**) and the
  submission pack noted as the new distribution asset; **(3)** `control/status.md`
  heartbeat is overwritten LAST as neutral prose pointers only. Pure
  docs/orientation refresh; **publishing stays owner-gated** (no publish, no
  Gumroad/KDP action, no SKU, no generated-file edits — OWNER-START-HERE is the
  hand-maintained curated companion, not the generated OWNER-QUEUE).
- **scope (files):** UPDATE `docs/publishing/OWNER-START-HERE.md` (submission-pack
  quick-win step + two new books in the book step); UPDATE
  `docs/current-state.md` (restamp to HEAD `3bb962b`, book/product counts,
  submission-pack asset); OVERWRITE `control/status.md` (neutral heartbeat,
  pointers only, NO routine/trigger state); NEW
  `control/claims/owner-list-heartbeat-eod.md`. This card. Docs + orientation
  only; no SKU, no publish surface, no OWNER-QUEUE row, no generated file, no
  scripts/ touched.

## Work log

- 2026-07-20 — Isolated worktree; branch `claude/owner-list-heartbeat-eod`
  hard-synced to `origin/main` (`3bb962b`, Night Kiln Book 6), which carries
  today's #277/#278/#279. Ground: confirmed OWNER-START-HERE.md is the
  **hand-maintained** curated companion (the generated file is OWNER-QUEUE.md via
  `scripts/derive_owner_queue.py`; `check_owner_queue_staleness.py` INV-1 only
  asserts the companion's `D<n>`/`§N` cross-refs still resolve into the queue — so
  the refresh adds no new D-refs). Read the submission pack index
  (`docs/launch/submissions/README.md`, 11 paste-and-post channel files) and the
  two new `kdp-ready/book-N/` packages. Born-red card + claim = first commit.
  Build begins.
- 2026-07-20 — Content commits. **OWNER-START-HERE.md** (hand-maintained; edited
  directly — the generated file is OWNER-QUEUE.md via
  `scripts/derive_owner_queue.py`, untouched): added a new **Section 2 / Step 2
  "Free distribution"** — post each of the four free lead magnets in one paste
  from `docs/launch/submissions/README.md`, framed as the zero-cost,
  seat-independent fix for the funnel diagnostic's binding distribution
  constraint; renumbered the following sections/steps (2→3 … 4→5; Steps 2–7 → 3–8)
  and the one internal self-ref (`§4, Step 7` → `§5, Step 8`); added the two new
  books to the book step (now **Step 8**) — *The Common Blue* (Ultramarine Bk 3,
  trilogy finale) and *The Summer Ember* (Night Kiln Bk 6), each with its
  `kdp-ready/book-N/` path, five→seven counts, dropped the now-stale "finale" tag
  on Night Kiln Bk 5, proofread gate kept. Verified with
  `python3 scripts/check_owner_queue_staleness.py` (exit 0 — companion cross-refs
  still resolve, INV-1/2/3 hold) and `check_owner_queue_idempotent.py` (exit 0 —
  queue byte-identical). **current-state.md**: restamped to HEAD `3bb962b` /
  #277–#279; Night Kiln now a 6-book series, Ultramarine a complete 3-book Delft
  trilogy, KDP-ready packages 5→7, submission pack added as the new distribution
  asset, Recently-shipped updated. Committed `6dfdc7c` (owner list), `b238272`
  (current-state).
- 2026-07-20 — Heartbeat: overwrote `control/status.md` LAST (neutral prose +
  read-path pointers only; NO trigger/cron/routine/session-binding state — that
  class is classifier-walled here), restamped to HEAD `3bb962b`, kit `v1.17.0`,
  strict green. Committed `ff4907a`. Pre-flip `bootstrap.py check --strict` red on
  the **born-red HOLD only** (3 `[[fill:]]` slots + in-progress Status — the
  checker labels it "HOLD (by design)… nothing to investigate"); no guard reds, no
  D-ref/staleness/catalog guard, advisories pre-existing/non-gating. Then flip to
  `complete` (this commit): Status flipped, three `[[fill:]]` slots resolved, four
  byte-markers present (`**Status:**`, `📊 Model:`, `💡`, `previous-session
  review`); re-ran strict → EXIT 0. Guard-fires ledger left unstaged to keep the
  diff scoped.

## 💡 Session idea

💡 **An advisory that guards `OWNER-START-HERE.md`'s OWN internal section/step
numbering and self-references** — the exact renumber-drift class I navigated by
hand this session. `check_owner_queue_staleness.py` INV-1 already guards the
companion's *outbound* cross-refs (its `D<n>` / `§N` pointers INTO the generated
OWNER-QUEUE), but nothing guards the companion's *internal* consistency: I
inserted one new section and had to renumber eight `### Step N` headers, five
`## N.` section headers, and one in-body self-ref (`§4, Step 7 above` → `§5,
Step 8 above`) entirely by discipline. One missed edit and the digest silently
sends a non-technical owner to a step that moved. Guard recipe: add a fourth
invariant to `scripts/check_owner_queue_staleness.py` (new `check_companion_selfrefs`
alongside `check_companion_crossrefs`, wired into `main()` + itemized findings)
that parses the companion's `^##\s+(\d+)\.` and `^###\s+Step\s+(\d+)` headers,
asserts each sequence is gap-free and strictly monotonic, and asserts every
in-body "§N" / "Step N above" self-ref on a line that does NOT name OWNER-QUEUE
resolves to a real header in the same file (reuse the existing `COMPANION_SREF_RE`;
exclude OWNER-QUEUE-naming lines exactly as INV-1 does). Test target: a new
fixture case in `scripts/test_check_owner_queue_staleness.py` with a deliberately
gap/renumber-broken companion. It is the natural sibling of INV-1 — companion→queue
already guarded, companion→itself is the open hole.

## previous-session review

previous-session review: the newest prior card
`2026-07-20-night-kiln-book6.md` (Night Kiln Book 6, *The Summer Ember*, one of
today's #279) is a **content** slice where mine is the **orientation** slice that
surfaces it to the owner — its finished KDP package under
`candidates/adult-novels/the-night-kiln/kdp-ready/book-6/` is exactly what I
added to OWNER-START-HERE's book step and counted in current-state. It reused the
born-red-card → content-commits → flip landing recipe I followed here (Status
in-progress first commit, `[[fill:]]` slots resolved and four byte-markers
confirmed at flip, `bootstrap.py check --strict` red on the born-red HOLD only
then EXIT 0), and it carefully kept `control/status.md` untouched to stay scoped —
my slice is the counterpart that DOES own the heartbeat, so I overwrote
`control/status.md` last, kept it to neutral prose + pointers, and deliberately
excluded all routine/automation state (the classifier-walled class). Its 💡
(a `catechism-drift` byte-equality advisory) and mine (a companion
section/step-numbering advisory) name the same footgun from opposite ends of the
repo — a hand-maintained invariant silently drifting from its own text — which is
why both are framed as tiny, non-gating siblings of an existing guard rather than
new hard walls.
