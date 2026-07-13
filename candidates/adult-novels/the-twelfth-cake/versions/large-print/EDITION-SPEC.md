# The Twelfth Cake — large-print paperback edition spec

Production spec for a large-print paperback of the **full** novella (canonical
manuscript `../../en/the-twelfth-cake.md`, **15,995 words** per
`wc -w candidates/adult-novels/the-twelfth-cake/en/the-twelfth-cake.md` →
`15995`, 2026-07-13). **Spec only — no new manuscript needed**; the interior
is set from the base manuscript unchanged. Structure mirrors the merged
the-slow-word large-print spec
(`candidates/adult-novels/the-slow-word/versions/large-print/EDITION-SPEC.md`,
PR #111) and the 2026-07-13 four-title bundle. Publishing is owner-gated
([`docs/publishing/vetting/the-twelfth-cake.md`](../../../../../docs/publishing/vetting/the-twelfth-cake.md) §7).

Provenance: created 2026-07-13 (night run, ORDER 011 item 2 — edition
variants for the EN adult catalog, relaying ORDER 008 item 1: "versions are
cheap once the research exists"). Source manuscript pinned above with its
measured `wc -w`.

## Trim size

- **6" × 9"** (KDP standard trim, no extended-distribution restrictions).
  Large-print editions conventionally use 6×9 or larger so the enlarged type
  doesn't balloon the page count; 6×9 keeps print cost lowest while leaving a
  ~4.5" text measure at 0.75" margins — comfortable for 16pt type (per the
  the-slow-word spec).
- Margins: 0.75" outside/top/bottom, gutter per KDP table for final page
  count (0.5"–0.625" at this length).

## Typography (large-print norms — per the the-slow-word spec)

Citations reused from the the-slow-word spec rather than re-searched; its
APH-guideline figure was itself marked "from prior knowledge, not fetched" —
that caveat carries over here. Verify at production.

- **Body: 16pt minimum** (floor for the "large print" label; accessibility
  bodies commonly recommend 18pt for low-vision readers — per the
  the-slow-word spec, unverified this session).
- **Face:** high-legibility book face with open counters and distinct
  numerals (Georgia, a Bookerly-like serif, or Atkinson Hyperlegible). The
  manuscript uses inline emphasis italics only — keep them inline; never set
  whole paragraphs italic. Resist any urge toward period display faces for
  the 1847 setting inside the book block (ornamental letterforms hurt
  legibility); save the Victorian flavor for the cover.
- **Leading:** 1.35–1.5× point size (16pt/22pt or looser).
- **Alignment:** left-aligned, ragged right; hyphenation OFF.
- **Contrast:** black ink on cream paper.
- Chapter openers: start each of the 12 chapters on a new page; no drop caps.

## Estimated page count

Not measured — no interior has been typeset. Estimate from density (density
band per the the-slow-word spec's internal estimate: 16pt/1.4× leading ≈
**160–200 words/page** at 6×9):

- Body: 15,995 words ÷ 160–200 wpp ≈ **80–100 pages**.
- Plus front/back matter, content note, and 12 chapter-opener pages: ≈ 10–16
  pages.
- **Working estimate: 90–115 pages; midpoint ~105 pages** used below.

## KDP print cost + royalty math

Source: [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340),
accessed 2026-07-13 (per the the-slow-word spec). Black ink, white/cream
paper, Amazon.com marketplace: **24–110 pages = flat $2.30**; 110–828 pages =
$1.00 fixed + $0.012/page. At novella length the whole working range sits in
or at the edge of the flat band — print cost is effectively $2.30–$2.38.

Print royalty = **60% of list − print cost** (per
`docs/publishing/CHECKLIST.md` §4).

| Pages | Print cost | List $11.99 | List $12.99 | List $14.99 |
|-------|-----------|-------------|-------------|-------------|
| 90 | flat band = **$2.30** | $7.194 − 2.30 = **$4.89** | $7.794 − 2.30 = **$5.49** | $8.994 − 2.30 = **$6.69** |
| 105 | flat band = **$2.30** | **$4.89** | **$5.49** | **$6.69** |
| 115 | $1.00 + 115×$0.012 = **$2.38** | **$4.81** | **$5.41** | **$6.61** |

- **Recommended list: $12.99.** The adult large-print precedents
  (the-slow-word, ultramarine) recommended $14.99 for ~28–29k-word novels at
  ~170–190 pages; this is a **16k novella at ~105 pages**, so it takes the
  **bottom of the only verified paperback band** ($12.99–$14.99, CHECKLIST
  §4). Yields ~$5.41–$5.49/unit. (Comparable large-print seasonal-fiction
  pricing not surveyed — not measured.)
- KDP's minimum-list floor (print cost ÷ 0.60 ≈ $3.97) is no constraint; the
  practical floor is the verified band's $12.99 start.
- The title's recommended **ebook** price is $3.99 (vetting packet §4) — a
  large-print paperback is structurally ~3.3× the ebook. That gap is the main
  commercial risk of the format at novella length.

## Accessibility notes

- Cover and title page carry **"Large Print"** prominently; KDP large-print
  attribute/keyword selected at listing time (owner does this at the publish
  click).
- Page numbers 14pt+, consistent outside-corner placement; no text over
  images, no grey-on-grey, no decorative display faces inside.
- Content note from the manuscript front matter carries over verbatim (adult
  seasonal historical fiction, London, 5 January 1847: the sale of a family
  business, remembered bereavements, remembered hard winters, and one
  snowbound night in which nobody comes to harm; no crime, no violence, no
  explicit content, no swearing).

## Title-specific notes

- **Seasonal window:** the book is a Twelfth Night / week-after-Christmas
  story; print sales of seasonal fiction concentrate in Q4–early January.
  Print-on-demand carries no inventory risk, but any owner publish click is
  best timed to land the listing before the season (spec is season-agnostic;
  the timing note is for the §7 queue). Christmas/holiday fiction is also a
  perennial large-print library staple — plausible fit, demand **not
  measured**: no comps surveyed, no sales data exists for this title in any
  format.
- The subtitle *"A Twelfth Night Novella"* stays on the cover (vetting
  packet §1 recommends it ON — the title is a historical common noun and
  needs the fiction signal).
- Sensible only as a near-zero-marginal-cost catalog extension once a
  standard edition exists; not a lead format.

## Production steps (when owner green-lights)

1. Typeset interior from `../../en/the-twelfth-cake.md` at the spec above;
   record actual page count.
2. Recompute the royalty row for the real page count (formula above; check
   which side of the 110-page flat-band boundary it lands).
3. Cover: reuse the standard-edition cover art (when it exists) with a
   "Large Print" banner; spine width from the KDP calculator at final page
   count.
4. Run the full `docs/publishing/CHECKLIST.md` pass.

⚑ **Publish/price clicks stay owner-gated** (CHECKLIST §7) — nothing in this
spec authorizes a listing, a price, or any spend.
