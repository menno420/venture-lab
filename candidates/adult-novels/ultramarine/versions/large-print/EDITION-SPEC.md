# Ultramarine — large-print paperback edition spec

Production spec for a large-print paperback of the **full** novel (canonical
manuscript `../../manuscript/ultramarine.md`, **27,865 words** per
`wc -w candidates/adult-novels/ultramarine/manuscript/ultramarine.md` →
`27865`, 2026-07-13). **Spec only — no new manuscript needed**; the interior
is set from the base manuscript unchanged. Structure mirrors the merged
the-slow-word large-print spec
(`candidates/adult-novels/the-slow-word/versions/large-print/EDITION-SPEC.md`,
PR #111). Publishing is owner-gated
([`docs/publishing/vetting/ultramarine.md`](../../../../../docs/publishing/vetting/ultramarine.md) §7).

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
  bodies commonly recommend 18pt for low-vision readers — per the the-slow-word
  spec, unverified this session).
- **Face:** high-legibility book face with open counters and distinct
  numerals (Georgia, a Bookerly-like serif, or Atkinson Hyperlegible). The
  manuscript uses inline italics for Dutch terms (*schuit*, *plateel*) —
  keep them, but never set whole paragraphs italic.
- **Leading:** 1.35–1.5× point size (16pt/22pt or looser).
- **Alignment:** left-aligned, ragged right; hyphenation OFF.
- **Contrast:** black ink on cream paper (cream reduces glare — usual
  large-print choice).
- Part openers: the novel is in three parts — start each on a recto with a
  plain part-title page; no drop caps.

## Estimated page count

Not measured — no interior has been typeset. Estimate from density (density
band per the the-slow-word spec's internal estimate: 16pt/1.4× leading ≈
**160–200 words/page** at 6×9):

- Body: 27,865 words ÷ 160–200 wpp ≈ **139–174 pages**.
- Plus front/back matter, historical note, and 3 part-title pages: ≈ 8–14
  pages.
- **Working estimate: 150–190 pages; midpoint ~170 pages** used below.

## KDP print cost + royalty math

Source: [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340),
accessed 2026-07-13 (per the the-slow-word spec). Black ink, white/cream
paper, Amazon.com marketplace: 110–828 pages = **$1.00 fixed + $0.012/page**.

Print royalty = **60% of list − print cost** (per
`docs/publishing/CHECKLIST.md` §4).

| Pages | Print cost | List $12.99 | List $14.99 | List $16.99 |
|-------|-----------|-------------|-------------|-------------|
| 150 | $1.00 + 150×$0.012 = **$2.80** | $7.794 − 2.80 = **$4.99** | $8.994 − 2.80 = **$6.19** | $10.194 − 2.80 = **$7.39** |
| 170 | $1.00 + 170×$0.012 = **$3.04** | **$4.75** | **$5.95** | **$7.15** |
| 190 | $1.00 + 190×$0.012 = **$3.28** | **$4.51** | **$5.71** | **$6.91** |

- **Recommended list: $14.99** — same reasoning as the the-slow-word spec:
  large print carries a customary premium over the standard edition, and
  $14.99 sits inside the only paperback band the repo has verified
  ($12.99–$14.99, CHECKLIST §4). Yields ~$5.71–$6.19/unit across the range.
  (Comparable large-print literary-fiction pricing not surveyed — not
  measured.)
- KDP's minimum-list floor (list must cover print cost at 60%): $3.04 ÷ 0.60
  ≈ $5.07 — no constraint. The practical floor is the market one: the repo's
  verified paperback band starts at **$12.99**, and pricing a large-print
  paperback below it would undercut the (future) standard paperback for no
  reason.

## Accessibility notes

- Cover and title page carry **"Large Print"** prominently; KDP large-print
  attribute/keyword selected at listing time (owner does this at the publish
  click).
- Page numbers 14pt+, consistent outside-corner placement; no text over
  images, no grey-on-grey, no decorative display faces inside.
- Content note from the title README carries over verbatim (mass-casualty
  disaster on the page, death of a teenage character, child in peril, grief;
  no explicit sexual content — adult general readers).

## Title-specific notes

- ⚑ **Pending owner decision (vetting packet §2/§7): retitle to "The
  Widow's Blue — A Novel of Delft, 1654"** is the recommended default but NOT
  decided. This spec keeps the working title *Ultramarine* and does NOT apply
  the retitle; any typeset interior/cover applies the owner's title pick
  first (pointer also recorded in `../README.md`).
- Demand for large-print literary fiction from an unknown author: **not
  measured**. The format's economics only work as a low-cost catalog
  extension of an already-selling standard edition.

## Production steps (when owner green-lights)

1. Typeset interior from `../../manuscript/ultramarine.md` at the spec above;
   record actual page count.
2. Recompute the royalty row for the real page count (formula above).
3. Cover: reuse the standard-edition cover art (when it exists) with a
   "Large Print" banner; spine width from the KDP calculator at final page
   count; apply the owner's title decision first.
4. Run the full `docs/publishing/CHECKLIST.md` pass.

⚑ **Publish/price clicks stay owner-gated** (CHECKLIST §7) — nothing in this
spec authorizes a listing, a price, or any spend.
