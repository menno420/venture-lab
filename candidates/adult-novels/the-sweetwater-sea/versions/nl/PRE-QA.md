# PRE-QA — *De zoete zee* (mechanical pre-annotation)

> **DISCLAIMER.** Mechanical pre-annotation by an AI (not a native speaker);
> does **NOT** substitute for or clear the §7 native-speaker proofread gate —
> owner sign-off still required. Consistency-based static analysis of the actual
> manuscript (`de-zoete-zee.md`) cross-read against `NOTES.md`; candidate spots
> only, no judgment of idiom or register quality. A mechanical **hunspell nl_NL
> spellcheck pass was subsequently run — see §6** for the candidate-misspelling
> list; §§1–5 below are the consistency checks.

Line numbers are 1-based in `de-zoete-zee.md`; one line ≈ one paragraph. This is
the lowest-expansion NL edition in the catalog (**+1.5%**), so the seams are
tight and there is little surplus to isolate — reflected in §4.

---

## 1. Period fishery / waterworks craft-neologism inventory

`NOTES.md` weights the proofread pass toward *"the period fishery/waterworks
register (besomming, boeten, tanen…)."* An AI can verify these specialized terms
are spelled consistently and hand the human the exact sites to confirm each is
the right word in context (not the register-quality judgment, which stays the
owner's):

- **`besomming`** (catch-proceeds share) — 3×; **`boekstaving`** (the clerk's
  record) — 3×; **`teenwilg`** (osier) — 1×; **`wiepen`** — 2×; **`gesjord`**
  (lashed) — 2×. Each appears in one spelling only; no variant inflection
  detected. Confirm the singletons (`teenwilg`) read correctly where they land.
- **`tanen` (net-tanning) returns 0 exact hits** — likely present only inflected
  (e.g. *getaand/taande*) rather than as the bare infinitive the glossary lists.
  Not necessarily missing; worth a native glance to confirm the tanning motif is
  actually on the page in some form.

## 2. `steunwet` capitalization — checked, reads intentional

The manuscript itself disambiguates: **line 107** introduces the full proper
name *"de **Zuiderzeesteunwet**, de wet van [nineteen-twenties]… die iedereen
kortweg de **steunwet** noemde"* — i.e. the capitalized compound is the law's
name, and the lowercase *steunwet* is explicitly the colloquial short form.
Subsequent lowercase uses (lines 209, 341) are that short form. So the
`NOTES.md` glossary's capitalized *Steunwet* is just the lemma; the text's
lower/upper split is **deliberate and internally explained** — no normalization
needed. Flagged so the human can skip re-checking these 4 sites.

## 3. Mechanical nits

- **Quote system is clean:** **196** straight apostrophes, **zero** double-quotes,
  zero curly quotes — uniform single-quote dialogue throughout.
- **Doubled-word scan (low-value in NL):** the one that looks like an error,
  **line 69 `Van Van`**, is grammatical — *"'Van Van der Oord. Wieringers
  voornamelijk.'"* = the preposition *Van* ("of/from") followed by the surname
  prefix *Van der Oord*. The rest (lines 23 *ze ze*, 171/217 *je je*, 255/335
  *het het*) are grammatical adjacent repeats. No true doubling found; a
  demonstration of why this check is noise in Dutch — listed so it's skipped
  knowingly.

## 4. Word-count expansion seams (+1.5% over the EN source — the tightest in the catalog)

With only ~1.5% surplus there is little padding surface; `NOTES.md` reports the
count is at the very bottom of the measured band and two forces (compression vs
expansion) roughly cancel. Densest paragraphs, if the owner still wants to spot
the surplus, compare against `../../en/the-sweetwater-sea.md`: **line 339 (379
words)**, **line 33 (267)**, **line 331 (254)**, **line 267 (250)**, **line 215
(246)**, **line 291 (246)**. Given the +1.5% overall, calque-padding risk here is
lowest of the four titles carrying a PRE-QA note.

## 5. Not a proofread item — pointer only

`NOTES.md`/§5 flag a **title-collision** risk (a same-register Dutch novel
*Zoete zee* / A. Kok on the shelf). That is a market/title-ratify owner gate in
the packet, **not** a mechanical proofread item, and is **not** addressed or
cleared here — noted only so it isn't mistaken for something this pass covered.

---

## 6. Mechanical spellcheck pass — nl_NL hunspell (candidate misspellings)

> **Header.** Tool: **spylls 0.1.7** (pure-Python hunspell engine). Dictionary:
> **OpenTaal / LibreOffice `nl_NL` hunspell v2.20.21 (2021-07-03)**, 180,715
> stems, from `raw.githubusercontent.com/LibreOffice/dictionaries/master/nl_NL/`.
> Run date: **2026-07-16 (UTC)**. Manuscript: `de-zoete-zee.md`.
> **Total tokens checked: 15,430. Total unique flags: 91. Genuine candidates
> after filtering: 0.** This section adds the spellcheck pass the §Preamble
> explicitly deferred ("hunspell nl_NL is not installed here, so NO spellcheck
> pass was run").
>
> **DISCLAIMER (unchanged).** Mechanical flags are *candidates*, not a quality
> attestation, and do **not** clear the §7 native-speaker proofread gate. hunspell
> nl_NL does no free compounding, so it flags every valid novel compound; the
> period fishery/waterworks register (§1) is exactly this class and is filtered,
> not corrected.

### 6a. Genuine candidate misspellings (ranked)

**None found.** The residual flags are dominated by the period
fishery/waterworks register that §1 already inventoried and by valid nautical
compounds/derivations. Every one reviewed on context reads as a real or
transparently-formed Dutch term (e.g. `afvieren` = to pay out a rope, `bijgewarpt`
= warped alongside, `geklank` = clanging, `moeringen` = moorings, `landmaken` =
land-reclaiming, `te-veelheid` = excess-ness). No typo-shaped token survived.

### 6b. Excluded tally (auditable — see `categorize.py`)

Of 91 unique flags:

| Bucket | unique | occ | basis |
|--------|-------:|----:|-------|
| Proper nouns (names / places) | 16 | 53 | `NOTES.md` name & place lists (Trijn, Vlieter, Wieringer(s), Makkumer, Rotgans, Snoek, Sint-Anthonis, Vliekant, Vollenhoofse, Waddenman, MUZ, WR, …) |
| Documented craft/glossary coinages | 23 | 37 | `NOTES.md` glossary + §1 craft-neologism inventory (zouting, boekstaving, steunwet, Zuiderzeesteunwet, besomming, boeten, meitrek, kipkarren, kopbanken, steenstorters, telloon, spoeltobbe, netvallen, moeringen, ansjoviszouter, dakpannenrood, …) |
| Abbreviations / non-lexical | 2 | 2 | `MUZ`, `WR` (also proper-ish; counted once) |
| Emphatic acute-accent forms | 0 | 0 | — |
| Casing artifact (`Eén` = sentence-initial `één`) | 1 | 3 | dict has `één`; only the capitalized accented form fails |
| Valid productive compounds/derivations (dict gap) | 49 | 52 | transparent Dutch/nautical compounds the dict lacks (afvieren, bijgewarpt, gekettingd, geklank, groenruggig, halfverdronken, houtklovend, kerkjas, mastbok, meslemmet, paaizanden, terugroeiend, uitgemiddeld, zoutkoninkrijk, …) — reviewed, none typo-shaped |

**Net: 91 flags → 0 genuine candidate misspellings.** The +1.5% tightest-seam
edition also produced the fewest raw flags, as expected for a narration-heavy text.
