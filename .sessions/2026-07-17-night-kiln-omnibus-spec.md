# Session — The Night Kiln EN omnibus/box-set EDITION-SPEC (gate-free higher-AOV listing)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · edition-spec (content)
- **started (date -u):** Fri Jul 17 23:42:15 UTC 2026
- **branch:** `claude/night-kiln-omnibus-spec-2026-07-17` (PR #226)
- **base:** `main@94e9769`
- **purpose:** add a new **gate-free single-volume omnibus / box-set edition**
  of the already-complete, already-verified EN *Night Kiln* trilogy — a
  recombination-only **EDITION-SPEC** landed as ONE PR. New file
  `candidates/adult-novels/the-night-kiln/versions/omnibus-en/EDITION-SPEC.md`,
  mirroring the sibling `versions/large-print/EDITION-SPEC.md` +
  `versions/README.md` convention and the just-merged Paper Orange audio spec
  (PR #225). The spec ships **edition identity** (proposed omnibus
  title/subtitle — DECISIONS names none), the **three books in reading order**,
  a **unified front matter** (single title page, combined 36-chapter TOC, one
  copyright/colophon), an **inter-book continuity/transition note** (half-title
  dividers, book-to-book flow, the growing three-line catechism), **back
  matter**, an **honest total `wc -w`** from per-book counts (15,999 / 15,995 /
  23,334 = **55,328**) with a trade-paperback page/trim estimate, and an
  explicit **owner-gated NOT-included** section. **Recombination spec only — the
  three component EN masters stay byte-for-byte UNTOUCHED; no new prose, no
  cover, no ISBN, no publish, no spend.**
- **distinct-from:** the `versions/large-print/` + `large-print-book-2/` specs
  are *per-book print* format extensions (6×9, 16pt, KDP royalty math); the
  `nl/` `nl-book-2/` `nl-book-3/` dirs are *translations*. THIS is a
  *single-volume recombination* of the three finished EN books into one
  higher-AOV product off the SAME masters — no overlap, near-zero marginal cost
  ("versions are cheap once the research exists").
- **NL note:** this spec is **EN-only**. An NL omnibus (*De Nachtoven* /
  *De Morgendeur* / *De Oogstslag*) is **deferred** pending the owner's
  one-word length-band ratify still open in `LENGTH-BAND-PREP.md`; the EN
  omnibus does NOT depend on that ratify and does not touch it.
- **queue note:** editions do **not** get their own §7 vetting packet or
  OWNER-QUEUE row — the large-print sibling created neither, and
  `scripts/derive_owner_queue.py` derives the queue only from vetting packets'
  §7 blocks (confirmed on the slice-3 audio spec, #225). This slice adds **no
  queue row** and regenerates nothing. Omnibus cover/ISBN/print-KDP **publish
  stays owner-gated** under the title's existing packet gate.
- **session:** Born-red card holds substrate-gate red (in-progress badge +
  unresolved fill slots) until the deliberate completion flip; mirrors the
  edition-spec scaffold exactly (identity → reading order → unified front
  matter → combined TOC → continuity note → back matter → word count/trim →
  owner-gate → provenance footer).

## 💡 Session idea

💡 This spec is recombination-only and its scaffolding is **series-agnostic** —
identity (with the Book-One-vs-series title-collision fix) → reading order →
unified front matter (single title/copyright/consolidated content note) →
combined-TOC-derived-from-`grep '^# Chapter'` → planted-hook continuity note →
honest summed `wc -w` → trade page/trim estimate → owner-gate → per-`file@sha`
provenance footer. Lift it into a reusable **`versions/omnibus/EDITION-SPEC.template.md`**
(or a `scripts/new_omnibus_spec.py` that stubs the combined TOC and the summed
word-count block straight from the component masters' `# Chapter` lines + `wc
-w`), and **any completed trilogy/series in the catalog** inherits a
box-set edition for the cost of one grep-and-fill — the only genuinely
per-series parts are the proposed title and the continuity chain, both cheap to
write once the books exist. This is the third gate-free format tier now proven
off the SAME masters (large-print = print accessibility, audio = audio
accessibility, omnibus = higher-AOV bundling), so the three templates together
turn "the books are done" into a whole gate-free product shelf, each edition
landing red→green as its own tiny PR with cover/ISBN/publish parked at the one
owner ⚑ gate.

## previous-session review

previous-session review: `.sessions/2026-07-17-paper-orange-audio-spec.md`
(PR #225, slice-3 of ORDER 016) — the exemplar this slice mirrored: a
recombination-adjacent edition spec off a finished master that did the honest
things right (per-chapter `csplit`+`wc -w` runtime that sums *exactly* to the
whole-file count; a grep-verified pronunciation guide that omits terms the text
doesn't use; an explicit owner-gate + `file@sha` provenance footer) and
correctly added **no** OWNER-QUEUE row because editions aren't a publish
surface. Its 💡 — a title-agnostic `versions/audio/EDITION-SPEC.template.md` —
is the same "templatize the gate-free tier" instinct this card's omnibus 💡
extends to the third format; adopting one shared template-generator across all
three edition types is the natural next consolidation.
