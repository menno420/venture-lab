# Catalog keyword & category allocation map

> **Status:** `reference`
>
> One table answers "who owns this KDP phrase?" for the 14-title catalog.
> Implements the 💡 idea from `.sessions/2026-07-12-publishing-plan-retier.md`
> (PR #94): vetting packets draft "2 categories + 7 keywords" in isolation, so
> with 14 titles heading for the same storefront several will converge on the
> same high-value phrases and cannibalize each other's placement. This map
> makes each packet CLAIM its phrases at vetting time — the way
> `control/claims/` claims work — so the catalog deliberately tiles the KDP
> search space instead of piling onto the same shelf.
>
> **Measured basis (ORDER 011 / V057 (sim-lab `32ff5c3`)):** VERDICT 057
> (approve) — the cannibalization theory above now carries a measured
> 12-cell basis instead of a gesture, and the coordination cost
> (CONFLICTS-before-ship, ⚑ OWNER gates, one-row-per-phrase discipline) is
> priced as worth paying: at every nonzero registered same-catalog
> dilution γ, tiling buys **6.5%–144.7%** catalog discovery traffic over
> independent greedy picks (γ = 1/4 row: LOW +71.8%, MED +15.4%,
> HIGH +6.5%) — sim-lab `sims/verdict-057-keyword-tiling/REPORT.md`.
> C2-style KEEP BOTH stays the **argued exception, not the default**.
> **γ = 0 boundary (rides every citation):** tiling pays IFF same-catalog
> dilution is nonzero — at γ = 0 exactly the convention is dead weight or
> worse (MED −37.8%, HIGH −31.5%); γ carries no live datapoint anywhere in
> the fleet, so the C2 page-co-occurrence browse check (one owner session
> once ≥ 2 titles are live, zero new tooling) ships as the pre-priced live
> measurement regardless. **APPLICATION GUARD (pre-registered):** the
> verdict conditions on this map's 14 × (2 + 7) first-claim shape @
> `be6c75d` — a restructured claim discipline means re-run, not reuse.

## How to use this map

- **Packets claim phrases here at vetting time** (CHECKLIST §6): before
  locking your 2 categories + 7 keywords, check this table; add one row per
  keyword/category you take. First claim on `main` wins a collision
  (convention ratified with a measured basis by VERDICT 057 — see the
  header note; ORDER 011 / V057 (sim-lab `32ff5c3`)).
- **One row per keyword** — no shared free-text blob; conflicts are resolved
  in the CONFLICTS section below **before a packet ships** (§7 owner gate).
- **Files are truth:** each vetted title's rows below reproduce its packet §6
  verbatim; if a packet and this map disagree, fix the map in the same PR
  that changed the packet.
- Disputed reallocations that would change an already-shipped packet carry a
  **⚑ OWNER** marker — the seat proposes, the owner decides; packets are not
  edited retroactively without that decision.

## 1. Ownership table — vetted packets (source: each packet's §6, verbatim)

### Categories

| Category (KDP browse node) | Owning title | Source |
|---|---|---|
| Science Fiction → **First Contact** | The Slow Word | [`vetting/the-slow-word.md`](vetting/the-slow-word.md) §6 |
| **Literary Fiction** | The Slow Word | [`vetting/the-slow-word.md`](vetting/the-slow-word.md) §6 — **CONTESTED, see C1** |
| Mystery, Thriller & Suspense → Crime Fiction → **Police Procedurals** | The Weigh House | [`vetting/the-weigh-house.md`](vetting/the-weigh-house.md) §6 |
| Mystery → **International Mystery & Crime** | The Weigh House | [`vetting/the-weigh-house.md`](vetting/the-weigh-house.md) §6 |
| Literature & Fiction → Genre Fiction → **Historical Fiction** | Ultramarine (default title *The Widow's Blue*, ⚑ OWNER pick pending) | [`vetting/ultramarine.md`](vetting/ultramarine.md) §6 |
| Literature & Fiction → **Literary Fiction** | Ultramarine — **CONTESTED, see C1** | [`vetting/ultramarine.md`](vetting/ultramarine.md) §6 |
| Children's Books → **Mysteries & Detectives** | The Painted Stones | [`vetting/the-painted-stones.md`](vetting/the-painted-stones.md) §6 |
| Children's Books → Growing Up & Facts of Life → **Friendship** | The Painted Stones | [`vetting/the-painted-stones.md`](vetting/the-painted-stones.md) §6 |
| Historical Fiction → **World War II** | De papieren sinaasappel (NL edition of The Paper Orange, first claimant) **+ The Paper Orange (EN edition — SHARED since its graduation 2026-07-13, per C4)** | [`vetting/de-papieren-sinaasappel.md`](vetting/de-papieren-sinaasappel.md) §6 + [`vetting/the-paper-orange.md`](vetting/the-paper-orange.md) §6 |
| Literature & Fiction → **War & Military** | De papieren sinaasappel (NL edition, first claimant) **+ The Paper Orange (EN edition — SHARED since graduation 2026-07-13, per C4)** | [`vetting/de-papieren-sinaasappel.md`](vetting/de-papieren-sinaasappel.md) §6 + [`vetting/the-paper-orange.md`](vetting/the-paper-orange.md) §6 |
| Science Fiction & Fantasy → Fantasy → **Cozy Fantasy** (fallback Fantasy → Contemporary) | De Nachtoven (NL edition of The Night Kiln, first claimant — EN packet concept-stage, shares at graduation per C4) **+ De Morgendeur (Night Kiln Book Two NL — SHARED 2026-07-14 per the §3 series rule: series shares the shelf, deliberate co-location; separate listing, no duplicate row)** **+ De Oogstslag (Night Kiln Book Three NL — SHARED 2026-07-14 per the §3 series rule; separate listing, no duplicate row)** | [`vetting/de-nachtoven.md`](vetting/de-nachtoven.md) §6 + [`vetting/de-morgendeur.md`](vetting/de-morgendeur.md) §6 + [`vetting/de-oogstslag.md`](vetting/de-oogstslag.md) §6 |
| Literature & Fiction → Genre Fiction → **Magical Realism** | De Nachtoven (NL edition, first claimant — EN shares at graduation per C4) **+ De Morgendeur (Book Two NL — SHARED 2026-07-14, series rule as above)** **+ De Oogstslag (Night Kiln Book Three NL — SHARED 2026-07-14 per the §3 series rule; separate listing, no duplicate row)** | [`vetting/de-nachtoven.md`](vetting/de-nachtoven.md) §6 + [`vetting/de-morgendeur.md`](vetting/de-morgendeur.md) §6 + [`vetting/de-oogstslag.md`](vetting/de-oogstslag.md) §6 |
| Mystery, Thriller & Suspense → Mystery → Cozy → **Amateur Sleuths** | De Marmeladepost (NL edition of The Marmalade Post, first claimant — EN packet concept-stage, shares at graduation per C4) | [`vetting/de-marmeladepost.md`](vetting/de-marmeladepost.md) §6 |
| Mystery, Thriller & Suspense → Mystery → **Women Sleuths** | De Marmeladepost (NL edition, first claimant — EN shares at graduation per C4) | [`vetting/de-marmeladepost.md`](vetting/de-marmeladepost.md) §6 |
| Literature & Fiction → Genre Fiction → **Ghosts** | De glazen pastorie (NL edition of The Glass Rectory, first claimant — EN packet concept-stage, shares at graduation per C4) | [`vetting/de-glazen-pastorie.md`](vetting/de-glazen-pastorie.md) §6 |
| Horror → **Gothic** | De glazen pastorie (NL edition, first claimant — EN shares at graduation per C4) | [`vetting/de-glazen-pastorie.md`](vetting/de-glazen-pastorie.md) §6 |
| Literature & Fiction → Genre Fiction → **Holidays** | De Driekoningentaart (NL edition of The Twelfth Cake, first claimant — EN packet concept-stage, shares at graduation per C4) | [`vetting/de-driekoningentaart.md`](vetting/de-driekoningentaart.md) §6 |
| Literature & Fiction → Genre Fiction → Historical Fiction → **Victorian** (era sub-node; parent node is Ultramarine's — Paper Orange sub-node precedent) | De Driekoningentaart (NL edition, first claimant — EN shares at graduation per C4) | [`vetting/de-driekoningentaart.md`](vetting/de-driekoningentaart.md) §6 |
| Science Fiction → **Climate Fiction** (exact node name re-verified against the live browse tree at upload) | De geborgen boomgaard (NL edition of The Salvage Orchard, first claimant — EN packet concept-stage, shares at graduation per C4) | [`vetting/de-geborgen-boomgaard.md`](vetting/de-geborgen-boomgaard.md) §6 |
| Literature & Fiction → Genre Fiction → **Urban Life** | De geborgen boomgaard (NL edition, first claimant — EN shares at graduation per C4) | [`vetting/de-geborgen-boomgaard.md`](vetting/de-geborgen-boomgaard.md) §6 |
| Romance → **Clean & Wholesome** | Liefde in de kantlijn (NL edition of The Seed Catalogue Courtship, first claimant — EN packet concept-stage, shares at graduation per C4; the catalog's first Romance-storefront claim) | [`vetting/liefde-in-de-kantlijn.md`](vetting/liefde-in-de-kantlijn.md) §6 |
| Romance → **Later in Life** | Liefde in de kantlijn (NL edition, first claimant — EN shares at graduation per C4) | [`vetting/liefde-in-de-kantlijn.md`](vetting/liefde-in-de-kantlijn.md) §6 |
| Literature & Fiction → Genre Fiction → **Sea Stories** | The Sweetwater Sea (manuscript-backed, claimed 2026-07-14 — no prior §3 reservation) **+ De zoete zee (NL edition — SHARED 2026-07-14 per C4: same-title editions share browse nodes; separate listing, no duplicate row)** | [`vetting/the-sweetwater-sea.md`](vetting/the-sweetwater-sea.md) §6 + [`vetting/de-zoete-zee.md`](vetting/de-zoete-zee.md) §6 |
| Literature & Fiction → **Small Town & Rural** | The Sweetwater Sea **+ De zoete zee (NL edition — SHARED 2026-07-14 per C4: same-title editions share browse nodes; separate listing, no duplicate row)** | [`vetting/the-sweetwater-sea.md`](vetting/the-sweetwater-sea.md) §6 + [`vetting/de-zoete-zee.md`](vetting/de-zoete-zee.md) §6 |
| Literature & Fiction → Genre Fiction → Historical Fiction → **World War I** (era sub-node; parent node is Ultramarine's — Paper Orange WWII / Driekoningentaart Victorian sub-node precedent; sibling of Paper Orange's World War II sub-node) | The Wire Garden (manuscript-backed, claimed 2026-07-14 — no prior §3 reservation) | [`vetting/the-wire-garden.md`](vetting/the-wire-garden.md) §6 |
| Literature & Fiction → Genre Fiction → **Animals** (exact node name re-verified against the live browse tree at upload) | The Wire Garden (manuscript-backed, claimed 2026-07-14) | [`vetting/the-wire-garden.md`](vetting/the-wire-garden.md) §6 |
| Literature & Fiction → Genre Fiction → Historical Fiction → **20th Century** (era sub-node; parent Historical Fiction node is Ultramarine's — the Paper Orange WWII / Wire Garden WWI / Driekoningentaart Victorian sub-node precedent; 1953 is postwar, hence the general 20th-Century era node, not a war sub-node) | The Salt Bell (manuscript-backed, claimed 2026-07-16 — no prior §3 reservation) | [`vetting/the-salt-bell.md`](vetting/the-salt-bell.md) §6 |
| Literature & Fiction → Genre Fiction → **Disaster** (exact node name re-verified against the live browse tree at upload; owner picks a genuinely unclaimed second node at upload if the Disaster node is absent — Small Town & Rural is The Sweetwater Sea's and is NOT to be co-claimed) | The Salt Bell (manuscript-backed, claimed 2026-07-16) | [`vetting/the-salt-bell.md`](vetting/the-salt-bell.md) §6 |

*Edition-sharing note (C4):* **Het trage woord** (NL edition of The Slow
Word, [`vetting/het-trage-woord.md`](vetting/het-trage-woord.md) §6) uses
The Slow Word's two nodes above — same-title editions share browse nodes by
design and add no duplicate category row. **De Waag** (NL edition of The
Weigh House, [`vetting/de-waag.md`](vetting/de-waag.md) §6) likewise uses
The Weigh House's two nodes above (Police Procedurals + International
Mystery & Crime). **Weduwenblauw** (NL edition of Ultramarine,
[`vetting/weduwenblauw.md`](vetting/weduwenblauw.md) §6) likewise uses
Ultramarine's two nodes above (Historical Fiction + Literary Fiction,
inheriting the C1 CONTESTED marker via the EN row). **The Paper Orange**
(EN edition, graduated 2026-07-13,
[`vetting/the-paper-orange.md`](vetting/the-paper-orange.md) §6) is the
inverted case C4 anticipated: its manuscript-backed NL edition claimed the
two WWII nodes first (PR #131), and the EN edition now SHARES those same
nodes at graduation — same rule, no duplicate category row beyond the
shared-owner annotation above. **The 2026-07-14 NL wave repeats that
inverted case four times:** *De Nachtoven*, *De Marmeladepost*, *De glazen
pastorie*, and *De Driekoningentaart* (NL editions of the four concept-stage
EN packets, manuscripts merged as PRs #175/#176/#177/#178) each claim their
title's two nodes first in the rows above; each EN edition shares them at
its own graduation. **The 2026-07-14 NL-completion batch adds two more of
the same inverted case** — *De geborgen boomgaard* (PR #184) and *Liefde in
de kantlijn* (PR #183) claim their concept-stage EN titles' nodes first —
**plus the map's first SERIES node-sharing:** *De Morgendeur* (Night Kiln
Book Two NL, PR #185) is a separate listing that SHARES De Nachtoven's two
nodes per the §3 series rule ("series shares the niche") extended to browse
nodes — deliberate co-location, per-book keywords differentiated, no
duplicate category row beyond the shared-owner annotation above. **The
2026-07-14 night-final slice adds one of each case:** *De zoete zee* (NL
edition of The Sweetwater Sea,
[`vetting/de-zoete-zee.md`](vetting/de-zoete-zee.md) §6) uses The
Sweetwater Sea's two nodes above — the straight C4 case (EN claimed first
at its manuscript-backed vetting; the NL edition shares) — and *De
Oogstslag* (Night Kiln Book Three NL,
[`vetting/de-oogstslag.md`](vetting/de-oogstslag.md) §6) is the map's
second SERIES node-sharing, riding De Nachtoven's two nodes per the same
§3 series rule.

### Keywords

| Keyword (verbatim) | Owning title |
|---|---|
| `first contact novella` | The Slow Word |
| `deep time science fiction` | The Slow Word |
| `literary sci-fi Pacific island` | The Slow Word |
| `radio telescope alien signal story` | The Slow Word |
| `indigenous knowledge science fiction` | The Slow Word |
| `slow message from the stars` | The Slow Word |
| `generational legacy novella` | The Slow Word |
| `Amsterdam crime novel` | The Weigh House |
| `Dutch police procedural` | The Weigh House |
| `police diver mystery` | The Weigh House |
| `canal murder Netherlands` | The Weigh House |
| `atmospheric European noir` | The Weigh House |
| `money laundering crime fiction` | The Weigh House |
| `widow investigates husband's death` | The Weigh House (see C2 — watched adjacency) |
| `Dutch Golden Age novel` | Ultramarine |
| `Delft 1654 historical fiction` | Ultramarine |
| `Vermeer era Netherlands story` | Ultramarine |
| `painter pigment art historical novel` | Ultramarine |
| `widow grief literary fiction` | Ultramarine (see C2 — watched adjacency) |
| `Delft Thunderclap gunpowder explosion` | Ultramarine |
| `17th century historical novella` | Ultramarine |
| `picture book mystery ages 4-8` | The Painted Stones |
| `girl detective picture book` | The Painted Stones |
| `new kid making friends story` | The Painted Stones |
| `read aloud mystery for kids` | The Painted Stones |
| `shy child friendship picture book` | The Painted Stones |
| `seaside village children's story` | The Painted Stones |
| `welcoming new neighbors book` | The Painted Stones |
| `Hunger Winter novel` | The Paper Orange (graduated 2026-07-13 — C3 WWII-occupation register) |
| `WWII Netherlands fiction` | The Paper Orange (C3 WWII-occupation register) |
| `Amsterdam occupation 1944 story` | The Paper Orange (see the C2-pattern watched adjacency vs Weigh House's `Amsterdam crime novel` — disjoint intent: WWII-historical vs contemporary-crime) |
| `Dutch resistance historical novel` | The Paper Orange (C3 WWII-occupation register) |
| `ration coupon forgery wartime story` | The Paper Orange (C3 WWII-occupation register) |
| `Liberation of Holland fiction` | The Paper Orange (C3 WWII-occupation register) |
| `wartime widow survival novella` | The Paper Orange (widow stem, C2 pattern: wartime-survival intent — disjoint from Weigh House's crime row and Ultramarine's grief-literary row) |
| `sciencefiction novelle Nederlands` | Het trage woord (NL — C4 namespace) |
| `eerste contact roman` | Het trage woord (NL — C4 namespace) |
| `literaire sciencefiction` | Het trage woord (NL — C4 namespace) |
| `buitenaards signaal roman` | Het trage woord (NL — C4 namespace) |
| `radiotelescoop Stille Oceaan roman` | Het trage woord (NL — C4 namespace) |
| `diepe tijd sciencefiction` | Het trage woord (NL — C4 namespace) |
| `boodschap van de sterren novelle` | Het trage woord (NL — C4 namespace) |
| `literaire roman Hongerwinter` | De papieren sinaasappel (NL — C4 namespace) |
| `Tweede Wereldoorlog Amsterdam roman` | De papieren sinaasappel (NL — C4 namespace) |
| `bezetting 1944 roman` | De papieren sinaasappel (NL — C4 namespace) |
| `bonkaarten vervalsing oorlog` | De papieren sinaasappel (NL — C4 namespace) |
| `drukkerij verzet roman` | De papieren sinaasappel (NL — C4 namespace) |
| `oorlogsweduwe roman Nederland` | De papieren sinaasappel (NL — C4 namespace) |
| `bevrijding 1945 roman` | De papieren sinaasappel (NL — C4 namespace) |
| `Amsterdamse misdaadroman` | De Waag (NL — C4 namespace, C3 modern-crime register) |
| `Nederlandse politiethriller` | De Waag (NL — C4 namespace, C3 modern-crime register) |
| `politieduiker thriller` | De Waag (NL — C4 namespace, C3 modern-crime register) |
| `moord in de gracht roman` | De Waag (NL — C4 namespace, C3 modern-crime register) |
| `witwassen grachtenpand thriller` | De Waag (NL — C4 namespace, C3 modern-crime register) |
| `literaire thriller Amsterdam` | De Waag (NL — C4 namespace, C3 modern-crime register) |
| `weduwe onderzoekt dood echtgenoot` | De Waag (NL — C4 namespace; Dutch mirror of the EN C2 watched adjacency — crime intent vs Weduwenblauw's grief-literary phrase below) |
| `Gouden Eeuw roman` | Weduwenblauw (NL — C4 namespace, C3 Golden-Age register) |
| `Delft 1654 historische roman` | Weduwenblauw (NL — C4 namespace, C3 Golden-Age register) |
| `Delftse donderslag roman` | Weduwenblauw (NL — C4 namespace, C3 Golden-Age register) |
| `historische roman schilderkunst` | Weduwenblauw (NL — C4 namespace, C3 Golden-Age register) |
| `Vermeer tijdperk roman` | Weduwenblauw (NL — C4 namespace, C3 Golden-Age register) |
| `weduwe rouw literaire roman` | Weduwenblauw (NL — C4 namespace; grief-literary mirror of the C2 watched adjacency, opposite De Waag's crime-intent row above) |
| `zeventiende eeuw novelle` | Weduwenblauw (NL — C4 namespace, C3 Golden-Age register) |
| `cozy fantasy Nederlands` | De Nachtoven (NL — C4 namespace) |
| `cozy fantasy novelle` | De Nachtoven (NL — C4 namespace) |
| `dorpsheks fantasy roman` | De Nachtoven (NL — C4 namespace) |
| `magische pottenbakkerij herinneringen` | De Nachtoven (NL — C4 namespace) |
| `hartverwarmende fantasy voor volwassenen` | De Nachtoven (NL — C4 namespace) |
| `found family fantasy novelle` | De Nachtoven (NL — C4 namespace) |
| `thee en magie fantasy` | De Nachtoven (NL — C4 namespace) |
| `cozy mystery Nederlands` | De Marmeladepost (NL — C4 namespace) |
| `Engels dorpsmysterie` | De Marmeladepost (NL — C4 namespace) |
| `postkantoor cozy mystery` | De Marmeladepost (NL — C4 namespace) |
| `moordmysterie Engels dorp` | De Marmeladepost (NL — C4 namespace; shares only the "moord" stem with De Waag's `moord in de gracht roman` — disjoint intent per the C2 pattern: cozy England vs procedural Amsterdam; watched adjacency, not a conflict) |
| `gezellige detective zonder geweld` | De Marmeladepost (NL — C4 namespace) |
| `dorpsgeheimen detective roman` | De Marmeladepost (NL — C4 namespace) |
| `nieuwe cozy detectiveserie` | De Marmeladepost (NL — C4 namespace) |
| `Victoriaans spookverhaal` | De glazen pastorie (NL — C4 namespace) |
| `klassiek spookverhaal novelle` | De glazen pastorie (NL — C4 namespace) |
| `gothic novelle Nederlands` | De glazen pastorie (NL — C4 namespace) |
| `spookhuis pastorie roman` | De glazen pastorie (NL — C4 namespace) |
| `sfeervolle stille horror` | De glazen pastorie (NL — C4 namespace) |
| `griezelverhaal voor volwassenen` | De glazen pastorie (NL — C4 namespace) |
| `gothic mysterie op de heide` | De glazen pastorie (NL — C4 namespace) |
| `Driekoningen roman` | De Driekoningentaart (NL — C4 namespace) |
| `driekoningentaart verhaal fictie` | De Driekoningentaart (NL — C4 namespace) |
| `Victoriaanse feestdagen novelle` | De Driekoningentaart (NL — C4 namespace) |
| `bakkerij historische roman Londen` | De Driekoningentaart (NL — C4 namespace) |
| `boon in de taart traditie verhaal` | De Driekoningentaart (NL — C4 namespace) |
| `Dickensiaanse wintervertelling` | De Driekoningentaart (NL — C4 namespace; register etiquette: the exact Dickens NL titles "kerstverhaal"/"een kerstvertelling" deliberately NOT drafted — the Oorlogswinter/Terlouw no-title-squatting rule) |
| `historische feelgood novelle` | De Driekoningentaart (NL — C4 namespace) |
| `solarpunk novelle` | De geborgen boomgaard (NL — C4 namespace) |
| `hoopvolle klimaatfictie` | De geborgen boomgaard (NL — C4 namespace) |
| `cozy sciencefiction gemeenschap` | De geborgen boomgaard (NL — C4 namespace; shares only the bare `sciencefiction` stem with Het trage woord's rows — disjoint intent per the C2 pattern: climate-repair vs literary first-contact; watched adjacency, not a conflict) |
| `stadslandbouw nabije toekomst roman` | De geborgen boomgaard (NL — C4 namespace) |
| `boomgaard enten roman` | De geborgen boomgaard (NL — C4 namespace) |
| `optimistische wederopbouw roman` | De geborgen boomgaard (NL — C4 namespace) |
| `reparatiecultuur sciencefiction` | De geborgen boomgaard (NL — C4 namespace; `sciencefiction` stem — same watched adjacency as above) |
| `roman in brieven` | Liefde in de kantlijn (NL — C4 namespace; the "brieven" stem was unclaimed catalog-wide) |
| `briefroman liefdesverhaal` | Liefde in de kantlijn (NL — C4 namespace) |
| `liefde op latere leeftijd` | Liefde in de kantlijn (NL — C4 namespace) |
| `feelgood liefdesroman Engeland` | Liefde in de kantlijn (NL — C4 namespace; shares only the `feelgood` stem with De Driekoningentaart's row above — disjoint intent per the C2 pattern: contemporary-set romance vs Victorian seasonal-historical; watched adjacency, not a conflict) |
| `zadencatalogus roman` | Liefde in de kantlijn (NL — C4 namespace) |
| `tuinieren liefdesverhaal zaden` | Liefde in de kantlijn (NL — C4 namespace) |
| `ommuurde tuin restauratie roman` | Liefde in de kantlijn (NL — C4 namespace) |
| `cozy fantasy serie` | De Morgendeur (NL — C4 namespace; all seven Morgendeur rows are NEW phrases — Book Two is a separate listing and deliberately re-claims none of De Nachtoven's seven) |
| `gezellige fantasy dorpsverhaal` | De Morgendeur (NL — C4 namespace; `gezellige` stem vs De Marmeladepost — disjoint intent, fantasy vs detective; watched adjacency) |
| `fantasy novelle rouw en troost` | De Morgendeur (NL — C4 namespace) |
| `magie van herinneringen roman` | De Morgendeur (NL — C4 namespace; `herinneringen` stem vs De Nachtoven's row — DELIBERATE series adjacency: Books One/Two share the buyer by design; full phrases distinct, one row each) |
| `pottenbakkerij fantasy vervolg` | De Morgendeur (NL — C4 namespace; `pottenbakkerij` stem — same deliberate series adjacency as above) |
| `troostrijke fantasy novelle` | De Morgendeur (NL — C4 namespace) |
| `zachte fantasy zonder geweld` | De Morgendeur (NL — C4 namespace; `zonder geweld` stem vs De Marmeladepost — disjoint intent; watched adjacency) |
| `Zuiderzee novel` | The Sweetwater Sea (C3 interwar Zuiderzee-closure register) |
| `Afsluitdijk historical fiction` | The Sweetwater Sea (C3 interwar Zuiderzee-closure register) |
| `Dutch fishing village story` | The Sweetwater Sea (C3 interwar Zuiderzee-closure register) |
| `1930s Netherlands historical novel` | The Sweetwater Sea (C3 interwar register; shares only the `Netherlands` stem with Paper Orange's `WWII Netherlands fiction` — disjoint era intent per the C2 pattern: interwar public works vs wartime occupation; watched adjacency, not a conflict) |
| `father and son fishing novel` | The Sweetwater Sea |
| `interwar Holland novella` | The Sweetwater Sea (C3 interwar register; `Holland` stem vs Paper Orange's `Liberation of Holland fiction` — same watched adjacency as above) |
| `historical fiction about fishermen` | The Sweetwater Sea |
| `Zuiderzee roman` | De zoete zee (NL — C4 namespace, C3 interwar Zuiderzee-closure register; Dutch mirror of the EN edition's `Zuiderzee novel` — different query language per C4) |
| `Afsluitdijk historische roman` | De zoete zee (NL — C4 namespace, C3 interwar register; bare `historische roman` stem vs Weduwenblauw/De Driekoningentaart rows — watched adjacency in the C2 pattern, disjoint era intent) |
| `Wieringen vissersroman` | De zoete zee (NL — C4 namespace, C3 interwar register) |
| `historische novelle interbellum` | De zoete zee (NL — C4 namespace, C3 interwar register; bare `novelle` stem shared catalog-wide — watched adjacency only) |
| `ansjovisvisserij roman` | De zoete zee (NL — C4 namespace, C3 interwar register) |
| `vader en zoon vissersroman` | De zoete zee (NL — C4 namespace; Dutch mirror of the EN edition's `father and son fishing novel`) |
| `roman over de Zuiderzeewerken` | De zoete zee (NL — C4 namespace, C3 interwar register) |
| `cozy fantasy trilogie` | De Oogstslag (NL — C4 namespace; all seven Oogstslag rows are NEW phrases — Book Three is a separate listing and re-claims none of De Nachtoven's or De Morgendeur's fourteen) |
| `roeiwedstrijd roman` | De Oogstslag (NL — C4 namespace; `roeiwedstrijd` stem unclaimed catalog-wide) |
| `sfeervolle herfst fantasy` | De Oogstslag (NL — C4 namespace; `sfeervolle` stem vs De glazen pastorie's `sfeervolle stille horror` — disjoint intent, cozy fantasy vs quiet horror; watched adjacency in the C2 pattern, not a conflict) |
| `fantasy novelle over geheugenverlies` | De Oogstslag (NL — C4 namespace; `fantasy novelle` stem vs De Nachtoven/De Morgendeur rows — DELIBERATE series adjacency: the three books share the buyer by design; full phrases distinct, one row each) |
| `hartverwarmend verhaal over ouder worden` | De Oogstslag (NL — C4 namespace; `hartverwarmend` stem vs De Nachtoven's `hartverwarmende fantasy voor volwassenen` — same deliberate series adjacency) |
| `magisch ambacht dorpsverhaal` | De Oogstslag (NL — C4 namespace; `magisch` stem vs De Nachtoven, `dorpsverhaal` stem vs De Morgendeur's `gezellige fantasy dorpsverhaal` — same deliberate series adjacency; full phrase distinct) |
| `oogstfeest fantasy verhaal` | De Oogstslag (NL — C4 namespace; harvest-festival niche, unclaimed; no folk-dark stems — Hollowtide's reserved register untouched) |
| `Dodendraad novel` | The Wire Garden (C3 WWI neutral-border/Dodendraad register) |
| `Wire of Death WWI story` | The Wire Garden (C3 WWI register — "Wire of Death" is the standing English name for the Dodendraad) |
| `beekeeper historical novel` | The Wire Garden (`beekeeper`/`bee` stems unclaimed catalog-wide) |
| `WWI Dutch Belgian border novel` | The Wire Garden (C3 WWI register; bare `Dutch` stem vs Weigh House / Ultramarine / Paper Orange / Sweetwater rows — watched adjacency in the C2 pattern, disjoint war and intent) |
| `First World War neutral Netherlands fiction` | The Wire Garden (C3 WWI register; `Netherlands` stem vs Paper Orange's `WWII Netherlands fiction` and Sweetwater's `1930s Netherlands historical novel` — watched adjacency, disjoint era intent: WWI neutrality vs WWII occupation vs interwar public works) |
| `electric fence Great War novella` | The Wire Garden (C3 WWI register; `fence`/`Great War` stems unclaimed) |
| `smuggled letters wartime story` | The Wire Garden (C3 WWI register; `wartime` stem vs Paper Orange's rows — watched adjacency, disjoint war; `letters` stem watched vs The Seed Catalogue Courtship's §3 novel-in-letters reservation — smuggled-correspondence intent vs epistolary-romance intent, disjoint; no widow stems drafted, deliberately — the C2 widow cluster already carries three titles) |
| `1953 North Sea flood novel` | The Salt Bell (C3 postwar 1953-flood/Zeeland-Watersnood register) |
| `Zeeland flood historical fiction` | The Salt Bell (C3 1953-flood register; bare `historical fiction` stem shared catalog-wide — watched adjacency, disjoint era intent) |
| `Watersnoodramp novel` | The Salt Bell (C3 1953-flood register — "Watersnoodramp" is the standing Dutch name for the disaster, used here in the EN listing for the reader who searches it) |
| `Dutch flood disaster novella` | The Salt Bell (C3 1953-flood register; bare `Dutch` stem vs Weigh House / Ultramarine / Paper Orange / Sweetwater / Wire Garden rows — watched adjacency in the C2 pattern, disjoint era and event) |
| `Delta Works historical novel` | The Salt Bell (C3 1953-flood register; the Delta Works are the disaster's real aftermath — `Delta`/`sea defence` stems unclaimed catalog-wide) |
| `oyster village Zeeland story` | The Salt Bell (C3 1953-flood register; oyster/village intent watched vs The Sweetwater Sea's `Dutch fishing village story` and `historical fiction about fishermen` — disjoint trade and intent per the C2 pattern: oyster culture / 1953 disaster vs. anchovy salting / 1927–32 enclosure; the nearest in-catalog adjacency, deliberately phrased to stay clear of it) |
| `church bell ringer historical fiction` | The Salt Bell (`bell ringer`/`carillon`/`sexton` stems unclaimed catalog-wide) |

## 2. CONFLICTS (resolved here before any packet ships)

### C1 — Category **Literary Fiction**: The Slow Word vs Ultramarine (dispute)

Both packets claim a Literary Fiction browse node as their second category
(Slow Word: "Literary Fiction"; Ultramarine: "Literature & Fiction →
Literary Fiction"). Two catalog titles occupying the same second node
compete with each other for the same also-boughts and category ranking
instead of covering two shelves.

**Proposed resolution:** **The Slow Word keeps Literary Fiction** — it is
that book's only non-SF node, so losing it would leave the title entirely
inside genre-SF browse, which its register doesn't fit. **Ultramarine swaps
its second category** to another Literature & Fiction node that matches a
widow-grief Delft novel: proposed **Literature & Fiction → Women's Fiction →
Domestic Life** (a widowed dyer's-daughter rebuilding a household and a
craft after the 1654 Thunderclap is squarely domestic-life fiction; the
Chevalier/Burton readership browses there too). Fallback alternative:
Literature & Fiction → Genre Fiction → **Family Saga** (weaker fit — the
book spans one household, not generations). Ultramarine keeps Historical
Fiction as its first node unchanged.

⚑ OWNER — this changes a shipped packet (`vetting/ultramarine.md` §6, landed
in PR #98). Packet NOT edited this slice; the swap is applied to the packet
(and this map's ownership row) only on owner approval, naturally bundled
with the pending ⚑ OWNER title pick from the same packet.

### C2 — "widow" keyword stem: Weigh House vs Ultramarine (watched adjacency, KEEP BOTH)

- The Weigh House: `widow investigates husband's death` — **crime buyer
  intent** (a reader searching this wants a mystery/procedural).
- Ultramarine: `widow grief literary fiction` — **literary buyer intent**
  (a reader searching this wants interior grief fiction).

The shared stem is superficial; the full phrases target disjoint intents and
would not surface in each other's result pages. **Resolution: KEEP BOTH.**
Recorded as a **watched adjacency**, not a dispute — revisit only if live
search results ever show the two listings landing on the same results page.
No packet change; no owner action.

### C3 — Netherlands/Dutch cluster: genre split as the ownership rule

Both Dutch-set titles draw on Netherlands phrases. The split that holds
today, recorded as the standing rule:

- **The Weigh House owns modern-Netherlands crime phrases** (`Amsterdam
  crime novel`, `Dutch police procedural`, `canal murder Netherlands`).
- **Ultramarine owns Golden-Age historical phrases** (`Dutch Golden Age
  novel`, `Delft 1654 historical fiction`, `Vermeer era Netherlands story`).
- **The Paper Orange owns WWII-occupation phrases** (`Hunger Winter novel`,
  `Amsterdam occupation 1944 story`, `Dutch resistance historical novel`) —
  the THIRD Netherlands era-register, ownership rows claimed at its
  graduation (2026-07-13; reserved name-level in §3 since the concept
  wave).
- **The Sweetwater Sea owns interwar Zuiderzee-closure phrases**
  (`Zuiderzee novel`, `Afsluitdijk historical fiction`, `Dutch fishing
  village story`, 1927–1932) — the FOURTH Netherlands era-register,
  claimed at its manuscript-backed vetting (2026-07-14, negotiated here
  per this rule's own procedure; disjointness from the WWII register
  pre-checked in the title's DECISIONS.md: no occupation, war, Amsterdam,
  or 1940s stems).
- **The Wire Garden owns WWI neutral-border / Dodendraad phrases**
  (`Dodendraad novel`, `Wire of Death WWI story`, `electric fence Great
  War novella`, 1915–1918) — the FIFTH Netherlands era-register, claimed
  at its manuscript-backed vetting (2026-07-14, negotiated here per this
  rule's own procedure; disjointness pre-checked in the title's
  DECISIONS.md by era AND valence: neutrality/witness at a watched
  border vs Paper Orange's occupation/survival under it — different war,
  different decade, different search phrases by construction).
- **The Salt Bell owns postwar 1953-flood / Zeeland-Watersnood phrases**
  (`1953 North Sea flood novel`, `Zeeland flood historical fiction`,
  `Watersnoodramp novel`, `Delta Works historical novel`, 1953) — the
  SIXTH Netherlands era-register, claimed at its manuscript-backed vetting
  (2026-07-16, negotiated here per this rule's own procedure; disjointness
  pre-checked in the title's DECISIONS.md: a 1953 coastal-disaster novel
  shares no occupation, war, Golden-Age, or interwar-engineering stems).
  Nearest in-catalog adjacency is The Sweetwater Sea (both Dutch
  water-and-a-drowned-trade novellas) — held disjoint by decade
  (1953 vs 1927–32), event (flood disaster vs slow enclosure), and trade
  (oyster culture vs anchovy salting); the Salt Bell's oyster/village
  phrasing is deliberately steered clear of Sweetwater's fishing-village
  rows.

**Ownership rule:** Netherlands-flavored phrases are allocated by GENRE ERA
— contemporary-crime register → Weigh House; 17th-century-historical
register → Ultramarine; WWII-occupation register → The Paper Orange (EN;
its NL edition De papieren sinaasappel holds the same register in the C4
Dutch namespace); interwar Zuiderzee-closure register → The Sweetwater Sea;
WWI neutral-border/Dodendraad register → The Wire Garden; postwar
1953-flood/Zeeland-Watersnood register → The Salt Bell.
Any future Dutch-set title must pick phrases outside all
six registers or negotiate a row here first. No conflict today; rule
recorded to prevent one.

### C4 — Dutch-LANGUAGE editions: separate keyword namespace, shared browse nodes (standing rule)

The catalog's first two NL editions (*Het trage woord*, PR #126; *De
papieren sinaasappel*, PR #130) set the rule for every translated edition
that follows:

- **Dutch-language keywords are a separate namespace.** An NL listing's
  keywords are Dutch phrases typed by Dutch-language buyers; they cannot
  cannibalize the EN rows (different query language), so an NL edition
  never "re-claims" its EN title's phrases. But NL phrases CAN cannibalize
  each other — so they get ownership rows in §1 like every other phrase,
  tagged `(NL — C4 namespace)`.
- **Same-title editions share browse nodes.** KDP browse nodes are
  storefront-global; the language metadata, not the node, splits the
  audience. An NL edition uses its EN title's nodes and adds no duplicate
  category row (see the §1 edition-sharing note). Where the EN packet is
  still concept-stage, the manuscript-backed NL packet claims the nodes
  first and the EN edition shares them at graduation — this fired for The
  Paper Orange on 2026-07-13 (EN graduation; the two WWII nodes in §1 now
  carry both editions).
- **C3 extends into Dutch:** the era-register split governs the Dutch
  namespace too. Future NL editions of The Weigh House own
  modern-crime-register Dutch phrases; of Ultramarine, Golden-Age-register
  Dutch phrases; De papieren sinaasappel holds the WWII/Hongerwinter
  register (`literaire roman Hongerwinter`, `bezetting 1944 roman`, …).
- **Register etiquette recorded** (from the packet §6 notes): the word
  "Oorlogswinter" is never drafted as a keyword — it is Jan Terlouw's
  famous title, and squatting it would be title-adjacent keyword piracy;
  the shared "Hongerwinter" STEM is split by intent — our phrases say
  "literaire roman" to keep clear of the YA (Currie) and nonfiction
  (De Zwarte/Barnouw) shelves that legitimately share the stem.

## 3. Name-level reservations — unvetted titles (niche only, NO keyword drafting)

Reservations block other catalog titles from squatting a niche; actual
phrases are drafted only by that title's own vetting packet (CHECKLIST §6),
checked against this map at that time.

| Title (plan §7 name) | Reserved niche (name level only) | Notes |
|---|---|---|
| Lull | Middle-grade portal-fantasy trilogy — dream/mirror worlds, cliff-ended adventure (Percy-Jackson register); COMPLETE, Books 1–3 | Bare word unsearchable; a genre-signalling MG-fantasy subtitle is planned (plan §7). **Re-scoped 2026-07-20** from a stale *"Quiet/literary novella — stillness, small-town hush"* label that mismatched the actual MG content (flagged in the Bk2/Bk3 `KDP-METADATA.md` §3 reconciliation notes). Actual per-title keyword drafting remains an owner/vetting step (§1). |
| The Last Good Frequency | Post-collapse / analog-nostalgia radio DRAMA — **not** first-contact/alien-signal | **Must NOT reuse The Slow Word's radio/signal/first-contact phrases** — Slow Word owns `radio telescope alien signal story` and `first contact novella`. Reserve the human/apocalyptic radio angle instead (e.g. last-broadcast, ham-radio survival register). |
| The Undertow | Coastal/psychological suspense | Very strong title collision (plan §7) — rename/subtitle first; niche reserved regardless of final name. |
| Hollowtide | Seasonal/folk dark fantasy | Strong collision with an active fantasy series (plan §7); genre-signalling subtitle planned. |
| The Lantern Door | Kids bedtime / magical-door picture book | Kids cluster rule: Painted Stones owns picture-book-mystery + making-friends phrases; Lantern Door reserves the bedtime/door niche. |
| Tummel | Scottish river / journey fiction (tier pending owner illustration call) | One letter from *Tumble* (autocorrect drift, plan §7). |
| Dormouse / *"Pippa and the Tear in the Night"* | Kids night-comfort / fears-at-bedtime niche | Publish under the alt title (plan §7). Distinct from Lantern Door's bedtime/door: comfort-from-fear vs door-adventure. |
| Comet Biscuit (Book 1) | Kids space-adventure series niche | Kids cluster rule: space-adventure belongs to Comet Biscuit + Star Pirates, NOT to Painted Stones' mystery/friendship phrases. Series tag per cover (plan §7). |
| Comet Biscuit (Book 2) | Kids space-adventure series niche (shared with Book 1) | Series shares the niche; per-book keywords differentiate at vetting time. |
| Comet Biscuit (Book 3) | Kids space-adventure series niche (shared with Book 1) | Same as Book 2. |
| Bram the Yak Cannot Whisper | Kids animal-humor / loud-animal read-aloud niche | Best-differentiated title in the catalog (plan §7: collision None). |
| Star Pirates | Kids/YA space-pirate adventure niche | Shares the space shelf with Comet Biscuit — pirate-flavored phrases vs Comet Biscuit's cozy-space; split finalized when the second of the two is vetted. Avoid alt title *The Wrong Way Down* (plan §7). |
| ~~The Paper Orange~~ — **GRADUATED 2026-07-13** ([packet](vetting/the-paper-orange.md)) | ~~Adult WWII-occupation Netherlands literary-historical — Hunger Winter register~~ | **Reservation retired — the map's first §3→§1 graduation.** The manuscript landed (PR #122, measured 15,811 words) and the packet graduated 2026-07-13: its 7 EN keywords are now full §1 ownership rows and the EN edition shares the NL edition's two WWII browse nodes per C4. The WWII-occupation era-register is now recorded as C3's third register (owned by The Paper Orange), so nothing niche-blocking is lost by retiring this row. |
| The Night Kiln (concept, [packet](vetting/the-night-kiln.md)) | Adult cozy fantasy — low-stakes magical-craft comfort read | The catalog's first adult fantasy shelf; deliberately the OPPOSITE register from Hollowtide's reserved YA seasonal/folk DARK fantasy (comfort vs dread). Kiln→kill autocorrect drift noted in packet §1. Concept-stage; ownership rows at graduation — its NL edition *De Nachtoven* ([packet](vetting/de-nachtoven.md), 2026-07-14) claimed the browse nodes + NL C4 keyword rows in §1 first per C4. |
| The Morning Door (The Night Kiln, Book 2; [manuscript](../../candidates/adult-novels/the-night-kiln/en/the-morning-door.md)) | Adult cozy fantasy — Night Kiln series register (memory-craft comfort read, Book 2) | Shares The Night Kiln's reserved niche above (series shares the niche; per-book keywords differentiate at vetting time, per the Comet Biscuit series rule). "Door" stem is NOT Lantern Door's kids bedtime/magical-door niche — adult shelf, disjoint intent. Manuscript-backed; ownership rows at graduation — its NL edition *De Morgendeur* ([packet](vetting/de-morgendeur.md), 2026-07-14) claimed 7 new NL C4 keyword rows in §1 and SHARES De Nachtoven's two browse nodes per the series rule (per-book keywords differentiate: none of Book One's seven NL phrases re-claimed). |
| The Harvest Rows (The Night Kiln, Book 3; [manuscript](../../candidates/adult-novels/the-night-kiln/en/the-harvest-rows.md)) | Adult cozy fantasy — Night Kiln series register (memory-craft comfort read, Book 3) | Shares The Night Kiln's reserved niche above (series shares the niche; per-book keywords differentiate at vetting time, per the Comet Biscuit series rule). "Harvest" stem sits on the adult cozy-fantasy shelf only — no contact with the kids cluster or the C3 registers. Manuscript-backed; ownership rows at graduation — its NL edition *De Oogstslag* ([packet](vetting/de-oogstslag.md), 2026-07-14) claimed 7 new NL C4 keyword rows in §1 and SHARES De Nachtoven's two browse nodes per the series rule (per-book keywords differentiate: none of Book One's or Book Two's fourteen NL phrases re-claimed). |
| The Pepper Ledger (concept, [packet](vetting/the-pepper-ledger.md)) | YA age-of-sail / spice-route maritime adventure (17th-century era) | Reuses Ultramarine's 17th-century research base in a different lane per the C3 rule: drafts ZERO Netherlands-branded phrases (no Dutch/Golden Age/Delft/Amsterdam stems) — maritime-adventure register only; Ultramarine's Golden-Age-historical register untouched. Concept-stage; ownership rows at graduation. |
| The Marginalia Society (concept, [packet](vetting/the-marginalia-society.md)) | YA dark academia / boarding-school secret-society mystery | Teen & YA mystery shelf — distinct from Painted Stones' Children's Mysteries & Detectives node, and non-supernatural (no overlap with Hollowtide's folk-fantasy dark). Concept-stage; ownership rows at graduation. |
| The Windmill Mouse (concept, [packet](vetting/the-windmill-mouse.md)) | Kids windmill / miller-mouse little-helper picture book (daytime competence register) | Netherlands-flavored at the KIDS register only — outside both C3 adult registers. NO "old Amsterdam" phrasing (1965 song adjacency, packet §2 differentiator) and NO "bedtime" phrasing (Lantern Door/Pippa own the night shelf). Concept-stage; ownership rows at graduation. |
| The Puddle Museum (concept, [packet](vetting/the-puddle-museum.md)) | Kids rainy-day / weather-wonder / imaginative-play picture book | Daytime-wonder shelf, empty in the catalog; distinct from Painted Stones' mystery/friendship phrases and Pippa's night-comfort niche. Puddle→poodle autocorrect drift noted in packet §1. Concept-stage; ownership rows at graduation. |
| The Marmalade Post (concept, [packet](vetting/the-marmalade-post.md)) | Adult contemporary COZY mystery — English-village amateur-sleuth register, series-native (one misdelivered parcel per book) | The catalog's first cozy shelf. Distinct by register from The Weigh House's owned contemporary-crime PROCEDURAL rows (cozy vs procedural, England vs NL — no C3 contact). No widow stems (C2 untouched). Marmalade→marmelade misspelling drift noted in packet §1. Concept-stage; ownership rows at graduation — its NL edition *De Marmeladepost* ([packet](vetting/de-marmeladepost.md), 2026-07-14) claimed the browse nodes + NL C4 keyword rows in §1 first per C4. |
| The Glass Rectory (concept, [packet](vetting/the-glass-rectory.md)) | Adult gothic / classic ghost-story novella — Victorian supernatural, inland | Distinct from BOTH reserved dark niches: Hollowtide (seasonal folk DARK FANTASY — folklore-magic stems stay Hollowtide's) and The Undertow (COASTAL psychological suspense — no coastal stems drafted here). Rectory→directory autocorrect drift noted in packet §1. Concept-stage; ownership rows at graduation — its NL edition *De glazen pastorie* ([packet](vetting/de-glazen-pastorie.md), 2026-07-14) claimed the browse nodes + NL C4 keyword rows in §1 first per C4. |
| The Seed Catalogue Courtship (concept, [packet](vetting/the-seed-catalogue-courtship.md)) | Adult epistolary romance — clean & wholesome, later-in-life, novel-in-letters register | First Romance-storefront title in the catalog; no owned register adjacent. "Letters" stem unclaimed catalog-wide. Catalogue/Catalog regional-spelling fork noted in packet §1 (UK spelling kept; US spelling absorbed as keyword). No Netherlands stems (C3 untouched). Concept-stage; ownership rows at graduation — its NL edition *Liefde in de kantlijn* ([packet](vetting/liefde-in-de-kantlijn.md), 2026-07-14) claimed the browse nodes + NL C4 keyword rows in §1 first per C4. |
| The Salvage Orchard (concept, [packet](vetting/the-salvage-orchard.md)) | Adult solarpunk SF novella — hopeful climate-repair register, near-future Earthbound | Second SF shelf, disjoint from The Slow Word's owned register by construction: NO first-contact / radio / signal / telescope / deep-time / generational-legacy stems (Slow Word owns those rows in §1) — repair/community/climate stems only. Also must not collide with The Last Good Frequency's reserved post-collapse RADIO niche (no radio/broadcast stems). Salvage→savage drift noted in packet §1. Concept-stage; ownership rows at graduation — its NL edition *De geborgen boomgaard* ([packet](vetting/de-geborgen-boomgaard.md), 2026-07-14) claimed the browse nodes + NL C4 keyword rows in §1 first per C4. |
| The Halfway Ferry (concept, [packet](vetting/the-halfway-ferry.md)) | MIDDLE-GRADE (ages 8–12) portal-fantasy series — river-ferry-between-worlds niche, one crossing per book | The catalog's first middle-grade title (age-band gap between the picture-book cluster and the YA pair). Kids-cluster rules respected: no mystery/friendship stems (Painted Stones), no space stems (Comet Biscuit/Star Pirates), no bedtime/night stems (Lantern Door/Pippa). Renamed same-day from *The Thistlewick Ferry* (occupied stem — packet §2). Ferry→fairy drift noted in packet §1. Concept-stage; ownership rows at graduation. |
| The Twelfth Cake (concept, [packet](vetting/the-twelfth-cake.md)) | Adult seasonal/holiday historical novella — Twelfth Night (Jan 5) Victorian-London hearth register | First seasonal/holiday shelf. Opposite pole from Hollowtide's reserved seasonal folk-DARK niche (warm vs dread — no folk-fantasy stems). Victorian era sub-register only: parent Historical Fiction node is Ultramarine's (§1); the packet follows the Paper Orange sub-node precedent. No crime stems (Marmalade Post holds this wave's cozy-mystery register). Collision Moderate (common-noun search crowding, packet §2) — subtitle mandatory. Concept-stage; ownership rows at graduation — its NL edition *De Driekoningentaart* ([packet](vetting/de-driekoningentaart.md), 2026-07-14) claimed the browse nodes + NL C4 keyword rows in §1 first per C4. |

---

*Consult at CHECKLIST §6 time; add your rows in the same PR as your packet;
resolve any collision here before the §7 owner gate. First claim merged to
main wins.*
