# Self-Edit Pass — The Spring Cup (The Night Kiln, Book Five)

> A genuine proofreading read of the full manuscript
> (`candidates/adult-novels/the-night-kiln/en/the-spring-cup.md`, 15,568 words,
> 12 chapters) made while building the KDP package. Line numbers below refer to
> the **canonical source** `en/the-spring-cup.md` (the KDP manuscript adds 32
> lines of front matter, so its body line numbers = source + 32).
>
> **⚠ This pass does NOT replace a professional native-speaker proofread.** It
> is a build-time editorial read by the packaging worker, not a copy-edit of
> record. A human proofreader should still pass the finished text before
> publication — this is the series hard-gate.

## (a) Mechanical fixes — APPLIED

**None. Zero mechanical corrections were needed, and none were made.** The
manuscript body is preserved **byte-for-byte** in `MANUSCRIPT-KDP.md` (verified
by diff against source lines 13–337 — identical). No `sed` fix step was run.

Checked and found clean across the whole text:

- **Doubled words** (`the the`, `and and`, etc.) — none.
- **Double spaces / spacing before punctuation** — none.
- **Common misspellings** (recieve, seperate, definately, occured, thier, untill, begining, …) — none.
- **Quote / apostrophe consistency** — consistent straight ASCII quotes (U+0022) and apostrophes (U+0027) throughout; zero mixed curly quotes. (House style for this manuscript; deliberately left as-is, not "corrected," since it is uniform.)
- **Dashes** — consistent em-dashes (U+2014, 179 of them); no stray hyphen-as-dash.
- **Scene breaks** — four `⁂` marks, consistent with the series.

This is an unusually clean manuscript; the honest result is that there was
nothing mechanical to fix.

## (b) Continuity questions — FLAGGED, not auto-fixed

These are editorial questions for the author/owner. **I did not change the
text.** As the series finale, the book was read specifically for consistency
with Books 1–4; the threads it resolves (see the positive checks below) are
consistent, with the following questions.

### B1. Glaze chemistry: "iron celadon under reduction → red-brown" contradicts the series' own rule (worth the author's eye)

*The Spring Cup* describes the wedding cup's glaze, four times, as a red / red-brown
**iron celadon** fired **under reduction**:

- Ch. 1 (src ~L43): *"a glaze the warm deep red-brown of an iron celadon gone rich under a good reduction."*
- Ch. 7 (src ~L217): *"the iron celadon that would come up red-brown under reduction."*
- Ch. 10 (src ~L263) and Ch. 11 (src ~L281): *"its glaze come out the deep warm red of an iron celadon under a good reduction."*

But Books 1 and 4 repeatedly establish the opposite result for the same recipe —
that iron celadon **reduced** comes out **blue** ("winter-glass blue"):

- *The Night Kiln* L111: *"celadon is nothing in the world but iron… Starve the fire of air at the right hour and the iron forgets to be rust and turns to winter glass. Reduction."* And L149 / L491: *"the celadon had come through winter-glass blue" / "gone a blue there was no name for outside of first snowfalls."*
- *The Winter Wheel* L319: *"The celadon had gone a blue there was no name for outside a first snowfall."*

So within the series, "iron celadon + reduction = winter-glass blue" is a
stated rule; Book 5 uses the same words to get a warm red-brown. This also runs
against real-world practice (reduced iron celadon is green/blue; warm red-brown
iron effects are a different, oxidised or saturated-iron family). **Question for
the author:** is the red cup meant to be a different glaze family (e.g. an iron
red / tenmoku / oxidised iron), in which case the word "celadon" and/or
"reduction" may want adjusting for consistency with Books 1 & 4 — or is the
warm-red celadon a deliberate one-off? Thematically the red cup matters (it is
"the red cup" throughout), so this is a wording question, not a plot problem. Not
changed here.

### B2. The fifth catechism line is compressed in Ch. 1 vs. its canonical form (finale precision)

Chapter 1 (src L15) glosses the catechism's fourth line as
*"…and what one hand throws, another hand fills"* — dropping the coda Book 4
canonised: *"— for a first pot is not one you fill alone"* (compare
`the-winter-wheel.md` L333/L369). The full coda **is** correctly restored in
this book's closing recital (src L331/L333). The Ch. 1 version reads as an
intentional narrative compression, but because the refrain is the series'
signature and this is the finale, **worth confirming** the shortened form in
Ch. 1 is deliberate and not an oversight.

### B3. Minor: the cup's age — "thirty years" vs. "thirty-two years"

Narration mostly says the cup was fired / has hummed **"thirty years and more"**
(src L43, L250, and throughout), while Ilsabet's ledger dates it **"thirty-two
years back"** (src L121, L129). These are consistent as rounding ("thirty and
more" ≈ thirty-two), and the hum is consistently "thirty years." Flagged only so
a copy-editor can confirm the intended interval; **no change made.**

### Positive continuity checks (verified consistent with Books 1–4 — no action needed)

- **Perrin Loft**, the apprentice made a second witch in *The Winter Wheel*, opens Book 5 already "a witch of Wenholt these three months" — consistent (Bk 4 L185/L263/L325).
- **Griet** (memory loss; the two lamps at the ferry — the porridge bowl and the mended dish) and her line *"cross and ask her yourself"* pick up the exact foreshadow planted at the end of *The Winter Wheel* (Bk 4 L349) and *The Harvest Rows* — consistent, including the girl "inherited the not-happening."
- The private-shelf callbacks — **Widow Sorrel's honey-jar lid** (Bk 2), the **dunted race-dish gone to a ferry-window lamp** (Bk 3), and **Grams Ilsabet's first pot handed back to the clay** (Bk 4, Wintermark) — are all present and consistent (src L39).
- The **two-rook mark / Ansel Rooke / Rooke Brothers** lineage matches Bk 4 (L203).
- The **catechism grows to a fifth line** here, exactly as the four-book progression sets up (keep → give back → mend → hand on → keep the love, not the loss).

## (c) Caveat

**This self-edit pass is a build-time editorial read only. It is NOT a substitute
for a professional native-speaker proofread**, which remains the series' hard
gate before any publication. Zero mechanical errors were found and the body is
preserved byte-for-byte; the continuity items above are questions for the
author, deliberately left unchanged in the text.
