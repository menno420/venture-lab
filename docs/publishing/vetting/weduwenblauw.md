# Title Vetting — Weduwenblauw

> **Status:** `plan`
>
> **NL-edition packet** — vetting for the Dutch edition of *Ultramarine*,
> per the one-pass [title-vetting checklist](../CHECKLIST.md). The
> manuscript exists and is complete
> (`versions/nl/weduwenblauw.md`, landed in the SAME PR as this packet —
> the one-PR pattern set by *De Waag*, PR #134). A Dutch listing is a
> SEPARATE KDP listing with its own language metadata and Dutch-language
> keywords — the EN packet [`ultramarine.md`](ultramarine.md) does not
> cover it. Everything marked **⚑ OWNER-GATE** is an owner click, never
> automated.

**Title:** Weduwenblauw · **Category:** adult / literary historical
fiction, Dutch language (NL) · **Date vetted:** 2026-07-13

Manuscript:
[`candidates/adult-novels/ultramarine/versions/nl/`](../../../candidates/adult-novels/ultramarine/versions/nl/NOTES.md)
(complete Dutch translation of the full EN source; verbatim `wc -w`
28,439, measured in its NOTES.md 2026-07-13; EN source 27,865 words).
Fixes propagate EN → NL, never the reverse.

## 1. Title

- [x] Working title: **Weduwenblauw** — locked by the manuscript's own
      title decision (NOTES.md: alternatives *Ultramarijn*, *Het blauw
      van de weduwe*, *Het geheim van Holland*, *Het blauwe uur*
      considered and rejected with reasons; not relitigated here).
      Subtitle: ***Een roman over Delft, 1654*** — default ON, mirroring
      the EN packet's "A Novel of Delft, 1654" (place + date, the two
      searchable genre anchors).
- [x] **Upstream coupling (the packet's one live dependency):** the EN
      title is itself a pending ⚑ OWNER pick (EN packet §2/§7, default
      ***The Widow's Blue***). *Weduwenblauw* is that default's natural
      Dutch form (the Ch. 11 title, made the book's title), AND it
      survives the alternate outcome: if the owner keeps *Ultramarine*
      for EN, the direct Dutch title *Ultramarijn* is independently
      blocked (§2), so the NL edition keeps *Weduwenblauw* either way.
      Decide-and-flag: chosen now, ⚑ ratification rides the same owner
      click as the EN pick (§7).
- [x] Bare-word searchability: a coined compound — unlike the catalog's
      bare-word problem titles (Lull, De Waag) it has essentially zero
      competing search surface; the risk inverts to "nobody searches it",
      which the subtitle's `Delft, 1654` anchors mitigate.
- [x] Homophone / autocorrect drift: low; "weduwenblauw" is spell-stable
      Dutch compounding. Fuzzy overlap with *Nachtblauw* (van der Vlugt)
      is shelf-adjacency, not drift (§2).

## 2. Collision scan (discoverability, not legality — NL market)

- [x] Fresh web checks this session (2026-07-13, three queries:
      `"Weduwenblauw" boek roman titel`, `"Ultramarijn" roman Henk van
      Woerden boek`, `"Het blauw van de weduwe" OR "Het geheim van
      Holland" boek roman`):
      1. **Weduwenblauw: no same-named book found.** Nearest shelf
         neighbour is Simone van der Vlugt's *Nachtblauw*
         ([bol.com](https://www.bol.com/nl/nl/f/nachtblauw/9200000052033846/))
         — a bestselling Dutch historical novel of **Delft Blue pottery,
         17th century**: logged as a strong ADJACENCY (same city, same
         century, colour-compound title) that doubles as comp evidence —
         the register demonstrably sells in Dutch — and as the title to
         differentiate from in the blurb (pigment/painters, not
         plateel).
      2. ***Ultramarijn* is head-on taken:** Henk van Woerden,
         *Ultramarijn* (2005), Gouden Uil winner 2006, in print, on
         school reading lists
         ([hebban](https://www.hebban.nl/boek/ultramarijn-h-van-woerden),
         [bol.com](https://www.bol.com/nl/f/ultramarijn/9200000079749911),
         [DBNL](https://www.dbnl.org/titels/titel.php?id=woer001ultr01),
         [Goodreads](https://www.goodreads.com/book/show/3334912)). The
         EN working title's direct translation is unavailable in-register
         in the NL market — which independently supports the EN packet's
         rename recommendation.
      3. *Het geheim van Holland*: existing nonfiction title (Uitgeverij
         Noord-Holland, Hembrugterrein history,
         [uitgeverij-noord-holland.nl](https://www.uitgeverij-noord-holland.nl/de-zaanstreek/het-geheim-van-holland/))
         — rejected. *Het blauw van de weduwe*: clean but wordier;
         retained as fallback only. *Het blauwe uur*: rejected upstream
         (Paula Hawkins collision per the EN packet; her Dutch edition
         occupies the phrase).
- [x] Verdict: **None for Weduwenblauw** (standing caveat: Dutch self-pub
      titles are unevenly web-indexed; "none found" is weaker evidence
      than for trad-pub — same caveat as all three prior NL packets).
- [x] Strong+ differentiator: the compound title is itself the
      differentiator; subtitle carries genre/era.
- [x] Final bol.com/KDP title-availability recheck at upload time remains
      the owner's standard §7 step.

## 3. Market verification

- [x] **Length class (measured, not guessed):** verbatim `wc -w`
      **28,439** (NOTES.md, measured 2026-07-13) — mid-novella band,
      +2.1% over the EN source's 27,865, inside the catalog's measured
      NL expansion band (+1.5%…+2.5%). Complete resolved arc, all 12
      chapters, zero placeholder markers (EN completeness verified in
      the EN packet §3; the NL mirrors it heading-for-heading).
- [x] Category comps: **NL-market comps not formally pulled** — honest
      gap, carried from all prior NL packets — but the §2 scan surfaced
      real qualitative evidence unprompted: van der Vlugt's *Nachtblauw*
      (Delft, 17th century, craft-and-widowhood themes) is a proven NL
      bestseller register. Positioning: literaire historische roman on
      the Chevalier/Burton shelf, which reads native in Dutch (the
      book's furniture — Verwersdijk, Sint-Lucasgilde, het Secreet van
      Holland — needs no translation). Price band inherited, not
      re-derived (§4).
- [x] Language/platform: KDP supports Dutch ebooks; reflowable Dutch
      epub is the clean path (fixed-layout PDF gotcha applies to picture
      books only — verified in the plan §5, carried by every NL packet
      since #126).
- [x] Series/KU context: standalone, no series home; KDP Select/KU
      enrollment (90-day reversible) is the standing mitigation; KU
      exists on Amazon.nl. The EN edition is the natural cross-listing
      companion once both are live.
- [x] Revenue framing: **unknown-author, translated-niche base case
      ≈ $0.** Unit economics only: €4.99 at the 70% tier ≈ €3.49/sale
      (minus delivery fee). No sales projection is made.

## 4. Price band

- [x] Band: inherited from the EN packet **$3.99–$5.99 (≈ €3.49–€5.49)**
      → **recommended €4.99** (Amazon.nl storefront prices in EUR; 70%
      band respected; catalog-consistent with De Waag and the EN
      recommendation for this title). NOT re-derived from NL comps —
      flagged in §3; owner may adjust at click time. Fallback €3.99.
- [x] No impulse-price trade-off recommended (drops to 35%).
- [x] Print: not in first-release scope — ebook-only, cover-only gate.

## 5. Packaging (production gate)

- [x] Gate: **cover-only** — adult text title, no interior illustration.
- [x] Ebook spec: **reflowable Dutch-language epub** built from
      `versions/nl/weduwenblauw.md` (clean Markdown, 12 `##`-headed
      chapters under three `#` part heads — direct epub conversion
      path). Language metadata: **Dutch (nl)** — set at upload, not
      defaulted. Cover 1600×2560 px minimum.
- [x] Cover: the EN packet's §6a composition brief (drift of ground
      ultramarine on a dark table / lapis by a stone muller, low
      Vermeer-style window light; alt: Nieuwe Kerk silhouette against a
      blue-hour sky) **translates unchanged** — only title/subtitle type
      swaps to Dutch. One composition, two type layers if the EN cover
      is commissioned first. ⚑ spend/approval is OWNER-GATE (§7).
- [x] Quality gate carried from NOTES.md: **native-speaker proofread
      pass before any listing is drafted** — weighted toward the
      pigment-trade and guild registers (loper/wrijfsteen, gebeurnis,
      keur, weduwenverlof) — queued as an explicit §7 row.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] **Blurb/description** (KDP book description, Dutch, draft v1 —
      same register as the manuscript):

> Delft, najaar 1654. Blauw komt moeizaam tot Clara Wijnants — per
> gewicht, door malen, door de geduldige vernieling van het ene ding om
> er een ander van te maken. Als weduwe drijft ze aan de Verwersdijk de
> kleurhandel van haar gestorven man voort: ze breekt lazuursteen tot
> ultramarijn, een poeder duurder dan hetzelfde gewicht aan munt, voor
> schilders als Carel Fabritius — Rembrandts stoutmoedigste leerling,
> haar klant en bijna een vriend, die aan haar toonbank hardop droomt
> van een blauw dat nog niemand in een schilderij heeft gelegd. Een
> blauw dat je ademen kunt.
>
> Twee straten van haar deur, achter de muren van een oud klooster,
> bewaart de stad tachtigduizend pond buskruit en noemt het het Secreet
> van Holland — half als grap, zoals je een ding klein maakt dat te
> groot is om naar te blijven kijken.
>
> Op de twaalfde oktober spreekt het Secreet, en een kwart van Delft is
> weg in één wit ogenblik: Clara's winkel, haar maaljongen, haar
> schilder, en bijna ook het verweesde nichtje dat alles is wat haar aan
> familie rest. Wat overblijft is een kind dat niet meer spreekt, een
> gildeoudste die het recht van een vrouw op haar kraam altijd al
> betwijfelde, en een voorraad van het kostbaarste blauw ter wereld,
> ergens begraven onder het puin. Om haar leven terug op te graven moet
> Clara doen wat haar ambacht haar leerde: breken wat mooi is, wassen
> wat gebroken is, en dankbaar leren zijn voor wat bezinkt.
>
> *Weduwenblauw* is een zelfstandige literaire roman (~28.000 woorden)
> over de historische Delftse donderslag — rouw, ambacht en de prijs van
> schoonheid — voor lezers van Tracy Chevalier, Jessie Burton en Simone
> van der Vlugts *Nachtblauw*.

- [x] **Two categories:** (1) Literature & Fiction → Genre Fiction →
      **Historical Fiction**; (2) Literature & Fiction → **Literary
      Fiction** — the EN edition's two nodes (KDP browse nodes are
      storefront-global; the Dutch edition surfaces to NL-language
      browsers via language metadata). No new category row vs the
      keyword map: same-title editions share their nodes by design (map
      rule C4). The Literary Fiction node carries the standing C1
      CONTESTED marker via the EN row; nothing new claimed.
- [x] **7 keywords (Dutch-language — separate C4 namespace from the EN
      rows; claimed in [`keyword-map.md`](../keyword-map.md) §1 this PR,
      all in the Golden-Age register the C3 rule assigns Ultramarine):**
      1. `Gouden Eeuw roman`
      2. `Delft 1654 historische roman`
      3. `Delftse donderslag roman`
      4. `historische roman schilderkunst`
      5. `Vermeer tijdperk roman`
      6. `weduwe rouw literaire roman`
      7. `zeventiende eeuw novelle`
      Register note: `weduwe rouw literaire roman` is the Dutch mirror
      of the EN C2 watched adjacency (grief-literary intent) opposite De
      Waag's crime-intent `weduwe onderzoekt dood echtgenoot` — exactly
      the split De Waag's map row anticipated. No van der Vlugt title
      words are drafted (register etiquette per C4: no title-adjacent
      keyword squatting).
- [x] **Subtitle decision locked into metadata draft:** subtitle **ON** —
      *Een roman over Delft, 1654* (§1; era/genre anchors for a coined
      compound title).
- [x] **Content note for the listing** (mirrors the manuscript front
      matter): een ramp met vele doden op de bladzijde (ontploffing,
      dood, niet-identificeerbare slachtoffers), de dood van een
      tienerpersonage en een kind in gevaar, rouw en verlies, en de
      maatschappelijke en economische hardheid van een weduwenbestaan in
      een gildestad. Geen expliciet seksuele inhoud; geen nodeloos
      bloedige beschrijvingen. Voor volwassen lezers.
- [x] **KDP Select (KU): YES — enroll** (90-day exclusive, reversible) —
      standalone with no series home, same rationale as the catalog's
      other NL editions; KU exists on Amazon.nl.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none**
of it. The Dutch edition's clicks are naturally bundled AFTER the EN
edition's (shared cover composition, shared account/tax setup) — and the
EN edition itself carries the ⚑ title pick this packet is coupled to.

**OWNER-ACTION — Publish "Weduwenblauw" (Dutch edition)**
1. **Sequencing:** publish the EN edition first (packet
   [`ultramarine.md`](ultramarine.md) §7) — account/tax interview and the
   cover composition carry over.
2. **Title coupling (⚑ one click, two editions):** when picking the EN
   title (default *The Widow's Blue*), ratify the NL pairing
   **Weduwenblauw** (recommended default; fallback *Het blauw van de
   weduwe*; *Ultramarijn* is blocked by van Woerden regardless of the EN
   outcome). Then the KDP + bol.com title-availability recheck at upload.
3. **Proofread:** commission or perform a native-speaker proofread pass
   of `versions/nl/weduwenblauw.md` (NOTES.md quality follow-up,
   pigment/guild register weighted); owner approves any spend.
4. **Cover:** reuse the EN §6a composition with Dutch title + subtitle
   type (1600×2560 px min); owner approves any incremental spend.
5. **Format:** reflowable Dutch epub from
   `candidates/adult-novels/ultramarine/versions/nl/weduwenblauw.md`;
   language metadata **Dutch (nl)**; subtitle *Een roman over Delft,
   1654* ON (§1/§6).
6. **Price:** **€4.99** (70% tier; inherited band, not NL-re-derived —
   owner may adjust; fallback €3.99).
7. **Categories/keywords:** Historical Fiction + Literary Fiction; the 7
   Dutch keywords in §6 verbatim; paste the §6 Dutch blurb + content
   note.
8. **KDP Select (KU):** **Yes** — enroll (90-day exclusive, reversible),
   then the publish click.

- [ ] ⚑ **Owner:** EN edition published first (sequencing dependency).
- [ ] ⚑ **Owner:** EN+NL title pair ratified (The Widow's Blue ↔
      Weduwenblauw recommended); title-availability recheck (KDP +
      bol.com) at upload.
- [ ] ⚑ **Owner:** native-speaker proofread pass approved/commissioned.
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
edition and coupled to its ⚑ title pick.** Collision scan clean for
*Weduwenblauw* (2026-07-13; the direct-translation title *Ultramarijn* is
evidenced blocked by van Woerden's Gouden Uil winner); length measured
(28,439); the honest gaps — NL comps not formally pulled, price band
inherited, native proofread pending — are explicit §7 rows, not skipped.
