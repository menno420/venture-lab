# Nederlandse editie (NL) — NOTES

## What this is

A complete literary Dutch (Netherlands register) translation of *The
Seed-Catalogue Courtship*. Source text:
`../../en/the-seed-catalogue-courtship.md` at its merged state on `main`
(landed via PR #152, commit `32a8332`; pinned for this translation at main
`d93aee502a4daf2b3f7cd249067eb5c5a5ac046c`; verbatim `wc -w` 15,133 words
including title, front matter, and part headings). All 4 Parts translated
in full, and within them every document individually — 15 + 12 + 12 + 13 =
52 document blocks (printed notices, order forms, compliments slips, a
solicitors' letter, seed-packet instructions, an estate agent's
particulars, a measured garden plan, a sale catalogue, an auctioneer's
account, a hand-printed seed list, and the letters) — every line finished
prose, no summary placeholders, no stubs. The EN manuscript stays the
source of truth for the story; fixes propagate EN → NL, never the reverse.

The book is epistolary, so the translation's real work is **register per
document type**: period-commercial administrative Dutch for the order
forms, compliments slips, auction and legal papers (notariaat formulas:
"vereffening", "vrij van huur en gebruik", "van rechtswege door
tijdsverloop", "uw dienstwillige dienaren"; auction Dutch: "kavel",
"hamerprijs", "veilingvoorwaarden"); voice-differentiated personal Dutch
for the letters (Edith's round disciplined hand vs. Tull's numbered
engineer's reports vs. Dilys Pring's blunt broad nib vs. an
eight-year-old's careful best handwriting). The English closing-formula
progression that carries the love story (faithfully → sincerely → Yours →
first name → the devastating typed regression) is mapped onto a Dutch
progression that keeps Tull's plot-load-bearing observation literally
true: "Hoogachtend" → "Geheel de uwe" → "De uwe" (the structure sheds the
word *Geheel*) → "Edith" → back to "Hoogachtend … (in liquidatie)".

Run under ORDER 011 item 2 (night run 2026-07-14, BOOKS lane; relaying
ORDER 008 item 1: versions across different angles, audiences, lengths —
this version adds a different-**language** audience), as one of the three
remaining EN adult manuscripts without an NL edition.

## Honest word count

Verbatim `wc -w` on 2026-07-14 (includes title, front matter, and part
headings):

```
15633 candidates/adult-novels/the-seed-catalogue-courtship/versions/nl/liefde-in-de-kantlijn.md
15133 candidates/adult-novels/the-seed-catalogue-courtship/en/the-seed-catalogue-courtship.md
```

Dutch running +3.3% longer than the English sits inside the catalog's
measured NL expansion band (+2.5%–5.3% on the previous NL editions); the
count is reported as measured, not targeted. Structural parity checked
mechanically: 48 `⁂` separators in both files; per-part document blocks
15/12/12/13 and bracketed archivist framings 16/13/15/17 identical EN vs
NL.

## Title decision

**Chosen: *Liefde in de kantlijn*** (subtitle *Een roman in brieven*).
The margin is the book's engine — the courtship literally happens in the
margins of order forms, the blurb ends on "written more in the margin
than on the line", and the final leaflet closes "Margins are provided.
The firm reads them." A literal rendering of the EN title compounds badly
in Dutch. Alternatives considered:

- ***De zaadcatalogus-hofmakerij* / *Hofmakerij per zaadcatalogus*** —
  faithful to the EN title but a lumpy compound; "hofmakerij" is
  charmingly period but buries the romance signal under the apparatus.
- ***Wat zou u planten?*** — the load-bearing question, but as a title it
  reads as a gardening manual in the NL market.
- ***De laatste zaadlijst*** — clean, but elegiac; sells the winding-up
  and hides the love story, which is the market.

**Collision scan (run 2026-07-14, web search):** two queries — `"Liefde
in de kantlijn" boek roman` and `"Liefde in de kantlijn" bol.com OR
goodreads` — returned **no exact-title match**. Nearest neighbours found
and judged non-colliding: *De Kantlijn* (Elke Wambacq, memoir-novel), *In
de kantlijn van de tijd* (Uitgeverij Balans, nonfiction), *Notities in de
kantlijn* (Bomans, essay classic — different title, different register,
not squatted), and the "Liefde in …" romance-title family (*Liefde in de
steigers*, *Liefde in Leeuwarden* etc.), which the chosen title joins
without duplicating. Verdict: low collision. Honest caveat: US-routed
search results and self-published NL titles index poorly — re-verify at
listing time per the standard vetting-packet caveat.

## Glossary — recurring term choices (kept consistent throughout)

| EN | NL | Note |
|----|----|------|
| Prowse & Daughters, Seedsmen since 1931 | Prowse & Dochters, zaadhandel sinds 1931 | Firm name translated so Ezra's 1968 rename lands against the Dutch "& Zonen" convention |
| Prowse & Tull, Seedsmen | Prowse & Tull, Zaadhandel | Final leaflet |
| the margin / margins | de kantlijn / kantlijnen | Title anchor; "in the margin" → "in de kantlijn" at every occurrence |
| What would you plant, if it were yours? | Wat zou u planten, als het van u was? | The standing question, held verbatim at every occurrence |
| The firm does not advise on hypotheticals. | De firma adviseert niet over hypothesen. | Recurring |
| order form / order No. | bestelformulier / order nr. | Period commercial register |
| compliments slip | complimentenbriefje | "Met de complimenten van…" |
| sweet pea | lathyrus | Standard Dutch gardeners' name; avoids pronkboon confusion |
| 'Saltmarsh Pink' | 'Roze van Saltmarsh' | Dutch heritage-cultivar naming pattern ("Roem van…"); keeps "named for the village" true |
| 'Norfolk Morning' | 'Norfolkse Morgen' | Keeps the "county's mornings" joke |
| 'Moonglow' / 'Fen Giant' / 'Marian's June' | 'Maanglans' / 'Veenreus' / 'Marians Juni' | Invented cultivars translated as invented |
| 'Dyke Field Scarlet' / 'Granary Longpod' etc. | 'Dijkveld-scharlaken' / 'Graanschuur Langpeul' etc. | Derive from translated place names below |
| Dyke Field / The Granary / the Walled Garden | het Dijkveld / de Graanschuur / de Ommuurde Tuin | Working place-names translated; village names (Saltmarsh St Peter, Marchfield) kept |
| standard / wing (sweet-pea flower) | vlag / zwaarden | Correct Dutch papilionaceous morphology; "bleek aan de vlag, zoutroze aan de zwaarden" |
| rogue without pity | wied zonder genade | Marian's motto, underlined twice, held verbatim |
| it holds true / came true | hij komt zuiver door / kwam zuiver door | Breeder's register |
| hot wall / furnace / flues | stookmuur / stookplaats / rookkanalen | Heated fruit-wall vocabulary |
| germination / germination records | kieming / kiemkracht(registers) | "kiemkracht getest op 96 procent" — exact seed-trade term |
| accessions / seed store | accessies / het zaadmagazijn | Genebank register |
| grown out / regenerated | uitgezaaid en vermeerderd / geregenereerd | |
| winding-up | de vereffening (solicitors) / de opheffing (speech) | Voice split kept |
| lot / hammer price / auctioneers | kavel / hamerprijs / veilinghouders | |
| of no commercial value | zonder handelswaarde | Recurring, held verbatim |
| Better sold than skipped. | Beter verkocht dan gestort. | |
| the dash (grandfather's open orders) | het streepje | "TO BE COLLECTED —" → "AF TE HALEN —" |
| docketed "Unanswered" | van een opschrift voorzien: "Onbeantwoord" | Dilys: geen punt, maar een streepje |
| tell the seed the news / chip, don't soak | vertel het zaad het nieuws / kerven, niet weken | |
| load / load-bearing / designed for load | belasting / dragend / berekend op belasting | Tull's engineer register |
| kept my word by its weakest member | mijn woord gehouden bij zijn zwakste onderdeel | Repeated by Edith in the unsent draft |
| Michaelmas | Sint-Michiel | Old Dutch lease term |
| solicitors (Mowbray & Kett) | notarissen | Function here is conveyancing/vereffening |
| Hessian (the cat) | Jute | Packing-cloth joke kept; "catalogue-trained" → "catalogusvast" |
| Sea View ("it hasn't") | Zeezicht ("heeft het niet") | Bungalow name translated so the joke lands |
| the Fens | het veenland | |
| Yours faithfully / sincerely / Yours | Hoogachtend / Geheel de uwe / De uwe | See register note in "What this is" |
| Dear Mr Tull / Dear Miss Prowse | Geachte heer Tull / Geachte mejuffrouw Prowse | Formal frame kept constant while closings warm, as in EN |

## Gloss reversions

None in the paper-orange sense: the EN glosses no Dutch realities (the
book is English-set), so there was nothing to un-gloss. The traffic runs
the other way — EN realities carried into Dutch without explanatory
padding: imperial units kept (voet, yard, mijl, acres) for period
texture; sterling kept (£, pence, postwissel); "de watersnood van '53"
translates the '53 flood remark and happens to resonate doubly for Dutch
readers (same North Sea flood) without adding a word; "lurchers" is
rendered plainly as "windhonden" ("de windhondenman") rather than
footnoted; the Royal Engineers get one appositive ("de genie, de Royal
Engineers") — the only added gloss in the book, two words. One count
adjustment for honesty: Dilys's "The person is known" is four Dutch words
("De persoon is bekend"), so Tull's "in five words" became "in vier
woorden".

## Market note (honest)

- **Format:** novella-length epistolary ebook (reflowable, cover-only
  production), same tier logic as the EN edition.
- **Market:** clean/wholesome epistolary romance with a horticultural
  frame; NL comps not pulled, no NL-storefront category/keyword research
  done tonight — NL-market specifics not measured. The title deliberately
  joins the visible "Liefde in …" NL romance shelf; whether that shelf
  converts for translated, England-set, older-protagonist romance is
  unverified.
- Price band carried over conservatively from the EN packet
  ($3.99–$5.99, rec. $4.99 ≈ €3.49–€5.49 equivalent), not re-derived for
  NL.
- Base-case sales for an unknown author remain ≈ $0, as for every
  candidate on this shelf; unit economics only, no forecast.

## ⚑ Owner gates and follow-ups

- ⚑ **Publishing stays owner-gated** exactly like the EN master: per
  `docs/publishing/vetting/the-seed-catalogue-courtship.md` §7 OWNER-GATE
  (KDP account/tax interview, cover approval and any art spend, price
  set, categories/keywords re-verified at graduation, title-availability
  recheck at upload). Nothing published, no accounts touched, no spend by
  this session.
- ⚑ **An NL listing needs its own vetting/keyword rows in
  `docs/publishing/`** — the existing vetting packet covers the EN title
  only; collision scan + keyword rows are language-specific (C4 Dutch
  keyword namespace, V057 first-claim-wins). **Out of scope for this
  slice** (docs/publishing/** untouched) — flagged as follow-up.
- ⚑ **Native-speaker proofread recommended before any listing** — the
  period-commercial registers (notarial, auction, seed-trade) are the
  riskiest surface: a wrong formula reads instantly as translationese to
  the NL reader this book is for.
