# The Slow Word — large-print paperback edition spec

Production spec for a large-print paperback of the **full** novel (canonical
`en/` text, 29,403 words body text per `wc -w` on the 12 chapter files,
2026-07-13). **Spec only — no new manuscript needed**; the interior is set
from `en/` unchanged. Publishing is owner-gated (see `NOTES.md` in
`../novella-cut/` and `docs/conventions.md` §13).

## Trim size

- **6" × 9"** (KDP standard trim, no extended-distribution restrictions).
  Large-print editions conventionally use 6×9 or larger so the enlarged type
  doesn't balloon the page count; 6×9 keeps print cost lowest while leaving a
  ~4.5" text measure at 0.75" margins — comfortable for 16pt type.
- Margins: 0.75" outside/top/bottom, gutter per KDP table for final page
  count (0.5"–0.625" at this length).

## Typography (large-print norms)

- **Body: 16pt minimum.** 16pt is the floor for the "large print" label;
  accessibility bodies commonly recommend 18pt for low-vision readers (APH
  large-print guidelines — figure from prior knowledge, **not fetched this
  session**; verify at production).
- **Face:** a high-legibility book face with open counters and distinct
  numerals — e.g. Georgia, Bookerly-like serif, or the sans Verdana/Atkinson
  Hyperlegible. Avoid condensed faces and long italic passages (the master
  text uses inline italics for Samoan terms and emphasis; keep them but never
  set whole paragraphs italic).
- **Leading:** 1.35–1.5× point size (16pt/22pt or looser).
- **Alignment:** left-aligned, ragged right; hyphenation OFF (broken words
  are a documented low-vision stumbling block).
- **Contrast:** black ink on white or cream paper; cream reduces glare and is
  the usual large-print choice.
- Chapter openers: start each of the 12 chapters on a new page; drop caps
  avoided (ornamental letterforms hurt legibility).

## Estimated page count

Not measured — no interior has been typeset. Estimate from density:

- A 6×9 trade novel at ~11pt runs ~300–350 words/page; scaling to 16pt with
  1.4× leading cuts density to roughly **160–200 words/page** (internal
  estimate from line/character metrics, not a cited figure).
- Body: 29,403 words ÷ 160–200 wpp ≈ **147–184 pages**.
- Plus front/back matter and 12 chapter-opener part-pages: ≈ 10–16 pages.
- **Working estimate: 160–200 pages; midpoint ~180 pages** used below.

## KDP print cost + royalty math

Source: [KDP printing cost](https://kdp.amazon.com/en_US/help/topic/G201834340),
accessed 2026-07-13. Black ink, white/cream paper, Amazon.com marketplace:
110–828 pages = **$1.00 fixed + $0.012/page** (24–110 pages = flat $2.30).

Print royalty = **60% of list − print cost** (per
`docs/publishing/CHECKLIST.md` §4).

| Pages | Print cost | List $12.99 | List $14.99 | List $16.99 |
|-------|-----------|-------------|-------------|-------------|
| 160 | $1.00 + 160×$0.012 = **$2.92** | $7.794 − 2.92 = **$4.87** | $8.994 − 2.92 = **$6.07** | $10.194 − 2.92 = **$7.27** |
| 180 | $1.00 + 180×$0.012 = **$3.16** | **$4.63** | **$5.83** | **$7.03** |
| 200 | $1.00 + 200×$0.012 = **$3.40** | **$4.39** | **$5.59** | **$6.79** |

- **Recommended list: $14.99.** Large-print editions carry a customary
  premium over the standard edition; $14.99 sits inside the kids-paperback
  band the repo has already verified as viable ($12.99–$14.99, CHECKLIST §4)
  and yields ~$5.59–$6.07/unit across the page-count range. (Comparable
  large-print fiction pricing not surveyed this session — not measured.)
- Minimum list at 180pp/60%: $3.16 ÷ 0.60 ≈ $5.27 — no constraint at any
  realistic price.

## Accessibility notes

- Title page and cover should carry the words **"Large Print"** prominently
  (discoverability for the low-vision market; also set the cover title in
  high contrast).
- Page numbers: large (14pt+), consistent outside-corner placement.
- No text over images, no grey-on-grey, no decorative display faces inside.
- KDP category: select the Large Print attribute/keyword at listing time so
  the edition surfaces in large-print browse (owner does this at the publish
  click).
- Content note from `en/README.md` (grief/terminal illness, colonial themes,
  one restrained intimate scene, occasional profanity) carries over verbatim
  — same readership, same warning.

## Production steps (when owner green-lights)

1. Typeset interior from `en/` at the spec above; record actual page count.
2. Recompute the royalty row for the real page count (formula above).
3. Cover: reuse the standard-edition cover art (when it exists) with "Large
   Print" banner; spine width from KDP calculator at final page count.
4. Run the full `docs/publishing/CHECKLIST.md` pass; publish click is
   owner-only.
