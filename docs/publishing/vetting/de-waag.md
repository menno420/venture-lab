# Title Vetting — De Waag

> **Status:** `plan`
>
> **NL-edition packet** — vetting for the Dutch edition of *The Weigh
> House*, per the one-pass [title-vetting checklist](../CHECKLIST.md). The
> manuscript exists and is complete
> (`versions/nl/de-waag.md`, landed in the SAME PR as this packet — the
> first NL edition to ship manuscript + vetting together, closing the gap
> the first two NL editions left as a ⚑ follow-up). A Dutch listing is a
> SEPARATE KDP listing with its own language metadata and Dutch-language
> keywords — the EN packet [`the-weigh-house.md`](the-weigh-house.md) does
> not cover it. Everything marked **⚑ OWNER-GATE** is an owner click,
> never automated.

**Title:** De Waag · **Category:** adult / crime fiction, Dutch language
(NL) · **Date vetted:** 2026-07-13

Manuscript:
[`candidates/adult-novels/the-weigh-house/versions/nl/`](../../../candidates/adult-novels/the-weigh-house/versions/nl/NOTES.md)
(complete Dutch translation of the full EN source; verbatim `wc -w`
36,997, measured in its NOTES.md 2026-07-13; EN source 36,434 words).
Fixes propagate EN → NL, never the reverse.

## 1. Title

- [x] Working title: **De Waag** — locked by the manuscript's own title
      decision (NOTES.md: alternatives *Het waaggebouw*, *Zwart water*,
      *De lijn* considered and rejected with reasons; not relitigated
      here). Subtitle: ***Een Amsterdamse misdaadroman*** — unlike the
      catalog's other NL editions this subtitle is **default ON**: it is
      the load-bearing disambiguator for a bare-word title (next item)
      and does the genre work "misdaadroman" buyers search on.
- [x] Bare-word searchability: **known handicap, mitigated.** "De Waag"
      alone is dominated by the building itself plus venues named after
      it (restaurants, hotels, a brasserie in Drachten surfaced in the
      scan) — the catalog's "Lull" problem in Dutch form. The subtitle
      is the standing mitigation (CHECKLIST pattern set by Lull's
      *"A Novella"* call); full search phrase "De Waag misdaadroman" is
      distinctive.
- [x] Homophone / autocorrect drift: "Waag" → "waag" (verb, *wie niet
      waagt*) is a real stem collision in casual search but not in title
      search with the subtitle attached; no other close drift identified.

## 2. Collision scan (discoverability, not legality — NL market)

- [x] Fresh web checks this session (2026-07-13, three queries:
      `"De Waag" boek roman misdaadroman titel`, `"De Waag" boek
      bol.com`, `"De waag" thriller Amsterdam roman hebban`): **no
      same-named Dutch fiction title surfaced.** Nearest book hit is E.
      Kurpershoek's *De waag op de Nieuwmarkt*
      ([bol.com](https://www.bol.com/be/nl/p/de-waag-op-de-nieuwmarkt/1001004001539492/),
      accessed 2026-07-13) — **nonfiction architecture/local history of
      the building itself**, different shelf, different buyer intent;
      logged as an adjacency, not a collision. Remaining hits were
      venues (Brasserie De Waag Drachten, Hotel De Waag Bergen) — search
      noise, not books.
- [x] Verdict: **None** for fiction (standing caveat: Dutch self-pub
      titles are unevenly web-indexed; "none found" is weaker evidence
      than for trad-pub — same caveat as both prior NL packets).
- [x] Strong+ differentiator: the subtitle (§1) already carries this.
- [x] Final bol.com/KDP title-availability recheck at upload time remains
      the owner's standard §7 step.

## 3. Market verification

- [x] **Length class (measured, not guessed):** verbatim `wc -w`
      **36,997** (NOTES.md, measured 2026-07-13) — short-novel band, the
      catalog's longest NL edition (the EN source calls itself a novella
      at ~36k; either way it clears the novella floor with margin).
      Length is a verified fact carried from the manuscript's own
      measurement, not a guess.
- [x] **Language/platform check (verified in the plan):** KDP supports
      Dutch for ebook; the Dutch **PDF-upload gotcha applies only to
      fixed-layout picture books**, not a reflowable text novel
      ([plan §5, KDP language support, accessed 2026-07-12](../PUBLISHING-PLAN.md#5-translation-strategy)).
      A reflowable Dutch epub is a clean path.
- [x] Category comps: **NL-market comps not pulled** — honest gap,
      carried verbatim from the manuscript NOTES.md. Qualitative
      positioning only: misdaadromans/thrillers are the NL market's
      best-selling fiction shelf and this book's Amsterdam furniture
      reads native, not translated-exotic — but that shelf is also the
      market's most crowded, competing against Dutch-original crime
      authors. Price band therefore inherited conservatively from the EN
      packet, not re-derived (see §4).
- [x] Series/KU context: standalone with series potential (the EN
      README's dive-unit series note); no series home today — mitigation
      per plan §4 is KDP Select/KU enrollment (90-day reversible). The
      EN edition is the natural cross-listing companion once both are
      live.
- [x] Revenue framing: **unknown-author, translated-niche base case
      ≈ $0.** Unit economics only: €4.99-equivalent at the 70% tier
      ≈ €3.49/sale (minus delivery fee). No sales projection is made.

## 4. Price band

- [x] Band: inherited from the EN adult band **$3.99–$5.99
      (≈ €3.49–€5.49)** → **recommended €4.99** (Amazon.nl storefront
      pricing is set in EUR; 70%-royalty band respected). NOT re-derived
      from NL comps — flagged in §3; owner may adjust at click time.
- [x] No impulse-price trade-off recommended (drops to 35%).
- [x] Print: not in first-release scope — ebook-only, cover-only gate.

## 5. Packaging (production gate)

- [x] Gate: **cover-only** — adult text title, no interior illustration.
- [x] Ebook spec: **reflowable Dutch-language epub** built from
      `versions/nl/de-waag.md` (clean Markdown; direct epub conversion
      path). Language metadata: **Dutch (nl)** — set at upload, not
      defaulted. Cover 1600×2560 px minimum.
- [x] Cover: the EN packet's composition brief (winter canal at dawn,
      police-tent glow on dark water, the Waag's towers) **translates
      unchanged** — only the title/subtitle type swaps to Dutch. No
      separate art spend needed if the EN cover is commissioned first:
      one composition, two type layers. ⚑ spend/approval is OWNER-GATE
      (§7).
- [x] Quality gate carried from NOTES.md: **native-speaker proofread
      pass before any listing is drafted** — weighted here toward the
      police-diving technical register (seinlijn/daallijn/tamp) — queued
      as an explicit §7 row.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] **Blurb/description** (KDP book description, Dutch, draft v1 —
      same register as the manuscript):

> Het water is drie graden en heeft de kleur van niets. Wanneer
> politieduiker Sanne Kessler bij het eerste licht een verzwaard lichaam
> uit de Kloveniersburgwal haalt, leest ze de gordels op de tast: duiklood,
> teamuitgifte, aangesnoerd op de ruggengraat waar geen mens er zelf bij
> kan. Het korps noemt het zelfmoord. Sanne weet beter — want dit is
> precies hoe haar eigen man twee jaar geleden verdronk, in een dood die
> binnen drie dagen werd afgedaan als ongeval.
>
> Samen met Nadia Okonkwo, een rechercheur uit Rotterdam die nog geen
> vrienden heeft om uit te geven, volgt Sanne het spoor van de dode
> compliancemedewerker naar zes volmaakte, lege grachtenpanden en een
> notariskantoor waar vuil geld schoon papier wordt. Maar de gordels om de
> dode man zijn gemarkeerd met de letters van haar eigen duikteam — en hoe
> dichter Sanne bij de waarheid komt, hoe duidelijker wordt dat de
> moordenaar het water even goed kent als zij. Dat hij haar kent. Dat hij,
> elke keer dat ze afdaalt in het zwart, het andere eind van haar lijn
> vasthoudt.
>
> *De Waag* is een Amsterdamse misdaadroman over vertrouwen aan de lijn,
> over geld dat van naam verandert, en over wat het kost om de waarheid
> naar boven te brengen uit water dat is gebouwd om haar te houden.

- [x] **Two categories:** (1) Mystery, Thriller & Suspense → Crime
      Fiction → **Police Procedurals**; (2) Mystery → **International
      Mystery & Crime** — the EN edition's two nodes (KDP browse nodes
      are storefront-global; the Dutch edition surfaces to NL-language
      browsers via its language metadata, not via different nodes). No
      new category row vs the keyword map: same-title editions share
      their nodes by design (map rule C4).
- [x] **7 keywords (Dutch-language — separate C4 namespace from the EN
      rows; claimed in [`keyword-map.md`](../keyword-map.md) §1 this
      PR, all in the modern-crime register the C3 rule assigns The Weigh
      House):**
      1. `Amsterdamse misdaadroman`
      2. `Nederlandse politiethriller`
      3. `politieduiker thriller`
      4. `moord in de gracht roman`
      5. `witwassen grachtenpand thriller`
      6. `literaire thriller Amsterdam`
      7. `weduwe onderzoekt dood echtgenoot`
- [x] **Subtitle decision locked into metadata draft:** subtitle **ON** —
      *Een Amsterdamse misdaadroman* (§1 bare-word mitigation; genre
      signalling).
- [x] **Content note for the listing** (mirrors the manuscript front
      matter): moord, verdrinking, niet-grafisch geweld, rouw en het
      verlies van een echtgenoot, thema's van criminele geldstromen,
      incidenteel grof taalgebruik. Geen seksueel expliciete inhoud.
- [x] **KDP Select (KU): YES — enroll** (90-day exclusive, reversible) —
      same standalone rationale as the catalog's other NL editions; KU
      exists on Amazon.nl.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none**
of it. The Dutch edition's clicks are naturally bundled AFTER the EN
edition's (shared cover composition, shared account/tax setup).

**OWNER-ACTION — Publish "De Waag" (Dutch edition)**
1. **Sequencing:** publish the EN edition first (packet
   [`the-weigh-house.md`](the-weigh-house.md) §7) — account/tax interview
   and the cover composition carry over.
2. **Proofread:** commission or perform a native-speaker proofread pass of
   `versions/nl/de-waag.md` (NOTES.md quality follow-up, police-diving
   register weighted); owner approves any spend.
3. **Cover:** reuse the EN composition with Dutch title + subtitle type
   (1600×2560 px min); owner approves any incremental spend.
4. **Format:** reflowable Dutch epub from
   `candidates/adult-novels/the-weigh-house/versions/nl/de-waag.md`;
   language metadata **Dutch (nl)**; subtitle *Een Amsterdamse
   misdaadroman* ON (§1/§6).
5. **Price:** **€4.99** (70% tier; inherited band, not NL-re-derived —
   owner may adjust).
6. **Categories/keywords:** Police Procedurals + International Mystery &
   Crime; the 7 Dutch keywords in §6 verbatim; paste the §6 Dutch blurb +
   content note.
7. **KDP Select (KU):** **Yes** — enroll (90-day exclusive, reversible);
   final title-availability recheck (KDP + bol.com) before upload.

- [ ] ⚑ **Owner:** EN edition published first (sequencing dependency).
- [ ] ⚑ **Owner:** native-speaker proofread pass approved/commissioned.
- [ ] ⚑ **Owner:** title-availability recheck (KDP + bol.com) at upload.
- [ ] ⚑ **Owner:** cover type-swap approved / any incremental spend
      authorized.
- [ ] ⚑ **Owner:** price set (€4.99 recommended, band inherited not
      NL-re-derived).
- [ ] ⚑ **Owner:** the publish click + KDP Select enrollment.
- [ ] Seat (post-click, no money moved): record the launch durably on
      `main` — verified listing URL, price, timestamp, kill-rule dates —
      in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md).

---

**Verdict: publish-ready up to the owner gate, sequenced behind the EN
edition.** Collision scan clean for fiction (2026-07-13, bare-word
handicap mitigated by subtitle); length measured; the honest gaps — NL
comps not pulled, price band inherited, proofread pending — are flagged
as explicit §7 rows, not skipped.
