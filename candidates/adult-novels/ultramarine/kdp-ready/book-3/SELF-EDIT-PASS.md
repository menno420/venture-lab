# Self-Edit Pass — *The Common Blue* (Ultramarine, Book Three)

> A genuine proofreading and continuity read of the canonical manuscript
> `../../book3/the-common-blue.md` (2026-07-20), performed as part of building
> `MANUSCRIPT-KDP.md`. **One correction was applied to the canonical source**
> during this pass (a period-anachronism fix, logged in §(a) below); the KDP
> build was then compiled from the corrected source, and its body reproduces that
> corrected canonical body **byte-for-byte** (verified by line-range diff — zero
> body changes between `book3/the-common-blue.md` lines 11–350 and the compiled
> body). This pass records what was checked, what was fixed, and what a human
> should still confirm.

---

## (a) Mechanical / fidelity fixes APPLIED

**One.** During the continuity read a single **period-anachronism** was caught and
corrected in the canonical manuscript before the byte-preserving KDP build:

- **ch. 4 — "the Mauritshuis" → "a burgomaster's best wall."** In Agatha's line
  contrasting a grand private display with the plates going out to the world, the
  original draft read *"He'd have liked that better than the Mauritshuis."* In
  1656 the Mauritshuis was Johan Maurits's private residence, not a picture
  gallery (it became a museum only in 1822); the phrasing reads to a modern eye as
  the museum, an anachronism the series style-sheet forbids (`bible/style.md` — "No
  anachronism"). Replaced with a period-safe equivalent that keeps Agatha's exact
  sense (a grand private wall vs. the common plate). The KDP body was compiled
  **after** this fix, so it reproduces the corrected canonical body byte-for-byte.

No other mechanical edits were applied — the text is otherwise clean. Checks run
over the full manuscript (20,413 words), all passing with nothing further to
correct:

- **Doubled words** (`the the`, `and and`, etc.): none. The one regex hit — "had
  had it all the autumn to copy" (ch. 10) — is correct English ("had had"), not a
  repetition.
- **Double spaces / spaces before punctuation / doubled punctuation** (`,,`,
  `..`, ` ,`): none.
- **Missing space after a sentence period** (`word.Word`): none.
- **Tabs / trailing whitespace:** none.
- **Em-dash usage:** consistent throughout — 74 spaced em-dashes (` — `), zero
  unspaced. No hyphen-for-dash slips.
- **Ellipses:** none used; no malformed `..`/`....` forms.
- **Proper-noun spelling consistency:** Clara, Grietje, Spronck, Machteld,
  Pauwels, Doncker, Barent, Gerrit, Fabritius, Wijnants, Agatha, and the new
  Book-3 potters (Adriaen Block, Govert van Nes, Verhaar, Huybert) all spelled
  uniformly; no variant forms (no *Spronk*, *Grietge*, *Fabricius*, *Machtelt*,
  *Barend*, etc.).
- **Chapter/part structure:** 3 parts, 12 chapters, headings sequential (`## 1.`
  … `## 12.`) with no gaps or duplicates; ends with `*THE END*`.
- **Named-person guard:** zero occurrences of *Vermeer* / *Johannes* / *Reyniersz*
  — the young painter stays unnamed per `DECISIONS.md` [D-0003] (verified by grep).

---

## (b) Continuity questions FLAGGED (not auto-fixed)

Checked against `../../bible/book2-additions.md`, `../../book2/outline.md`,
`../../book2/the-blue-and-the-white.md` (Book 2), and Book One
(`../../manuscript/ultramarine.md`). The manuscript is, notably, **already
consistent** with the bible and with Book 2's ending on every point below — these
are recorded as human-confirmation checkpoints, **not** as detected errors, and
nothing was changed.

1. **Fabritius's goldfinch — held in trust, not owned.** The bible fixes this
   (`book2-additions.md`: "Agatha van Pruyssen gave it into Clara's keeping — not
   ownership"). Book 3 honours it: Agatha, the owner, comes for the panel (ch. 4),
   decides to sell it to the Amsterdam collector but leaves it in the shop through
   autumn for Grietje to copy, and it is crated and taken by the collector's man
   in ch. 8 — Clara never sells or claims to own it. **Consistent.**
2. **No true ultramarine left in Clara's hands.** The bible fixes this — the old
   stone-blue trade is closed, the last reclaimed lapis passed into the young
   painter's picture. Book 3 does **not** reintroduce a hoard: the last true blue
   is explicitly located in the young painter's finished *woman-by-a-window*
   picture, "in a room she would never stand in" (ch. 4), and Clara grinds only
   the fired cobalt (zaffer/smalt) throughout. **Consistent.**
3. **Grietje's "bright things": five, then four.** Book 2 ends with Grietje
   counting **five** (the fifth being her own first fired blue-bird tile). Book 3
   opens with five (ch. 1, the count established at Book 2's close, correctly not
   re-revealed as new), and tracks a deliberate arc: in ch. 8 she gives the fifth
   thing (the fired tile) to Machteld "to keep," leaving four — a chosen act, not
   a drift. **Consistent — confirm the five→four transition reads as intended.**
4. **The unnamed young painter (Vermeer).** Per `DECISIONS.md` [D-0003] he must
   never be named on the page. Verified: zero occurrences of the name or its
   variants; his patron is likewise left generic ("a Delft man"). **Consistent.**
5. **Clara's age.** Book 2 gives Clara "five-and-thirty" (Book 2 ch. 9, spring
   1656). Book 3 spans summer 1656 → autumn 1657 and uses "five-and-thirty" in the
   winter-1656/57 low point (ch. 8) and as Doncker's backward reference in summer
   1657 (ch. 11, "you saw it at five-and-thirty," pointing to when she began
   grinding the grey). Internally coherent (she is 35 turning 36 across the span).
   **Confirm this reading is intended, not an age-drift.**
6. **Doncker controls the *dying* stone-blue, not the *rising* fired-blue.** The
   bible (`book2-additions.md`) says the potters' cobalt comes via a Hamburg/Saxon
   factor "deliberately outside Doncker's lapis/painter-colour network," and that
   Doncker controls the dying stone-blue trade, "not the rising fired-blue one."
   Book 3's central plot is Doncker **attempting to cross that line** — buying the
   independent Saxon cobalt road late in life (ch. 7–8) — and **failing** (the
   Company routes around him, ch. 9). This is a deliberate *extension* of the
   bible's boundary (the antagonist reaching for the trade the bible says was kept
   from him, and being defeated), **not** a contradiction of it: at no point does
   Doncker actually hold the fired-blue trade; his bought road is made worthless.
   **Confirm this is read as the intended pay-off of the bible's boundary, not a
   drift across it.**
7. **Timeline reckoning.** Book 2 ends spring 1656; Book 3 opens summer 1656 and
   closes autumn 1657, with Doncker dying summer 1657 and the freight sailing that
   autumn. The town is described as "three years and more into its twenty years'
   rebuilding" (consistent with Book 2's "three years"). **Confirm the span is the
   intended reckoning.**
8. **Pottery name form — "De Blauwe Hand" vs "the Blue Hand."** As in Book 2, the
   full Dutch name appears and the narration otherwise anglicises it to "the Blue
   Hand" — deliberate house style, matching Book 2's established usage. **Confirm
   the series style guide permits the mixed usage.**
9. **New invented canon in Book 3.** The rival potters and their houses — **Adriaen
   Block** (Molslaan), **Govert van Nes**, **Verhaar**, and van Nes's head painter
   **Huybert** — plus the six-pottery consortium and the shared cobalt factor are
   new invented canon introduced here, logged in `../../DECISIONS.md` (Book-3
   entries). They extend, and do not contradict, the `book2-additions.md` pottery
   world. **Confirm before any Book-4 (none planned — this closes the trilogy).**

---

## (c) Typography note (not a typo — flagged for the conversion pass)

The manuscript uses **straight ASCII quotation marks and apostrophes throughout**
(zero curly/typographic marks) — applied **consistently**, matching Books One and
Two, so it is a house-style choice, not an error, and was deliberately **left
unchanged** to preserve the body byte-for-byte and keep the series uniform. If the
KDP edition is to ship with typographic ("curly") quotes, apply a single global
smart-quotes pass **at ebook-conversion time**, and match whatever Books One and
Two ship with so the series is uniform. This is a formatting decision, out of
scope for a byte-preserving manuscript build.

---

## ⚠ This does NOT replace a professional proofread

**This pass was performed by an automated reading and does not substitute for a
professional, native-speaker proofread and copy-edit.** It catches mechanical and
continuity-consistency issues at the level a careful machine read can; it does
**not** vouch for register, idiom, period diction, rhythm, or the subtle
line-level choices a human editor would weigh, nor for factual/historical fidelity
beyond the series bible. **A human native-speaker proofread remains a required
gate before publication** (consistent with the catalog's standing owner-gate on a
native-speaker pass).
