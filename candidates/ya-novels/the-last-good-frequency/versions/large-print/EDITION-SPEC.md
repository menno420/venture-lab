# The Last Good Frequency — large-print paperback edition spec

Production spec for a large-print paperback of the **full** YA novel
(canonical text `../../the-last-good-frequency.en.md`, **26,390 words** per
`wc -w candidates/ya-novels/the-last-good-frequency/the-last-good-frequency.en.md`
→ `26390`, 2026-07-13 — single file, count includes its front matter).
**Spec only — no new manuscript needed**; the interior is set from the base
file unchanged. Structure mirrors the merged the-slow-word large-print spec
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
- Chapter openers on new pages; no drop caps.

## Estimated page count

Not measured — no interior has been typeset. Estimate from density (density
band per the the-slow-word spec's internal estimate: 16pt/1.4× leading ≈
**160–200 words/page** at 6×9):

- Body: 26,390 words ÷ 160–200 wpp ≈ **132–165 pages**.
- Plus front/back matter, content note, and chapter-opener pages: ≈ 10–15
  pages.
- **Working estimate: 145–180 pages; midpoint ~160 pages** used below.

## KDP print cost + royalty math

Source: [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340),
accessed 2026-07-13 (per the the-slow-word spec). Black ink, white/cream
paper, Amazon.com marketplace: 110–828 pages = **$1.00 fixed + $0.012/page**.

Print royalty = **60% of list − print cost** (per
`docs/publishing/CHECKLIST.md` §4).

| Pages | Print cost | List $11.99 | List $12.99 | List $14.99 |
|-------|-----------|-------------|-------------|-------------|
| 145 | $1.00 + 145×$0.012 = **$2.74** | $7.194 − 2.74 = **$4.45** | $7.794 − 2.74 = **$5.05** | $8.994 − 2.74 = **$6.25** |
| 160 | $1.00 + 160×$0.012 = **$2.92** | **$4.27** | **$4.87** | **$6.07** |
| 180 | $1.00 + 180×$0.012 = **$3.16** | **$4.03** | **$4.63** | **$5.83** |

- **Recommended list: $12.99.** The repo's only verified paperback band is
  $12.99–$14.99 (CHECKLIST §4, kids paperback); a verified YA-paperback band
  does not exist in-repo — **not measured**. $12.99 takes the bottom of the
  verified band for the same reason as the other YA large-print specs: the
  YA *ebook* band is $2.99–$3.99, so the paperback is already a 3–4× step.
- **$12.99ish floor implication:** KDP's mathematical minimum list ($2.92 ÷
  0.60 ≈ $4.87) is no constraint; the binding floor is the market/band one at
  ~$12.99, which puts this edition far above the ebook price point — main
  commercial risk of the format for YA.

## Accessibility notes

- Cover and title page carry **"Large Print"** prominently; KDP large-print
  attribute/keyword selected at listing time (owner, at the publish click).
- Page numbers 14pt+, consistent outside-corner placement; no text over
  images, no grey-on-grey, no decorative display faces inside.
- Content note from `../../README.md` carries over verbatim (grief —
  off-page death of a grandmother; parental absence; economic decline; teen
  anxiety; a gentle same-gender first-love arc, nothing explicit; mild
  language only — ages 13–17).

## Title-specific notes

- **Tier-1 cover-only title** per `docs/publishing/PUBLISHING-PLAN.md` §2
  (Tier 1, item 3 — "The Last Good Frequency", title adjacency noted but
  differentiated; no illustration gate). Of the four titles in this
  large-print bundle it is the only one already in the publish-first tier,
  so if any YA large-print edition is piloted, this is the natural first —
  but the ebook still leads; large print is a follow-on format.
- **Large-print YA is a smaller niche than large-print adult fiction**:
  low-vision teen readers plus a reluctant-reader crossover (larger type and
  generous leading lower the reading barrier — arguably a fit for this
  title's quiet, hopeful register). Demand for either segment: **not
  measured** — no comps surveyed, no sales data exists for this title in any
  format.

## Production steps (when owner green-lights)

1. Typeset interior from `../../the-last-good-frequency.en.md` at the spec
   above (strip the file's repo front matter); record actual page count.
2. Recompute the royalty row for the real page count (formula above).
3. Cover: reuse the standard-edition cover art (when it exists) with a
   "Large Print" banner; spine width from the KDP calculator at final page
   count. Keyword lane per `docs/publishing/keyword-map.md` (no reuse of The
   Slow Word's radio/signal/first-contact phrases).
4. Run the full `docs/publishing/CHECKLIST.md` pass.

⚑ **Publish/price clicks stay owner-gated** (CHECKLIST §7) — nothing in this
spec authorizes a listing, a price, or any spend.
