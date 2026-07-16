# PRE-QA — *De Marmeladepost* (mechanical pre-annotation)

> **DISCLAIMER.** Mechanical pre-annotation by an AI (not a native speaker);
> does **NOT** substitute for or clear the §7 native-speaker proofread gate —
> owner sign-off still required. Consistency-based static analysis of the actual
> manuscript (`de-marmeladepost.md`) cross-read against `NOTES.md`; candidate
> spots only, no judgment of idiom or register quality. A mechanical **hunspell
> nl_NL spellcheck pass was subsequently run — see §6** for the
> candidate-misspelling list; §§1–5 below are the consistency checks.

Line numbers are 1-based in `de-marmeladepost.md`; one line ≈ one paragraph.

---

## 1. The coined title phrase — single deliberate mint (confirmed)

`NOTES.md`: *"the villagers coin the phrase* de marmeladepost *at the show-day
urn in Hoofdstuk elf, exactly as the EN coins 'the marmalade post'."* Verified:
the phrase appears **exactly once in running text, line 521** (ch 11):
*"…bij de ketel de uitdrukking* de marmeladepost *gemunt (Vera hoord…)"*,
italicized as a minting. The book title (`# DE MARMELADEPOST`, line 1) is the
only other instance. So the single in-text coinage is **by design**, matching
the EN — not an under-use. No action; noted so the human doesn't hunt for
"missing" repetitions.

## 2. Two-tier quote system — inner-quote inventory

The manuscript runs a consistent **single-outer / double-inner** quote nesting:
dialogue uses straight single quotes (`'…'`), and a quotation *inside* speech —
a remembered saying, a written label, a phrase being named — uses straight
double quotes (`"…"`). Char inventory: **502** straight apostrophes, **26**
straight double-quotes, **zero** curly quotes.

An AI can't certify the nesting reads naturally, but it can hand the human the
**complete list of the 26 inner-quote sites** so the two-tier convention is
spot-checked, not re-derived: lines **141** (`"Seville & Kapelklokken"`), **202**
(nested inside Dilys's speech, three inner quotes), **204** (`"de juiste
manier"`), **222** (`"Stroperig,"`), **292** (`"voor het geval van
watersnood"`), **376** (`"Donkere Seville…"`), **396** (the rubber-stamp text),
**404** (`"ongeveer drieduizend"`), **444** (the show notice, three inner
quotes), **495** (`"Het kantoor voor dode brieven"`, `"achterste bladzijden"`).
Confirm each inner quote is genuinely a quote-within-speech (double) and not a
top-level line that should be single.

## 3. Register per relationship (je / u) — the load-bearing decision

`NOTES.md` fixes address forms per relationship: *"Vera → young Draycott 'je' +
'agent', Draycott → Vera 'u'; Ruth's letter and graveside words to Walter 'jij'
(intimate)."* This is exactly the axis a native reader must verify and an AI
cannot. No mechanical inconsistency is claimable here — flagging it as the
**#1 human-judgment item**: read Vera↔Draycott exchanges and Ruth→Walter
passages for a consistent je/u/jij choice per pair, since a single slip
(u where jij was established) is the kind of thing this cozy register lives on.

## 4. Mechanical nits

- **Doubled-word scan (low-value in NL):** candidates at lines 149, 161
  (*het het* — grammatical), 200 (*haar haar* — "her hair"/"her her", read as
  grammatical), 382, 459 (*je je* — grammatical). No true doubling found;
  listed so they can be skipped knowingly.
- No curly-quote contamination; the straight-quote system is uniform.

## 5. Word-count expansion seams (+4.0% over the 15,040-word EN source)

`NOTES.md` notes this sits slightly above the catalog's earlier NL ratios and is
already flagged for the proofread pass. Densest paragraphs (where surplus most
plausibly concentrates), compare against `../../en/the-marmalade-post.md`: **line
485 (321 words)**, **line 376 (263)**, **line 459 (232)**, **line 145 (202)**,
**line 495 (196)**, **line 396 (192)**. If each carries the EN beats, the
expansion is faithful, not padding — an AI can only point; the native pass
decides.

---

## 6. Mechanical spellcheck pass — nl_NL hunspell (candidate misspellings)

> **Header.** Tool: **spylls 0.1.7** (pure-Python hunspell engine). Dictionary:
> **OpenTaal / LibreOffice `nl_NL` hunspell v2.20.21 (2021-07-03)**, 180,715
> stems, fetched from
> `raw.githubusercontent.com/LibreOffice/dictionaries/master/nl_NL/`. Run date:
> **2026-07-16 (UTC)**. Manuscript: `de-marmeladepost.md`. **Total tokens
> checked: 15,573. Total unique flags: 140. Genuine candidates after filtering:
> 2** (1 high-confidence, 1 medium). This supersedes the preamble note that "no
> spellcheck pass was run" — a real hunspell dictionary pass **was** now run.
>
> **DISCLAIMER (unchanged).** Mechanical flags are *candidates*, not a quality
> attestation, and do **not** clear the §7 native-speaker proofread gate. hunspell
> nl_NL does not do free compounding, so it flags every novel-but-valid Dutch
> compound; those are filtered below, not corrected.

### 6a. Genuine candidate misspellings (ranked)

| Word | ×  | Line | Best-guess correction | Confidence / note |
|------|----|------|-----------------------|-------------------|
| `schifte` | 1 | 396 | **`schiftte`** | **HIGH.** Past tense of *schiften* (to curdle/turn). Stem `schift` ends in -t, so past = `schift`+`te` = **`schiftte`** (double t). Dict confirms: `schiftte` is known, `schifte` is not. Context L396: *"…het schifte tot het andere, en ze schreef me…"* — clearly the verb. |
| `geproefleesd` | 1 | 256 | **`proefgelezen`** | **MEDIUM.** Past participle of *proeflezen* (to proofread). *lezen* is a strong verb → participle `proefgelezen`; `geproefleesd` both mis-places *ge-* and weakens the strong verb (`leesd` for `gelezen`). Context L256: *"…parochieblad dat ze in haar eerste maand had geproefleesd…"*. Correct form `proefgelezen` is itself a dict gap, so this rests on grammar, not the dict. |

### 6b. Reviewed and kept (residual OPEN flags that are NOT misspellings)

Three residual flags looked typo-shaped but read as intentional on context —
listed so the human doesn't re-flag them:

- `officialiteit` (2×, L87/L459) — used consistently for "officialdom/officialness"
  (*"de vorm van officialiteit zoals een lokeend de vorm heeft van een eend"*).
  Rare real word / deliberate register coinage, not a typo — native register glance only.
- `gegis` (2×, L105/L254) — well-formed *ge-* collective of *gissen* ("that
  guessing", like *gedoe/gezeur*). Valid.
- `dichtmaast` (1×, L461) — 2nd-person of *dichtmazen* (to close a net-hole by
  meshing), fits the postal/handwork register. Valid.

### 6c. Excluded tally (auditable — see `categorize.py`)

Of 140 unique flags, filtered out as **not** candidate misspellings:

| Bucket | unique | occ | basis |
|--------|-------:|----:|-------|
| Proper nouns (names / places / institutions) | 46 | 342 | `NOTES.md` name & topography lists (Vera Cusworth, Dilys Pring, Finch, Little Dunnock, Truro, Porthgullow, St Botolph's, Women's Institute, Returned Letter Centre, Lyle's, …) |
| Documented craft/glossary coinages | 25 | 38 | `NOTES.md` glossary + this file §1 (marmeladepost, bewaarla, bewijsla, baliesteek, pakkerssteek, strafport, retourenhal, sevilla's, klokkensnit, citroencurd, Finch-gedachtenisbeker, …) |
| Abbreviations / non-lexical | 3 | 3 | `ca`, `Mr`, `St` |
| Emphatic acute-accent forms (valid klemtoon) | 9 | 9 | `míj`, `míjn`, `wíj`, `wóórd`, `zíjn`, `gepóste`, `gevráágd`, `gewéten`, `áfgemaakt` — strip accent → known word |
| Casing artifact (`Eén` = sentence-initial `één`) | 1 | 5 | dict has `één`; `Eén` fails only on capitalization of the accented vowel |
| Valid productive compounds/derivations (dict gap) | 54 | 65 | transparent Dutch compounds the dict lacks (dorpshuissleutel, marktwoensdag, inmaakpan, kerkraamvuur, voetpadgeschil, gebarcodeerde, herschikten, onverzendbaren, …) — reviewed, none typo-shaped |

**Net: 140 flags → 2 genuine candidate misspellings** (`schifte`, `geproefleesd`).
Neither is in a name, address, or the load-bearing clue lines. Native proofreader
confirms/corrects.
