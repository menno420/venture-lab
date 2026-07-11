# Bababoefoe — Make-It-Real Plan (money-protocol, phased)

> **Status:** `plan`
>
> **Money protocol (binding).** Agents never spend, never create accounts, never
> contact suppliers, never publish. This plan produces owner-gated steps with
> **conservative** earnings expectations and payback estimates. Expect bad results;
> never overstate. Every number is either **CITED** (URL) or explicitly marked
> **NOT VERIFIED — never invented**. Physical products sit OUTSIDE the lane's
> proven one-click-digital path — treat every revenue line as unproven.

Each gated step is a six-field **OWNER-ACTION**:
**WHAT / WHERE / HOW / WHY / UNBLOCKS / VERIFIED-WHEN.**

---

## Phase 0 — Zero cost, agent-done (stories + site + QR registry live)

Already built in-repo: `BRAND-BIBLE.md`, 5 stories, a working stdlib static site
(`site/build.py` → `site/dist/`), and the `editions.json` registry that is the
source of truth for printed QR tags. The only thing between "built" and "live" is a
single GitHub Pages toggle.

**QR path taken:** neither `segno` nor `qrcode` is installed in this environment,
and per the no-spend/no-install rule nothing was added. `build.py` therefore emits
`site/dist/qr-urls.txt` (slug → full Pages URL) as the printable source of truth.
Rendering actual QR images is a **zero-cost owner/local step**: `pip install segno`
(pure-Python, MIT-licensed — NOT a repo dependency) locally, then re-run
`python3 build.py`; the script auto-detects segno/qrcode and writes an SVG QR per
edition into `dist/qr/`, referenced automatically on each edition page. No code
change needed.

### OWNER-ACTION 0.1 — Enable GitHub Pages
- **WHAT:** turn on GitHub Pages for the `venture-lab` repo so the built site is publicly reachable.
- **WHERE:** github.com/menno420/venture-lab → Settings → Pages.
- **HOW:** under "Build and deployment", set Source = "Deploy from a branch", Branch = `main`, folder = `/ (root)`, Save. (One click + Save. No build action, no spend.)
- **WHY:** publishes the story pages the QR tags point at; without it every QR is a dead link.
- **UNBLOCKS:** the entire QR-tag concept, and Phase 1/2 marketing (a real URL to show).
- **VERIFIED-WHEN:** `https://menno420.github.io/venture-lab/candidates/bababoefoe/site/dist/index.html` returns 200 and each edition page in `qr-urls.txt` loads its story.

> Note: the base URL in `editions.json` assumes Pages serves the repo root. If the
> owner instead configures a `/docs` or Actions-based Pages source, update
> `base_url` + the per-edition `url` in `editions.json` and re-run `build.py`
> BEFORE any tag is printed — the slug/URL must be frozen before print.

**Phase 0 conservative expectation:** $0 revenue. This is content + infrastructure,
not a sales channel. Its only job is to make the QR promise real and give later
phases something to point at.

---

## Phase 1 — No-upfront-cost physical (crowdfunded plush + print-on-demand)

Two no-inventory routes. Both are owner-gated; agents build the assets, owner runs
the accounts.

### Route A — Crowdfunded plush (Makeship-style)
How the model works (CITED):
- Fans back a **petition** with small **$2 pledges**; once it hits a minimum
  supporter count, the platform builds a prototype. [makeship.com/how-it-works]
- A funded **21-day campaign** then takes pre-orders; the model cited needs roughly
  your **200 biggest fans to pre-order**, and production only begins if the
  **minimum order quantity is reached** — otherwise all backers are refunded.
  [makeship.com/how-it-works]
- The process is **free to the creator**; you **earn commissions once funded**, and
  production takes **2–4 months** shipping direct to backers.
  [makeship.com/how-it-works], [makeship.com/launch-campaign]

> **NOT VERIFIED — never invented:** the exact creator revenue split / per-unit
> commission and the precise minimum-unit threshold are not published as a fixed
> public number; Makeship states them per-campaign after application. Do NOT quote a
> split until the owner sees it in the dashboard.

**Reality check / kill signal:** the whole route depends on an existing fanbase —
"200 biggest fans" assumes you already have fans. Bababoefoe has **no audience
yet**, so the honest conservative expectation for a cold launch is **campaign does
not reach threshold → $0, all backers refunded.** The campaign's vote/pre-order
count IS the validation signal (see kill-rule).

### OWNER-ACTION 1.1 — Apply to a crowdfunded-plush platform (only after an audience exists)
- **WHAT:** submit Bababoefoe (one hero edition, e.g. Pirate) to a Makeship-style plush campaign platform.
- **WHERE:** makeship.com/launch-campaign (or an equivalent crowdfunded-plush platform).
- **HOW:** create the free creator account, upload the concept art + Pirate story, set the campaign; review the platform's per-campaign minimum-unit threshold and commission BEFORE accepting.
- **WHY:** it is the only physical route with **zero upfront cost and zero inventory risk** — production only runs if pre-orders clear the minimum.
- **UNBLOCKS:** first real demand test + first physical revenue, with no owner cash at risk.
- **VERIFIED-WHEN:** campaign page is live with a real pre-order count; funded = threshold reached before day 21.

### Route B — Print-on-demand accessories (keychains, pillows)
No-inventory printed goods carrying the artwork (2-D art, not plush). CITED costs:
- **Keychains:** production ~**$1–$3**, typical retail **$8–$15**, ~**50–70% margin
  before platform fees**. [e-comprofits.com/print-on-demand-profit-margins-by-category]
- **Pillows:** POD base cost ~**$24.92 (Printify) / $26.94 (Printful)** per unit;
  retail must clear that + fees to profit. [inkandpxl.com POD 2026 Printify vs Printful guide]
- General POD guidance: aim **15–30% margin over production cost**; base cost is
  ~**55–70% of true landed cost**. [printful.com/blog/what-is-a-good-profit-margin-for-print-on-demand]

### OWNER-ACTION 1.2 — Stand up a print-on-demand storefront for accessories
- **WHAT:** list Bababoefoe keychains + pillows as print-on-demand (no inventory).
- **WHERE:** a POD provider (Printful/Printify) connected to an Etsy or Shopify store.
- **HOW:** upload edition artwork, place it on the keychain + pillow blanks, set retail at keychain $10–14 / pillow ~$34–39 to hold margin, publish the listings.
- **WHY:** zero inventory, tests whether the ART sells even before plush manufacturing.
- **UNBLOCKS:** a live product page + a low-risk revenue signal that de-risks Phase 2.
- **VERIFIED-WHEN:** listings are live at 200-OK URLs and a test order routes to the POD provider.

**Phase 1 conservative revenue expectation:** cold launch, no audience → realistic
**$0–$150 first 90 days** across both routes; a POD keychain at $12 on ~$2 cost nets
~$10 before fees, so even 10 sales ≈ $100 gross / well under that net. **Payback:**
$0 cash out (no upfront), so payback is on OWNER TIME, not money — do not overstate.

---

## Phase 2 — Owner-funded batch (custom plush manufacturing)

Only after Phase 1 shows a real demand signal. This phase requires **owner cash** and
carries real inventory risk. Agents produce the plan only.

Custom plush manufacturing basics (CITED):
- **MOQ:** large Chinese export factories typically quote **1,000–5,000 pcs/SKU**;
  smaller domestic/Vietnamese operations may run **100–300 pcs**.
  [kenwangtoys.com/plush-toy-manufacturing-moq-explained]
- **Indicative unit cost:** a standard 20–25 cm custom plush at **100–300 pcs runs
  ~$7–$12/unit**; at **500 pcs (10-inch) ~$5–$7/unit excluding delivery**.
  [plushtoys-factory.com/custom-plush-toy-manufacturing-cost], [factoryplush.com/custom-plush-toy-costs-manufacturing-guide]
- **Pre-production fees:** budget **$400–$1,400** (sampling, pattern, embroidery
  setup) before the first production unit ships.
  [plushtoys-factory.com/custom-plush-toy-manufacturing-cost]

> The task's assumed **~300–500 unit** MOQ is consistent with the smaller-factory
> end of these CITED ranges. The **magnetic-hands and hidden-pocket features add
> tooling/assembly cost NOT captured in the standard per-unit figures above —
> NOT VERIFIED; never invent a surcharge.** Get it quoted.

### Landed-cost + margin table (illustrative; unit cost CITED, freight/fees NOT VERIFIED)
Assumes $7/unit factory cost (mid of the 500-pc range) + an assumed $2/unit landed
freight/duty allowance (**NOT VERIFIED — placeholder, owner must quote**) = ~$9
landed. Retail scenarios:

| Retail | Landed cost | Gross/unit | Gross margin | Notes |
|---|---|---|---|---|
| $12 | ~$9 | ~$3 | ~25% | thin; keychain-tier pricing, weak after platform fees |
| $18 | ~$9 | ~$9 | ~50% | mid; needs the story/collectible angle to justify |
| $25 | ~$9 | ~$16 | ~64% | collector edition; requires brand pull to sustain |

At 500 units × $9 landed ≈ **$4,500 owner cash at risk** before a single sale (plus
$400–$1,400 pre-production). Sell-through is the risk, not margin.

### OWNER-ACTION 2.1 — Commission a plush sampling quote (NO commitment)
- **WHAT:** request a sample + quote for one Bababoefoe edition, magnetic-hands feature flagged for compliance review.
- **WHERE:** a custom-plush factory (owner-selected; agents do not contact suppliers).
- **HOW:** send concept art + size spec + the safety questions (below); ask for MOQ, per-unit at 300/500/1000, pre-production fees, and whether they can supply CE/EN71 + ASTM F963 test reports.
- **WHY:** replaces every NOT-VERIFIED number here with real quotes before any cash commits.
- **UNBLOCKS:** a real landed-cost model + the compliance answer that gates the magnet feature.
- **VERIFIED-WHEN:** written quote in hand with MOQ, tiered unit cost, pre-pro fees, and named safety-test capability.

### OWNER-ACTION 2.2 — Open the retail storefront for the batch
- **WHAT:** list the manufactured plush for direct sale.
- **WHERE:** Etsy (collectible/handmade discovery) and/or a Shopify store.
- **HOW:** publish edition listings at $18–25 using the story pages + QR concept as the differentiator; link each listing to its Pages story.
- **WHY:** the sales channel for owner-funded inventory.
- **UNBLOCKS:** first-dollar on the physical product.
- **VERIFIED-WHEN:** live listings at 200-OK URLs with real inventory attached.

**Phase 2 conservative expectation:** with 500 units and no proven audience, assume
**slow sell-through** — plan for months, not weeks, and for the real possibility of
**unsold inventory (loss of the ~$4,500+ outlay)**. Payback only after roughly
**300+ units at $18 (~$9 gross each ≈ $2,700)** begins to clear the landed+pre-pro
outlay — i.e. **more than half the batch must sell just to break even.** Do NOT
enter Phase 2 without a Phase 1 demand signal.

---

## SAFETY / COMPLIANCE (owner homework — NOT agent-verifiable)

Children's products are regulated; this is a professional/legal matter, not
something an agent can verify. Flags (CITED):
- **US:** toys for children ≤12 must meet **ASTM F963**, a mandatory standard under
  the **CPSIA**, with third-party testing + certification. [cpsc.gov Toy Safety Business Guidance]
- **Small parts:** toys for children under 3 are governed by **16 CFR Part 1501**
  (choking/small-parts). [cpsc.gov]
- **EU:** the **EN71** series (EN71-1 mechanical/physical) + **CE** marking apply;
  ASTM F963 has been revised toward EN71-1 harmonization. [astm.org F963 press release]
- **MAGNETS (the magnetic-hands feature — flag explicitly):** ASTM F963 defines a
  **hazardous magnet** as one with **flux index > 50 kG²·mm² that also fits within
  the small-parts cylinder**; loose/separable magnets that fit the cylinder must
  stay under that flux limit. Magnet ingestion is a specifically regulated,
  incident-driven hazard. [astm.org], [cpsc.gov Magnets Business Guidance], [federalregister.gov Safety Standard for Magnets 2022]

**Compliance decision the owner must make (NOT agent-verifiable):**
- **Option A — embedded sewn-in magnets:** magnets fully enclosed/secured so they
  cannot detach under the use-and-abuse tests; requires lab testing + certification
  to prove the magnets stay put. Higher cost, keeps the "boefoe-chain" feature.
- **Option B — magnet-free editions:** drop magnets from kid-targeted plush
  (especially under-3 and keychains); keep hand-holding as a story-only feature or a
  hook-and-loop / snap alternative. Lowest regulatory risk.

> Stated plainly: **the magnet feature is a compliance decision requiring a
> qualified toy-safety professional and lab testing. Agents cannot verify it.**
> Resolve this BEFORE OWNER-ACTION 2.1 commits to any magnet-bearing design.

---

## Kill-rule fields (binding)

- **Validation signal:** Phase 1 is the test. Signal within 60 days / owner-click
  steps = ANY of: (a) a crowdfunded-plush campaign reaches ≥25% of its minimum
  pre-order threshold, (b) ≥3 POD accessory sales, (c) any single physical sale.
  No signal by the effort cap = ledgered negative; do NOT advance to Phase 2.
- **First-ten-customers path (⚑ = owner-gated):** (1) crowdfunded-plush campaign
  page ⚑; (2) Etsy collectible listing ⚑; (3) POD keychain/pillow listings ⚑;
  (4) the free story-site itself as an organic discovery/QR surface (Phase 0);
  (5) owner's own social/family network for the first backers ⚑. Honest note: with
  no existing audience, channels (1)–(3) start cold.
- **Max agent-effort budget (this slice):** **150k tokens incl. CI.** Over budget
  without a validation signal = ledgered negative.
- **Conservative revenue expectation:** Phase 0 $0. Phase 1 $0–$150 / 90 days cold.
  Phase 2 requires ~$4,500+ owner cash at risk with real chance of unsold inventory.
- **Payback:** Phase 0/1 cost is owner TIME (no cash). Phase 2 breaks even only
  after ~half the batch sells — unproven; do not enter without a Phase 1 signal.

---

## Sources
- https://www.makeship.com/how-it-works
- https://www.makeship.com/launch-campaign
- https://www.e-comprofits.com/print-on-demand-profit-margins-by-category/
- https://inkandpxl.com/blogs/feature/print-on-demand-2026-printify-vs-printful-the-definitive-profit-guide
- https://www.printful.com/blog/what-is-a-good-profit-margin-for-print-on-demand
- https://kenwangtoys.com/plush-toy-manufacturing-moq-explained/
- https://plushtoys-factory.com/custom-plush-toy-manufacturing-cost/
- https://factoryplush.com/custom-plush-toy-costs-manufacturing-guide/
- https://www.cpsc.gov/Business--Manufacturing/Business-Education/Toy-Safety
- https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Magnets
- https://www.astm.org/news/press-releases/astm-toy-safety-standard-f963-08-issued-updates-address-magnet-ingestion-jaw
- https://www.federalregister.gov/documents/2022/01/10/2021-27826/safety-standard-for-magnets
