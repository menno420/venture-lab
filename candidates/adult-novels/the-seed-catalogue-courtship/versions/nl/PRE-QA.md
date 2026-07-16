# PRE-QA — *Liefde in de kantlijn* (mechanical pre-annotation)

> **DISCLAIMER.** Mechanical pre-annotation by an AI (not a native speaker);
> does **NOT** substitute for or clear the §7 native-speaker proofread gate —
> owner sign-off still required. Consistency-based static analysis of the actual
> manuscript (`liefde-in-de-kantlijn.md`) cross-read against `NOTES.md`;
> candidate spots only, no judgment of idiom or register quality. A mechanical
> **hunspell nl_NL spellcheck pass was subsequently run — see §6** for the
> candidate-misspelling list; §§1–5 below are the consistency checks.

The book is **epistolary**, so `NOTES.md` names its real work as *"register per
correspondent."* That axis is a native-ear judgment an AI cannot make — but the
salutation/closing register is a *mechanical spine* an AI can map exactly, and
mapping it isolates the handful of spots where the human's read is actually
due. Line numbers are 1-based in `liefde-in-de-kantlijn.md`.

---

## 1. Epistolary register spine — closings arc, with the spots to confirm

Every closing in the Tull↔Prowse correspondence, in order:

- **Formal phase:** `Hoogachtend` — lines 120, 142, 177, 213.
- **Warming:** `Geheel de uwe` — lines 244, 263, 282, 303.
- **Intimate:** `De uwe` — line 324, then **← line 359 steps back to `Geheel de
  uwe`**, then `De uwe` sustained: 395, 421, 438, 467, 486, 504, 523, 542.

Two candidate spots where the closing runs **against** the warming trend —
confirm each is intentional per-correspondent pacing, not drift:

- **Line 359 `Geheel de uwe`** lands *after* line 324's `De uwe`. Likely the two
  writers warm at different rates (359 is the other sender); confirm it's meant.
- **Line 645 `Hoogachtend`** to *heer Tull*, long after `De uwe` was
  established, reads as a late **cooling** — plausibly the rupture beat around
  line 679 (*"Dat is de wond, als u haar opgemeten wilt hebben…"*). Confirm the
  formal snap is deliberate characterization, not an inconsistency.
- **Not reversions:** the `Hoogachtend` at lines 553 and 566 are addressed to a
  *third party* (line 558 `Geachte heer Herring`), correctly formal — flagged so
  they aren't mistaken for a Tull↔Prowse retreat.

**Salutation stays invariant `Geachte heer Tull` / `Geachte mejuffrouw Prowse`
throughout** — the opening never shifts to *Beste/Lieve/Waarde* even as the
closings reach `De uwe`. That opening-formal / closing-intimate tension is a
period-register choice; confirm it was intended to hold `Geachte` the whole way
(a native reader may otherwise expect `Beste` once intimacy is on the page).
The closing `De uwe` also carries the book's thematic double — the unclaimed
open order *"de uwe"* at line 171 — so its consistency is load-bearing.

## 2. `belasting` — load vs tax dual sense (7 sites, confirm each reads clean)

`NOTES.md` puts *belasting* in the engineer's register (**structural load**:
*belasting / dragend / berekend op belasting*). But *belasting* also means
**tax** in Dutch, and the manuscript uses **both** senses on purpose — so each
site wants a glance that context disambiguates it:

- **Structural load:** line 417 (*belasting houdt*), 419 (*de belasting
  eronder*), 519 (*berekend op belasting*), 540 (*Uw alinea over belasting*),
  639 (*welk onderdeel de belasting draagt*), 711 (*belastinggevallen* =
  load-cases).
- **Tax:** line 835 (*de man schat belasting voor de kost* = assesses tax for a
  living).

No inconsistency claimed — this is exactly the ambiguous word where a native ear
confirms no site reads in the wrong sense.

## 3. Seed-trade / commercial-register terms — consistent

`bestelformulier` (3), `kiemkracht` (6), `accessies` (5), `zaadmagazijn` (7) each
appear in one spelling; the salutation/closing lemmas above are internally
consistent (`Hoogachtend` 7, `Geheel de uwe` 5, `De uwe` 10). No variant
inflections detected. A glance to confirm the trade terms land correctly is
enough; nothing to normalize.

## 4. Mechanical nits

- **Quote system is clean:** 193 straight apostrophes, zero double-quotes, zero
  curly quotes.
- **Doubled-word scan (low-value in NL):** candidates at lines 224, 498, 608,
  835 are all *het het* — grammatical adjacent repeats. No true doubling found.

## 5. Word-count expansion seams (+3.3% over the 15,133-word EN source)

Densest paragraphs, compare against `../../en/the-seed-catalogue-courtship.md`:
**line 657 (193 words)**, **line 711 (192)**, **line 604 (183)**, **line 300
(169)**, **line 608 (168)**, **line 238 (153)**. The +3.3% is mid-band; if each
carries the EN beats, the expansion is faithful. An AI can only point to where;
the native pass judges padding vs faithful expansion.

---

## 6. Mechanical spellcheck pass — nl_NL hunspell (candidate misspellings)

> **Header.** Tool: **spylls 0.1.7** (pure-Python hunspell engine). Dictionary:
> **OpenTaal / LibreOffice `nl_NL` hunspell v2.20.21 (2021-07-03)**, 180,715
> stems, from `raw.githubusercontent.com/LibreOffice/dictionaries/master/nl_NL/`.
> Run date: **2026-07-16 (UTC)**. Manuscript: `liefde-in-de-kantlijn.md`.
> **Total tokens checked: 15,262. Total unique flags: 116. Genuine candidates
> after filtering: 0.** Supersedes the preamble "no spellcheck pass was run" note.
>
> **DISCLAIMER (unchanged).** Mechanical flags are *candidates*, not a quality
> attestation, and do **not** clear the §7 native-speaker proofread gate. hunspell
> nl_NL does no free compounding, so it flags every valid novel compound; those
> are filtered below.

### 6a. Genuine candidate misspellings (ranked)

**None found.** Every residual flag resolves to a proper noun, a documented
seed-trade/commercial coinage, a period abbreviation, or a valid transparent
Dutch compound/derivation the dictionary simply lacks. No typo-shaped token
survived review. (This is the cleanest of the four manuscripts.)

### 6b. Excluded tally (auditable — see `categorize.py`)

Of 116 unique flags:

| Bucket | unique | occ | basis |
|--------|-------:|----:|-------|
| Proper nouns (names / places) | 38 | 222 | `NOTES.md` glossary + names (Prowse, Marchfield, Saltmarsh, Dilys, Deane, Whitlow, Herring, Herefordshire, Pring, Coker, Norwich, Fakenham, Mowbray & Kett, cultivar names 'Maanglans'/'Veenreus'/'Norfolkse Morgen', …) |
| Documented craft/glossary coinages | 14 | 29 | `NOTES.md` glossary (kantlijn, bestelformulier, kiemkracht, accessies, zaadmagazijn, catalogusvast, zoutroze, hamerprijs, ingenieurscursief, veredelaarster, stenosleutel, …) |
| Abbreviations / roman numerals (non-lexical) | 9 | 36 | `nr`, `mej`, `mevr`, `incl`, `ca`, `Ontv`, `ii`, `iii`, `iv` |
| Emphatic acute-accent forms (valid klemtoon) | 1 | 1 | `hád` — strip accent → known word |
| Casing artifact (`Eén` = sentence-initial `één`) | 1 | 2 | dict has `één`; only the capitalized accented form fails |
| Valid productive compounds/derivations (dict gap) | 53 | 81 | transparent Dutch compounds the dict lacks (middenbed, tuinmanshuis, oostbedden, theekas, retourbak, herbeglaasd, herbeglazing, herbinden, herfstzaai, hervulling, verpulper, wanmachines, mooiweerconstructie, zilverberijpt, …) — reviewed, none typo-shaped |

**Net: 116 flags → 0 genuine candidate misspellings.**
