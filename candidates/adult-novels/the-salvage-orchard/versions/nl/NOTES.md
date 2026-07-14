# Nederlandse editie (NL) — NOTES

## What this is

A complete literary Dutch (Netherlands register) translation of *The
Salvage Orchard*. Source text: `../../en/the-salvage-orchard.md` at its
merged state on `main` @ `b1eddbff16dbe609ed5b3bf753352751c9004838` (landed
via PR #151; verbatim `wc -w` 15,045 words including title, front matter,
and chapter headings; re-verified identical at tonight's HEAD). All 12
chapters translated in full — every line finished prose, no summary
placeholders. The EN manuscript stays the source of truth for the story;
fixes propagate EN → NL, never the reverse. World facts are held exactly to
the EN text and `../../DECISIONS.md`: Rende is an invented near-future
city, the civic machinery (Resilience Ordinance, Strategic Reserve Office,
consensus process) is translated as invented, and nothing was added to or
drifted from the EN's ledger of facts in translation.

Provenance: run under **ORDER 011 item 2** (owner night run 2026-07-14,
relaying ORDER 008 item 1: versions across "different angles, audiences,
lengths — versions are cheap once the research exists"; this version adds a
different-**language** audience). This edition closes one of the three
remaining NL gaps in the EN adult catalog (coverage 8/11 at session start).

**Deliberately DEFERRED:** the NL vetting packet, the keyword-map C4 rows,
and the OWNER-QUEUE regen are *not* in this slice — those rows are owed to
the finalizer slice of this session per the session plan (packets/counts
ride together, the #166 remedy class).

## Honest word count

Verbatim `wc -w` on 2026-07-14 (includes title, front matter, and chapter
headings), run from the repo root:

```
15750 candidates/adult-novels/the-salvage-orchard/versions/nl/de-geborgen-boomgaard.md
15045 candidates/adult-novels/the-salvage-orchard/en/the-salvage-orchard.md
```

NL runs **+4.7%** over the EN source — inside the catalog's measured NL
expansion band (+1.5% De Waag … +5.3% De Nachtoven); the count is reported
as measured, not targeted. Likely driver: the book's long clause-stacked
periods plus the they/them pronoun strategy (see Glossary), which
occasionally needs a recast full clause where English spends one word.
Flagged for the native-speaker proofread pass to confirm none of the
surplus is calque padding.

## Title decision

**Chosen: *De geborgen boomgaard*** (subtitle *Een solarpunknovelle*).
"Geborgen" is the past participle of *bergen* — to salvage, to bring to
safety, to store the harvest — **and** the everyday adjective for
sheltered/safe (*geborgenheid*). The double meaning is exactly the book:
an orchard built out of salvage, and the safety a neighborhood builds by
sharing. It also keeps the EN title's noun-phrase shape and the orchard's
in-text signature ("— De Geborgen Boomgaard").

Collision scan, dated **2026-07-14** (`date -u`: Tue Jul 14 01:51 UTC
2026; WebSearch, three queries):

- **`"De geborgen boomgaard" boek roman`** — **no same-named book found.**
  Hits were orchard-titled shelf neighbours, none colliding: *De geheime
  boomgaard* (Sharon Gosling, feelgood,
  [bruna.nl](https://www.bruna.nl/boeken/de-geheime-boomgaard-9789020555059)),
  *De boomgaard* (Lynn Austin, historical,
  [hebban](https://www.hebban.nl/boek/de-boomgaard-lynn-austin)).
- **`"geborgen boomgaard"`** — the exact phrase surfaces only as loose
  real-estate/school copy ("een geborgen plek"), no book, which is
  favourable: the compound is natural Dutch but unclaimed as a title.
- **`"De geborgen boomgaard" bol.com boek`** — no listing; nearest
  shape-adjacent shelf neighbours are *De ondergrondse boomgaard* (Mat
  Larkin,
  [bol.com](https://www.bol.com/be/nl/p/de-ondergrondse-boomgaard/9200000102317770/)),
  *Uit de boomgaard* (Ovenden, cookbook) and *Het lijk in de boomgaard*
  (Van Istendael) — different words, different genres; logged as
  adjacency, not collision.

Verdict: **no collision found; adjacency risk low** (the "boomgaard" shelf
exists in NL but every neighbour is title-distinct). Alternatives
considered and rejected without scan (quality grounds): *De
sloopboomgaard* (reads as "orchard slated for demolition" — inverts the
hope), *De boomgaard op de werf* (descriptive, weak spine title), *De
wrakhoutgaard* (coinage too obscure, loses "boomgaard" searchability).
Standing caveat carried from all prior NL packets: Dutch self-pub titles
are unevenly web-indexed; "none found" is weaker evidence than for
trad-pub. Final KDP/bol.com title recheck at upload is the owner's §7
step.

## Glossary — recurring term choices (kept consistent throughout)

**Pronoun strategy (the load-bearing decision).** Ash Okafor uses
they/them in the EN. The NL edition uses **hen/hen/hun**
(subject/object/possessive) with **singular verb agreement** ("hen liep de
rijen langs"), the Transgender Netwerk Nederland convention most common in
recent NL literary translation. *Die/diens* was considered and rejected:
a whole novel focalized through Ash would collide constantly with
demonstrative *die* at clause openings. Ambiguity with plural *hen/hun* is
managed as the EN manages they/their: plural referents near Ash-sentences
are rendered with *ze*, and clauses are recast to keep one antecedent per
pronoun. Possessive after the name follows Dutch sibilant rules: *Ash'
idee*. Applied at every occurrence; no she/he slippage anywhere.

| EN | NL | Note |
|----|----|------|
| the Salvage Orchard | de Geborgen Boomgaard | Title anchor; the orchard's own signature in ch 1/9 |
| the Fleet Yard / the yard | de Wagenwerf / de werf | Official notice: "VOORMALIGE WAGENWERF NR. 3, GEMEENTEWERKEN" |
| Millbrook Flats / the Flats | de Molenbeekvlakte / de Vlakte | Semantic toponym translated; "de Flats" would misread as tower blocks |
| the Heights | de Hoogten | Rooftop-orchard crew's district |
| Kettle Row | de Ketelstraat | Faction named for its street, as in EN |
| Bridge Street | de Brugstraat | The notary |
| the Millbrook reach | het Molenbeekrak | *Rak* = straight stretch of waterway; used at every "reach" |
| scionwood / scion | enthout / ent | The craft register throughout |
| whip-and-tongue | copuleren met tong | Real Dutch horticultural term ("Engels copuleren"); "copuleermaand" ch 1 |
| cleft graft / chip bud / top-work | spleetent / chip-oculatie / omenten | |
| rootstock / budwood | onderstam / oculatiehout | |
| *A graft is a gift, or it dies.* | *Een ent is een gift, of hij sterft.* | Tin-lid sentence, held verbatim at every return; *gift* = gave/donation double |
| *Line up the living layer. Keep the air out. Then wait.* | *Leg de levende laag tegen de levende laag. Sluit de lucht buiten. En dan wachten.* | The craft's one sentence, held verbatim ch 1/5/12 |
| the (biscuit) tin / the tin voice | de (koek)trommel / de trommelstem | Motif; "that's a tin" → "dat is een trommel" |
| slack | speling | Iris's recurring accounting word |
| the rubric / column | de scoretabel / de kolom | "We vullen hem" ch 9 |
| swales / check dams / berms | greppels / stuwtjes / wallen | Stuwtjes "van geborgen baksteen" — title echo kept |
| the old fuel pad / hardpan | de oude tankvloer | The offered corner |
| Resilience Ordinance | de Weerbaarheidsverordening | |
| Strategic Reserve Office | het Bureau Strategische Reserve / het Reservebureau | |
| evidence of existing use | bewijs van bestaand gebruik | Held verbatim at every occurrence |
| strategic / productive reserve | strategische / productieve reserve | |
| stewardship covenant | het beheerconvenant | |
| community capacity | gemeenschapscapaciteit | The proposed fifth column |
| THE LIVING RESERVE | DE LEVENDE RESERVE | Proposal pages 7–19 |
| the Scion Library | de Enthoutbibliotheek | "Entenbibliotheek" rejected (enten = ducks); Annex C naam |
| the coastal corps | het Kustkorps | Nef's two-year hitch |
| phone tree | de belboom | |
| forecast collective | het weercollectief | |
| the Gauge Night | de Peilnacht | Ch 7; gauge boards → peillatten |
| wolf apple / wolf tree | wolfsappel / wolfsboom | The yard's own jargon, as in EN |
| Tree One | Boom Eén | |
| pear drops and cellar stone | perendrops en keldersteen | The Kernel's taste, ch 1/10/12 |
| stand aside / block (consensus) | zich terzijde stellen / blokkeren | Consensus-method register |
| *I can live with this* | *hier kan ik mee leven* | The palms-up sign |
| *before* / *after* / the dead (dark) years | *voor* / *na* / de dode (donkere) jaren | Italics as in EN |
| Old Mo | Ouwe Mo | Only nickname translated; all other names unchanged (Ash Okafor, Blessing Okafor, Marisol Reyes, Hank Bae, Nef Duarte, Iris Duplessis, mevrouw Okonjo, mevrouw Szabó, zuster Fabiola, Rende, Ibadan, Ashmead's Kernel) |

Forms of address: Iris ↔ the Flats is "u" both ways throughout (she stays
an official even as she starts pouring the tea); all neighbours "jij";
mevrouw Szabó says "jij/jongmens" to Ash by elder's right.

## Gloss reversions

None in the strict sense: unlike the catalog's WWII titles, the EN glosses
no Dutch realities that NL can simply unwrap — Rende is invented and the
craft register is universal. What this section records instead, honestly,
is the four **deliberate adaptations** of the same class (each a place the
NL speaks its own language rather than calquing):

1. **Units** — acres → hectares at natural roundings, ratios preserved:
   the eleven-acre motif → *vierenhalve hectare* (its ~8 recurrences kept
   as a motif), the four-acre template → *anderhalve hectare*, the
   two-acre offer → *een krappe hectare*; "every acre" → "elke vierkante
   meter"; the quart jar → *een liter*.
2. **The tin-lid sentence** — EN counts it as "six words"; the Dutch
   sentence (*Een ent is een gift, of hij sterft.*) counts eight, so both
   meta-references (ch 3, ch 12) say *acht woorden*. Count follows the
   sentence, not the source.
3. **Craft terms localized, not calqued** — whip-and-tongue → *copuleren
   met tong*, reach → *rak*, espalier → *leiboom*, wedging/props/gauges in
   real Dutch orchard-and-water vocabulary.
4. **Semantic toponyms translated** (Molenbeekvlakte, de Hoogten,
   Ketelstraat, Brugstraat) while invented proper nouns (Rende) and
   variety names (Ashmead's Kernel) stay — mirroring the EN's own split
   between meaning-bearing and opaque names.

One untranslatable noted for the proofreader: the EN pun "volunteer ash
trees" against Ash's name (ch 1) has no Dutch equivalent (*essen*/Ash);
it is let go without compensation rather than forced.

## Market note (honest)

- **Format:** novella ebook (reflowable, cover-only production), same tier
  logic as the EN edition; the EN cover concept translates unchanged.
- **Market:** solarpunk is barely established as a Dutch shelf category —
  the NL edition would be filed under literaire roman / klimaatfictie
  ("cli-fi") in practice. That cuts both ways: low competition, low
  category pull. **No NL comps pulled, no NL-storefront category/keyword
  research done tonight — NL-market specifics not measured.** The
  they/them Dutch rendering (hen/hun) is still contested register for some
  NL readers; flagged as a review-risk, not softened in the text.
- Price band carried over conservatively from the EN packet
  (`docs/publishing/vetting/the-salvage-orchard.md` §4: $3.99–$5.99, rec.
  $4.99 ≈ €3.49–€5.49 equivalent), not re-derived for NL.
- Base-case sales for an unknown author remain ≈ $0, as for every
  candidate on this shelf; unit economics only, no forecast.

## ⚑ Owner gates and follow-ups

- ⚑ **Publishing stays owner-gated** exactly like the EN master: per the
  EN vetting packet §7 OWNER-GATE block (KDP account/tax interview, cover
  approval and any art spend, price set, categories/keywords re-verified
  at graduation, title-availability recheck at upload). Nothing published,
  no accounts touched, no spend by this session.
- ⚑ **An NL listing needs its own vetting packet + keyword-map C4 rows in
  `docs/publishing/`** — the existing the-salvage-orchard packet covers
  the EN title only, and it is still `plan`-stage, so per C4 the
  manuscript-backed NL packet would claim the browse nodes first and the
  EN shares at graduation. Owed to the finalizer slice of this session
  (with the `derive_owner_queue.py` regen, same-session per the standing
  queue-hygiene rule).
- ⚑ **Native-speaker proofread recommended before any listing** — extra
  weight here for the non-binary pronoun strategy (consistency of
  hen/hun + singular agreement across 15,750 words) and the horticultural
  register (copuleren/oculeren/onderstam used correctly but worth a
  grower's read).
- ⚑ **Owner ratifies the title** *De geborgen boomgaard* (collision scan
  above is discoverability-grade, not legal clearance).
