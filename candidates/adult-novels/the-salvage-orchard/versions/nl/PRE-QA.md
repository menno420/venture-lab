# PRE-QA — *De geborgen boomgaard* (mechanical pre-annotation)

> **DISCLAIMER.** Mechanical pre-annotation by an AI (not a native speaker);
> does **NOT** substitute for or clear the §7 native-speaker proofread gate —
> owner sign-off still required. Everything below is a *candidate spot* for a
> human to check, produced by consistency-based static analysis of the actual
> manuscript (`de-geborgen-boomgaard.md`) cross-read against `NOTES.md`. It
> finds nothing about idiom, naturalness, or register *quality* — only
> mechanical consistency an agent can legitimately verify. A mechanical
> **hunspell nl_NL spellcheck pass was subsequently run — see §6** for the
> candidate-misspelling list; §§1–5 below are the consistency checks.

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

---

## 6. Mechanical spellcheck pass — nl_NL hunspell (candidate misspellings)

> **Header.** Tool: **spylls 0.1.7** (pure-Python hunspell engine). Dictionary:
> **OpenTaal / LibreOffice `nl_NL` hunspell v2.20.21 (2021-07-03)**, 180,715
> stems, from `raw.githubusercontent.com/LibreOffice/dictionaries/master/nl_NL/`.
> Run date: **2026-07-16 (UTC)**. Manuscript: `de-geborgen-boomgaard.md`.
> **Total tokens checked: 15,717. Total unique flags: 165. Genuine candidates
> after filtering: 0 clear misspellings; 2 nonstandard-form items for a native
> register glance.** Supersedes the preamble "no spellcheck pass was run" note.
>
> **DISCLAIMER (unchanged).** Mechanical flags are *candidates*, not a quality
> attestation, and do **not** clear the §7 native-speaker proofread gate. hunspell
> nl_NL does no free compounding, so it flags every valid novel compound; those
> are filtered below.

### 6a. Genuine candidate misspellings (ranked)

**No high- or medium-confidence misspellings found.** Two residual flags are
nonstandard *forms* rather than typos — kept for a native register glance, not
proposed as corrections:

| Word | ×  | Line | Note | Confidence |
|------|----|------|------|-----------|
| `anderser` | 1 | 425 | Comparative of *anders* (*"…en zou nog anderser worden."*). Standard Dutch has no comparative of *anders* (one would say *nog anders / meer anders*); reads as a deliberate literary coinage, parallel to `warere` L387. Native reader confirms it's intended. | LOW — likely deliberate |
| `gewrakte` | 2 | 327, 413 | *"de door de storm gewrakte boom"* — participle used = "wrecked" (from *wrak*, wreck), thematically apt for a salvage novel; *wraken* normally means "to challenge/reject" (→ `gewraakte`). Register choice, not a spelling slip. | LOW — likely deliberate coinage |

`warere` (L387, *"het warere antwoord"*) is a **correctly formed** comparative of
*waar* (true) → *warer* → inflected *warere*; dict gap only. Not flagged.

### 6b. Excluded tally (auditable — see `categorize.py`)

Of 165 unique flags:

| Bucket | unique | occ | basis |
|--------|-------:|----:|-------|
| Proper nouns (names / places) | 35 | 273 | `NOTES.md` glossary + name list (Ash, Marisol, Nef, Okafor, Duplessis, Okonjo, Szabó, Bae, Ibadan, Molenbeekvlakte, Wagenwerf, Enthoutbibliotheek, Ashmead's Kernel, Kustkorps, …) |
| Documented craft/glossary coinages | 25 | 56 | `NOTES.md` glossary (enthout, ent, spleetenten, chip-oculatie, omgeënt, wolfsappels, wolfsboom, weercollectief, belboom, peillat, kloosterpeer, kweepeerpasta, leerrij, …) |
| Emphatic acute-accent forms (valid klemtoon) | 4 | 4 | `díe`, `míj`, `gáán`, `zíjn` — strip accent → known word |
| Casing artifact (`Eén` = sentence-initial `één`) | 1 | 10 | dict has `één`; only the capitalized accented form fails |
| Valid productive compounds/derivations (dict gap) | 98 | 131 | transparent Dutch compounds/derivations the dict lacks (westhek, noordhek, zuidhek, ciderhuis, dakploeg, tramhal, waspotten, melganzenvoet [real plant], onovertuigd, herplante, gegeleerd, bedraadde, messchuwe, …) — reviewed, none typo-shaped |

**Net: 165 flags → 0 clear misspellings** (2 nonstandard forms flagged for a
register glance only). Consistent with a carefully edited literary translation.
