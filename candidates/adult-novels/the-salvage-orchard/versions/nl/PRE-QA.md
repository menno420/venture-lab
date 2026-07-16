# PRE-QA — *De geborgen boomgaard* (mechanical pre-annotation)

> **DISCLAIMER.** Mechanical pre-annotation by an AI (not a native speaker);
> does **NOT** substitute for or clear the §7 native-speaker proofread gate —
> owner sign-off still required. Everything below is a *candidate spot* for a
> human to check, produced by consistency-based static analysis of the actual
> manuscript (`de-geborgen-boomgaard.md`) cross-read against `NOTES.md`. It
> finds nothing about idiom, naturalness, or register *quality* — only
> mechanical consistency an agent can legitimately verify. **hunspell nl_NL is
> not installed in this environment, so NO spellcheck pass was run**; there is
> no candidate-misspelling list here, only the consistency checks below.

Purpose: shrink the proofread read from a cold 15,750-word pass to a guided
one. Line numbers are 1-based in `de-geborgen-boomgaard.md`; paragraphs sit on
single lines, so a line number pins a paragraph.

---

## 1. Pronoun-strategy consistency — the load-bearing decision

`NOTES.md` commits Ash Okafor to **hen / hen / hun** (subject/object/
possessive) with **singular verb agreement** and possessive **`Ash'`** (sibilant
apostrophe), and claims *"no she/he slippage anywhere."* An AI cannot judge
whether a given `hij/zij/haar` reads as slippage — that needs a native ear on
the antecedent — but it **can** enumerate every place the check is due.

- **Subject `Hen` + singular verb — spot-confirm the agreement holds.** e.g.
  line 29 *"Hen liet zichzelf binnen…"*, line 49 *"Hen liep de rijen eenmaal
  langs…"*. These are the sentences `NOTES.md`'s *"hen liep"* rule governs.
- **Possessive `Ash'` (straight apostrophe) — 8 occurrences, all one form:**
  lines 27, 93, 125, 183, 187 (×3), 281. No `Ash's`/`Ashs` variant appears.
  Consistent; confirm the apostrophe form reads right in each.
- **43 sentences contain BOTH `Ash` and a gendered 3rd-person pronoun
  (`hij/zij/haar/hem`).** In every one the pronoun *should* point at a tree
  (trees are `hij` in this text — *"hij bloeide"*, *"de boom had zijn
  schouders"*), a feminine-gender noun (*"de kwekerij … uit haar jasje"*), or
  another character (Nef/Marisol = *ze/haar*) — **never at Ash**. Confirm the
  antecedent on each. Lines: 23, 29, 49, 71, 93, 95, 99, 105, 107, 113, 117,
  119, 121, 125, 127, 133, 135, 175, 185, 187, 201, 253, 257, 283, 295, 297,
  299, 301, 315, 327, 329, 331, 341, 345, 349, 351, 357, 385, 413, 419, 429,
  433, 439. (Sampled: line 23 *"zoals hun grootmoeder"* = Ash's, correct; line
  95 *"Ash keek op haar neer"* = down at Nef, correct. No slip found in the
  samples; the full 43 still want a native pass — this list makes it a
  finite check, not a re-read.)

## 2. Coined-name consistency

- **`Enthoutbibliotheek` capitalization is split.** Lowercase *enthoutbibliotheek*
  at lines 307 (ch-9 title), 321, 387, 437; **capitalized `Enthoutbibliotheek`
  once, line 413** (ch 11). `NOTES.md`'s glossary lemmatizes it capitalized
  (*de Enthoutbibliotheek*). Decide once: proper noun (cap everywhere) or common
  noun (lowercase everywhere) — line 413 is the current outlier.
- Toponyms checked and **internally consistent** (one spelling each):
  *de Geborgen Boomgaard* (4, always capitalized — no lowercase running-text
  variant), *de Wagenwerf/de werf* (7), *de Molenbeekvlakte* (7),
  *het Molenbeekrak* (1), *de Ketelstraat* (11), *de Peilnacht* (2),
  *de Weerbaarheidsverordening* (1), *het beheerconvenant* (1, lowercase as
  glossed). No action beyond a glance.

## 3. Verbatim-motif punctuation drift (confirm intentional)

`NOTES.md` says two craft sentences are *"held verbatim at every return."* They
are close but **not byte-identical** across returns — likely deliberate
tightening, but a native eye should confirm it's craft, not drift:

- *"Een ent is een gift, of hij sterft."* — full form at **line 129** and
  **line 299**; shortened to *"Een ent is een gift."* at **line 349**; embedded
  lowercase echo *"…want — een ent is een gift."* at **line 189**.
- The living-layer sentence — canonical three-full-stop form only at **line 421**
  (ch 12): *"Leg de levende laag tegen de levende laag. Sluit de lucht buiten.
  En dan wachten."* At **line 49** (ch 1) and **line 189** (ch 5) it appears
  comma-spliced and continues differently. If the intent is "prose-embedded
  early, freestanding by ch 12," fine — flagging so it's a decision, not an
  accident.

## 4. Mechanical nits

- **Quote system is clean and consistent:** straight apostrophe throughout for
  dialogue (`'…'`), possessive (`Ash'`), and Dutch plural (`silo's`) — **303**
  straight apostrophes, **zero** curly quotes. **Two** straight double-quotes,
  both at **line 283** (`"toekomstige reservecapaciteit"`) — the *only* place a
  quoted phrase uses double quotes; comparable quoted phrases elsewhere use
  single quotes (line 5 `'strategische reserve'`, line 37 `'bewijs van bestaand
  gebruik'`). Normalize line 283 to single quotes unless intended.
- **Doubled-word scan is low-value in Dutch** (adjacent repeats like *dat dat,
  die die, het het, op op, voor voor, haar haar, ze ze* are grammatical here).
  Candidates surfaced — lines 89, 169, 187, 197, 217, 221, 243, 323, 327, 329,
  385, 387 — were spot-checked and read as grammatical; no true doubling found.
  Listed only so the human can skip them knowingly.

## 5. Word-count expansion seams (+4.7% over the 15,045-word EN source)

`NOTES.md` flags ~707 surplus words for the proofread pass to confirm none is
calque padding. The densest single paragraphs — the likeliest place surplus
concentrates — are **line 187 (297 words)**, **line 385 (262)**, **line 111
(254)**, **line 71 (227)**, **line 221 (225)**. Compare each against its EN
counterpart paragraph in `../../en/the-salvage-orchard.md`; if the NL paragraph
carries the story in the same beats, the expansion is honest translation, not
padding. (An AI cannot tell padding from faithful expansion — this only
isolates *where* to look.)
