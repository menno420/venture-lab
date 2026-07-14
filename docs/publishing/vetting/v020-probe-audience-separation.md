# Title Vetting — V020 Probe: audience-separation s (Paper Orange EN ↔ NL)

> **Status:** `plan`
>
> **PRE-REGISTERED MEASUREMENT PROTOCOL** — not a title packet: this file
> pre-registers the two-version live probe that VERDICT 020's NULL named as
> the lane's cheapest next step, in packet §7 form so its owner clicks ride
> the derived queue like every other gate. Protocol frozen at the commit
> that lands it and BEFORE any publish material was prepared; any edit to
> §§3–5 before the §8 data row lands voids the pre-registration and must be
> recorded in §8 as a re-registration. Everything marked **⚑ OWNER-GATE**
> is an owner click, never automated — the seat publishes NOTHING.

**Probe:** two-version audience-separation measurement · **Consumes:**
VERDICT 020 (NULL), idea-engine `control/outbox.md@2808b16` · **Ordered
by:** ORDER 011 item 5 (`control/inbox.md@991aff1`) · **Date
pre-registered:** 2026-07-14

## 1. What this probe is (source-canonical)

VERDICT 020 (sim-lab PR #64; served via idea-engine
`control/outbox.md@2808b16`, fetched at source and read in full
2026-07-14) ruled the book breadth-vs-versioning question **NULL** — the
pre-registered honest straddle:

> "the two publication modes give OPPOSITE allocation defaults — Mode P
> pick-best K*=1 in 85.19% of cells, median ΔR +0.0000; Mode A publish-all
> K*≥2 in 88.89%, median ΔR +0.4062"

Its binding NULL consequence: *"neither 'always version' nor 'always
breadth' may be cited as settled"*; the citable finding is the CONDITIONAL
rule — route by publish mode, and inside publish-all the gate is **audience
separation s**: *"publish-all with any real audience separation (different
angles/audiences/lengths listed separately, s > 0) → version-heavy
allocation is robustly right (grid-median K* = 6)"*. The verdict's own
LIMITS line names the unlock: *"no live sales data anywhere — s and f are
model dials, not measurements (the live probe is the named unlock)"*, and
its recommendation names the probe verbatim:

> "the lane's cheapest LIVE probe, named: publish two versions of ONE
> existing-research book with disjoint audience keywords and record whether
> their draws actually separate — measuring s in the wild for one
> night-slice's budget"

In the sim, s interpolates the publish-all return between full
cannibalization and full additivity: `R = (1−s)·max_i r_i + s·Σ_i r_i`
(s = 0: all K versions share ONE audience and only the best draw counts;
s = 1: each version taps its own audience and draws ADD). This probe puts
an observable number against that dial for one real version pair.

## 2. The two versions compared (and why this pair)

**ONE work, two editions, both already click-ready on merged main:**

| Version | Manuscript | Packet | Keywords |
|---|---|---|---|
| A — *The Paper Orange* (EN, "A Novel of the Hunger Winter") | `candidates/adult-novels/the-paper-orange/en/the-paper-orange.md` (15,811 w, PR #122) | [`the-paper-orange.md`](the-paper-orange.md) — GRADUATED 2026-07-13 (PR #146) | 7 EN rows owned in [`keyword-map.md`](../keyword-map.md) §1 |
| B — *De papieren sinaasappel* (NL, "Een roman over de Hongerwinter") | `candidates/adult-novels/the-paper-orange/versions/nl/de-papieren-sinaasappel.md` (16,203 w, PR #130) | [`de-papieren-sinaasappel.md`](de-papieren-sinaasappel.md) (PR #131) | 7 NL rows owned in the map §1 (C4 namespace) |

Why this pair, honestly:

- **It is the verdict's own shape:** two versions of ONE existing-research
  book (the Hongerwinter research underlies both editions) with **disjoint
  audience keywords** — disjointness here is structural, not curated: the
  map's C4 standing rule gives Dutch-language editions a SEPARATE keyword
  namespace (7 EN rows vs 7 NL rows, zero shared phrases; shared browse
  nodes by design).
- **Zero new material needed:** both packets carry complete §7 publish
  sequences already in the derived queue. The probe adds a pairing
  constraint and a measurement step — it creates no new versions and no
  new listings beyond the two already queued.
- **Why not the four fresh NL editions (#175–#178):** they have no NL
  vetting packets yet (owed per `.sessions/2026-07-13-night-book-variants.md`),
  and their EN packets are un-graduated concept-stage — neither side is
  click-ready, and building 2 packets + 1 graduation would blow the
  night-slice budget. The Night Kiln series is additionally held by a
  concurrent session tonight. The large-print specs (#172) are production
  specs, not publishable artifacts.
- **The selection bias this creates is §6 caveat 1** — read it before
  citing any result.

## 3. The separation statistic s — exact definition and computation

**Measurement window W:** let T0 = the later of the two listings' go-live
dates (both recorded in §8). W = the 14 full UTC days T0+1 … T0+14
(the partial go-live day is excluded). Both listings MUST go live within
48 h of each other or the probe is VOID (§6 caveat 5).

**Draws per version.** For version i ∈ {A, B} over W:

    r_i = U_i + floor(KENP_i / KENPC_i)

- `U_i` = net units ordered (orders minus refunds/returns), all
  marketplaces, from the KDP Orders report;
- `KENP_i` = Kindle Edition Normalized Pages read over W (KDP KENP
  report); `KENPC_i` = the edition's total KENP count as shown on the KDP
  bookshelf — so the second term is whole KU read-equivalents, floored;
  0 if the edition is not in KDP Select.

**Primary statistic (draw balance):**

    s_hat = 2 · min(r_A, r_B) / (r_A + r_B)        ∈ [0, 1]

defined only when r_A + r_B ≥ N_min = 5. Worked example: r_A = 4,
r_B = 3 → s_hat = 2·3/7 = 0.857. Degenerate case: one version 0 draws →
s_hat = 0.

**Co-primary check (home-market attribution)** — because s_hat alone
confounds separation with audience-size imbalance (§6 caveat 4):

    h_B = (version-B draws on Amazon.nl) / r_B
    h_A = (version-A draws NOT on Amazon.nl) / r_A

each defined only when its r_i ≥ 1, computed from the per-marketplace
split of the same KDP reports.

**Relation to the sim's s — stated plainly:** the sim's s is defined
against a counterfactual (what ONE listing would have drawn) that is not
observable in the wild. s_hat is a pre-registered observable PROXY: two
same-size disjoint audiences → s_hat → 1; one shared audience picking a
winner → s_hat → 0. It is NOT an unbiased estimator of the model dial,
and no such estimator exists from this data.

## 4. Data the owner collects (post-publish — the measurement step)

At T0+15 (first day after the window closes), export and hand to the
seat, per edition (2 ASINs), per marketplace, covering exactly W:

1. Go-live timestamps + ASINs for both listings (recorded at publish
   time, §7 click C).
2. KDP Orders report: units ordered and refunds/returns.
3. KDP KENP report: KENP read; plus each edition's KENPC from the
   bookshelf.
4. Confirmation that **zero paid traffic** ran in W (no ads, no paid
   placement, either edition). Any paid traffic → probe VOID, recorded
   honestly in §8 (organic separation is the thing being measured).

That is the complete list — four items, one export session.

## 5. Decision rule (pre-registered)

Evaluated once on the §4 data, in this order:

1. **VALIDITY:** go-live gap > 48 h, or paid traffic in W → **VOID**
   (no s reported; §8 records why; V020's NULL stands untouched).
2. **r_A + r_B < 5 → INCONCLUSIVE.** The likely outcome at
   unknown-author base rates (§6 caveat 3) and a legitimate result: s
   stays unmeasured, V020's NULL and conditional rule stand unmodified,
   no allocation default changes. One pre-registered extension: re-run
   this rule once on W' = T0+1 … T0+28; if still < 5, final.
3. **SEPARATED (refutes s = 0 for this pair class):** s_hat ≥ 0.5 AND
   both h_A, h_B defined with min(h_A, h_B) ≥ 0.8. Consequence: V020's
   branch (i) is activated **for translation variants only** — publish-all
   with version-heavy allocation (grid-median K* = 6) becomes the lane's
   default for cross-language editions of existing-research titles.
   Nothing is claimed for same-language variants (§6 caveat 2).
4. **NOT SEPARATED (consistent with s ≈ 0):** s_hat < 0.2, OR (both h
   defined and min(h_A, h_B) < 0.5 — draws crossing markets means the
   audiences are NOT disjoint even if balanced). Consequence: branch (ii)
   new-titles-first remains the default even for translation variants;
   the "versions are cheap" clause stays necessary-but-not-sufficient.
5. **Anything else → PARTIAL:** report s_hat and (h_A, h_B) as measured
   point estimates in §8; no default changes; one extension to W' as in
   rule 2, then final whatever it says.

What confirms vs refutes "the null": V020's NULL itself is FINAL (a
pre-registered straddle, not a re-run request) — this probe cannot and
does not re-open it. The probe tests the s-dial hypothesis inside the
NULL's conditional rule: H0 "s = 0 in the wild for this pair" is refuted
by rule 3 and supported by rule 4; rules 1–2 and 5 leave the map exactly
where V020 left it.

## 6. Honest caveats — K, selection, power

1. **Selection FOR separation (K-style bias):** this pair was chosen
   because it is click-ready and the NL edition is the catalog's
   strongest native-market listing — i.e., selected where separation is
   MOST likely. A SEPARATED result therefore licenses the
   translation-variant class only; it is evidence about the easiest case,
   not about versioning generally.
2. **The easy axis is not the interesting axis:** cross-language is the
   maximal-disjointness corner of V020's s. The verdict's branch (i) also
   covers same-language variants ("different angles/audiences/lengths") —
   large-print editions, novella cuts — where cannibalization is the real
   risk. This probe does NOT measure those; the named follow-on is a
   same-language pair (e.g. a full edition vs its novella cut) once this
   protocol's verdict lands.
3. **Power, stated before the fact:** unknown-author organic base rate is
   ≈ 0 draws (both packets say so; the live SWTK's T+14 kill bar is ≥ 1
   sale). INCONCLUSIVE is the modal expected outcome. At the N_min = 5
   floor, s_hat carries huge sampling noise — the §5 thresholds are
   pre-registered decision heuristics to prevent post-hoc rationalization,
   NOT significance tests, and no p-value will be quoted.
4. **s_hat confounds separation with market size:** the NL ebook market is
   far smaller than EN; perfectly separated but unequal audiences depress
   s_hat toward 0. That is why SEPARATED requires the h attribution check
   AND why NOT SEPARATED cannot be declared on low s_hat alone unless
   draws also fail the balance floor (rule 4's two independent clauses).
5. **Simultaneity:** the 48 h co-launch condition exists because listing
   age drives KDP's own surfacing; staggered launches would measure
   recency, not audience.
6. **KU normalization is approximate:** floor(KENP/KENPC) undercounts
   partial reads; both editions are affected symmetrically, which is why
   the statistic survives it.
7. **No money claims:** draws are relative units. This probe allocates
   future writing effort, never forecasts earnings — V020's own Q-0259
   r.4 restatement carries over verbatim.
8. **n = 1 title.** One pair, one window. The output is a measured point
   and a class-level default toggle, not a law.

## 7. ⚑ OWNER-GATE — probe clicks (queued, never automated)

Seat output = this queued block; the seat performed **none** of it. The
two publish sequences themselves live in the two title packets and are
already queued — this block adds the probe's PAIRING constraint and the
measurement step. Running the probe = running both existing sequences
within the same 48 h, then one data export.

**OWNER-ACTION — Run the V020 audience-separation probe (two clicks + one
export)**
1. **Publish click A:** execute the full §7 sequence of
   [`the-paper-orange.md`](the-paper-orange.md) (EN edition, $4.99, KDP).
2. **Publish click B:** execute the full §7 sequence of
   [`de-papieren-sinaasappel.md`](de-papieren-sinaasappel.md) (NL
   edition, €4.99, KDP) — **within 48 h of click A** (probe VOID
   otherwise, §5 rule 1); this sequence starts with the NL packet's own
   native-speaker proofread gate.
3. **Record go-live:** note both go-live timestamps + ASINs (the seat
   writes them into §8 and arms a T0+15 KILL-CHECK ⏲ line here on the
   next session after the owner reports them).
4. **No ads in the window:** run zero paid traffic on either edition
   through T0+14 (§4 item 4).
5. **Measurement export at T0+15:** the four §4 items, one export
   session; hand to the seat.

- [ ] ⚑ **Owner:** publish click A — *The Paper Orange* (EN) per its
      packet §7 sequence.
- [ ] ⚑ **Owner:** publish click B — *De papieren sinaasappel* (NL) per
      its packet §7 sequence, within 48 h of click A (inherits that
      packet's blocking native-speaker proofread gate).
- [ ] ⚑ **Owner:** measurement export at T0+15 — the §4 list (orders,
      KENP/KENPC, per-marketplace splits, no-ads confirmation) for both
      ASINs, handed to the seat.
- [ ] Seat (post-data, no money moved): compute s_hat, h_A, h_B per §3;
      apply §5 mechanically; record the verdict + raw numbers in §8 and
      the consequence (if any) in the packets it touches.

## 8. Probe log (empty until data — nothing measured yet)

| Field | Value |
|---|---|
| Pre-registered | 2026-07-14, this file's landing commit (PR #179) |
| Go-live A (EN) | *not yet — owner click pending* |
| Go-live B (NL) | *not yet — owner click pending* |
| Window W | *not yet — defined by go-live* |
| r_A, r_B, s_hat, h_A, h_B | **not measured** |
| §5 verdict | **not measured** |

---

**Verdict: protocol pre-registered; probe queued up to the owner gate.**
The seat prepared the pairing + measurement design and both versions'
listing materials to the click-ready floor; it published nothing,
measured nothing, and claims nothing — every number above the §8 line is
a definition, and every number below it says "not measured".
