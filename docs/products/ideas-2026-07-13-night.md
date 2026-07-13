# Product ideation batch — 2026-07-13 night (7 concepts, rubric-scored)

> **Status:** `ideas`
>
> PRODUCTS-lane ideation slice under ORDER 011 item 1 (`control/inbox.md@991aff1`,
> the fm ORDER 045 relay): "packet + build cc-cost-lens, or run a fresh
> ideation batch (the #142 batch's 3 BUILDs are consumed)." Path taken:
> **cc-cost-lens was KILLED at its intake gate** (Kill Rule 0/3 — verdict +
> in-place negative-ledger entry in `candidates/cc-cost-lens/INTAKE.md`
> § "Verdict at gate: KILL (2026-07-13)"), so this is the fresh batch. Seven
> NEW concepts in the proven vein — kits / guides / templates, Gumroad
> delivery, $15–$29 — every one scored on the shipped kill-rule intake rubric
> (`candidates/kill-rule-intake-kit/pack/SCORING-RUBRIC.md`, fixed weights:
> Distribution 35 / Buildability 20 / Launch-effort 15 / Speed 15 / WTP 15).
> Verdicts: **1 BUILD · 2 PARK · 4 KILL.** Nothing here is built, published,
> or spent on; per Kill Rule 0 every BUILD still requires its own full
> `INTAKE.md` (kill-rule fields + budget) before any code or copy.

## How to read this

- **Bands** (rubric's own reading): below ~3.0 = do not build; 3.0–3.5 =
  borderline, tight budget only; above 3.5 = best available — still not a
  promise anyone buys (SWTK, the only LIVE product, has 0 organic sales as
  of 2026-07-13; every revenue expectation below is conservative-$0).
- **No duplicates:** each concept was checked against the shipped catalog
  (SWTK $29 live · GWTK $29 · Owner-Click Queue Kit $19 · Multi-Agent
  Control-Plane Pack $29 · membership-kit $49 · template-packs $19 PWYW ·
  field manual $39 · kill-rule kit $15 · false-green $15 · merge-wall
  cookbook $19 · Ship-It Bundle $59; sources: `docs/current-state.md`
  "Product catalog", `docs/publishing/README.md` packet index) AND against
  the consumed #142 batch's verdicts (`docs/products/ideas-2026-07-13.md` —
  its parks and kills are not re-pitched). Where a concept borders a
  shipped product, the overlap boundary is stated in its scoring — the
  disclosed-cross-sell precedent is kill-rule-kit vs field-manual ch.8.
- **Distribution-first** (conventions #15): every concept names its
  first-ten-customers surface or scores down. The only proven channel this
  lane owns is a single-click Gumroad-style listing (plus owner-gated
  article funnels that have produced 0 sales so far) — scored accordingly,
  no directory-funnel plays (that pattern died with cc-cost-lens).
  **Token-cost** (conventions #14): each BUILD/PARK carries an estimated
  build budget; kills carry none (nothing will be spent on them).

---

## 1. AI Novella Production Kit — $29 — **BUILD (tight budget)**

**Pitch:** The one-session 15k-word manuscript method this repo actually
runs, packaged: the chapter-file structure and word-count discipline that
produced 16 complete manuscripts (10 adult titles, 5 YA, 1 MG — all
committed, all ~15k words), the series-bible `CANON.md` convention that
keeps multi-book continuity honest, the completeness-verification
checklist born from a real mid-turn death (PR #157 died at 0 words and
was resumed to a merged 15,995-word manuscript, PR #159), and the
fiction vetting-packet grammar that gates "written" from "publishable."
Zero-runtime content pack in the MACP mold: distillation of committed
conventions, every truth-claim cited to a real PR event, no manuscript
text resold.

**Target buyer:** writers and indie publishers using AI assistants for
long-form fiction who get 2k words of promising start and no finished
book — the gap between "the model can write" and "a manuscript exists."

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 3 | AI-assisted fiction is a large, genuinely searched surface (writing communities, "write a novel with AI" queries, Gumroad's writing-template category) — but it's crowded with prompt-pack sellers, we own no audience there, and it's a NEW funnel for this lane with zero evidence, unlike the agent-ops funnel which at least has a live listing. |
| Buildability | 20% | 4.5 | 16 complete manuscripts, 31 vetting packets, series CANON.md files, and the #157→#159 recovery case are all committed evidence to distill from; one learnable unknown — rewriting agent-fleet-specific vetting grammar for a non-fleet writing audience. |
| Launch-effort | 15% | 4 | One publish click on the already-live Gumroad account; listing copy at catalog parity. |
| Speed to first $ | 15% | 4 | Days-scale distillation of committed conventions — no new runtime surface. |
| WTP / moat | 15% | 2.5 | Buyers demonstrably pay for AI-writing prompt packs and courses (worse versions of this), but free substitutes are endless and the method is copyable in an afternoon — the moat is the receipts (16 finished manuscripts with PR-cited word counts), not the advice. |

**Total:** 0.35·3 + 0.20·4.5 + 0.15·4 + 0.15·4 + 0.15·2.5 = 1.05 + 0.90 +
0.60 + 0.60 + 0.375 = **3.525**

**Provisional kill-rule fields (bind at INTAKE):** signal = ≥1 sale OR ≥50
article reads within 30 days of publish, else ledgered negative ·
first-ten path = (1) "an agent lane finished 16 novellas — the method"
article on a writing-adjacent surface ⚑, (2) cross-link from the
template-packs + field-manual listings ⚑ (weak-fit disclosed: those buyers
are agent operators, not novelists), (3) Gumroad Discover, writing
category ⚑ · est. budget ≤60k tokens to v0.1 (tight — sole BUILD in a
borderline-topped batch). **Verdict: BUILD (#1), tight budget.**

## 2. Fiction Vetting-Packet Kit — $19 — **PARK**

**Pitch:** Just the publish-gate, standalone: the vetting-packet grammar
that 31 committed book packets run (quality-floor checklist, §-structured
packet template, owner click-script for the publish step), genericized
for anyone shipping AI-drafted books.

**Target buyer:** same as #1 minus the drafting problem — which is the
problem: it's a strict subset.

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 2.5 | "How do I know my AI manuscript is publishable" is a real pain but rarely searched as a *checklist* purchase; reach is pure cross-sell from #1's channel. |
| Buildability | 20% | 4.5 | 31 worked packets committed; genericizing repo-specific gate steps is the only work. |
| Launch-effort | 15% | 4 | One click, existing storefront. |
| Speed to first $ | 15% | 4 | Days-scale. |
| WTP / moat | 15% | 2 | A checklist + template grammar; the free substitute is reading any public repo that runs it — thin standalone value. |

**Total:** 0.35·2.5 + 0.20·4.5 + 0.15·4 + 0.15·4 + 0.15·2 = 0.875 + 0.90 +
0.60 + 0.60 + 0.30 = **3.275**

**Verdict: PARK** — borderline band, and it is a strict subset of concept
#1's audience and content (the same shape as the #142 batch's claims-kit →
MACP fold). Correct home: a chapter + template inside the AI Novella
Production Kit, not a standalone SKU. Revisit only if #1 ships and shows
signal. (No budget assigned.)

## 3. Pre-Registered Experiment Kit — $19 — **PARK**

**Pitch:** The pre-registration discipline the trading lane ran, packaged:
declare N experiments with promotion gates BEFORE running them, a
promotion-criteria template, and the honest-null reporting format that let
R3 (3,468 configs) and R4 (6 pre-registered experiments) close with **0
promotions** recorded as a deliverable instead of a quiet abandonment —
the anti-overfitting version of the kill rules, for parameter sweeps.

**Target buyer:** developers running strategy/parameter sweeps (trading
bots, prompt configs, model comparisons) who promote whatever looked good
in-sample because nothing forced the criteria up front.

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 2.5 | Overfitting/backtest pain is genuinely discussed in large quant and ML communities, but those channels are hostile to paid kits and this lane has never touched them — a named surface we cannot demonstrably reach. |
| Buildability | 20% | 4 | The discipline and its results are real but the worked evidence lives in the sibling trading repo — the shipped kit must cite it as external or re-run a toy sweep in-kit (the claims-kit external-citation wrinkle, again). |
| Launch-effort | 15% | 4 | One click, existing storefront. |
| Speed to first $ | 15% | 4 | Days-scale: templates + the reporting format. |
| WTP / moat | 15% | 2.5 | Pre-registration is preached for free everywhere (academic + quant blogs); the delta is worked agent-lane templates with a real 0-promotions run behind them — thin but non-zero. |

**Total:** 0.35·2.5 + 0.20·4 + 0.15·4 + 0.15·4 + 0.15·2.5 = 0.875 + 0.80 +
0.60 + 0.60 + 0.375 = **3.25**

**Verdict: PARK** — borderline band with no fold-in home in the current
catalog and a channel this lane has zero presence in. Revisit only if the
lane ever ships a trading-adjacent product that shows signal, or if the
external-evidence wrinkle resolves (re-run in-kit). (No budget assigned.)

## 4. Trilingual Edition Factory — $19 — **KILL**

**Pitch:** Deriving board-book, translation (EN/NL/DE), large-print, and
novella-cut editions from one manuscript, as templates + checklists:
EDITION-SPEC grammar, board-book cut rules, translation-parity checklist —
distilled from 27 committed board-book texts, 9 trilingual title-lines,
5 large-print specs, and 2 novella cuts.

**Target buyer:** children's-book self-publishers repurposing one story
across formats and languages.

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 2 | Children's-book self-publishers wanting multi-edition workflow kits are a niche of a niche with no named surface this lane can reach — smaller even than the agent-ops audience. |
| Buildability | 20% | 4.5 | All the edition artifacts are committed; distillation is mechanical. |
| Launch-effort | 15% | 4 | One click. |
| Speed to first $ | 15% | 4 | Days-scale. |
| WTP / moat | 15% | 2.5 | Real pain for the few who have it, but the kit cannot promise translation QUALITY generically — the honest offer is structure only, and structure is copyable. |

**Total:** 0.35·2 + 0.20·4.5 + 0.15·4 + 0.15·4 + 0.15·2.5 = 0.70 + 0.90 +
0.60 + 0.60 + 0.375 = **3.175**

**Verdict: KILL** — borderline score, but distribution 2 is disqualifying
under a 35% weight (the #142 batch's wake-chain precedent: same score
shape, same fatal axis), and the quality-promise gap caps WTP structurally.

## 5. Dead-Session Recovery Playbook — $15 — **KILL**

**Pitch:** What to do when an agent session dies mid-turn: detecting
work that died at 0 words vs work that half-landed, the born-red card as
the recovery beacon, and the resume protocol — anchored to a real worked
case (PR #157 died mid-turn at 0 words → resumed as PR #159, merged
complete; born-red recovery events #159/#160).

**Target buyer:** agent-fleet operators — the field-manual audience,
again.

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 2 | A subset of the field-manual buyer (already the smaller agent-ops population), reachable only through the same in-catalog cross-sell. |
| Buildability | 20% | 4.5 | The worked case and the born-red convention are committed; distillation is small and known. |
| Launch-effort | 15% | 4 | One click. |
| Speed to first $ | 15% | 4 | Days-scale. |
| WTP / moat | 15% | 2 | One convention + one war story; the field manual's born-red material is the near-free substitute in our own catalog. |

**Total:** 0.35·2 + 0.20·4.5 + 0.15·4 + 0.15·4 + 0.15·2 = 0.70 + 0.90 +
0.60 + 0.60 + 0.30 = **3.10**

**Verdict: KILL** — borderline score, but the delta over the field
manual's own chapters is too thin to defend against "I'll just re-read the
manual" (the #142 batch's wake-chain reasoning verbatim), and it deepens
the exact channel this batch is trying to stop over-serving.

## 6. Agent Session Retro Kit — $15 — **KILL**

**Pitch:** The standing-retro protocol, packaged: the by-ID retro question
bank (`docs/retro/QUESTIONS.md` pattern), the session-retro template, and
the answer-only-on-friction cadence — repo-committed and run across the
lane's sessions.

**Target buyer:** agent operators who want their sessions to compound
lessons instead of repeating them.

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 2 | Retro tooling reads like a blog post, not a purchase; no named surface beyond the same agent-ops cross-sell. |
| Buildability | 20% | 4.5 | Question bank + worked retros committed; extraction is mechanical. |
| Launch-effort | 15% | 4 | One click. |
| Speed to first $ | 15% | 4 | Days-scale. |
| WTP / moat | 15% | 1.5 | Abundant free retro templates next door, and our own template-packs ($19 PWYW) already ships session-discipline material — this half-cannibalizes it at a lower price. |

**Total:** 0.35·2 + 0.20·4.5 + 0.15·4 + 0.15·4 + 0.15·1.5 = 0.70 + 0.90 +
0.60 + 0.60 + 0.225 = **3.025**

**Verdict: KILL** — barely over the line arithmetically, but it partially
cannibalizes a shipped product (template-packs' session discipline) at a
lower price point — the #142 batch's fixture-vault precedent: a
borderline score does not survive a cannibalization finding.

## 7. Provenance-Freshness Checker Kit — $15 — **KILL**

**Pitch:** The `file@sha` citation-footer convention from the guide-shaped
products, plus a small advisory checker that nags when a cited source has
drifted since the pinned sha — turning "citation-verified" from a
point-in-time claim into a maintained one.

**Target buyer:** developers shipping docs/guides whose truth-claims cite
a moving codebase.

| Axis | W | Score | One-line justification |
|---|---|---|---|
| Distribution | 35% | 1.5 | Nobody searches for "citation freshness checking" — this is "post it and hope." |
| Buildability | 20% | 4 | The footer convention is committed across shipped guide chapters, but the checker script itself does NOT exist yet — it's a session-card idea, so the kit's core artifact is net-new code. |
| Launch-effort | 15% | 4 | One click. |
| Speed to first $ | 15% | 4 | Days-scale for a ~40-line advisory script + convention write-up. |
| WTP / moat | 15% | 1.5 | The whole trick fits in a gist; the free substitute is this paragraph. |

**Total:** 0.35·1.5 + 0.20·4 + 0.15·4 + 0.15·4 + 0.15·1.5 = 0.525 + 0.80 +
0.60 + 0.60 + 0.225 = **2.75**

**Verdict: KILL** — below the 3.0 do-not-build line; distribution 1.5 and
WTP 1.5 are the two honest lowest scores and they are fatal together.
(Worth keeping as an INTERNAL advisory-script idea — it's already ledgered
on a session card — just not as a SKU.)

---

## Ranked summary

| # | Concept | Price | Total | Verdict |
|---|---|---|---|---|
| 1 | AI Novella Production Kit | $29 | 3.525 | **BUILD** (tight budget) |
| 2 | Fiction Vetting-Packet Kit | $19 | 3.275 | PARK (fold into #1) |
| 3 | Pre-Registered Experiment Kit | $19 | 3.25 | PARK (no fold-in home) |
| 4 | Trilingual Edition Factory | $19 | 3.175 | KILL (distribution 2 fatal) |
| 5 | Dead-Session Recovery Playbook | $15 | 3.10 | KILL (thin delta over field manual) |
| 6 | Agent Session Retro Kit | $15 | 3.025 | KILL (cannibalizes template-packs) |
| 7 | Provenance-Freshness Checker Kit | $15 | 2.75 | KILL (<3.0) |

**Why the BUILDs might fail (Kill Rule 2, batch-level):** the sole BUILD
deliberately steps OFF the saturated agent-ops funnel (0 organic sales
across every click-queued product so far) into a writing-adjacent channel —
which diversifies channel risk exactly as far as zero evidence allows: the
lane has never posted, listed, or sold anything to writers, the AI-writing
space is thick with cheap prompt packs, and the buyer may want finished
fiction rather than a method for finishing fiction. The receipts (16
committed manuscripts) are the moat and they are only verifiable by people
who read repos — a skill the target buyer may not have. Both PARKs are
channel-mismatched today. Conservative expectation for the BUILD: $0
absent distribution. Note also that this batch tops out at 3.525 —
borderline-band territory; the #142 batch's two 3.60s were the better
draws, and they are spent.

*Verdict citation (ORDER 011 / V053 (sim-lab `32ff5c3`)):* this batch's
sole-BUILD channel diversification satisfies VERDICT 053's (approve)
reserve-one-untested-channel backstop — measured DIV − CON ≥ 1/100 in 9
of 9 registered belief cells (sim-lab
`sims/verdict-053-channel-concentration/REPORT.md`). Full ruling,
application guard (conditions on 0 organic sales as of 2026-07-13; stales
at the first incumbent organic sale) and independence boundary are
recorded in the #142 batch doc's Kill-Rule-2 note
([`ideas-2026-07-13.md`](ideas-2026-07-13.md)).

**Next slice:** write full `INTAKE.md` (kill-rule fields binding, budget
hard ≤60k tokens) for concept #1, then build to publish-READY on this
branch — build only after intake per Kill Rule 0.
