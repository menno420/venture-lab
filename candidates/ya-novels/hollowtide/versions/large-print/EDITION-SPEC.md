# Hollowtide — large-print paperback edition spec

Production spec for a large-print paperback of the **full** YA novel
(canonical text `../../manuscript/` ch01–ch16, **28,595 words** per
`wc -w candidates/ya-novels/hollowtide/manuscript/ch*.md` → chapter sum
`28595`; the assembled `../../hollowtide-full.md` measures `28610` including
front matter — 2026-07-13). **Spec only — no new manuscript needed**; the
interior is set from the chapter files unchanged. Structure mirrors the
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
  long italic passages.
- **Leading:** 1.35–1.5× point size (16pt/22pt or looser).
- **Alignment:** left-aligned, ragged right; hyphenation OFF.
- **Contrast:** black ink on cream paper.
- Chapter openers: start each of the 16 chapters on a new page; no drop caps.

## Estimated page count

Not measured — no interior has been typeset. Estimate from density (density
band per the the-slow-word spec's internal estimate: 16pt/1.4× leading ≈
**160–200 words/page** at 6×9):

- Body: 28,595 words ÷ 160–200 wpp ≈ **143–179 pages**.
- Plus front/back matter, content note, and 16 chapter-opener pages: ≈ 12–18
  pages.
- **Working estimate: 155–195 pages; midpoint ~175 pages** used below.

## KDP print cost + royalty math

Source: [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340),
accessed 2026-07-13 (per the the-slow-word spec). Black ink, white/cream
paper, Amazon.com marketplace: 110–828 pages = **$1.00 fixed + $0.012/page**.

Print royalty = **60% of list − print cost** (per
`docs/publishing/CHECKLIST.md` §4).

| Pages | Print cost | List $11.99 | List $12.99 | List $14.99 |
|-------|-----------|-------------|-------------|-------------|
| 155 | $1.00 + 155×$0.012 = **$2.86** | $7.194 − 2.86 = **$4.33** | $7.794 − 2.86 = **$4.93** | $8.994 − 2.86 = **$6.13** |
| 175 | $1.00 + 175×$0.012 = **$3.10** | **$4.09** | **$4.69** | **$5.89** |
| 195 | $1.00 + 195×$0.012 = **$3.34** | **$3.85** | **$4.45** | **$5.65** |

- **Recommended list: $12.99.** The repo's only verified paperback band is
  $12.99–$14.99 (CHECKLIST §4, kids paperback); a verified YA-paperback band
  does not exist in-repo — **not measured**. $12.99 takes the bottom of the
  verified band: YA buyers are more price-sensitive than the adult
  large-print market, and the CHECKLIST §4 YA *ebook* band tops out at $3.99,
  so any paperback is already a big step up.
- **$12.99ish floor implication:** KDP's mathematical minimum list (print
  cost ÷ 0.60 ≈ $3.34 ÷ 0.60 ≈ $5.57) is no constraint, but a large-print
  paperback structurally cannot price anywhere near the $2.99–$3.99 YA ebook
  — the format forces a ~$12.99 list, i.e. 3–4× the ebook. That gap is the
  main commercial risk of this edition.

## Accessibility notes

- Cover and title page carry **"Large Print"** prominently; KDP large-print
  attribute/keyword selected at listing time (owner, at the publish click).
- Page numbers 14pt+, consistent outside-corner placement; no text over
  images, no grey-on-grey, no decorative display faces inside.
- Content note from `../../README.md` carries over verbatim (child
  endangerment and peril, the "hollowing", grief, restrained non-graphic
  deaths including one sacrificial death; no sexual content, no graphic
  gore — ages 14–17).

## Title-specific notes

- **Large-print YA is a smaller niche than large-print adult fiction**: the
  natural buyers are low-vision teen readers plus a reluctant-reader /
  dyslexia-adjacent crossover (larger type and generous leading lower the
  reading barrier). Demand for either segment: **not measured** — no
  comps surveyed, no sales data exists for this title in any format.
- Sensible only as a near-zero-marginal-cost catalog extension once a
  standard edition exists; not a lead format.

## Production steps (when owner green-lights)

1. Typeset interior from `../../manuscript/ch01.md`–`ch16.md` at the spec
   above; record actual page count.
2. Recompute the royalty row for the real page count (formula above).
3. Cover: reuse the standard-edition cover art (when it exists) with a
   "Large Print" banner; spine width from the KDP calculator at final page
   count.
4. Run the full `docs/publishing/CHECKLIST.md` pass.

⚑ **Publish/price clicks stay owner-gated** (CHECKLIST §7) — nothing in this
spec authorizes a listing, a price, or any spend.
