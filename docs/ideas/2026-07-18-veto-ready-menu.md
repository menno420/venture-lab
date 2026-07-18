---
state: captured
origin: agent
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Veto-ready planning menu — 2026-07-18 (owner morning deliverable)

> **Status:** `ideas`
>
> A deliberately **EXCESSIVE**, line-by-line **veto-ready** menu, written to the
> owner's live overnight directive (2026-07-18, relayed by the coordinator):
> *"if your executable work is done, move over to planning… plan excessively…
> tomorrow morning I will skim the whole menu and VETO what I don't want; my veto
> is the filter, so don't pre-filter down to a few safe picks."* So this doc does
> **not** pre-filter to a few safe picks — it lists everything I can honestly
> justify, from one-line reversible checkers to gated ambitious swings, and lets
> the **owner's veto be the filter**. Nothing here is built, priced-live, or
> published; this is a **planning doc**, and every publish/spend/proofread remains
> an owner action. It **REFERENCES and EXTENDS** the two standing planning docs
> rather than re-deriving them — see "How this relates to the existing menus"
> below — and marks what has SHIPPED since they were written so no line proposes
> rebuilding a thing already in the tree.

## How the owner uses this

Skim top to bottom. Each proposal is one block with a **pitch** · **effort
(S/M/L)** · **risk & reversibility** · **what it unblocks** · **owner-gate
status**. **Cross out (veto) whatever you don't want.** Survivors become claimed
slices in later sessions. Quantity is intentional — the point is to give you a
wide field to cut from, not a shortlist someone already cut for you.

Owner-gate legend:
- **can-build-autonomously** — an agent takes it to owner-click-ready with only
  the always-present publish click (or nothing at all, for pure repo tooling)
  outstanding.
- **needs-owner-decision** — a yes/no or a design call only the owner can make
  (e.g. authorize a refactor of shipped kits).
- **needs-owner-spend/publish** — build is agent-completable but going live costs
  money or requires the owner's Gumroad/account action.
- **needs-owner-proofread** — hard-gated on the owner-only native-speaker NL/DE
  proofread pass (an AI can *tool* this gate but cannot *clear* it — see the
  honesty note under BOOK).

## How this relates to the existing menus (no duplication)

Two planning docs already stand:

- **`docs/ideas/2026-07-18-next-wave-roadmap.md`** — the ranked next-SKU pipeline
  R1–R10. Since it was written, **R1 (Rate-Limit), R2 (Pagination), R3 (JWT
  Auth), R4 (Idempotency & Retry Cookbook) and R7 (API Robustness Bundle) all
  SHIPPED** (PRs #236–#239, #234), and a genuinely-new **CORS Preflight Test Kit
  SHIPPED** (#242). Still open from that doc: **R5** (core extraction +
  provenance_lint), **R6** (pricing spec), **R8** (board-book bundle), **R9**
  (Night Kiln NL omnibus), **R10** (Salt Bell NL).
- **`docs/ideas/2026-07-17-overnight-menu.md`** — the 38-item P/PUB/REV/OPS menu.
  Its product lane (P-1…P-4, P-9, P-10-EN) shipped; its PUB/REV/OPS lanes are
  largely still open.

Where a proposal below **is** one of those existing IDs, I say so and extend it
rather than restate it. Everything with a fresh `[AREA-N]` id is **new to tonight**
or a distinct recombination the two prior docs don't carry. IDs here are
area-prefixed (`SKU-`, `BND-`, `LM-`, `ENG-`, `DIST-`, `BOOK-`, `MISC-`) so they
never collide with the R/P/PUB/REV/OPS namespaces.

## The one piece of standing context every line should be read against

- **The binding constraint is DISTRIBUTION, not inventory.** 1 LIVE SKU (Stripe
  Webhook Test Kit) with 0 organic sales, and ~18 publish-READY SKUs that are
  built-but-undiscovered (`docs/launch/CATALOG.md`). More inventory is cheap;
  more *first sales* is the scarce thing. I have ranked the distribution lane
  (DIST) high for this reason, and flagged the SKU lane honestly as "easy to
  build, does not by itself move revenue."
- **The live Stripe kit is under a kill clock** — T+7 funnel checkpoint
  **2026-07-19 (tomorrow)**, T+14 kill-rule **2026-07-26** (≥1 organic sale OR ≥1
  qualified inbound, else pause/delist). Two proposals below (DIST-3, MISC-3) are
  time-boxed against it.
- **The EAP goes read-only 2026-07-21** (`docs/current-state.md` "Platform
  wind-down"). After that the autonomous seats cannot write. Anything that must
  land as repo work should land before then; anything that is an *owner* click is
  unaffected by the write-wall but competes for the owner's finite pre-cutover
  attention. DIST-9 makes this its own line.

---

## AREA 1 — New sellable SKUs

> Honest framing for the whole area: the webhook-signature + API-robustness
> test-kit family is now **largely exhausted** — Stripe/GitHub/Slack/Shopify
> webhook kits and Idempotency/Rate-Limit/Pagination/JWT/CORS test kits are all
> built. New kits are therefore either (a) a **new provider** on the proven
> signature scaffold, or (b) a **new failure class** on the proven real-path
> scaffold, or (c) a genuinely **adjacent dev tool** (a runnable, not a test
> suite). All (a)/(b) items are `can-build-autonomously` — the whole kit
> (harness, correct/naive reference pair, real-path suite, PROVENANCE'd fixtures,
> byte-reproducible `package.sh`, §7 vetting packet, CI job) mirrors a shipped kit
> end-to-end with no live account or key. **None of these move revenue on their
> own** — they add shelf inventory to a shelf whose constraint is footfall, not
> stock. Build them for cross-sell breadth, not as a revenue lever.

### SKU-1. Twilio Webhook Test Kit — $29 · dev tool
- **Pitch:** proves your endpoint verifies `X-Twilio-Signature` correctly (HMAC-SHA1
  over the full URL + sorted POST params, the exact footgun-rich Twilio scheme) and
  rejects a tampered/missing signature. Correct + naive reference pair.
- **Effort:** M. **Risk/rev.:** low, fully reversible (new isolated `candidates/`
  dir). **Unblocks:** a webhook-provider mega-pack (BND-2); broadens the signature
  family past the four shipped providers. **Owner-gate:** can-build-autonomously.

### SKU-2. Discord Interaction Webhook Test Kit — $29 · dev tool
- **Pitch:** Discord verifies interactions with **Ed25519** (asymmetric), unlike
  the HMAC providers — a genuinely distinct crypto path that proves your bot
  rejects bad signatures and the required `PING`→`PONG` ack. Correct + naive pair.
- **Effort:** M. **Risk/rev.:** low; honest caveat — Ed25519 needs a vendored key,
  still no third-party account. **Unblocks:** signature-family breadth into the
  asymmetric case. **Owner-gate:** can-build-autonomously.

### SKU-3. SendGrid / Mailgun Inbound-Webhook Test Kit — $29 · dev tool
- **Pitch:** proves your inbound-email/event webhook verifies the provider's
  signature (SendGrid Ed25519 event webhook; Mailgun HMAC) and handles the
  parse/enclosure footguns. Correct + naive pair.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** email-infra buyer segment
  adjacent to the payments/CI segment. **Owner-gate:** can-build-autonomously.

### SKU-4. PayPal / Square Webhook Test Kit — $29 · dev tool
- **Pitch:** the two big non-Stripe payment webhooks (PayPal cert-chain
  verification; Square HMAC-SHA256 over URL+body). Proves rejection of a forged
  event. Highest-intent payments buyer, same as the live Stripe kit's.
- **Effort:** M (PayPal cert-chain is the fiddly bit — pin to documented shape).
  **Risk/rev.:** low. **Unblocks:** the payments cross-sell beside the live SKU.
  **Owner-gate:** can-build-autonomously.

### SKU-5. Timeout & Circuit-Breaker Test Kit — $29 · dev tool
- **Pitch:** proves your *client* actually times out a hung dependency, opens a
  circuit breaker after N failures, sheds load while open, and half-opens to
  recover — the failure the idempotency/retry kits assume you've already solved.
  Correct + naive (no timeout, retries forever) reference pair.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** completes the outbound-resilience
  story (timeout → breaker → retry → idempotency); native cross-sell into the
  API Robustness Bundle. **Owner-gate:** can-build-autonomously.

### SKU-6. ETag / Conditional-Request Test Kit — $29 · dev tool
- **Pitch:** proves optimistic concurrency works — `If-None-Match` returns `304`,
  `If-Match` returns `412` on a stale write, and two racing writers can't silently
  clobber each other. Correct + naive (last-write-wins) pair.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a real silent-data-loss class
  adjacent to the pagination kit's. **Owner-gate:** can-build-autonomously.

### SKU-7. Multipart / File-Upload Validation Test Kit — $29 · dev tool
- **Pitch:** proves your upload endpoint enforces size limits, sniffs real
  content-type (not the client's claim), neutralizes path-traversal in filenames,
  and refuses a zip-bomb. Correct + naive (trusts `Content-Type`, writes the
  client filename) pair. A high-severity, widely-shipped-broken class.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a security-tier SKU beside the
  JWT auth kit. **Owner-gate:** can-build-autonomously.

### SKU-8. SSE / Streaming-Response Test Kit — $29 · dev tool
- **Pitch:** proves a Server-Sent-Events stream reconnects, resumes from
  `Last-Event-ID` with no gap or dupe, and never emits a corrupt partial frame —
  the exact pain of anyone shipping token-streaming LLM UIs. Correct + naive pair.
- **Effort:** M–L (stateful stream rig). **Risk/rev.:** low. **Unblocks:** the
  LLM-app buyer segment (timely). **Owner-gate:** can-build-autonomously.

### SKU-9. GraphQL Error-Contract Test Kit — $29 · dev tool
- **Pitch:** proves your GraphQL API returns the spec `errors[]` shape with partial
  `data`, enforces a query-depth and query-cost limit, and doesn't leak internals
  in error extensions. Correct + naive pair.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a non-REST buyer the REST-shaped
  kits miss. **Owner-gate:** can-build-autonomously. *Speculative fit* — smaller
  audience than the REST kits; mark as a maybe.

### SKU-10. Money / Decimal-Rounding Test Kit — $29 · dev tool
- **Pitch:** proves you never represent money as a float, round with the right mode
  (banker's vs half-up as declared), and respect each currency's minor unit (JPY
  has 0 decimals, KWD has 3). Correct + naive (float money, blanket 2dp) pair.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** the fintech/billing buyer; pairs
  with the payment-webhook kits. **Owner-gate:** can-build-autonomously.

### SKU-11. Timezone / DST Test Kit — $29 · dev tool
- **Pitch:** proves you store UTC, never construct a naive datetime, and get the
  DST-boundary cases right (the "duplicated hour", the "skipped hour", scheduling
  across a transition). Correct + naive pair. Everyone ships this broken once.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a universal-pain SKU with a
  huge audience. **Owner-gate:** can-build-autonomously.

### SKU-12. CSV / Formula-Injection Test Kit — $19 · dev tool
- **Pitch:** proves your CSV/XLSX export neutralizes formula injection (a cell
  beginning `=`, `+`, `-`, `@` that executes in the recipient's spreadsheet) — a
  real, under-known data-exfil vector. Correct + naive (raw passthrough) pair.
- **Effort:** S–M. **Risk/rev.:** low. **Unblocks:** a cheap security-cluster
  breadth SKU. **Owner-gate:** can-build-autonomously.

### SKU-13. Env-Var / Config Validation Test Kit — $19 · dev tool
- **Pitch:** proves your service fails fast and loud at boot on a missing/malformed
  required config value, instead of crashing at 3am on the first request that
  needed it. Correct + naive (lazy `os.environ[...]` at call site) pair.
- **Effort:** S–M. **Risk/rev.:** low. **Unblocks:** a broad, cheap ops SKU.
  **Owner-gate:** can-build-autonomously.

### SKU-14. OpenAPI / Schema-Conformance Test Kit — $29 · dev tool
- **Pitch:** proves your live responses actually match your declared OpenAPI schema
  (the doc lies the moment the code drifts) — fires real requests, validates each
  response against the spec, flags undeclared fields and type drift. Correct +
  naive pair.
- **Effort:** M–L. **Risk/rev.:** low. **Unblocks:** an API-governance buyer.
  **Owner-gate:** can-build-autonomously. *Note:* schema validation may want a
  vendored validator — keep stdlib-only or vendor honestly.

### SKU-15. Health-Check / Readiness-Probe Test Kit — $19 · dev tool
- **Pitch:** proves liveness ≠ readiness — your readiness probe fails when a
  critical dependency is down (so the LB stops routing) while liveness stays up
  (so the orchestrator doesn't needlessly restart you). Correct + naive (one
  endpoint for both) pair.
- **Effort:** S–M. **Risk/rev.:** low. **Unblocks:** a k8s/ops buyer.
  **Owner-gate:** can-build-autonomously.

### SKU-16. Webhook Signature Verifier — CLI + GitHub Action — $19 · adjacent dev tool
- **Pitch:** not a test suite — a *runnable* that verifies a webhook signature in
  CI or at the edge, packaging the family's verification logic as a
  `verify-signature` CLI and a drop-in GitHub Action. Sells to the buyer who wants
  the guardrail, not the lesson.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** broadens the catalog past
  "test kits" into "tools"; a different purchase intent. **Owner-gate:**
  can-build-autonomously (publishing an Action to the Marketplace is an owner
  account step — the artifact and repo are agent-buildable).

### SKU-17. Test-Kit Runner — GitHub Action pack — $19 · adjacent dev tool
- **Pitch:** one Action that runs any of the shipped kits against a buyer's staging
  URL in their CI and emits a pass/fail badge — turns the kits from "download and
  wire up" into "add one workflow line." A distribution *and* a product move.
- **Effort:** M. **Risk/rev.:** low; depends on the kit shape being stable (so best
  after ENG-1). **Unblocks:** recurring-use stickiness for the whole kit family.
  **Owner-gate:** needs-owner-publish for the Marketplace listing; build is
  autonomous.

### SKU-18. The API Robustness Playbook — $39 · content anthology
- **Pitch:** collect the four cookbooks (False-Green Test Trap, Idempotency &
  Retry, Merge-Wall, Auto-Merge Enabler) plus new connective chapters into one
  premium guide — the "read this cover to cover" anchor above the à-la-carte
  cookbooks. Content already ~70% exists.
- **Effort:** M (mostly assembly + connective prose). **Risk/rev.:** low.
  **Unblocks:** a higher-AOV content SKU; upsell target for every cookbook.
  **Owner-gate:** can-build-autonomously.

---

## AREA 2 — Bundles (assemble existing SKUs)

> Bundles are cheap (a listing + a manifest) and raise average order value, but a
> storefront bundle references its components as **live listings** — so most are
> **HARD-GATED on the component publishes**. That gate is the recurring theme
> here; I mark it per line. Existing bundles already built: **Webhook Verifier
> Bundle $79** (4 signature kits), **API Robustness Bundle $79/$49** (4
> own-endpoint kits), **Ship-It Bundle** (Membership + Template). Do not rebuild
> those.

### BND-1. The Full API Hardening Bundle — $149 · mega-anchor
- **Pitch:** all nine shipped dev kits (4 webhook signature + idempotency +
  rate-limit + pagination + JWT + CORS) as one catalog-topping anchor vs the ~$243
  à-la-carte sum — the single biggest "you may also like" anchor the dev catalog
  can carry.
- **Effort:** S (listing + manifest). **Risk/rev.:** low, reversible.
  **Unblocks:** top-of-range AOV; anchors every single dev-kit listing.
  **Owner-gate:** **HARD-GATED** — needs all nine components published live first;
  build the manifest now, it stalls at those clicks.

### BND-2. Webhook Provider Mega-Pack — $99 · bundle
- **Pitch:** if the new provider kits (SKU-1…SKU-4) ship, bundle *all* webhook
  provider kits (Stripe/GitHub/Slack/Shopify + Twilio/Discord/SendGrid/PayPal) as
  the "verify any webhook" pack.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** AOV on the provider family.
  **Owner-gate:** **HARD-GATED** — depends on SKU-1…SKU-4 being built *and*
  published. Speculative (chains on un-built SKUs).

### BND-3. Founder's Everything Bundle — time-boxed tiered · bundle · (extends R6)
- **Pitch:** a time-boxed, catalog-wide anchor stacking every publish-READY dev +
  agent SKU at a launch discount vs the à-la-carte sum — to test whether a
  catalog-wide anchor converts where singles have not (0 organic sales to date).
  Named on the roadmap as R6/P-12; this is the bundle half of that pricing spec.
- **Effort:** S (spec + listing). **Risk/rev.:** medium — a public discount is a
  pricing signal that's awkward to unwind. **Unblocks:** the first deliberate
  pricing experiment. **Owner-gate:** needs-owner-decision (every price/bundle SKU
  is an owner click; the discount is an owner call).

### BND-4. Agent-Ops Starter Bundle — $79 · bundle
- **Pitch:** Agent Fleet Field Manual + Multi-Agent Control-Plane Pack +
  Owner-Click Queue Kit + Agent-Workflow Template Pack + Kill-Rule Intake Kit + the
  two merge cookbooks as one "run an autonomous coding fleet" pack — the agent-ops
  cluster's answer to the Webhook Verifier Bundle. Its lead magnet already exists
  (PR #246), so the funnel-top is live.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** AOV on the widest cluster by SKU
  count. **Owner-gate:** **HARD-GATED** on the component publishes.

### BND-5. "Merge & Ship" Cookbook Combo — $29 · bundle
- **Pitch:** the two merge cookbooks (Merge-Wall + Auto-Merge Enabler) as a
  breadth/depth pair — a small, low-friction combo that needs only two content
  publishes.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** a cheap entry bundle.
  **Owner-gate:** HARD-GATED on the two cookbook publishes (both content SKUs,
  low friction).

### BND-6. The Robustness Reading Bundle — $29 · bundle
- **Pitch:** the three discipline cookbooks (False-Green Test Trap + Idempotency &
  Retry + Merge-Wall) as a "the thinking behind the kits" reading pack — the
  content counterpart to the tool bundles.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** a content-lane AOV bump.
  **Owner-gate:** HARD-GATED on the three cookbook publishes.

### BND-7. Trilingual "First Library" board-book bundle · bundle/spec · (= R8)
- **Pitch:** already on the roadmap as R8 — bundle the 27 existing board-book texts
  (7 lines × EN/NL/DE + Comet Biscuit ×3) as a trilingual first-library box. Listed
  here for completeness; **do not duplicate R8's detail**, extend it.
- **Effort:** M. **Risk/rev.:** low (digital manifest). **Unblocks:** first
  children's-line bundle. **Owner-gate:** needs-owner-publish (digital); any
  physical POD is hard owner-gated.

### BND-8. The Writer's Starter — bundle
- **Pitch:** AI Novella Production Kit + a writing-cluster lead magnet (LM-2) as a
  "start your AI-assisted writing line" entry — pairs the one writing *tool* SKU
  with its funnel-top once LM-2 exists.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** the writing-tools cross-sell.
  **Owner-gate:** needs-owner-publish; depends on LM-2. Speculative until LM-2
  lands.

---

## AREA 3 — Free lead-magnet discovery articles (still-uncovered clusters)

> Two clusters now have a free funnel-top: **dev/api-robustness** (PR #243) and
> **agent-ops** (PR #246). The remaining uncovered clusters, per
> `docs/launch/CATALOG.md` §Cross-sell clusters, are below. Each magnet mirrors
> the proven shape (an honest, metrics-free teaching article → channel drafts →
> a CATALOG funnel-top registration; posting stays an owner paste-and-post). All
> are `can-build-autonomously` (a free article is not a publish surface — no
> OWNER-QUEUE row). This is the **highest-leverage autonomous distribution work
> left**, because the constraint is footfall.

### LM-1. Membership / boilerplate cluster lead magnet — free article
- **Pitch:** "The seven things every paid-membership site gets wrong about Stripe
  webhooks and access control" — teaches real failure modes (grace-period
  handling, webhook-driven access revocation, the double-charge on retry) and
  funnels to the Membership Kit + the live Stripe kit + the Ship-It Bundle.
- **Effort:** M. **Risk/rev.:** low, reversible. **Unblocks:** the membership
  cluster's missing funnel-top. **Owner-gate:** can-build-autonomously. **Channel
  copy status:** membership/template channel copy already exists in
  `distribution-drafts.md` — this adds the missing *teaching article*, not the
  channel drafts.

### LM-2. AI Novella / writing-tools cluster lead magnet — free article
- **Pitch:** "How to run an AI-assisted novella production line without shipping
  slop" — the honest craft-and-QA discipline behind the AI Novella Production Kit
  (structure passes, the anti-slop editing loop, the length-band check), funneling
  to the kit.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** the AI-Novella cluster's
  funnel-top. **Owner-gate:** can-build-autonomously. **Channel copy status:**
  **neither** an article nor channel drafts exist yet — this cluster is fully
  uncovered.

### LM-3. Fiction-catalog reader magnet — free first-chapter / short-story sampler
- **Pitch:** the *fiction* catalog (adult novels, YA, children's, dream series)
  has an entirely different audience from the dev/agent buyers; the reader-magnet
  pattern is a free first chapter or a standalone short story that funnels to the
  paid titles. This is the books lane's version of a lead magnet.
- **Effort:** M (curation/assembly of existing manuscript openings; a genuinely
  new short story would be L). **Risk/rev.:** low. **Unblocks:** the first
  distribution asset for the fiction catalog (which today has none). **Owner-gate:**
  can-build-autonomously for an *existing-content* sampler; a new short story is
  fine to draft but a book-catalog publish is an owner action. *Note honestly:*
  reader magnets convert on a mailing list the repo doesn't yet own (see DIST-4).

### LM-4. Photo-packs / visual-assets cluster lead magnet — free article
- **Pitch:** if the `photo-packs` cluster is intended as a sellable lane, it too
  lacks a funnel-top. A "how to use stock-style packs without the licensing
  landmines" article. *Speculative* — only worth it if photo-packs stay a live
  lane; flag for veto.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a fourth cluster's funnel-top.
  **Owner-gate:** can-build-autonomously. Marked speculative.

---

## AREA 4 — Engineering leverage (DRY / automation / honesty-enforcement)

> These pay for themselves across every future slice. Most are pure repo tooling
> with **no publish surface at all** — the safest, most reversible work on the
> whole menu, and mostly `can-build-autonomously`. ENG-2 directly machine-catches
> the exact bug class that cost the fleet two slices tonight (#244/#245).

### ENG-1. `_api-hardening-core/` extraction + `provenance_lint.py` · tooling · (= R5)
- **Pitch:** the roadmap's R5 — extract the ~70%-shared kit scaffold (allow-list
  `package.sh`, the reference-stub HTTP rig, the verdict pair, the side-effect
  counter) into a core the kits inherit, and a `provenance_lint.py` that FAILS a
  kit whose fixture lacks a pinned sha256 or a cited source. Makes kit N+1 a
  scheme-and-fixtures diff; machine-enforces the fixture-provenance honesty bar.
- **Effort:** M. **Risk/rev.:** **medium** — it refactors nine *shipped* kits, so
  there's regression risk to live-ish inventory; fully reversible as a branch.
  **Unblocks:** every future SKU-1…SKU-18 gets cheaper and more consistent.
  **Owner-gate:** **needs-owner-decision** — status.md ⚑5 already queues an owner
  yes/no on this exact refactor (regression risk vs zero pre-publish revenue).

### ENG-2. `check_catalog_drefs.py` — D-ref integrity checker · tooling · NEW tonight
- **Pitch:** machine-catch the **D-ref mispointing class that bit the fleet
  tonight** — PRs #244 and #245 were spent by hand re-syncing decision-ID
  references that silently mispointed after an OWNER-QUEUE renumber. A checker
  parses `OWNER-QUEUE.md` §1's decision→SKU map and asserts every `D-NN` reference
  in `CATALOG.md` and `candidates/*/{PROVENANCE,README,MANIFEST,vetting}` resolves
  to the *correct* SKU; advisory-warns (or fails, owner's call) on a dangling or
  mispointed ref.
- **Effort:** S–M. **Risk/rev.:** low, no publish surface. **Unblocks:** removes an
  entire recurring manual-resync tax; the next `derive_owner_queue.py` renumber
  becomes safe. **Owner-gate:** **can-build-autonomously** (highest-ROI autonomous
  item on the menu — it's a reversible checker that pays back the two slices this
  exact bug just cost).

### ENG-3. `check_funnel_coverage.py` — per-cluster funnel-top checker · tooling
- **Pitch:** the 💡 logged on the PR #246 card — a deriver that reads
  `CATALOG.md` §Cross-sell clusters and advisory-warns on any cluster with a
  singles/bundle list but no linked `*-lead-magnet.md` funnel-top. Turns "which
  cluster is the next magnet target" from a manual catalog read into a standing
  greppable signal (the membership + AI-Novella gaps LM-1/LM-2 fill would surface
  automatically).
- **Effort:** S. **Risk/rev.:** low, no publish surface. **Unblocks:** mechanizes
  the distribution-coverage roadmap. **Owner-gate:** can-build-autonomously.

### ENG-4. `check_funnel_assets.py` — per-KIT funnel-asset checker · tooling
- **Pitch:** the sibling 💡 from the PR #243 card — the per-KIT counterpart to
  ENG-3: assert every shipped kit's intake names a top-of-funnel asset. Distinct
  granularity (per-SKU vs per-cluster); could merge with ENG-3 as one checker with
  two advisories.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** funnel-completeness at the SKU
  level. **Owner-gate:** can-build-autonomously.

### ENG-5. `check_catalog_registration.py` — built-but-unregistered checker · tooling · NEW
- **Pitch:** assert every `candidates/<sku>/` dir has a `CATALOG.md` row, a
  `docs/launch/<sku>/` dir, and a vetting packet — catching the "built a SKU but
  never registered it in the storefront" drift class before it strands inventory.
- **Effort:** S–M. **Risk/rev.:** low. **Unblocks:** guarantees no built SKU is
  invisible. **Owner-gate:** can-build-autonomously.

### ENG-6. `derive_owner_queue.py` idempotence/self-test guard · tooling · NEW
- **Pitch:** a test that regenerates the owner queue twice and asserts the second
  run is a no-op *and* that no CATALOG D-ref drifted — pins the determinism the
  tonight-bug relied on breaking. Complements ENG-2 (ENG-2 catches drift after the
  fact; this prevents the regen from *introducing* it silently).
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** safe owner-queue regens.
  **Owner-gate:** can-build-autonomously.

### ENG-7. OWNER-QUEUE staleness / proofread-gate drift checker · tooling · (= PUB-9)
- **Pitch:** the overnight menu's PUB-9 — flag when a vetting packet changed but
  the derived queue wasn't regenerated, and when a proofread-gated row's gate state
  drifts from the manuscript's QA state. Extends, doesn't duplicate.
- **Effort:** S–M. **Risk/rev.:** low. **Unblocks:** trustworthy owner queue.
  **Owner-gate:** can-build-autonomously.

### ENG-8. Docs-freshness + link/orphan checker · tooling · (= OPS-5 + OPS-6)
- **Pitch:** roll the overnight menu's OPS-5 (flag stamped docs lagging main HEAD)
  and OPS-6 (dead-link + planted-set orphan check) into one advisory pass over
  `docs/`. Cheap repo hygiene that keeps the ledger honest.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** less stale-doc drift.
  **Owner-gate:** can-build-autonomously.

### ENG-9. Retire the legacy root `claims/` dir · tooling/hygiene · (= OPS-1)
- **Pitch:** OPS-1 — one claim home, not two. The root `claims/` still exists
  beside `control/claims/`; the checker already nags `claims-legacy-location`.
  Consolidate and delete the legacy dir.
- **Effort:** S. **Risk/rev.:** low, fully reversible. **Unblocks:** removes a
  standing advisory + a footgun for new sessions. **Owner-gate:**
  can-build-autonomously.

### ENG-10. Kit CI smoke-matrix consolidation · tooling · NEW
- **Pitch:** each kit ships its own CI job (`*-tests`); as the family grows this is
  N near-identical jobs. Consolidate into one matrix job that runs every kit's
  real-path suite — faster CI, one place to add kit N+1. Best paired with ENG-1.
- **Effort:** M. **Risk/rev.:** medium (touches CI config for shipped kits;
  reversible). **Unblocks:** cheaper CI as inventory grows. **Owner-gate:**
  can-build-autonomously.

---

## AREA 5 — Distribution & ops (the binding constraint)

> This is the lane that actually moves revenue, and the one the owner-gates bite
> hardest — most of it is either an owner *account* action or a spec an agent
> writes but the owner executes. I have kept the specs `can-build-autonomously`
> and marked the live-action items honestly. **DIST-3 and DIST-9 are
> time-sensitive** (kill clock tomorrow; EAP read-only in three days).

### DIST-1. Distribution playbook — consolidate the lead-magnet pattern · spec · NEW
- **Pitch:** a single `docs/launch/DISTRIBUTION-PLAYBOOK.md` that names the now-proven
  repeatable recipe (teaching article → channel drafts → CATALOG funnel-top
  registration → owner paste-and-post), so the next cluster magnet is fill-in-the-
  blank instead of re-derived. Distils what PRs #243/#246 did by hand into a
  template + a checklist.
- **Effort:** S–M. **Risk/rev.:** low, docs-only. **Unblocks:** every future LM-*;
  turns distribution into a rinse-repeat. **Owner-gate:** can-build-autonomously.

### DIST-2. "Owner publish hour" sequencer · spec/tool · (extends OWNER-LAUNCH-HOUR.md)
- **Pitch:** extend `docs/launch/OWNER-LAUNCH-HOUR.md` into a generated,
  copy-paste-ordered click-run — for each queued publish, the exact listing title,
  description, price, and file, in the sequence that unlocks bundles earliest — so
  the owner's finite pre-cutover attention converts to the most live listings per
  minute.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** faster owner throughput on the
  283-ish queued clicks. **Owner-gate:** can-build-autonomously (the build is the
  sequencer; the clicks stay owner-only).

### DIST-3. "Why zero sales" funnel diagnostic — live Stripe kit · spec · (= REV-2) · TIME-SENSITIVE
- **Pitch:** REV-2 — before the T+7 checkpoint (**2026-07-19, tomorrow**) and the
  T+14 kill-rule (2026-07-26), an honest diagnostic of the one live listing's
  funnel: is it a traffic problem, a listing-copy problem, or a price problem, and
  what's the cheapest test of each. The one piece of analysis directly tied to a
  live revenue decision.
- **Effort:** S–M. **Risk/rev.:** low (a diagnostic doc, no live change).
  **Unblocks:** an evidence-based keep/kill/iterate call on the live SKU.
  **Owner-gate:** can-build-autonomously; any listing edit is an owner click.

### DIST-4. Conversion-tracking / UTM + email-capture spec · spec · (= REV-3 + REV-5)
- **Pitch:** a spec for the instrumentation the funnel currently lacks — UTM tags
  across channel links, an email-capture on the lead magnets (so LM-3's reader
  magnet has somewhere to convert), and the minimal analytics to tell whether a
  post drove a visit. Rolls REV-3 and the capture half of REV-5.
- **Effort:** M. **Risk/rev.:** low (spec). **Unblocks:** the ability to *measure*
  distribution at all — precondition for iterating it. **Owner-gate:**
  needs-owner-decision (an email tool / analytics account is an owner spend/setup
  call).

### DIST-5. Static catalog landing microsite · spec + build · (= REV-4)
- **Pitch:** REV-4 — a static, self-hosted, agent-buildable one-page site that
  presents the whole catalog with the cross-sell clusters, so channel posts have a
  single branded destination instead of N Gumroad links. Buildable now as static
  HTML in-repo.
- **Effort:** M–L. **Risk/rev.:** low (static files). **Unblocks:** a real
  storefront hub; SEO surface. **Owner-gate:** needs-owner-publish (hosting/domain
  is an owner step; the site is agent-buildable).

### DIST-6. Launch-kit — Product Hunt / HN / Reddit playbook · spec · (= REV-5)
- **Pitch:** REV-5 — the ready-to-paste launch assets (PH tagline/gallery copy, an
  HN Show-HN post, subreddit-specific teasers) for a coordinated launch of the dev
  cluster, honest and self-promotion-rules-aware. The channel drafts exist per
  cluster; this is the *coordinated launch* layer above them.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a single high-visibility launch
  moment. **Owner-gate:** needs-owner-publish (posting is owner-only OWNER-ACTION).

### DIST-7. Cross-sell hub / storefront consolidation · spec · (= REV-8)
- **Pitch:** REV-8 — the storefront-side consolidation of the dev-tool family
  (consistent naming, cross-links, the bundle-anchor placement) so the catalog
  reads as one product line, not 18 orphans. Overlaps DIST-5; could be its content
  layer.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** coherent catalog presentation.
  **Owner-gate:** needs-owner-publish for the live storefront edits.

### DIST-8. Real-Stripe-path / payment test-harness spec · spec · (= REV-1)
- **Pitch:** REV-1 — the ORDER 003 real-Stripe-path spec + vendored-payload test
  harness, kept plan-only (the ⚑B/⚑D unfreeze). Named here for completeness;
  extend REV-1, don't restate. Only relevant if a live payment integration is on
  the table.
- **Effort:** M. **Risk/rev.:** medium (touches the payment path design).
  **Unblocks:** a real checkout beyond Gumroad. **Owner-gate:** needs-owner-decision
  + spend. Speculative — lowest distribution priority.

### DIST-9. Pre-EAP-read-only publish sprint plan · spec · NEW · TIME-SENSITIVE
- **Pitch:** the EAP goes **read-only 2026-07-21** (three days). Repo *work* must
  land before then; owner *clicks* don't need the seat but compete for finite
  owner attention. A one-page plan that (a) lists the must-land-before-cutover
  agent work in priority order and (b) front-loads the owner's highest-leverage
  publish clicks (the webhook trio → bundle unlock) into a single pre-cutover
  session. The honest "what happens to autonomy on the 21st" planning the repo
  needs now.
- **Effort:** S. **Risk/rev.:** low (a plan). **Unblocks:** an orderly wind-down
  instead of a scramble. **Owner-gate:** can-build-autonomously (plan); the clicks
  are owner-only.

---

## AREA 6 — Book / writing catalog path

> **Honesty gate up front (repo rule):** the binding lever on almost every NL/DE
> book edition is the **owner-only native-speaker proofread pass**. An AI can
> *draft* the translation and *tool* the gate (spellcheck-in-CI, length-band
> checks, a structured correction packet) but **cannot clear the gate** — a
> native-speaker read is the owner's, and 19+ OWNER-QUEUE rows hard-depend on it.
> So the writing lane splits into "agent drafts, owner proofreads" (BOOK-1…BOOK-5)
> and "agent tools the gate so the owner's pass is faster" (BOOK-6). I rank the
> tooling high because it's the only writing work that moves the gated cluster
> *without* owning the gate.

### BOOK-1. The Salt Bell — NL edition (*De zoute klok*) · writing · (= R10)
- **Pitch:** R10 — the single highest NL-market-fit title (Zeeland, the 1953
  Watersnoodramp; core Dutch national memory). EN packet exists (PR #211); the NL
  title is pre-named. Agent drafts the full manuscript.
- **Effort:** L (a real full-length adaptation). **Risk/rev.:** low to draft,
  reversible. **Unblocks:** the most obvious NL revenue gap; a bilingual listing.
  **Owner-gate:** **needs-owner-proofread** (the binding lever; ranked by the
  roadmap as slowest despite highest value).

### BOOK-2. The Wire Garden — NL edition · writing · (= P-6)
- **Pitch:** P-6 — NL edition of The Wire Garden (*Een novelle van de
  Dodendraad*). Agent drafts; same proofread gate.
- **Effort:** L. **Risk/rev.:** low to draft. **Unblocks:** a second NL adult
  title. **Owner-gate:** needs-owner-proofread.

### BOOK-3. The Paper Orange — DE edition · writing · (= P-8)
- **Pitch:** P-8 — the biggest reach and most sensitive subject; a German edition
  of The Paper Orange. Agent drafts to a careful, subject-aware draft.
- **Effort:** L. **Risk/rev.:** medium (sensitive subject demands the proofread be
  a real editorial pass, not a rubber stamp). **Unblocks:** the DE market.
  **Owner-gate:** needs-owner-proofread (native DE, the hardest to source).

### BOOK-4. The Night Kiln — NL omnibus (*De Nachtoven* box set) · writing · (= R9)
- **Pitch:** R9 — assemble the NL omnibus from the three already-complete,
  already-QA'd NL manuscripts; EN omnibus is the working template. Pure
  recombination.
- **Effort:** S–M. **Risk/rev.:** low. **Unblocks:** a higher-AOV NL listing off
  a completed trilogy. **Owner-gate:** **softened** — components already carry
  their proofread state; the omnibus adds only front/back-matter to clear. Also
  waits on the LENGTH-BAND-PREP one-word ratify (status.md ⚑3). The *most
  shippable* book item on the menu.

### BOOK-5. YA line — first NL edition pilot · writing · (= P-7)
- **Pitch:** P-7 — one YA title as the first-NL pilot, to test the YA-in-NL funnel
  before batch-translating the line.
- **Effort:** M–L. **Risk/rev.:** low to draft. **Unblocks:** the YA-NL lane.
  **Owner-gate:** needs-owner-proofread.

### BOOK-6. Native-speaker proofread TOOLING · tooling · (= PUB-1 + PUB-6 + PUB-7)
- **Pitch:** the highest-leverage way to move the whole gated book cluster *without*
  owning the gate: NL/EN spellcheck-in-CI (PUB-1/PUB-2), a length-band / expansion-
  ratio checker (PUB-6), and a structured proofread-packet + correction-capture
  format (PUB-7) so the owner's native-speaker pass is a fast, structured review
  instead of a cold full read. Rolls three overnight-menu PUB items into one
  gate-tooling slice.
- **Effort:** M. **Risk/rev.:** low, tooling-only. **Unblocks:** faster clearance
  of every proofread-gated row. **Owner-gate:** can-build-autonomously (it *tools*
  the gate; it does not clear it — the honest distinction).

### BOOK-7. Next adult-novella writes from the ideation batch · writing · (extends the 2026-07-14 batch)
- **Pitch:** the `2026-07-14-adult-title-concepts.md` batch ranked five concepts;
  the top (Sweetwater Sea) is written. Concepts 2–5 (The Wire Garden already
  exists; The Wire Garden note aside) are the next generative write-sessions — new
  EN manuscripts, no translation gate.
- **Effort:** L each. **Risk/rev.:** low to draft. **Unblocks:** EN fiction
  inventory. **Owner-gate:** can-build-autonomously to draft; a book publish is an
  owner action. *Note:* generative fiction is the least distribution-constrained-
  aware item here — build only if the fiction funnel (LM-3/DIST-4) exists to catch
  it.

### BOOK-8. Audiobook / narration-ready editions — extend beyond the two lead titles · spec · (extends P-9)
- **Pitch:** P-9's audio-edition spec is built for two lead titles (Paper Orange,
  Night Kiln); extend the same narration-ready spec across more of the catalog.
- **Effort:** S–M per title. **Risk/rev.:** low. **Unblocks:** an audio lane.
  **Owner-gate:** can-build-autonomously for the spec; narration/production is an
  owner spend. NL narration also waits on the LENGTH-BAND-PREP ratify (⚑3).

### BOOK-9. Book-catalog revenue path — KDP-first spec · spec · (= REV-7)
- **Pitch:** REV-7 — the KDP-first publishing spec with a Leanpub/serialization/
  newsletter fork, so the fiction catalog has a *channel* strategy distinct from
  the Gumroad dev-tool one. Precondition for any book actually earning.
- **Effort:** M. **Risk/rev.:** low (spec). **Unblocks:** the whole book revenue
  path. **Owner-gate:** needs-owner-decision (KDP account + the publish model is
  an owner call).

---

## AREA 7 — Anything else worth the owner's consideration

### MISC-1. Fresh-seat boot hardening for the post-EAP repo · hygiene · NEW
- **Pitch:** `current-state.md` says the owner is winding autonomy down and may
  recreate projects fresh, wanting the repo "clean enough that a fresh seat boots
  from the repo alone." A slice that verifies exactly that — one canonical
  START-HERE path (OPS-8), no dead trigger IDs, no EAP-ceremony a new seat must
  reconstruct.
- **Effort:** M. **Risk/rev.:** low. **Unblocks:** a clean relaunch. **Owner-gate:**
  can-build-autonomously.

### MISC-2. Pricing-experiment spec (PWYW floor + anchor) · spec · (= R6)
- **Pitch:** R6 — launch the AI Novella Kit as PWYW with a $19 floor to buy
  first-sale signal on the writing channel, plus the Founder's Everything anchor
  (BND-3). Referenced, not duplicated.
- **Effort:** S. **Risk/rev.:** medium (pricing signal). **Unblocks:** first
  deliberate pricing test. **Owner-gate:** needs-owner-decision (price edits are
  owner clicks).

### MISC-3. Live-SKU kill-clock decision packet · spec · NEW · TIME-SENSITIVE
- **Pitch:** the Stripe kit's T+14 kill rule fires **2026-07-26**. A pre-written
  decision packet (the rule, the evidence to check, the keep/iterate/delist
  options with their consequences) so the owner's call at the clock is a
  two-minute read, not a cold re-derivation. Pairs with DIST-3.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** a clean kill-clock decision.
  **Owner-gate:** can-build-autonomously; the decision is owner-only.

### MISC-4. Owner-postable catalog one-pager · asset · NEW
- **Pitch:** a single copy-paste block (the catalog, the clusters, the bundle
  anchors, the honest positioning) the owner can post as-is to a personal
  channel/newsletter — the lowest-effort distribution asset, requiring zero setup.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** an instant owner-channel post.
  **Owner-gate:** needs-owner-publish (owner posts it).

### MISC-5. Planning-doc conveyor consolidation · hygiene · NEW
- **Pitch:** three planning docs now stand (the two prior + this one). Per the
  `docs/ideas/README.md` "conveyor, not a graveyard" convention, a periodic sweep
  that reconciles them — mark shipped items, retire dead ones, keep one live index
  — so a future session doesn't re-derive a false "backlog dry" line. This doc's
  "how this relates" section is the manual version; a checker could keep it fresh.
- **Effort:** S. **Risk/rev.:** low. **Unblocks:** a self-maintaining backlog.
  **Owner-gate:** can-build-autonomously.

### MISC-6. Trading cross-ref (scope note only — NOT built here)
- **Pitch:** trading landed #152 (cross-round meta-analysis) tonight. The pattern
  — a periodic meta-analysis over prior rounds — could inform a venture-side
  "retro cadence over shipped slices," but **trading planning is a separate
  repo/PR** and this menu is scoped to **venture**. Logged as a cross-ref only; no
  venture work proposed against it tonight beyond the note. **Owner-gate:** n/a
  (cross-ref).

---

## What I deliberately did NOT build tonight, and why

Honest disclosure, per the repo's honesty bar:

- **None of the proposals above** — this slice is **planning-only** by the owner's
  directive ("move over to planning… plan excessively"). I built the *menu*, not
  the menu's items. The one thing I did *build* is this document + its control
  scaffolding.
- **No new SKU, bundle, lead magnet, checker, or book edition** — even the
  `can-build-autonomously` ones (LM-1, LM-2, ENG-2, BOOK-4) are left for **other
  slices**. The task scoped small reversible builds to *other* slices, not this
  one; landing a checker or a magnet here would blur a clean planning diff.
- **No pre-filtering to a shortlist** — deliberately. The owner asked for the full
  field so the *veto* is the filter. I resisted the instinct to cut to "the five
  safe picks," which is why the SKU lane is long even though I flag honestly that
  it does not move revenue.
- **No fabricated demand evidence** — no "N developers want this," no invented
  conversion numbers, no fake testimonials. Where I judged fit, I said "value:
  high/med" as *my* estimate and marked the genuinely speculative ones (SKU-9,
  LM-4, DIST-8, BOOK-7) as speculative.
- **No OWNER-QUEUE regen and no §7 vetting packet** — a planning doc adds no
  publish surface, so (unlike a SKU slice) it must not renumber decisions or add a
  queue row. This keeps the diff to the planning doc + control scaffolding only.
- **No trading-repo work** — scoped to venture per the task; trading planning is a
  separate repo/PR (see MISC-6).

## Provenance

Derived from the repo at `main@661ffce`, no fabricated metrics:

- Built-vs-open SKU/bundle status, prices, cluster map, publish order, the live-SKU
  kill clock — `docs/launch/CATALOG.md`, `docs/publishing/OWNER-QUEUE.md`.
- The distribution-is-the-constraint framing, the EAP read-only 2026-07-21 wind-down,
  the ~18-publish-READY count — `docs/current-state.md`.
- The R1–R10 pipeline and which of R1/R2/R3/R4/R7 shipped — `docs/ideas/2026-07-18-next-wave-roadmap.md`
  + `control/status.md` (today's #231–#246 merge list).
- The P/PUB/REV/OPS raw candidate pool this doc extends — `docs/ideas/2026-07-17-overnight-menu.md`.
- The two funnel-coverage checker 💡s (ENG-3/ENG-4) — the session cards
  `.sessions/2026-07-18-agent-ops-lead-magnet.md` and `.sessions/2026-07-18-api-robustness-lead-magnet.md`.
- The D-ref mispointing incident that motivates ENG-2/ENG-6 — PRs #244/#245 as
  recorded in `control/status.md`.
- The native-speaker proofread gate as the binding lever on the book lane, and the
  LENGTH-BAND-PREP / proofread owner items — `control/status.md` ⚑ owner-queue + `docs/current-state.md`.
- The adult-novella concept batch (BOOK-7) — `docs/ideas/2026-07-14-adult-title-concepts.md`.
