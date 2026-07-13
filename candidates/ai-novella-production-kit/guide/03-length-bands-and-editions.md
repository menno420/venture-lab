# 3. Length bands and edition variants

## Bands: declare the finish line before the race

A length band is a declared range — e.g. **15,000–16,000 words** —
chosen *before drafting* from what the target shelf actually supports,
and then honored by measurement. The production lane ran a 15k–16k
"book-parity" band as its novella default and landed title after title
inside it (15,040 · 15,045 · 15,117 · 15,133 · 15,173 · 15,995 —
honest `wc -w`, each cited to its merging PR). The band does three
jobs:

1. **It makes "finished" checkable.** A draft is done when the arc is
   complete AND the count is in band — not when enthusiasm runs out.
2. **It sizes chapters.** 15.5k ÷ 12 chapters ≈ 1,300 words each: a
   briefable, single-block unit of work.
3. **It forces the aimed pass** (chapter 1): under band → expand the
   thinnest promised beat; over band → cut ornamental density, never
   promised beats.

Band changes are amendments, not drift: when a plan said ~20k–30k and
the run's brief said band-parity, the delivered 15,995 was recorded
WITH the delta flagged in the plan, the decisions record, and the PR —
one source of truth for length, everywhere else cites it.

## Editions: one manuscript, a product line

A finished base manuscript can ship as multiple purchasable editions.
The production catalog derived, from single base manuscripts:
**novella cuts** (a 36k crime novel cut to a tighter paid edition),
**serial editions** (a 27,865-word literary novel split into three
standalone-purchasable episodes with written-for-serial cold opens,
in-voice "story so far" recaps, and episode-ending hooks),
**translations** (native re-tellings, not literal translations — 4
adult NL editions, 27 trilingual board-book texts), and **large-print
editions** (as written EDITION-SPECs: trim, font, leading — a spec an
owner can hand to any formatter).

The conventions that keep this honest:

- **One subdirectory per edition** under `versions/`, each with its
  complete text plus a `NOTES.md`.
- **NOTES.md carries honest counts** (command shown), what was
  added/cut vs the base, and the edition's market position —
  including every step that costs money or publishes, marked as the
  owner's.
- **The base manuscript is the source of truth for story canon.** An
  edition adapts *presentation* — angle, audience, length, format —
  never silently changes canon. Derive every edition from the base,
  never from another edition; two generations of derivation is how
  continuity errors breed.
- **An edition is a real product decision**, not free money: each one
  enters the same publish gate (chapter 4) as a new title.

`templates/edition-variant-matrix.md` is the planning surface: rows =
editions, columns = audience / band / format / what changes / gate
status.

## Honesty block

Bands are a discipline, not a market guarantee — the shelf data
behind the production band choices is cited in the pricing chapter,
and "the band the catalog used" is not "the band your genre wants."
And edition derivation multiplies *listings*, not demand: the
production catalog's serial and large-print editions are built and
gated but their sales are exactly as unproven as everything else in a
zero-distribution catalog.

---

**Sources:** `candidates/adult-novels/the-twelfth-cake/DECISIONS.md@3b159d9`
(band honored by tightening; single-source-of-length amendment) ·
`candidates/adult-novels/ultramarine/versions/README.md@873d5d9`
(versions/ convention: one dir per edition, NOTES.md with honest
`wc -w`, base-manuscript-wins rule, 27,865-word base measured) ·
`candidates/adult-novels/ultramarine/versions/serial-edition/NOTES.md@873d5d9`
(3-part serial: cold opens, in-voice recaps, episode hooks) ·
`candidates/adult-novels/ultramarine/versions/large-print/EDITION-SPEC.md@873d5d9`
(large-print as a written spec) ·
`candidates/adult-novels/the-slow-word/versions/@ca4c8a1` (novella cut
+ NL cut + large print derived from one base).
