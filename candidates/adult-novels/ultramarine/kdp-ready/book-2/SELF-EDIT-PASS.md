# Self-Edit Pass — *The Blue and the White* (Ultramarine, Book Two)

> A genuine proofreading and continuity read of the canonical manuscript
> `../../book2/the-blue-and-the-white.md` (2026-07-19), performed as part of
> building `MANUSCRIPT-KDP.md`. The canonical source was **not modified**; the
> KDP build preserves the body **byte-for-byte** (verified by line-range diff —
> zero body changes). This pass records what was checked, what was fixed, and
> what a human should still confirm.

---

## (a) Mechanical fixes APPLIED

**None.** No mechanical edits were applied to the manuscript body — the text is
clean. The `cat`-built KDP manuscript therefore reproduces the original body with
zero `sed` fixes.

Checks run over the full manuscript (22,079 words), all passing with nothing to
correct:

- **Doubled words** (`the the`, `and and`, etc.): none. The one regex hit —
  "would tell you you've wasted your morning" (ch. 2) — is correct English
  ("tell you [that] you've…"), not a repetition.
- **Double spaces / spaces before punctuation / doubled punctuation** (`,,`,
  `..`, ` ,`): none.
- **Missing space after a sentence period** (`word.Word`): none.
- **Tabs / trailing whitespace:** none.
- **Em-dash usage:** consistent throughout — 85 spaced em-dashes (` — `), zero
  unspaced. No hyphen-for-dash slips.
- **Ellipses:** none used; no malformed `..`/`....` forms.
- **Proper-noun spelling consistency:** Clara, Grietje, Spronck, Machteld,
  Pauwels, Doncker, Barent, Gerrit, Fabritius, Wijnants all spelled uniformly; no
  variant forms (no *Spronk*, *Grietge*, *Fabricius*, etc.).
- **Chapter/part structure:** 3 parts, 12 chapters, headings sequential (`## 1.`
  … `## 12.`) with no gaps or duplicates; ends with `*THE END*`.

---

## (b) Continuity questions FLAGGED (not auto-fixed)

Checked against `../../bible/book2-additions.md`, `../../book2/outline.md`, and
Book One (`../../manuscript/ultramarine.md`). The manuscript is, notably,
**already consistent** with the bible on every point below — these are recorded
as human-confirmation checkpoints, **not** as detected errors, and nothing was
changed.

1. **Fabritius's goldfinch — held in trust, not owned.** The bible fixes this
   ("Agatha van Pruyssen gave it into Clara's keeping — not ownership"). The
   manuscript honors it explicitly (ch. 9: "given into her keeping and not her
   ownership… held in trust") and makes the collector's-offer refusal turn on it.
   **Consistent — confirm parity with any Book Three.**
2. **Grietje's "bright things": four → five.** Bible says she ends counting five
   (adds her own first fired blue-bird tile). Manuscript honors it: "four bright
   things" early (ch. 5), then "the fifth thing now… the small fired tile with
   her own clumsy blue bird" (ch. 9). **Consistent — confirm the count is never
   stated as "five" before that reveal.**
3. **The unnamed young painter (Vermeer).** Per `DECISIONS.md` [D-0003] he must
   never be named on the page. Verified: zero occurrences of *Vermeer* /
   *Johannes* / *Reyniersz*. **Consistent.**
4. **Grietje's / Clara's ages across the two books.** Book One: Grietje 8, Clara
   unspecified. Book Two: Grietje "nine now" (ch. 1), aging toward ten across the
   autumn-1655→summer-1656 span; Clara "a woman of five-and-thirty" (ch. 9).
   Internally coherent — **confirm Clara's age and Grietje's birthday math are
   compatible with anything stated or implied in Book One.**
5. **Timeline reckoning ("two winters" vs "three years").** Early chapters say the
   ruin is "two winters on"; the close says Delft is "three years into its twenty
   years' rebuilding." Both are defensible from the Oct-1654 blast (two *winters*
   passed by winter 1655–56; the calendar touches 1654/1655/1656), but the two
   phrasings sit close together in the reader's mind. **Confirm this is the
   intended reckoning, not a drift.**
6. **Pottery name form — "De Blauwe Hand" vs "the Blue Hand."** The full Dutch
   name appears once (ch. 5, matching the bible); narration otherwise anglicizes
   it to "the Blue Hand." Reads as deliberate house style. **Confirm the series
   style guide permits the mixed usage** (Book One and the Dutch edition
   *Weduwenblauw* set precedent for Dutch-term handling).

---

## (c) Typography note (not a typo — flagged for the conversion pass)

The manuscript uses **straight ASCII quotation marks and apostrophes throughout**
(108 straight double-quotes; straight `'`; zero curly/typographic marks) — applied
**consistently**, so it is a house-style choice, not an error, and was
deliberately **left unchanged** to preserve the body byte-for-byte. If the KDP
edition is to ship with typographic ("curly") quotes, apply a single global
smart-quotes pass **at ebook-conversion time**, and match whatever Book One
(`../../manuscript/ultramarine.md`) ships with so the series is uniform. This is a
formatting decision, out of scope for a byte-preserving manuscript build.

---

## ⚠ This does NOT replace a professional proofread

**This pass was performed by an automated reading and does not substitute for a
professional, native-speaker proofread and copy-edit.** It catches mechanical and
continuity-consistency issues at the level a careful machine read can; it does
**not** vouch for register, idiom, period diction, rhythm, or the subtle line-level
choices a human editor would weigh, nor for factual/historical fidelity beyond the
series bible. **A human native-speaker proofread remains a required gate before
publication** (consistent with the catalog's standing owner-gate on a
native-speaker pass).
