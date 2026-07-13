# Nederlandse editie (NL) — NOTES

## What this is

A complete literary Dutch (Netherlands register) translation of *The Weigh
House*. Source text: `../../en/the-weigh-house.md` at its merged state on
`main` (verbatim `wc -w` 36,427 words after the 2026-07-13 continuity
patch, including title, front matter, and chapter headings). All 16
chapters translated in full — every line finished prose, no summary
placeholders. The EN manuscript stays the source of truth
for the story; fixes propagate EN → NL, never the reverse. The EN
DECISIONS.md explicitly deferred "NL/DE translations … to a follow-on
session (mirrors the childrens-books lane)" — this edition is that
follow-on for NL. Known EN continuity wobble (the Prinsengracht flat in
Ch 2 vs the houseboat from Ch 7 on) was carried over as-is per the
fixes-propagate-EN→NL rule at first landing, not silently repaired.
**RESOLVED 2026-07-13:** the EN master now standardises on the houseboat
on the Kloveniersburgwal (the same resolution the novella cut chose and
documented in its NOTES "Continuity smoothing" section — the houseboat is
load-bearing: Joke is a mooring neighbour, the night sighting happens on
that canal, and the master itself already put Sanne's "own dark window
over the Kloveniersburgwal" from Ch 11 on). The fix has been propagated
EN→NL into this edition in the same change; the seam is closed.

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: versions
across "different angles, audiences, lengths" — this version adds a
different-**language** audience). Like *De papieren sinaasappel*, this is a
market-native translation: the novel is set entirely in Amsterdam — the
Waag on the Nieuwmarkt, the duikteam, the grachtengordel, the Kadaster —
and the EN text glosses Dutch realities that the NL edition simply speaks.

## Honest word count

Verbatim `wc -w` on 2026-07-13, re-measured after the flat/houseboat
continuity patch (includes title, front matter, and chapter headings):

```
36997 candidates/adult-novels/the-weigh-house/versions/nl/de-waag.md
```

Versus the EN source's 36,427 (+1.6%). Slightly below the +2.5% ratio
measured on the catalog's first two NL editions — plausible for this book:
its heavy Dutch-institution vocabulary (duikteam, Kadaster, notaris,
recherche) was already Dutch in the EN and gains no words in translation.
The count is reported as measured, not targeted.

## Title decision

**Chosen: *De Waag*** (subtitle *Een Amsterdamse misdaadroman*). The Waag
on the Nieuwmarkt is the book's own title anchor: it stands over the Ch 1
recovery, over the Ch 4 café scene, and carries the entire Ch 16
meditation (the honest scale, the anatomists' weighing room) — the EN
title "The Weigh House" IS this building, and Dutch readers know it by
this name. Alternatives considered:

- ***De Waag* without subtitle** — rejected: the bare word is a
  searchability handicap (the building itself, plus restaurants/hotels
  named "De Waag", dominate results — the catalog's "Lull" problem in
  Dutch form). The subtitle does the genre work and disambiguates.
- ***Het waaggebouw*** — semantically exact but flat and municipal;
  loses the definite, monumental ring the book trades on.
- ***Zwart water*** — evokes the diving but is generic in the NL
  thriller shelf (existing film/title collisions) and surrenders the
  weighing metaphor that structures the ending.
- ***De lijn*** — the safety-line motif, but far too generic to search
  and claims less than the book is about.

Collision scan for the chosen title is in the vetting packet
(`docs/publishing/vetting/de-waag.md`, dated 2026-07-13): no same-named
Dutch *fiction* title surfaced; nearest book hit is E. Kurpershoek's
*De Waag op de Nieuwmarkt* (nonfiction architecture history of the
building itself — different shelf, different intent).

## Glossary — recurring term choices (kept consistent throughout)

| EN | NL | Note |
|----|----|------|
| the Waag / the weigh house | de Waag / het waaggebouw | Title anchor; EN's "weigh house" gloss dropped (see reversion list) |
| shot line | de daallijn | Diving register |
| tending line / to tend a line | de seinlijn / iemands lijn houden | NL police-diving register; Bram "seint" from the bank |
| line tender | seiner | Ch 11 ("waarom je je seiner absoluut vertrouwde") |
| drysuit / seams | droogpak / naden | "The cold found the seams" → "de kou vond de naden", held at every occurrence |
| regulator | ademautomaat | First stage → eerste trap; second stage → tweede trap |
| weight belt / weights / lead | loodgordel / duiklood / lood | |
| quick-release buckle | snelsluiting | "find the buckle, pull, drop the lead, live" → "vind de gesp, trek, laat het lood vallen, leef" |
| dorsal releases | dorsale sluitingen | Sanne's debrief refrain |
| half-hitch / standing part / tail | halve steek / het staande part / de tamp | Real Dutch knot/rope terms; the killer's signature |
| team issue | teamuitgifte | The Ch 1 revelation, two words in both languages |
| pony bottle / bailout | ponyfles / bailoutfles | "A separate life" |
| stage bottle | stagefles | |
| full-face mask | volgelaatsmasker | |
| comms | de comms | Team jargon kept as the EN keeps duikteam |
| zero vis | nul zicht | |
| recovery / recovery diver | berging / bergingsduiker | "Rope him and bring him up" → "Sla hem aan en breng hem op" |
| misadventure (ruling) | *dood door ongeval* | Coroner → lijkschouwer |
| SOCO / scene-of-crime people | de technische recherche | |
| the gap (valuation motif) | het gat | "Everything's in the gap" → "Alles zit in het gat"; "stand in the gap" → "in het gat staan"; echoes "een wak in het ijs" (Ch 13) |
| recorded value / real value | geregistreerde waarde / echte waarde | |
| ironing (Daan's word) | strijken | |
| the fixer | de fikser | Slootweg |
| leverage | drukmiddel(en) | Slootweg's Zeedijk warning |
| "Good girl" | 'Goed zo, meisje' | Bram's tic, held at both occurrences ("als een hand die zich sloot") |
| counting in threes / "One two three" | tellen in drieën / 'Eén twee drie' | The book's spine; "In. Hold. Out." → "In. Vasthouden. Uit." |
| "Don't make this heavier than it is" | 'Maak dit niet zwaarder dan het is' | The zwaar/gewicht motif carried into the title theme |
| the honest machinery / the honest scale | de eerlijke machinerie / de eerlijke weegschaal | Ch 15–16 |
| the beam (of the scale) | de evenaar | Period scales term, Ch 16 |
| "The water is a service" | 'Het water is een dienst' | Victor's letter |
| "So I made it clean" | 'Dus heb ik het schoon gemaakt' | Bram's confession; schoon/clean motif (schone uitspraak, schoon geld) held throughout |

**Gloss-reversion list** — places where the EN glossed a Dutch reality for
Anglophone readers and the NL text speaks plainly again (the mechanical
transform flagged by the paper-orange session's 💡):

1. **De Waag** — EN: "the Waag … the weigh house, the place where they had
   once cut open the dead"; NL drops the "weigh house" apposition, keeps
   the anatomical history as content.
2. **Kadaster** — EN: "the Kadaster, the public land registry that
   recorded every Dutch transfer in dry official Dutch"; NL: "uit het
   Kadaster", gloss dissolved.
3. **grachtenpand(en)** — EN italicizes and situates; NL uses the plain
   word.
4. **Officier van Justitie** — EN capitalizes as an exotic term; NL uses
   standard lowercase "officier van justitie" (institution register
   normalized), "het parket" for the office.
5. **duikteam / huisarts / huisbaas / recherche / commissaris / FIOD /
   sluis / jenever / poste restante** — already Dutch in the EN; carried
   without italics or explanation.
6. **meisje** — EN carries Bram's endearment as italic foreign speech
   ("like this, *meisje*"); NL absorbs it as ordinary speech, where it
   reads even more paternal.
7. **"Rotterdam Dutch"** — EN: "a short word in Rotterdam Dutch"; NL:
   "een kort woord in het Rotterdams".

All personal names unchanged (Sanne Kessler, Daan Kessler, Bram Verhoeven,
Nadia Okonkwo, Victor & Marije Maas, Tim, Ruud Slootweg, Cornelis Aalving,
Joke, Prins, Van Dijk, De Wit, Willemsen, Agata, Marijke); the invented
firm "Kanttekening Notariaat" and the boat name *Aaltje* carry over
verbatim. All topography unchanged (Kloveniersburgwal, Nieuwmarkt,
Zeeburg, Marineterrein, Magere Brug, Blauwbrug, Weesperzijde, Zeedijk,
Oostelijke Handelskade, Houthavens, Sloterdijk, Singel, Amstelveen,
Purmerend, Diemen, Almere, Schiphol). Chapter titles translated for sense,
not calqued: "Ruling" → "De uitspraak", "Narrowing" → "Wie overblijft",
"The Offer" → "Het bod", "Surfacing" → "Boven water" (which carries the
Dutch idiom for truths coming to light). Idioms adapted, not calqued
("the way you know a voice in the dark" → "zoals je een stem in het
donker kent"; "spreading it around like a man spreading a coat over a
puddle" → "zoals een man een jas over een plas spreidt"). Forms of
address: Bram–Sanne "jij" both ways (plus "meisje"); Sanne–Nadia "jij";
Sanne–Joke "je" (long-time mooring neighbours); Slootweg addresses Sanne
as "u"/„mevrouw Kessler" and slips to "je" only in his final panicked
"Neem je telefoon op"; officials and strangers (Agata, Marije at first
contact) are "u". Dialogue in single quotes, scene breaks ⁂, chapter
headers "Hoofdstuk een/twee/…" — all mirroring the landed NL-edition
formatting convention.

## Market position

- **Format:** full-length crime novel ebook (reflowable, cover-only
  production); at ~37k words it sits in the short-novel band, same tier
  logic as the EN edition.
- **Market:** the NL market advantage is real and double here: Amsterdam
  crime fiction is a *native* Dutch genre shelf (misdaadromans/thrillers
  are the NL market's best-selling fiction category), and this book's
  furniture — the Waag, the duikteam, the grachtengordel, notaris-witwas
  constructions — reads as local, not translated-exotic. That is a
  qualitative argument only: **no NL comps pulled, no NL-storefront
  category/keyword pricing research done tonight — NL-market specifics
  not measured.** Price band carried over conservatively from the EN
  packet ($3.99–$5.99, rec. $4.99 ≈ €3.49–€5.49 equivalent), not
  re-derived for NL.
- Base-case sales for an unknown author remain ≈ $0, as for every
  candidate on this shelf; unit economics only, no forecast.

## ⚑ Owner gates and follow-ups

- ⚑ **Publishing stays owner-gated** exactly like the EN master: per the
  NL vetting packet §7 OWNER-GATE block (`docs/publishing/vetting/
  de-waag.md`, landed in this same PR — KDP account/tax interview, cover
  approval and any art spend, price set, categories/keywords re-verified
  at graduation, title-availability recheck at upload). Nothing published,
  no accounts touched, no spend by this session.
- ⚑ **Native-speaker proofread recommended before any listing** — the
  diving/police procedural register uses real NL technical vocabulary
  (seinlijn, daallijn, ademautomaat, tamp, halve steek) that a
  native/professional reader should verify against unit usage.
- Follow-up (future slice): the DE translation the EN DECISIONS.md
  defers alongside this one; and the EN packet's full-novel-cut expansion
  note remains open.
