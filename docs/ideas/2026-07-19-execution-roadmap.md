---
state: captured
origin: agent
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Execution roadmap — 2026-07-19 (veto menu, groomed & sequenced)

> **Status:** `ideas`
>
> A **prioritized, sequenced execution roadmap** groomed from the 64-item
> veto-ready planning menu (`docs/ideas/2026-07-18-veto-ready-menu.md`, #247).
> Where that menu was a deliberately excessive *field to veto from*, this doc is
> the *order in which the survivors should be picked up* — reality-corrected
> against the overnight **#242–#257** wave (nine menu items already SHIPPED; they
> are marked **DONE** below so no session re-proposes them). Planning doc only:
> nothing here is built, priced-live, or published; every publish/spend/proofread
> remains an owner action. It **grooms and references** the veto menu rather than
> re-deriving it — line detail lives there, sequence lives here.

## How to read this

Each entry is **one line**: `item id — name · autonomous-safe | owner-gated ·
single unblock condition`. Owner-gate labels are copied from the veto menu's own
per-line fields, not re-guessed.

- **autonomous-safe** — a session can take it to owner-click-ready (or fully
  done, for pure repo tooling) with only the always-present publish click, or
  nothing at all, outstanding. **Sequenced first.**
- **owner-gated** — build may be agent-completable, but going live needs a named
  owner action (a decision, a publish/spend, a marketplace/account step, or the
  native-speaker proofread). **Grouped below by which gate they wait on.**

## The three constraints this sequence is tied to

Sequencing is not by raw value — it is by these three standing constraints, in
this precedence:

1. **The EAP goes read-only 2026-07-21** (`docs/current-state.md`, "Platform
   wind-down") — **two days out.** Any work that must land *as repo work* has to
   land while the seat can still write. Every autonomous-safe item below is repo
   work, so all of it competes for the same closing window; that is why the
   sequence front-loads pure-repo tooling that cannot be done later at all.
2. **Distribution, not inventory, is the binding constraint** (1 LIVE SKU, 0
   organic sales, 19 publish-READY SKUs undiscovered). New SKUs/books are cheap
   to build but **do not move revenue without an owner-gated publish + a
   distribution path**. So new inventory is deprioritized *below* tooling that
   protects and routes the inventory already built, and below the distribution
   enablers that convert the owner's finite attention into live listings.
3. **The live-SWTK Stripe kill clock** — T+7 checkpoint **2026-07-19 (today)**,
   T+14 kill-rule **2026-07-26**. The two autonomous artifacts this needed
   (DIST-3 funnel diagnostic #252, MISC-3 decision packet #253) already SHIPPED;
   what remains is the **owner's** keep/iterate/delist read at the clock —
   owner-gated, nothing autonomous left except keeping the packet reachable.

### Top-of-order rationale (my call, decide-and-flag)

**The 2026-07-21 write-wall dominates the ranking.** Because all autonomous repo
work must land in the next two days or not at all, the top of the sequence is the
work that (a) has zero publish surface, (b) is fully reversible, (c) makes the
pipeline *self-maintaining* for the post-cutover fresh-seat world the wind-down
is aiming at, and (d) protects or routes inventory the distribution constraint
says is already the scarce-value asset. New SKUs — which the same constraint says
won't move revenue on their own — rank *below* all of that, as breadth only.

---

## Lane A — Autonomous-safe, sequenced (do these first, before 2026-07-21)

> All are `can-build-autonomously` per the veto menu. Ordered by the top-of-order
> rationale above: pipeline-safety tooling → self-maintenance/wind-down hygiene →
> distribution throughput → remaining tooling/specs → new inventory (breadth).

### Tier A1 — Pipeline-safety tooling (zero publish surface, must land pre-cutover)

1. **ENG-6** — `derive_owner_queue.py` idempotence/self-test guard · autonomous-safe · unblock: none (pure repo tooling; completes the D-ref safety story ENG-2 #248 began by preventing a regen from *silently reintroducing* the #244/#245 mispoint).
2. **ENG-5** — `check_catalog_registration.py` (built-but-unregistered checker) · autonomous-safe · unblock: none (guarantees none of the 19 READY SKUs strands invisible — directly protects the already-built inventory the distribution constraint prizes).
3. **ENG-4** — `check_funnel_assets.py` (per-KIT funnel-asset checker) · autonomous-safe · unblock: none (per-SKU counterpart to the shipped per-cluster ENG-3 #256; could merge with it as one checker, two advisories).
4. **ENG-7** — OWNER-QUEUE staleness / proofread-gate drift checker (= PUB-9) · autonomous-safe · unblock: none (keeps the generated queue trustworthy after packet edits).
5. **ENG-8** — docs-freshness + link/orphan checker (= OPS-5 + OPS-6) · autonomous-safe · unblock: none (cheap `docs/` hygiene; keeps the ledger honest for a fresh seat).

### Tier A2 — Self-maintenance & wind-down hygiene (serves the fresh-seat relaunch)

6. **MISC-5** — planning-doc conveyor consolidation · autonomous-safe · unblock: none (reconciles the now-four planning docs so a post-cutover seat can't re-derive a false "backlog dry" — this doc is the manual version; a checker keeps it fresh).
7. **MISC-1** — fresh-seat boot hardening for the post-EAP repo · autonomous-safe · unblock: none (the wind-down explicitly wants the repo "clean enough that a fresh seat boots from the repo alone" — land it while writable).

### Tier A3 — Distribution throughput (highest leverage against the binding constraint)

8. **DIST-2** — "Owner publish hour" sequencer (extends `OWNER-LAUNCH-HOUR.md`) · autonomous-safe · unblock: none for the build (the clicks it orders stay owner-only) — converts the owner's finite pre-cutover attention into the most live listings per minute.
9. **DIST-5** — static catalog landing microsite (= REV-4) · autonomous-safe to build · unblock: owner hosting/domain publish to go live (build the static files in-repo now).
10. **DIST-6** — launch-kit: Product Hunt / HN / Reddit playbook (= REV-5) · autonomous-safe to build · unblock: owner posting (assets are agent-buildable; posting is OWNER-ACTION).
11. **LM-3** — fiction-catalog reader magnet (free first-chapter / sampler) · autonomous-safe (existing-content sampler) · unblock: none to build; note honestly it converts on a mailing list the repo doesn't yet own (see DIST-4).

### Tier A4 — Book-gate tooling & further tooling (autonomous, lower urgency)

12. **BOOK-6** — native-speaker proofread TOOLING (= PUB-1 + PUB-6 + PUB-7) · autonomous-safe · unblock: none (the only writing work that moves the gated book cluster *without* owning the gate — it tools the gate, cannot clear it).
13. **ENG-10** — kit CI smoke-matrix consolidation · autonomous-safe · unblock: none (best paired with ENG-1; touches shipped-kit CI, reversible).
14. **BOOK-8** — audiobook / narration-ready editions spec, beyond the two lead titles (extends P-9) · autonomous-safe for the spec · unblock: owner narration/production spend; NL also waits on LENGTH-BAND-PREP ratify (⚑3).
15. **BOOK-9** — book-catalog KDP-first revenue-path spec (= REV-7) · autonomous-safe to draft the spec · unblock: owner-decision (KDP account + publish model).

### Tier A5 — New sellable SKUs (breadth only — build for cross-sell, not revenue)

> The veto menu's own framing: "**None of these move revenue on their own** — they
> add shelf inventory to a shelf whose constraint is footfall, not stock." All are
> `can-build-autonomously`. Ranked *last* of the autonomous lane on purpose.
> Suggested pick order within the tier (highest cross-sell fit first):

16. **SKU-4** — PayPal / Square Webhook Test Kit $29 · autonomous-safe · unblock: publish click (highest-intent payments buyer, beside the live Stripe kit).
17. **SKU-5** — Timeout & Circuit-Breaker Test Kit $29 · autonomous-safe · unblock: publish click (completes the outbound-resilience story; native cross-sell into the API Robustness Bundle).
18. **SKU-11** — Timezone / DST Test Kit $29 · autonomous-safe · unblock: publish click (universal-pain class, largest audience).
19. **SKU-8** — SSE / Streaming-Response Test Kit $29 · autonomous-safe · unblock: publish click (timely — the LLM-app buyer segment).
20. **SKU-7** — Multipart / File-Upload Validation Test Kit $29 · autonomous-safe · unblock: publish click (high-severity security-tier class).
21. **SKU-1** — Twilio Webhook Test Kit $29 · autonomous-safe · unblock: publish click (broadens the signature family; feeds BND-2).
22. **SKU-2** — Discord Interaction Webhook Test Kit $29 · autonomous-safe · unblock: publish click (distinct Ed25519 asymmetric path).
23. **SKU-3** — SendGrid / Mailgun Inbound-Webhook Test Kit $29 · autonomous-safe · unblock: publish click (email-infra buyer segment).
24. **SKU-10** — Money / Decimal-Rounding Test Kit $29 · autonomous-safe · unblock: publish click (fintech/billing buyer).
25. **SKU-6** — ETag / Conditional-Request Test Kit $29 · autonomous-safe · unblock: publish click.
26. **SKU-13** — Env-Var / Config Validation Test Kit $19 · autonomous-safe · unblock: publish click (broad cheap ops SKU).
27. **SKU-12** — CSV / Formula-Injection Test Kit $19 · autonomous-safe · unblock: publish click (cheap security-cluster breadth).
28. **SKU-15** — Health-Check / Readiness-Probe Test Kit $19 · autonomous-safe · unblock: publish click (k8s/ops buyer).
29. **SKU-14** — OpenAPI / Schema-Conformance Test Kit $29 · autonomous-safe · unblock: publish click (API-governance buyer; keep stdlib-only or vendor honestly).
30. **SKU-18** — The API Robustness Playbook $39 (content anthology) · autonomous-safe · unblock: publish click (~70% assembled; higher-AOV content anchor).
31. **SKU-16** — Webhook Signature Verifier CLI + GitHub Action $19 · autonomous-safe to build · unblock: owner Marketplace publish for the Action.
32. **SKU-9** — GraphQL Error-Contract Test Kit $29 · autonomous-safe · unblock: publish click (*speculative* — smaller audience; a maybe).
33. **LM-4** — photo-packs / visual-assets cluster lead magnet · autonomous-safe · unblock: publish/post (*speculative* — only if photo-packs stay a live lane).
34. **BOOK-7** — next adult-novella writes from the 2026-07-14 batch (concepts 2–5) · autonomous-safe to draft · unblock: owner book publish — *build only once the fiction funnel (LM-3 / DIST-4) exists to catch it.*

---

## Lane B — Owner-gated, grouped by the gate they wait on

> Build artifacts here are largely agent-completable, but they cannot go live
> until the named gate clears. An agent may build the artifact and park it; it is
> listed under its **binding** gate.

### Gate B1 — Owner DECISION (a yes/no or design call only the owner can make)

- **ENG-1** — `_api-hardening-core/` extraction + `provenance_lint.py` (= R5) · owner-gated · unblock: owner yes/no on refactoring nine *shipped* kits (status.md ⚑5 already queues this exact call; regression risk vs zero pre-publish revenue).
- **MISC-2 / R6** — pricing-experiment spec (PWYW floor + Founder's Everything anchor) · owner-gated · unblock: owner price-edit decision.
- **BND-3** — Founder's Everything Bundle (time-boxed tiered, extends R6) · owner-gated · unblock: owner pricing/discount decision.
- **DIST-4** — conversion-tracking / UTM + email-capture spec (= REV-3 + REV-5) · owner-gated · unblock: owner email-tool / analytics account spend+setup.
- **DIST-8** — real-Stripe-path / payment test-harness spec (= REV-1) · owner-gated · unblock: owner decision + spend on a live payment integration (*speculative — lowest distribution priority*).

### Gate B2 — Owner PUBLISH / POST / hosting (build done; going live is an owner action)

- **DIST-7** — cross-sell hub / storefront consolidation (= REV-8) · owner-gated · unblock: owner live-storefront edits.
- **MISC-4** — owner-postable catalog one-pager · owner-gated · unblock: owner posts it to a channel/newsletter.
- *(DIST-5, DIST-6, SKU-16, LM-3, LM-4 are listed in Lane A because their **build** is autonomous; only their go-live is owner-gated.)*

### Gate B3 — Component PUBLISHES (bundles that reference live listings — HARD-GATED)

- **BND-1** — Full API Hardening Bundle $149 (nine kits) · owner-gated · unblock: all nine component kits published live.
- **BND-4** — Agent-Ops Starter Bundle $79 · owner-gated · unblock: its component publishes.
- **BND-5** — "Merge & Ship" Cookbook Combo $29 · owner-gated · unblock: the two cookbook publishes (low friction).
- **BND-6** — Robustness Reading Bundle $29 · owner-gated · unblock: the three cookbook publishes.
- **BND-2** — Webhook Provider Mega-Pack $99 · owner-gated · unblock: SKU-1…SKU-4 built *and* published (chains on un-built SKUs — speculative).
- **BND-7** — Trilingual "First Library" board-book bundle (= R8) · owner-gated · unblock: owner digital publish (any physical POD is a harder owner gate).
- **BND-8** — The Writer's Starter · owner-gated · unblock: LM-2 (done #251) live + owner publish — build once its component is publishable.
- **SKU-17** — Test-Kit Runner GitHub Action pack $19 · owner-gated · unblock: owner Marketplace listing (build autonomous; best after ENG-1).

### Gate B4 — Native-speaker PROOFREAD (owner-only; an AI can tool the gate, not clear it)

- **BOOK-4** — The Night Kiln NL omnibus (= R9) · owner-gated (**softened** — components carry their proofread state) · unblock: front/back-matter proofread + the LENGTH-BAND-PREP one-word ratify (⚑3) — *the most shippable book item.*
- **BOOK-1** — The Salt Bell NL edition (= R10) · owner-gated · unblock: native-speaker NL proofread (highest NL fit; slowest gate).
- **BOOK-2** — The Wire Garden NL edition (= P-6) · owner-gated · unblock: native-speaker NL proofread.
- **BOOK-5** — YA line first NL edition pilot (= P-7) · owner-gated · unblock: native-speaker NL proofread.
- **BOOK-3** — The Paper Orange DE edition (= P-8) · owner-gated · unblock: native-speaker DE proofread (biggest reach, most sensitive subject, hardest to source).

### Gate B5 — Owner READ at the kill clock (time-boxed; the autonomous work is already DONE)

- **Live-SWTK T+7/T+14 call** · owner-gated · unblock: owner reads the funnel diagnostic (`docs/launch/funnel-diagnostic.md`, DIST-3 #252) + the decision packet (`docs/launch/kill-clock-decision-packet.md`, MISC-3 #253) and makes the keep/iterate/delist call by **2026-07-26**.

---

## DONE — shipped in the #242–#257 wave (do NOT re-propose)

Verified against `git log` and `docs/current-state.md`; retired from the field so
no session rebuilds them:

| Veto item | What it became | PR |
|---|---|---|
| **ENG-2** | `check_catalog_drefs.py` D-ref guard + required `catalog-dref-guard` CI job | **#248** |
| **DIST-1** | reusable `docs/launch/DISTRIBUTION-PLAYBOOK.md` | **#249** |
| **LM-1** | membership / boilerplate cluster free lead-magnet article | **#250** |
| **LM-2** | AI-Novella / writing-tools cluster free lead-magnet article | **#251** |
| **DIST-3 / REV-2** | `docs/launch/funnel-diagnostic.md` (why-zero-sales) | **#252** |
| **MISC-3** | `docs/launch/kill-clock-decision-packet.md` | **#253** |
| **DIST-9** | pre-EAP-read-only publish sprint plan | **#255** |
| **ENG-3** | `check_funnel_coverage.py` per-cluster funnel-top checker | **#256** |
| **ENG-9 / OPS-1** | retire legacy root `claims/` dir | **#257** |

*(Also already live before the veto menu was written, per its own notes: the
api-robustness lead magnet #243 and the agent-ops lead magnet #246 — the two
clusters that already had a funnel-top, distinct from LM-1…LM-4.)*

## Scope note / cross-ref (not a venture roadmap item)

- **MISC-6** — trading cross-ref only; trading planning is a separate repo/PR.
  Carried here for completeness, **no venture work sequenced against it.**

## Provenance

Derived from the repo at `main@5d439bf`, no fabricated metrics:

- Every line item, its owner-gate label, and its unblock condition —
  `docs/ideas/2026-07-18-veto-ready-menu.md` (#247), the source menu this grooms.
- The nine DONE items and their PR numbers — `git log` (#242–#257) cross-checked
  against `docs/current-state.md` "Recently shipped."
- The three constraints (distribution binding · EAP read-only 2026-07-21 ·
  SWTK T+7 2026-07-19 / T+14 2026-07-26) — `docs/current-state.md` and the veto
  menu's "standing context" section.
- The R-namespace relationship (why this is a new doc, not an edit of the
  next-wave roadmap) — `docs/ideas/2026-07-18-next-wave-roadmap.md` and the
  `docs/ideas/README.md` "conveyor, not a graveyard" convention.
