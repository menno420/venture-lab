# Nederlandse editie (NL) — Boek drie — NOTES

## What this is

A complete literary Dutch (Netherlands register) translation of *The
Harvest Rows* (The Night Kiln, Book Three). Source text:
`../../en/the-harvest-rows.md` at its merged state on `main` @
`0375099b918481412611d33e1157ee1fb1679918` (verbatim `wc -w` **23,334**
words, including title, front matter, and chapter headings; re-measured
identical tonight in this clone). All 12 chapters translated in full —
every line finished prose, no summary placeholders. The EN manuscript
stays the source of truth for the story; fixes propagate EN → NL, never
the reverse.

The manuscript is translated **as written, at its current length**
(23,334 words EN, the packet's committed ~20k–30k band per ORDER 011
item 3): the ⚑ OWNER length-band question on Book Two
(`../../DECISIONS.md`, 2026-07-13; restated as recorded tension in the
Book 3 entry, 2026-07-14) is owner-queued and stays untouched by this
slice — if that ruling ever changes any EN text in the series, the
change propagates EN → NL like any other fix.

Series continuity: every recurring term, name, and load-bearing line was
taken from the **series-safe glossary of Book One's NL edition**
(`../nl/NOTES.md`) plus the **Book-Two additions**
(`../nl-book-2/NOTES.md`), both inherited unchanged — including the
kiln's law verbatim (*De oven bewaart. Hij neemt niet. Zeg het (me)
na.*) and Book Two's catechism line verbatim (*En wat hij bewaart, kan
hij, vriendelijk gevraagd, teruggeven.*). Only Book-Three-new terms were
added (table below).

Provenance: run under **ORDER 011** (owner night run 2026-07-14, EAP
final-night worklist; NL-completion remainder named in the
2026-07-14T02:40Z heartbeat: *The Harvest Rows* was one of the two
EN-only manuscripts left in the adult catalog).

Unlike Books One and Two, nothing is deferred out of this slice's batch:
the vetting packet (`docs/publishing/vetting/de-oogstslag.md`) ships in
the same session, and the keyword-map C4 rows are drafted as proposals
for the same PR (map edit handled at integration; full-map V057
first-claim scan run first — see the packet §6).

## Honest word count

Verbatim `wc -w` on 2026-07-14 (includes title, front matter, and
chapter headings):

```
24655 candidates/adult-novels/the-night-kiln/versions/nl-book-3/de-oogstslag.md
23334 candidates/adult-novels/the-night-kiln/en/the-harvest-rows.md
```

NL versus the EN source: **+5.7%**. That is the highest expansion in
the catalog to date, a shade above Book One's +5.3% (De Nachtoven) and
above Book Two's +4.6% (De Morgendeur); the catalog's narrative band
runs +1.5%–+2.5% (De Waag, Weduwenblauw, De papieren sinaasappel, Het
trage woord). Reported as measured, not targeted. The likely drivers
are the same as Book One's (dialogue-heavy cozy register; Dutch
conversational syntax runs long) plus this book's rowing/kiln craft
speech, where single EN craft words repeatedly become Dutch phrases
("dunted" → "gesprongen in het koelen", "level" → "in het lood
gehouden"). Per-chapter parity was checked during drafting: every
chapter lands between +2.7% and +8.5% of its EN count — no chapter was
compressed or padded. Flagged for the native-speaker proofread to
confirm none of the surplus is calque padding.

## Title decision

**Chosen: *De Oogstslag*** (subtitle *Een cozy-fantasynovelle · De
Nachtoven, boek drie*). **No pre-named NL title existed** for Book
Three (checked: series DECISIONS.md, both NL NOTES files, both NL
packets — the pre-naming 💡 convention postdates the Book 3 DECISIONS
entry), so this pick was derived tonight per the series convention:
one object-per-book compound, pairing with *De Nachtoven* and *De
Morgendeur*.

Why *De Oogstslag*: the EN title names the rowing race (and chapter 10);
the EN pun (rows of the harvest / rowing) does not survive Dutch, so the
title keeps the race side, which is the book's side. **De slag** is the
Dutch rowing word the series already owns: Book Two's NL text describes
this very dish as a race that "voor altijd midden in een slag ophield" —
so the title names the exact thing the crack falls on, the stroke. It
also carries chapter 9 natively (*My Stroke and Not Mine* → *Mijn slag
en niet de mijne*) and the contest sense of *slag* does the "race" work.
In-text the race is *de Oogstslag*, short form *de Slag* ("het jaar dat
je de Slag won").

Collision scan, dated **2026-07-14** (`date -u`: Tue Jul 14 03:27 UTC
2026; WebSearch, three queries):

- **`"De Oogstslag" boek roman titel`** — **no same-named book found.**
  Hits were harvest-titled Dutch shelf noise, none colliding: *De
  oogst* (Stijn Streuvels, 1900,
  [scholieren.com](https://www.scholieren.com/verslag/boekverslag-nederlands-de-oogst-door-stijn-streuvels-42165),
  [moorsmagazine](https://www.moorsmagazine.com/boeken/vertalingen-hertalingen/stijn-streuvels-de-oogst/streuvelsoogst/)),
  *De oogst* (Hjorth & Rosenfeldt thriller,
  [uitgeverijcargo.nl](https://www.uitgeverijcargo.nl/boek/de-oogst/),
  [hebban](https://www.hebban.nl/boek/de-oogst-hjorth-rosenfeldt)),
  *De oogst en het gisten* (Cossee). All bare "oogst", different
  genres; logged as adjacency, not collision.
- **`"Oogstslag" bol.com boek`** — no "Oogstslag" listing surfaced;
  results degraded to bare-oogst shelf neighbours (*Oogstkoken*,
  *Oogst* by Sien Volders,
  [bol.com](https://www.bol.com/be/nl/p/oogst/9300000003348861/)) and
  generic category pages — the storefront has nothing under the
  compound.
- **`"oogstslag" Nederlands`** — the compound barely exists in Dutch;
  results degrade to dictionary/agri-news noise for *oogst* and *slag*
  separately (Nieuwe Oogst farm news; *Slag bij Heiligerlee* battle
  pages). Favourable: distinctive, searchable, no competitor.

One register note, weighed and accepted: bare *slag* can read as
"battle" (*Slag bij Nieuwpoort*); on a cozy cover the subtitle's genre
phrase plus the series pairing disambiguate, and the rowing sense takes
over by chapter 1. Alternatives considered and rejected without scan
(quality grounds): *De Oogstwedstrijd* (wordy, no compound elegance),
*Het Oogstroeien* (gerund, weak spine title), *De Oogstbaan* (modern
Dutch reads *baan* as "job"), *De Oogstrijen* (keeps the crop-rows half
of the pun but loses the race, which is the book), *De Oogstschaal*
(names the vessel, but the EN names the race and chapter 10 must match
the book title).

**Verdict: no collision found; distinctive coinage; pairs with Books One
and Two.** Standing caveat carried from all prior NL packets: Dutch
self-pub titles are unevenly web-indexed; "none found" is weaker
evidence than for trad-pub. The pick is **⚑ owner-ratified, not
seat-ratified** (decide-and-flag): recorded in the series DECISIONS.md
tonight with these alternatives, queued in the packet §7 for
ratification together with the EN and Books One–Two titles; final
KDP/bol.com recheck at upload.

## Glossary — recurring term choices (kept consistent throughout)

**Inherited from Books One and Two** (`../nl/NOTES.md`,
`../nl-book-2/NOTES.md`) — held verbatim wherever Book Three re-uses
them; both full tables apply unchanged. Load-bearing inherited rows that
recur here: *de Nachtoven* ("hij" throughout), *ovenheks*, *een
vertelling/vertellen*, *de vertelplank* (negen kommen), *een bewaring*,
*een ontlediging*, the kiln's law verbatim, *de stook/stooknacht/de
proeve*, *maansopkomst*, *de goede stoel*, *de dorpsraad/de
raadszaal/de kerkmeesters*, *schout* (Odile Vance), *de sluitsteen*,
*het waterpas* (Ansel's oak-and-brass level — now load-bearing, see
below), *het slib*, *gesprongen in het koelen*, *blind
dichtsmeren/dichtmetselen*, *de kneedbank*, *twee aan het touw*,
*dingen in de kamer*, *een kanaal en geen vergaarbak*, *oom Aambeeld*,
*Gebroeders Rooke/twee roeken*, kin-titles (*Grootje Ilsabet, Ouwe Wim,
Oude Griet, oma Brock*), *De Koperen Ketel*, *de Bakkerssteeg/het
heksenlaantje*, *haardvertelsels*, kiln anatomy
(*stookmond/spiekgat/stookbank/kruin/flank/ton*), *het grootboek*, *de
papkom*, *lamp in het venster*, *geduldig als een klant*, the bird's-egg
simile verbatim, *het kapsel* (saggar), *het openingsvuur/het
bewaarvuur*, *de kalkkar*, *de bode*, *schooljuffrouw*, *de brink*, *de
naamkom van de decemberbaby* (pre-coined in Book One), *de veerstoep*,
*de treedploeg*, *de platen*, *de doft*, "Wim zette gravers over en
grijnsde als een vloedmerk" (verbatim Book One), *zondige kaneelmelk*,
the quitte liturgy, *warm aan de hartstenen … dragend/bewarend* (chapter
1 inverts the pair exactly as the EN does), *EINDE*.

**Book-Three additions** (new terms, translated series-safe in their
turn):

| EN | NL | Note |
|----|----|------|
| The Harvest Rows (race + title) | De Oogstslag / de Slag | Title anchor (see above); ch 10 title identical to book title, as in EN; "won the Rows" → "de Slag won" |
| Harvest Home | het Oogstfeest | Festival + ch 12 title; "Harvest Home week" → "de Oogstfeestweek" |
| the Harvest Crown / last-sheaf plait | de Oogstkroon / de vlecht van de laatste schoof | Winner crowns the first dance's partner |
| the level fire / the third temper | het waterpasvuur / het derde temperament | On Book Two's -vuur pattern; ch 4/11 title anchors; "held plumb" → "in het lood gehouden"; the EN pun survives natively: "je kunt een vuur niet waterpas stoken zonder waterpas" |
| to mend / the mend | helen / het helen | Verb-led; noun *heling* used only where the context is unambiguous (its Dutch stolen-goods sense never intrudes); Griet's folk register held verbatim at every return: *bewaar hem maar, kind, tot hij weer heel is*; workshop law: "helen is voor gestaakte wedstrijden, niet voor geopende deuren" |
| **new catechism line** (ch 8 + ch 12, byte-exact both) | ***En wat breekt, kan hij, samen verteld, helen.*** | Built parallel to Book Two's line (same "kan hij, …, …" spine, absolute participle *samen verteld* mirroring *vriendelijk gevraagd*) |
| a dunt / dunted | een koelscheur / gesprongen in het koelen | Noun form extends Book One's gloss; "A dunt is a small death" → "Een koelscheur is een kleine dood" |
| cradle-saggar | het wiegkapsel | Extends Book Two's *kapsel*; "a cradle more than a box" carries the gloss in-world |
| the seam | de naad | Also keeps the EN's face motif in the same word: "de naden van zijn gezicht" |
| lesser-freight law | "een allereerste vuur bewijst zich op mindere vracht" | Held at each return |
| a carry (noun) | een dracht | Extends Books One–Two's dragen/draagster/gedragen family |
| catch and pull | de inpik en de haal | Real Dutch rowing terms; Griet's time-beating motif "inpik en haal, inpik en haal" |
| to catch a crab | een snoek (vangen) | Real Dutch rowing slang ("een snoek slaan/vangen"); "A crab. Caught whole, at two lengths, off a laugh." → "Een snoek. In zijn geheel gevangen, op twee lengten, om een lach." |
| stroke / bow / cox | slag / boeg / stuurman | Rowing seats; "two oars and a cox" → "twee riemen en een stuurman" |
| oar / loom / button / blade / feathering | de riem / de steel / de kraag / het blad / het blad vlak leggen | The burned oar is *de riem*; label verbatim: *As: de riem. Genoeg.* |
| thwart / painter / gunwale / shingle | de doft / de vanglijn / het dolboord / het grind | Doft inherited from Book Two |
| *Dob's Revenge* / *Second Thoughts* | *Dobs Wraak* / *Bij Nader Inzien* | Boat names translated for the jokes; *Bij Nader Inzien* keeps Nell's second-life/audit joke idiomatic |
| the post | de paal | "van start tot paal"; "the post as the post finds you" |
| mill-race / mill bend | de molenstroom / de molenbocht | Griet "trekkend als de molenstroom zelf" |
| tithe-barn | de tiendschuur | Real Dutch word |
| ledger entry / answering line | de inschrijving / de antwoordregel | Ch 2 title anchor; ch 12 closes the pair |
| shard-pile / wasters | de schervenhoop / misbaksels | Dutch potters' term |
| flux / ground glaze / slaked | het vloeimiddel / gemalen glazuur / geblust | Ceramics-real |
| What the Frost Took (ch 3) | Wat de vorst nam | Keeps the deliberate catechism echo ("Hij neemt niet") |
| "All hands, then." | 'Alle hens, dan.' | Ch 9 close |
| owl-light | het uilenlicht | The sorting ritual's hour |
| Harvest weather | oogstweer | Ch 1 title anchor |

All personal names otherwise unchanged (Dob Askew, Bett, Tally Weaver,
Tom Chandler, Mercy Hale, plus the whole Books One–Two cast). Place
names unchanged. Forms of address follow the series map: Perrin gives
Edda "u"/"meesteres"; villagers and Edda are "je/jij"; Wim–Edda "je"
with "heks"/"meesteres" exactly where the EN has "witch"/"mistress";
Edda–Odile "u" both ways; Wim–Griet "je"/"lief" — except the ch 7
kitchen scene, where Wim, playing the stranger his wife sees, gives her
"u"/"mevrouw" (the EN's "Soon, missus" register). Griet calls Edda
"kind" (she is the elder). Idioms adapted, not calqued ("with the wet
side kept to the water" → "met de natte kant naar het water gekeerd";
"like a duchess fainting" → "als een hertogin die flauwvalt"; "rowing a
straight course across a current" → "een rechte koers roeien dwars over
een stroom").

## Gloss reversions

None required — as with Books One and Two, the EN glosses no Dutch
realities (invented cozy-fantasy world). The EN's in-world teaching
appositions (the cradle-saggar built up at the bench; "Dunting, we call
it") are craft speech and are kept as speech. Logged for symmetry with
precedent.

## Market note (honest)

- No NL comps pulled beyond the three-query title scan — qualitative
  only: the same live NL "cozy fantasy" shelf as Books One and Two, now
  a complete three-book series if the owner ratifies the titles
  together (already the queued §7 step; a completed trilogy is the
  strongest series signal in the catalog).
- Book Three's Dutch keywords are **7 all-new phrases** (none of De
  Nachtoven's or De Morgendeur's fourteen re-claimed) — drafted with a
  full-map V057 first-claim scan; see the vetting packet §6.
- Price band carried over conservatively from the series' EN packet
  logic (€4.99-tier novella), not re-derived for NL.
- Base-case sales for an unknown translated author ≈ $0, as for every
  candidate on this shelf; unit economics only, no forecast.

## ⚑ Owner gates and follow-ups

- ⚑ **NL title ratification** — *De Oogstslag* is a tonight-derived
  pick (no pre-naming existed), scanned clean (above) and recorded with
  alternatives in the series DECISIONS.md, but the pick is the owner's:
  ratify together with *De Nachtoven*, *De Morgendeur*, and the EN
  titles. Final bol.com/KDP recheck at upload.
- ⚑ **Native-speaker proofread before any listing** — weighted toward
  the rowing register (inpik/haal/snoek/doft/vanglijn), the craft
  register (waterpasvuur/koelscheur/wiegkapsel/vloeimiddel), the ledger
  entries (ch 2, ch 12), and the +5.7% expansion noted above (the
  catalog's highest).
- ⚑ **Publish sequencing behind the EN edition** — and the EN Book
  Three is itself unvetted as a standalone packet (concept-stage inside
  `docs/publishing/vetting/the-night-kiln.md`), behind the standing
  series sequencing. Same pattern as the catalog's other NL editions.
- ⚑ **Book Two length-band ruling (standing, carried forward
  untouched)** — the open ⚑ OWNER question in `../../DECISIONS.md`
  (2026-07-13, restated as tension in the Book 3 entry) is owner-queued
  and was not touched by this slice; this edition translates Book Three
  **as written** at its committed band. If any ruling changes the EN,
  the NL follows EN → NL.
- ⚑ **Publishing stays owner-gated** exactly like the EN masters, per
  the title's vetting packet §7 OWNER-GATE block. Nothing published, no
  accounts touched, no spend by this session.
