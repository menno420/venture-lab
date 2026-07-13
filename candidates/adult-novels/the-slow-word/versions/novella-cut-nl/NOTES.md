# Novella cut — Nederlandse editie (NL) — NOTES

## What this is

A complete literary Dutch (Netherlands register) translation of the novella
cut. Source text: `../novella-cut/the-slow-word-novella.md` at its merged
state on `main` (landed via PR #111; verbatim `wc -w` 18,986 words including
title, front matter, and chapter headings). All 12 chapters translated in
full — every line finished prose, no summary placeholders. The EN novella cut
stays the source of truth for the story; fixes propagate EN → NL, never the
reverse (per `../README.md` convention, `en/` master → novella cut → this
edition).

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: versions
across "different angles, audiences, lengths" — this version adds a
different-**language** audience).

## Honest word count

Verbatim `wc -w` on 2026-07-13 (includes title, front matter, and chapter
headings):

```
19467 candidates/adult-novels/the-slow-word/versions/novella-cut-nl/het-trage-woord.md
```

Versus the EN source's 18,986. Dutch running ~2.5% longer than the English
is normal for this language pair (Dutch periphrasis around English compact
verbs outweighs its compound nouns); the count is reported as measured, not
targeted.

## Title decision

**Chosen: *Het trage woord*.**

The book's central image is a single *word* said too slowly for a lifetime —
one phoneme per century, "the first sound of the answer," and the closing
line of the logbook entry, "The word held" (rendered *Het woord hield
stand*, which the title sets up directly). Alternatives considered:

- ***De trage taal*** — attractive alliteration, but shifts the image from
  *word* to *language*; the Slow Ones explicitly have "no words, only
  relations," so "taal" claims more than the text does, and the title/ending
  echo is lost.
- ***Het langzame woord*** — semantically fine; "langzaam" is flatter and
  more colloquial than "traag," which carries the deliberate, viscous
  quality the register needs.
- ***Een woord van eeuwen*** — evocative but editorializing; drops the
  deliberate plainness of the EN title.

## Glossary — recurring term choices (kept consistent throughout)

| EN | NL | Note |
|----|----|------|
| the Slow Ones | de Tragen | Capitalized as a name, mirroring Marcus "giving it back with capitals in it" (Ch 6) |
| the slow word / "The word held" | het trage woord / "Het woord hield stand" | Title anchor, Ch 12 |
| the ears (of the sky) | de oren (van de hemel) | *O taliga o le lagi* kept verbatim |
| the Metronome | de Metronoom | |
| held stone(s) | neergelegde steen/stenen | "a hand sets a stone down" → "een hand legt een steen neer"; "ten thousand years of held stone" → "tienduizend jaar neergelegde steen" |
| phoneme | foneem | |
| polarisation angle | polarisatiehoek | |
| steady (the question's key word) | standvastig | "Is there anyone there steady enough to answer?" → "Is daar iemand die standvastig genoeg is om te antwoorden?" |
| continuous (the crueller variant) | bestendig | Ch 7/10/11; Lani's Ch 11 paraphrase uses "lang genoeg" as the EN there uses plainer diction |
| deep time | de diepe tijd | |
| error-correcting code | foutcorrigerende code | |
| call and response | beurtzang (chant contexts) / aanroep en antwoord (protocol contexts) | Two registers deliberately, as EN moves between ritual and engineering framings |
| checksum | controlesom | |
| keeper | hoeder | Ropati "de bewaarder" (of the fa'alupega) vs. the transmission line's "hoeders" (Lani, Ioane) |
| decommissioning | ontmanteling | |
| the drift / the lean | de drift / de overhelling | |
| wobble (Lani's word) | wiebel | Keeps the one-year-of-physics irreverence |
| grand-niece | achternichtje | Lani addresses Tuli as "tante" |
| causeway | de dam | |
| logbook | het logboek; "het leren boek" for the leather-bound reply book | |

Samoan terms (gafa, fa‘alupega, tulāfale, matai, fale, fono, va, ma‘au,
saofa‘i, fue, aiga, palagi, lavalava, fetū, "Sili") are kept untranslated
exactly as the EN keeps them, with the same in-line glosses and no others
added. All personal and place names unchanged (Tuli/Teuila Va‘a, Lani,
Marcus, Ropati, Fa‘amanu, Malaefou, Sina, Ioane, Ravai, Halvorsen, Vaituga,
Fenua); "Geneva" → "Genève" as standard Dutch exonym. Idioms adapted, not
calqued (e.g. "game of telephone" → "doorfluisterspel"; "You've got a face
on" → "Je hebt een gezicht opstaan"). Forms of address: Tuli uses "u" to
Ropati and he "jij" to her (elder/junior asymmetry); Dr. Ravai uses "u";
Tuli–Marcus and Tuli–Lani are "jij" throughout.

## Market position

- **Format:** novella ebook (reflowable, cover-only production), same tier
  logic as the EN novella cut.
- **Market:** the Dutch-language ebook market (NL/BE) is real but small
  relative to EN; literary SF in translation is a niche within it, and this
  would compete against traditionally published translations. **Price band
  conservatively $3.99–$5.99 equivalent (≈ €3.49–€5.49) — not measured** for
  NL market specifics: no comps pulled for Dutch-language novella ebooks, no
  KDP category/keyword research for the NL storefront done tonight.
- Base-case sales for an unknown author remain ≈ $0, as for every version on
  this shelf; unit economics only, no forecast.

## ⚑ Owner gates and follow-ups

- ⚑ **Publishing stays owner-gated** exactly like the EN master and the EN
  novella cut: no cover art, no pricing set, no KDP submission, no publish
  click without the owner (repo hard rail `docs/conventions.md` §13).
- ⚑ **An NL listing needs its own vetting/keyword rows in
  `docs/publishing/`** — the existing the-slow-word vetting packet and
  keyword map cover the EN title only; a Dutch edition needs its own
  metadata, category, and keyword work for the NL storefront. **Out of scope
  tonight** (docs/publishing/** untouched) — flagged as follow-up for a
  future slice.
- Quality follow-up (normal for translation work): a native-speaker
  proofread pass before any listing is drafted.
