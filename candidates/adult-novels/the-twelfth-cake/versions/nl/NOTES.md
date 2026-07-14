# Nederlandse editie (NL) — NOTES

## What this is

A complete literary Dutch (Netherlands register) translation of *The
Twelfth Cake*. Source text: `../../en/the-twelfth-cake.md` at its merged
state on `main` @ `ed3f2dfa679bdd527e14d78818bf9ea8594caf8b` (the
origin/main this branch forked from; verbatim `wc -w` 15,995 words,
including title, front matter, and chapter headings). All 12 chapters
translated in full — every line finished prose, no summary placeholders;
per-chapter paragraph counts match the EN exactly, ⁂ scene breaks 6 = 6.
The EN manuscript stays the source of truth for the story; fixes propagate
EN → NL, never the reverse. The EN `../../DECISIONS.md` register fences are
honored in translation: warm hearth register throughout, no crime/dread
stems, no Dec-25 iconography (the Dutch text's whole festive vocabulary is
Driekoningen, not Kerstmis — see glossary), and the invented names (Pridd,
Pell, Crail, Nib, Gamage, Pettifer, Tarleton, Finck, Culpepper, Trott,
Sprat) carry over unchanged.

Provenance: run under **ORDER 011 item 2** (owner night run 2026-07-13,
relaying ORDER 008 item 1: versions across "different angles, audiences,
lengths — versions are cheap once the research exists"; this version adds a
different-**language** audience).

**Deliberately DEFERRED:** the NL vetting packet, the keyword-map C4 rows,
and the OWNER-QUEUE regen are *not* in this slice — `docs/publishing/` is
held tonight by the concurrent night-product-slice session; those rows are
owed to a follow-up session.

## Honest word count

Verbatim `wc -w` on 2026-07-13 night run (includes title, front matter,
and chapter headings):

```
16897 candidates/adult-novels/the-twelfth-cake/versions/nl/de-driekoningentaart.md
```

Versus the EN source's 15,995: **+5.6%**. That is at the top of — a shade
above — the catalog's measured NL expansion band (De Waag +1.6%,
Weduwenblauw +2.1%, Het trage woord +2.5%, De papieren sinaasappel ~+2.5%,
De Marmeladepost +4.0%, De Nachtoven +5.3%); the count is reported as
measured, not targeted. The likely driver is the same one logged on De
Nachtoven: this is a talk-heavy book (the twelve accounts, the king's two
long speeches, Comfort's window speech), and period-formal spoken Dutch —
full "u"-forms, separable verbs, legal doublets in the Ch 11 deed language
— runs longer than Dutch narration. Flagged for the native-speaker
proofread pass to confirm none of the surplus is calque padding.

## Title decision

**Chosen: *De Driekoningentaart*** (subtitle *Een driekoningennovelle*).
"Twelfth cake" has an exact, living Dutch-market anchor: the
driekoningentaart with the hidden bean — whoever finds it is king — is a
real, currently practiced Dutch/Flemish tradition, so the title does in NL
precisely what the EN title does in EN, and the bean rule needs no gloss
for Dutch readers. The subtitle carries the EN packet's MANDATORY
fiction-signal subtitle ("A Twelfth Night Novella") into Dutch.

Collision scan, dated **2026-07-13** (`date -u`: Mon Jul 13 23:37 UTC
2026; WebSearch, three queries):

- **`"De Driekoningentaart" boek roman titel`** — **no same-named book
  found.** Every hit is the pastry, not a novel: recipe/tradition pages
  ([Corman](https://www.corman.pro/be/nl/chefs/blog/driekoningentaart-een-traditie-gaat-de-wereld-rond/),
  [ilovefoodwine](https://ilovefoodwine.nl/recept/driekoningentaart-een-franse-klassieker/),
  [njam!](https://njam.tv/recepten/traditionele-driekoningentaart),
  [rutgerbakt](https://rutgerbakt.nl/bladerdeeg-recepten/driekoningentaart-recept/)),
  plus unrelated shelf noise (*Waar is de taart?*,
  [Lannoo](https://www.lannoo.be/nl/producten/prentenboeken/waar-de-taart);
  *Het grote taartenboek*). No fiction collision.
- **`"Driekoningentaart" bol.com boek`** — the word appears on bol.com
  only inside cookbooks and one children's picture book that mentions the
  bean custom (*De winterpret van Jens en Lin*,
  [bol.com](https://www.bol.com/be/nl/f/de-winterpret-van-jens-en-lin/34489647/));
  no adult fiction title. Logged as adjacency, not collision — and the
  search crowding is by *recipes*, the same honest Moderate common-noun
  crowding the EN packet already priced in, mitigated the same way (the
  fiction-marker subtitle).
- **`"Driekoningen" roman novelle Dickens kerstverhaal Nederlandse
  titel`** — the Dutch Victorian-seasonal shelf clusters under *(Dickens')
  Kerstverhaal* / *Een kerstvertelling*
  ([hebban](https://www.hebban.nl/boek/een-kerstvertelling-charles-dickens),
  [Blossom Books](https://www.blossombooks.nl/product/dickens-kerstverhaal/),
  [Wikipedia](https://nl.wikipedia.org/wiki/A_Christmas_Carol_(boek)));
  no Driekoningen-titled novel surfaced — favourable: the title sits next
  to that shelf without colliding with it.

Alternatives considered and rejected without scan (quality grounds): *De
twaalfde taart* (calque; "twelfth cake" means nothing in Dutch and
surrenders the tradition anchor), *Driekoningenavond* (bare feast name,
generic to the point of invisibility and collides head-on with Shakespeare's
*Twelfth Night*, conventionally *Driekoningenavond* in Dutch), *De taart
in het raam* (loses the feast and the bean).

Standing caveat carried from all prior NL packets: Dutch self-pub titles
are unevenly web-indexed; "none found" is weaker evidence than for
trad-pub. Final KDP/bol.com title recheck at upload is the owner's §7
step.

## Glossary — recurring term choices (kept consistent throughout)

| EN | NL | Note |
|----|----|------|
| the Twelfth cake / the great cake | de driekoningentaart / de grote taart | Title anchor; the cake is "hij" throughout |
| Twelfth Night | Driekoningenavond | 5 January; "Twelfthtide" → driekoningentij |
| Twelfth Day / Epiphany | Driekoningendag (Driekoningen) / Epifanie | 6 January; "Epifanie" reserved for the liturgical register (Snell, the narrator's feast-name) |
| Twelfth-buns | driekoningenbroodjes | |
| the bean / the pea | de boon / de erwt | Dutch custom knows the boon natively; the pea (queen) kept as the house's English custom |
| king/queen of the feast | koning/koningin van het feest | |
| "apprentice or alderman, no appeals" | 'leerjongen of alderman, geen beroep mogelijk' | Blurb + rule speech, held verbatim; "NO APPEALS!" → 'GEEN BEROEP!'; Crail's "I must appeal" → 'beroep aantekenen' keeps the legal echo |
| the most inconvenient slice in London | het ongelegenste stuk taart van heel Londen | Blurb + finding, held verbatim |
| the world agrees to turn upside down | de wereld spreekt af op zijn kop te gaan staan | Blurb + Tarleton, held verbatim |
| the crier (under the table) | de roeper | "Call it, crier" → 'Roep maar, roeper' |
| bakehouse / shop | het bakhuis / de winkel | The two rooms kept strictly distinct, as in EN |
| the window / the glass | het raam / de ruit (het glas) | "Etalage" avoided as anachronism; children at the glass → kinderen aan/voor de ruit |
| peel / peel-rack | de schieter / het schietersrek | Dutch bakers' term; peel-handle sceptre → scepter van een schietersteel |
| the fire is drawn | het vuur is uitgehaald | "You drew the fire. You didn't draw the heat." → 'Jullie hebben het vuur uitgehaald. Niet de warmte.' |
| falling bread-heat | dalende broodhitte | "within a faggot of it" → 'of er één takkenbos vandaan' |
| sponge / straight dough / barm | het voordeeg / een rechtstreeks deeg / gist | Trade-accurate period terms |
| quartern loaf / heel | vierpondsbrood / het kapje | |
| sugar-baker / pastrycook | suikerbakker / banketbakker | Real Dutch trade words; the frigate-captain/ferryman joke survives natively |
| Kummel mould | een vorm van Kummel / Kummel-vorm | Herr Kummel kept with German honorific, as in EN |
| conveyance / engrossed / instrument | de transportakte / in het net geschreven (gesteld) / de akte | Real Dutch conveyancing vocabulary |
| Lady Day / Michaelmas | Maria-Boodschap / Sint-Michiel | Quarter-days by their Dutch feast names; Michaelmas quarter → het Sint-Michielskwartaal |
| Alderman | alderman | City of London office kept untranslated (lowercase in running Dutch); Court of Common Council, Guildhall, Lord Mayor, Mansion House likewise kept |
| crossing-sweeper | veegjongen | "of no fixed crossing" → 'zonder vaste oversteek' |
| hackney coachman, badge 1109 | huurkoetsier, penningnummer 1109 | |
| law-stationer's writer | kopiist bij een rechtskundig schrijfkantoor | Nib's self-description |
| the Golden Sheaf | de Gulden Schoof | Shop sign translated (the sign is load-bearing: "I knew the sign"); the Swan → De Zwaan |
| lamb's-wool | een kraag van lamswol | Rendered as the image the EN itself leans on |
| the account / it will not balance | de rekening / zij komt niet in evenwicht | Crail's ledger idiom, held at every recurrence |
| "the bean makes no mistakes" | 'de boon vergist zich niet' | Kit's line, held verbatim at each return (Ch 7, 9, 12) |
| "dinner in its Sunday best" | 'eten in zijn zondagse goed' | Kit's motif, held verbatim (Ch 4, 5) |
| consulting master | raadgevend meester | |
| Mistress Pell / master | meesteres Pell / meester | Per the catalog's NL precedent |
| PRIDD'S. ESTABLISHED 1762 | PRIDD'S. SEDERT 1762 | Sign; shop name kept as brand |
| *and successor* | *en opvolger* | Finck's gold letters |
| THE END | EINDE | |

All personal names unchanged (Josiah/Obadiah/Ezra Pridd, Barnabas
Trott/Barney, Kit, Pettifer, mevrouw Gamage & Samuel, Decimus Snell →
"dominee Snell", Sally Sprat, sergeant Culpepper, Fan Tarleton, juffrouw
Fanshawe, Tobias Finck, Herr Kummel, Elias Nib, Comfort & Noah Pell,
Onesiphorus Crail, Mowl, Huggins and the horse Duchess, Gudgeon & Sharp).
London street and place names unchanged (Bread Street, Pannier Court,
Cheapside, Old Jewry, Leadenhall Street, Whitechapel, Goodman's Fields,
Honey Lane, Queenhithe, Milk Street, Aldersgate, Bow Lane, Distaff Lane,
Crutched Friars, Pentonville, Lambeth, Pudding Lane, Temple Bar, Drury
Lane, Portman Square, the Borough; Rochester, Maidstone, Norwich, Ipswich,
Kent, Underhanger). Forms of address: adults among strangers are "u" both
ways and stay there (period-formal); Pridd and the Alderman give the boys
"je/jij"; the boys and Barney answer "u/meneer"; the Alderman's ward
familiarity gives Pridd "je" while Pridd returns "u" (rank, kept even
after the crowning — the inversion runs through the *feast's* law, not
through Dutch pronouns); Kit speaks a light street register ('d'r zijn
geen oversteken meer', 'een DIKKE voor de suikermeneer') without eye-dialect
spelling. Idioms adapted, not calqued (e.g. "the cold came in like a
creditor" → 'de kou kwam binnen als een schuldeiser' kept, but "boiled ham
that had lost its way" → 'een gekookte ham die de weg kwijt was'; "came on
to snow" → 'het gaat sneeuwen... als het het van plan is'; "flattery with
currants in it" → 'vleierij met krenten erin').

## Gloss reversions

One, in the title's favour — the EN's core custom needed stating for
Anglophone readers and is *native* for Dutch ones:

1. **The bean custom itself** — the EN blurb and Pridd's Ch 5 rule speech
   teach the custom from zero. The NL keeps every sentence (the speech is
   in-world house law, not a translator gloss — Pridd is instructing the
   guests "die de taart alleen van de raamkant kennen"), but the Dutch
   reader arrives already knowing it; nothing needed adding, and the title
   word does silently what the EN title cannot.

No EN-glossed Dutch realities exist in this book (invented Victorian
London), so no compression reversions were required. The EN's in-text
teaching appositions (what a Twelfth cake hides, why the youngest goes
under the table) are all in-world speech and kept as speech.

## Market note (honest)

- No NL comps pulled, no NL-storefront category/keyword research done
  tonight — deferred with the vetting packet (see the DEFERRED block
  above). Qualitative only: Driekoningen is a living calendar feast in NL
  and Flanders (bean cake, kinderen zingen), and the Dutch market reads
  Victorian seasonal fiction under the Dickens umbrella (*Dickens'
  Kerstverhaal* is a standing shelf); this book positions one feast later
  than that shelf, exactly as the EN packet positions it after Dec 25.
- Price band carried over conservatively from the EN packet logic ($3.99
  novella), not re-derived for NL.
- Base-case sales for an unknown translated author ≈ $0, as for every
  candidate on this shelf; unit economics only, no forecast.

## ⚑ Owner gates and follow-ups

- ⚑ **Publishing stays owner-gated** exactly like the EN master, per the
  title's vetting packet §7 OWNER-GATE block (account/tax, cover per §5 —
  candlelit shop window, towering iced cake, snow, small crown motif, no
  Dec-25 iconography — price, categories/keywords, title recheck at
  upload, launch timing). Nothing published, no accounts touched, no spend
  by this session.
- ⚑ **NL title ratification** — *De Driekoningentaart* is scanned clean
  (above) but the pick is the owner's; ratify together with the EN title.
  The subtitle *Een driekoningennovelle* is the NL carrier of the EN
  packet's MANDATORY fiction-marker subtitle and should travel with the
  title. Final bol.com/KDP recheck at upload.
- ⚑ **Native-speaker proofread before any listing** — weighted toward the
  period register (the Ch 11 deed language, the trade terms
  schieter/voordeeg/transportakte) and toward the +5.6% expansion noted
  above.
- ⚑ **Publish sequencing behind the EN edition** (shared cover
  composition, account setup) — same pattern as the catalog's other NL
  editions.
- Follow-up (deferred, owed): NL vetting packet + keyword-map C4 rows +
  OWNER-QUEUE regen in `docs/publishing/` once tonight's concurrent
  session releases the directory.
