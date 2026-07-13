# The Undertow — large-print paperback edition spec

Production spec for a large-print paperback of the **full** YA novel
(canonical text `../../en/` files `00-epigraph.md` through
`16-first-air-epilogue.md`, **27,781 words** story text per
`wc -w candidates/ya-novels/the-undertow/en/*.md` → total `28653`, minus
`EXPANSION.md` `410` and `README.md` `462` which are not story text —
2026-07-13). **Spec only — no new manuscript needed**; the interior is set
from the numbered files unchanged, in numeric order. Structure mirrors the
merged the-slow-word large-print spec
(`candidates/adult-novels/the-slow-word/versions/large-print/EDITION-SPEC.md`,
PR #111). Publishing is owner-gated (`docs/publishing/CHECKLIST.md` §7).

## Trim size

- **6" × 9"** (KDP standard trim, no extended-distribution restrictions) —
  same rationale as the the-slow-word spec: enlarged type without ballooning
  page count; ~4.5" text measure at 0.75" margins, comfortable for 16pt.
- Margins: 0.75" outside/top/bottom, gutter per KDP table for final page
  count (0.5"–0.625" at this length).

## Typography (large-print norms — per the the-slow-word spec)

Citations reused from the the-slow-word spec rather than re-searched; its
APH-guideline figure was itself marked "from prior knowledge, not fetched" —
that caveat carries over. Verify at production.

- **Body: 16pt minimum**; 18pt commonly recommended for low-vision readers
  (per the the-slow-word spec, unverified this session).
- **Face:** high-legibility book face with open counters (Georgia, a
  Bookerly-like serif, or Atkinson Hyperlegible); no condensed faces, no
  long italic passages. The first-person-present voice uses occasional
  emphasis italics — keep them inline only.
- **Leading:** 1.35–1.5× point size (16pt/22pt or looser).
- **Alignment:** left-aligned, ragged right; hyphenation OFF.
- **Contrast:** black ink on cream paper.
- Openers: epigraph page, then each of the 15 chapters and the epilogue on a
  new page; no drop caps.

## Estimated page count

Not measured — no interior has been typeset. Estimate from density (density
band per the the-slow-word spec's internal estimate: 16pt/1.4× leading ≈
**160–200 words/page** at 6×9):

- Body: 27,781 words ÷ 160–200 wpp ≈ **139–174 pages**.
- Plus front/back matter, content note, epigraph page, and 16
  chapter/epilogue openers: ≈ 12–18 pages.
- **Working estimate: 150–190 pages; midpoint ~170 pages** used below.

## KDP print cost + royalty math

Source: [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340),
accessed 2026-07-13 (per the the-slow-word spec). Black ink, white/cream
paper, Amazon.com marketplace: 110–828 pages = **$1.00 fixed + $0.012/page**.

Print royalty = **60% of list − print cost** (per
`docs/publishing/CHECKLIST.md` §4).

| Pages | Print cost | List $11.99 | List $12.99 | List $14.99 |
|-------|-----------|-------------|-------------|-------------|
| 150 | $1.00 + 150×$0.012 = **$2.80** | $7.194 − 2.80 = **$4.39** | $7.794 − 2.80 = **$4.99** | $8.994 − 2.80 = **$6.19** |
| 170 | $1.00 + 170×$0.012 = **$3.04** | **$4.15** | **$4.75** | **$5.95** |
| 190 | $1.00 + 190×$0.012 = **$3.28** | **$3.91** | **$4.51** | **$5.71** |

- **Recommended list: $12.99.** The repo's only verified paperback band is
  $12.99–$14.99 (CHECKLIST §4, kids paperback); a verified YA-paperback band
  does not exist in-repo — **not measured**. Same bottom-of-band reasoning as
  the other YA large-print specs (YA ebook band $2.99–$3.99 makes any
  paperback a 3–4× step).
- **$12.99ish floor implication:** KDP's mathematical minimum list ($3.04 ÷
  0.60 ≈ $5.07) is no constraint; the binding floor is the ~$12.99 band
  floor, far above the YA ebook price point — main commercial risk of the
  format for YA.

## Accessibility notes

- Cover and title page carry **"Large Print"** prominently; KDP large-print
  attribute/keyword selected at listing time (owner, at the publish click).
- Page numbers 14pt+, consistent outside-corner placement; no text over
  images, no grey-on-grey, no decorative display faces inside.
- Content note from `../../en/README.md` carries over verbatim (authoritarian
  state, a rigged coming-of-age rite, asphyxiation as a tool of control
  rendered through dread not graphic detail, one off-page character loss,
  non-graphic injury; restrained romantic thread; no sexual content, no
  graphic gore, no strong profanity — ages 13–17).

## Title-specific notes

- **Large-print YA is a smaller niche than large-print adult fiction**:
  low-vision teen readers plus a reluctant-reader crossover (larger type and
  generous leading lower the reading barrier; the short-chapter,
  present-tense thriller pacing is the part of this title that fits that
  crossover). Demand for either segment: **not measured** — no comps
  surveyed, no sales data exists for this title in any format.
- Sensible only as a near-zero-marginal-cost catalog extension once a
  standard edition exists; not a lead format.

## Production steps (when owner green-lights)

1. Typeset interior from `../../en/00-epigraph.md`–`16-first-air-epilogue.md`
   (numeric order; exclude `EXPANSION.md` and `README.md`) at the spec above;
   record actual page count.
2. Recompute the royalty row for the real page count (formula above).
3. Cover: reuse the standard-edition cover art (when it exists) with a
   "Large Print" banner; spine width from the KDP calculator at final page
   count.
4. Run the full `docs/publishing/CHECKLIST.md` pass.

⚑ **Publish/price clicks stay owner-gated** (CHECKLIST §7) — nothing in this
spec authorizes a listing, a price, or any spend.
