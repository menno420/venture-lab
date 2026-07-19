# Session — Ultramarine, Book 2 (The Blue and the White)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · long-form fiction drafting

- **started (date -u):** Sun Jul 19 17:16 UTC 2026
- **branch:** `claude/ultramarine-book2`
- **base:** `main@6954e9a`
- **purpose:** write a genuine literary sequel — **Ultramarine, Book 2 (*The
  Blue and the White*)** — as landable repo content, grounded strictly in the
  existing series `bible/` (style/world/characters) and Book 1's ending. A
  complete finished manuscript in the series voice/format (close third on Clara
  Wijnants, past tense, 12 chapters in three parts, ~22–28k band to match Book
  1's chapter band), continuing the established characters and world (Clara,
  Grietje, Doncker, the unnamed young painter, the surviving goldfinch) into
  Delft's documented economic turn — the collapse of the breweries and the rise
  of the blue-and-white delftware potteries. No reboot; a real sequel that ends
  on a forward hook. Pure repo content; **publishing stays owner-gated** (no
  publish, no Gumroad/KDP, no SKU, no generated-file edits).
- **scope (files):** NEW `candidates/adult-novels/ultramarine/book2/outline.md`
  (the new Book-2 outline, derived from the bible + Book 1's ending); NEW
  `candidates/adult-novels/ultramarine/book2/the-blue-and-the-white.md` (the
  complete manuscript, single combined file mirroring Book 1's
  `manuscript/ultramarine.md`); NEW
  `candidates/adult-novels/ultramarine/book2-cover-brief.md`; NEW
  `candidates/adult-novels/ultramarine/book2-listing.md`; NEW
  `candidates/adult-novels/ultramarine/bible/book2-additions.md` (new canon
  introduced in Book 2); APPEND
  `candidates/adult-novels/ultramarine/DECISIONS.md`; NEW
  `control/claims/ultramarine-book2.md`. This card. Property content + prep only;
  no SKU, no publish surface, no OWNER-QUEUE row, no generated file touched.

## Work log

- 2026-07-19 — Isolated clone; branch `claude/ultramarine-book2` from
  `origin/main` (`6954e9a`). Baseline `bootstrap.py check --strict` EXIT 0 (2
  seat-digest + 4 model-line advisories pre-existing, non-gating). Ground: read
  the full property tree — Book 1 manuscript (`manuscript/ultramarine.md`,
  27,890 words) and its ending, the series `bible/` (style/world/characters),
  `outline.md`, `README.md`, `INTAKE.md`, `DECISIONS.md`, and the serial/NL/
  large-print variants (tone only). Born-red card + claim committed (first
  commit), pushed; PR opened READY. Build begins.
- 2026-07-19 — Wrote the Book-2 outline first (`book2/outline.md`), derived
  strictly from the `bible/` + Book 1's ending, then drafted to it. Wrote the
  complete manuscript `book2/the-blue-and-the-white.md`, honest `wc -w` =
  **22,079**, 12 chapters in three parts, THE END + forward hook — single
  combined file mirroring Book 1's `manuscript/ultramarine.md`, in the series
  voice (close third on Clara, past tense, sensory/restrained, motifs threaded).
  Spine is a real sequel, not a reboot: the returning cast (Clara, Grietje,
  Doncker, the unnamed young painter, Agatha, the surviving goldfinch) carried
  into Delft's documented turn from painters' colour to the rising blue-and-white
  delftware trade; Book 1's guild-leash and year's-grace clock drive the plot;
  fire is transmuted from the Book-1 blast into the kiln that makes "a blue you
  can't see till the fire has it." Added `book2-cover-brief.md`,
  `book2-listing.md`, and `bible/book2-additions.md` (new canon: Coenraad
  Spronck, De Blauwe Hand, Machteld, Grietje→plateelschilster, the fired-cobalt
  craft, the goldfinch-held-in-trust provenance). Appended `DECISIONS.md`
  [D-0007…D-0010] (title, ~22k word count, spine, bible-grounding; dated
  2026-07-19; model family "Claude Opus"). Content committed (`7ceb7ce`), pushed.
  Diff carries only the 6 intended property files (+ card + claim); no SKU, no
  generated file, no publish surface, `control/status.md` untouched.
- 2026-07-19 — Verified pre-flip: `bootstrap.py check --strict` red on the
  **born-red HOLD only** (in-progress Status + 3 auto-draft slots — the designed
  hold); no guard reds; advisories pre-existing/non-gating (2 seat-digest, 4
  model-line on other cards). CI test suites run locally all green: membership-kit
  36, stripe-webhook 14, github-webhook 18, owner-click-queue 38 — all OK.
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level "Claude Opus"), one 💡 idea, previous-session review, all three
  auto-draft slots resolved. Re-ran `bootstrap.py check --strict` — born-red HOLD
  clears. Did NOT touch `control/status.md`; `.substrate/guard-fires.jsonl` left
  unstaged to keep the diff scoped to the deliverable.

## 💡 Session idea

💡 **Add a `long-form fiction drafting` (creative/long-form) task-class to the
PL-004 taxonomy the model-line checker validates against.** `bootstrap.py check
--strict` now emits a non-gating `[model-line-class]` advisory on *three* cards —
`2026-07-19-lull-book2-mirror-city.md`, `2026-07-19-night-kiln-book4.md`, and this
one — all recording `long-form fiction drafting`, because none of the 9 taught
classes (docs-only | mechanical refactor | test writing | runtime bugfix |
kernel/architecture design | review/verify | research | idea/planning | feature
build) fits a book-drafting session, so the fiction lane keeps writing the truest
label it has and getting flagged for it. The book-building lane is now a
recurring, first-class kind of work in this repo (multiple novels/sequels
shipped), and the PL-004 telemetry is silently recording it as "unclassed" every
time. Guard recipe: extend the class list in the kit's PL-004 constants (the
module `engine/checks` consumes for `[model-line-class]`; mirror in
`.sessions/README.md`'s taught form and the kit's model-line test) with a
creative-drafting class, so the fiction sessions telemeter cleanly instead of
each tripping a permanent advisory. Kit-owned change (advisory only, never
exit-affecting), so it is a clean low-risk grammar addition.

## previous-session review

previous-session review: the most recent prior card,
`2026-07-19-night-kiln-book4.md` (#269), executed the same "genuine cozy sequel as
landable repo content, publishing owner-gated" pattern with exemplary discipline
— honest `wc -w`, born-red→complete card ritual, family-level model attribution,
and a scoped diff that left every generated/owner-gated surface untouched. I
mirrored its landing recipe here for the Ultramarine property (born-red card +
claim first, content second, flip last; no `control/status.md` touch; no SKU/
publish surface), and independently hit the same `long-form fiction drafting`
model-line advisory it did — which is exactly the recurring, cross-session
friction my 💡 above proposes to retire at the taxonomy level rather than
per-card.
