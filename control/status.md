# Venture Lab — status log (neutral snapshot)
updated: 2026-07-19T00:12:00Z

> The `control/*` manager↔lane message-bus remains **retired**. This file is a
> neutral status pointer, not a source of truth. The successor reads
> [`../docs/current-state.md`](../docs/current-state.md),
> [`../docs/NEXT-TASKS.md`](../docs/NEXT-TASKS.md),
> [`../docs/launch/CATALOG.md`](../docs/launch/CATALOG.md), and
> [`../docs/ideas/2026-07-18-next-wave-roadmap.md`](../docs/ideas/2026-07-18-next-wave-roadmap.md).

**Session CLOSED 2026-07-18** by the owner-pasted v3.8 session ender (coordinator
chat). This seat is released; the `control/*` bus stays retired.

**Routine disposition:**
- All seat routines closed per the v3.8 ender; zero routines remain for this
  seat. Trigger ids are recorded in the coordinator session and team memory, not
  carried in-repo. The successor's failsafe is re-armed by the next startup
  paste, not carried over.

**Day's merged PRs (this seat, all merged green):**
- Last night `#219`–`#228` — docs restamp/reconcile, routine record, ORDER 016,
  Slack Kit, Auto-Merge Cookbook, Night Kiln EN omnibus spec, Paper Orange audio
  spec, Night Kiln audio spec, Shopify Kit.
- Today `#231`–`#240` — Webhook Verifier Bundle, storefront CATALOG, Idempotency
  Key Kit, next-wave roadmap, Paper Orange back-matter, Rate-Limit Kit,
  Pagination Kit, JWT Auth Kit, API Robustness Bundle, Idempotency & Retry
  Cookbook.
- `#229`/`#230` were other-session PRs (owner doctrine correction + pycache
  cleanup), not this seat.
- Pointer: trading-strategy `#141`–`#151` landed in its own repo.

**In flight (later seat, 2026-07-18, ORDER 016 — new sellable):**
- PR #242 (`claude/cors-preflight-test-kit`) adds a NEW dev-tool SKU — **CORS
  Preflight Test Kit $29** — at `candidates/cors-preflight-test-kit/` (stdlib-only
  `cptk.py`+`cptk.js` harness, correct/naive reference stubs, 37-test HTTP
  real-path suite, byte-reproducible bundle). Vetting packet at
  `docs/publishing/vetting/cors-preflight-test-kit.md`, launch assets at
  `docs/launch/cors-preflight-test-kit/`, CATALOG row added, and a
  `cors-preflight-test-kit-tests` CI job. Publish stays owner-queued (§7 of the
  packet); the seat performed no publish/spend/account action. OWNER-QUEUE.md was
  NOT regenerated in this PR (it renumbers shared decision IDs) — running
  `scripts/derive_owner_queue.py` to fold this packet in is a follow-up.

**In flight (later seat, 2026-07-18 — distribution-first, no new SKU):**
- PR #243 (`claude/api-robustness-lead-magnet`) adds a FREE top-of-funnel
  discovery asset for the webhook + API-robustness test-kit cluster — NOT a new
  sellable. New `docs/launch/api-robustness-lead-magnet.md` (a dev.to/Hashnode/
  Show-HN-ready article teaching six real failure modes: replay-unsafe webhook
  handlers, missing signature verification, retry storms, offset-pagination
  drift, a 429 with no Retry-After, the CORS/Authorization footgun; soft honest
  funnel — bundles first, then singles). Dev-cluster channel drafts appended to
  `docs/launch/distribution-drafts.md`; the article registered as the
  dev-cluster funnel-top asset in `docs/launch/CATALOG.md`. Folded in an honest
  stale-count fix in `docs/current-state.md` (Products/revenue "10 publish-READY"
  → 18, citing CATALOG.md as the fresh source). Docs/markdown-only, reversible;
  no OWNER-QUEUE row (a free article is not a publish surface). Posting stays an
  owner paste-and-post (OWNER-ACTION) — the seat performed no publish/spend/
  account action.

**In flight (later seat, 2026-07-18 — owner-queue CORS fold, banks PR #242):**
- PR #244 (`claude/owner-queue-cors-fold`) folds the **CORS Preflight Test Kit**
  (merged in PR #242, ORDER 016) into `docs/publishing/OWNER-QUEUE.md`, which PR
  #242 had left as an explicit follow-up because the derive script renumbers
  shared decision IDs. Regenerated the queue with `scripts/derive_owner_queue.py`
  (the on-main CORS vetting packet derives as new decision **D4**; every
  alphabetically-later decision shifts +1, D4→D5 … D27→D28; 28 decisions, was 27;
  58/58 inputs clean, deterministic). Resynced every renumbered D-ref in
  `docs/launch/CATALOG.md` (comparison table, per-SKU headers, bundle gates,
  cross-sell, publish order, and the sourcing/provenance notes) so each resolves
  to the correct SKU — all 19 table D-refs + 19 positioning headers verified
  against the regenerated queue; no dangling or wrong D-ref remains. Docs-only,
  reversible; no packet edited (the packet is the source of truth). The seat
  performed no publish/spend/account action — the CORS publish is now an
  owner-actionable click at D4. Pre-existing note: some `candidates/*/PROVENANCE.md`
  D-refs were already stale on main and are out of this slice's scope.

**In flight (later seat, 2026-07-18 — bundle D-ref resync, follows PR #244):**
- PR #245 (`claude/bundle-dref-resync`) resyncs the two sellable-bundle doc
  families whose D-ref cross-references were left stale after PR #244's CORS fold
  renumber (they had mispointed to the wrong SKUs' owner-queue rows). Fixed
  against the live `OWNER-QUEUE.md` §1 map: api-robustness-bundle Idempotency
  D6→D7 / JWT D7→D9 / Pagination D13→D15 / Rate-Limit D16→D18, and
  webhook-verifier-bundle GitHub D5→D6 / Slack D14→D20 / Shopify D13→D19, across
  each family's owner-actions, listing-copy, vetting packet, MANIFEST.json,
  README.md, and PROVENANCE.md. `OWNER-QUEUE.md` was REGENERATED via
  `scripts/derive_owner_queue.py` (the vetting packets are the queue's source, so
  the §7 fix un-stales the queue's own §2 bundle click-run rows); §1 numbering is
  unchanged (D1–D28, CORS still D4) and CATALOG.md's D-refs still all resolve.
  Also fixed the one `scripts/lint_owner_gates.py` FAIL — a stray `— DONE` marker
  on the UNCHECKED Shopify owner box (no owner action falsely marked done).
  Docs-only, reversible; the seat performed no publish/spend/account action. The
  `candidates/*/PROVENANCE.md` staleness noted above is resolved by this PR.

**In flight (later seat, 2026-07-18 — distribution-first, no new SKU):**
- PR #246 (`claude/agent-ops-lead-magnet`) adds a FREE top-of-funnel discovery
  asset for the **agent-ops / fleet cluster** (the next uncovered cluster after
  PR #243 gave the dev/webhook + API-robustness cluster its lead magnet) — NOT a
  new sellable. New `docs/launch/agent-ops-lead-magnet.md` (a dev.to/Hashnode/
  Show-HN-ready article teaching six real fleet-operating failures: "tests pass"
  when the check never ran the code, work that self-certifies done, parallel
  sessions colliding on shared state, the green PR that can't self-merge, the
  ungated spend/publish, and the beautifully-built undiscoverable artifact — each
  with its mechanical gate; soft honest funnel — Agent Fleet Field Manual umbrella
  first, then the supporting SKUs mapped to each failure). Agent-ops-cluster
  channel drafts appended to `docs/launch/distribution-drafts.md` (existing
  sections untouched); the article registered as the agent-ops-cluster funnel-top
  asset in `docs/launch/CATALOG.md` (dev-cluster funnel-top row format). Docs/
  markdown-only, reversible; no OWNER-QUEUE row (a free article is not a publish
  surface). Posting stays an owner paste-and-post (OWNER-ACTION) — the seat
  performed no publish/spend/account action. Distribution-first justification for
  the cluster pick is in the PR body.

**In flight (later seat, 2026-07-18 — planning-only, owner morning deliverable):**
- PR #247 (`claude/veto-ready-menu`) adds a single planning doc,
  `docs/ideas/2026-07-18-veto-ready-menu.md` — the owner-morning veto-ready menu
  for the 2026-07-18 overnight directive ("plan excessively… my veto is the
  filter, don't pre-filter to a few safe picks"). ~55 distinct venture proposals
  across seven areas (new SKUs · bundles · lead magnets · engineering leverage ·
  distribution/ops · book/writing path · misc), each with pitch · S/M/L ·
  risk/reversibility · what-it-unblocks · owner-gate status. REFERENCES and
  EXTENDS the next-wave roadmap (R1–R10, marking R1–R4/R7 shipped) and the
  overnight menu (P/PUB/REV/OPS) rather than duplicating them; linked into
  `docs/ideas/README.md` per the conveyor convention. Scoped to venture (trading
  planning is a separate repo/PR). Planning-only — no SKU, no publish surface, no
  OWNER-QUEUE row; the seat performed no publish/spend/account action. Diff is the
  menu doc + README link + control scaffolding (claim/card/this heartbeat) only.

**In flight (later seat, 2026-07-18 — engineering guard, no new SKU):**
- PR #248 (`claude/dref-regression-guard`) adds a stdlib checker
  `scripts/check_catalog_drefs.py` + `scripts/test_check_catalog_drefs.py`,
  wired into `.github/workflows/kit-tests.yml` as a required `catalog-dref-guard`
  job. It builds the live decision-ID → SKU map from `docs/publishing/OWNER-QUEUE.md`
  §1 headers (the source of truth) and asserts every allowlisted LIVE D-ref
  cross-reference (CATALOG + the two bundle families) both resolves to an existing
  decision and points at the SKU its surrounding context names — machine-catching
  the OWNER-QUEUE renumber-mispoint class that shipped green in PR #244 and was
  hand-resynced in PR #245 (`bootstrap --strict` is semantic-blind to cross-refs).
  Scoping is allowlist-based: frozen snapshots (`.sessions/*`, `control/inbox.md`/
  `outbox.md`, `docs/NEXT-*.md`, `docs/current-state.md`) are history and out of
  scope; renumber-arrow / decision-range lines are skipped inside live files. On
  the current tree all 163 cross-refs resolve — no real mispoint found (the #245
  fix holds). No packet/queue edited (OWNER-QUEUE is read-only authority); the
  seat performed no publish/spend/account action. Diff is scripts/ + test + the one
  CI job + claim/card + this heartbeat only.

**In flight (later seat, 2026-07-18 — distribution-first, no new SKU):**
- PR #249 (`claude/dist-1-distribution-playbook`) adds a reusable
  `docs/launch/DISTRIBUTION-PLAYBOOK.md` — NOT a new sellable and NOT a new
  article. It distils the recipe PRs #243 and #246 each ran by hand (teaching
  article → channel drafts in `distribution-drafts.md` → CATALOG funnel-top
  registration → owner paste-and-post) into one fill-in-the-blank playbook: a
  step-by-step template, a copy-paste skeleton for a new
  `docs/launch/<cluster>-lead-magnet.md`, a pre-publish checklist, and an
  OWNER-ACTION handoff that stops at paste-ready (owner-gated publishing — the
  doc never auto-publishes). Linked from `docs/launch/README.md` (Cross-product)
  so the docs-gate reaches it; #243/#246 cited as the worked examples. Docs/
  markdown-only, reversible; no OWNER-QUEUE row (a playbook is not a publish
  surface). Posting stays an owner paste-and-post (OWNER-ACTION) — the seat
  performed no publish/spend/account action.

**In flight (later seat, 2026-07-18 — distribution-first, no new SKU) — LM-1:**
- PR #250 (`claude/lm-1-membership-lead-magnet`) adds a FREE top-of-funnel
  discovery asset for the **membership / boilerplate cluster** (the last uncovered
  cluster after PR #243 gave the dev/webhook + API-robustness cluster its magnet
  and PR #246 gave the agent-ops / fleet cluster its own) — NOT a new sellable.
  New `docs/launch/membership-lead-magnet.md`, a dev.to/Hashnode/Show-HN-ready
  article titled "The seven things every paid-membership site gets wrong about
  Stripe webhooks and access control," teaching seven real membership/Stripe
  failure modes (unverified webhook grants, double-grant on retry, instant revoke
  with no grace period, boolean access vs. derived subscription state, revocation
  riding on a single droppable webhook, out-of-order re-grants, keying membership
  off the email), each as The failure. / Why it bites in production. / The fix.,
  with a soft honest footer funnelling to the Ship-It Bundle then the
  Membership-Site Boilerplate Kit + Stripe Webhook Test Kit then The False-Green
  Test Trap. Built from `docs/launch/DISTRIBUTION-PLAYBOOK.md` (PR #249). Channel
  drafts already in `docs/launch/distribution-drafts.md` are cross-referenced, NOT
  duplicated (one-writer discipline); one Cross-product index link added in
  `docs/launch/README.md` so the docs-gate reaches the article. Docs/markdown-only,
  reversible; no OWNER-QUEUE row (a free article is not a publish surface).
  Posting stays an owner paste-and-post (OWNER-ACTION) — the seat performed no
  publish/spend/account action.

**In flight (later seat, 2026-07-18 — distribution-first, no new SKU) — LM-2:**
- PR #251 (`claude/lm-2-ai-novella-lead-magnet`) adds a FREE top-of-funnel
  discovery asset for the **AI-Novella / writing-tools cluster** (the last fully
  uncovered cluster — no funnel-top article and no channel drafts existed for it,
  after PR #243/#246/#250 covered the dev, agent-ops, and membership clusters) —
  NOT a new sellable. New `docs/launch/ai-novella-lead-magnet.md`, a
  dev.to/Hashnode/Medium/Show-HN-ready article titled "How to run an AI-assisted
  novella production line without shipping slop," teaching seven real craft-and-QA
  failure modes (no declared length band, no structure pass, infinite-rewrite
  editing vs. one aimed repair pass, no mechanical promise-manifest check,
  continuity drift with canon only in the last session, unrecoverable crashed
  sessions, and shipping "a draft exists" as "publishable"), each as The failure.
  / Why it bites. / The fix., with a soft honest footer funnelling to the AI
  Novella Production Kit ($29, READY, D2). Built from
  `docs/launch/DISTRIBUTION-PLAYBOOK.md` (PR #249). One Cross-product index link
  added in `docs/launch/README.md` so the docs-gate reaches the article; the
  cluster had no existing channel drafts, so this slice ships the funnel-top
  article only. Docs/markdown-only, reversible; no OWNER-QUEUE row (a free article
  is not a publish surface). Posting stays an owner paste-and-post (OWNER-ACTION) —
  the seat performed no publish/spend/account action.

**In flight (later seat, 2026-07-18 — diagnostic, no new SKU) — DIST-3 / REV-2:**
- PR #252 (`claude/dist-3-funnel-diagnostic`) adds a single diagnostic doc,
  `docs/launch/funnel-diagnostic.md` — an honest, repo-grounded read of *why the
  one LIVE listing (Stripe Webhook Test Kit, $29, live on Gumroad since
  2026-07-12) has zero organic sales*, written for tomorrow's **T+7 checkpoint
  (2026-07-19)** and the **T+14 kill rule (2026-07-26)**. It separates the three
  candidate causes — **traffic vs listing-copy vs price** — grounds each in repo
  evidence (`LAUNCH-LOG.md`, `CATALOG.md`, `LISTING.md`), and gives the cheapest
  owner-executed test of each in a "what the owner would click" section
  (owner-action, never auto-executed). No invented metrics: Gumroad views/sales
  are owner-dashboard-only and agent surfaces do not see them, so unmeasured
  funnel stages are marked "not measured (owner-dashboard-only)" with the cheapest
  way to measure, never guessed. One Cross-product index link added in
  `docs/launch/README.md` so the docs-gate reaches it. Pairs with the upcoming
  MISC-3 live-SKU kill-clock decision packet. Docs/markdown-only, reversible; no
  live change, no listing edit, no OWNER-QUEUE row — the seat performed no
  publish/spend/account action.

**In flight (later seat, 2026-07-18 — decision packet, no new SKU) — MISC-3:**
- PR #253 (`claude/misc-3-kill-clock-packet`) adds a single decision doc,
  `docs/launch/kill-clock-decision-packet.md` — a pre-written **keep / iterate /
  delist** decision packet for the live Stripe Webhook Test Kit ($29)'s **T+14
  kill-clock call (2026-07-26)**, so the owner's decision is a two-minute read,
  not a cold re-derivation. It carries the kill rule **quoted verbatim** from
  `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md` (signal = ≥1 organic sale
  OR ≥1 qualified inbound by 2026-07-26, else ledger ⚑E NEGATIVE + pause/delist),
  the exact evidence to check before deciding (pointing at the DIST-3 funnel
  diagnostic's traffic-vs-copy-vs-price hypotheses, #252), each option with its
  concrete consequences, and an owner-only action checklist. Consumes, does NOT
  duplicate, `docs/launch/funnel-diagnostic.md` (#252). No invented metrics —
  Gumroad views/sales are owner-dashboard-only, so unmeasured data is marked "not
  measured (owner-dashboard-only)", never guessed. One Cross-product index link
  added in `docs/launch/README.md` so the docs-gate reaches it. The decision is
  owner-only, never auto-executed. Docs/markdown-only, reversible; no live change,
  no listing edit, no price change, no OWNER-QUEUE row — the seat performed no
  publish/spend/account action.

**In flight (later seat, 2026-07-18 — docs ledger refresh, no new SKU):**
- PR #254 (`claude/current-state-refresh`) refreshes the stale
  `docs/current-state.md` state ledger to current HEAD. Before: stamped
  2026-07-17 at HEAD `9edfcba` / PR #218, still citing the 38-proposal overnight
  menu as the standing backlog — ~7 merges behind. After: restamped 2026-07-18 to
  HEAD `7d5229f` / PR #253, with the **64-item** veto-ready menu (#247) as the
  standing backlog and #242 + #246–#253 in Recently-shipped (one honest line
  each). Counts re-verified against the tree: 1 LIVE + 19 READY SKUs + 3 bundles
  (CORS Preflight Kit #242 is the new SKU), 28 OWNER-QUEUE decisions, four
  lead-magnet funnel-tops + `DISTRIBUTION-PLAYBOOK.md` (#249), the required
  `catalog-dref-guard` job (#248). Docs-only, reversible; no SKU, no publish
  surface, no OWNER-QUEUE renumber; the seat performed no publish/spend/account
  action. `control/inbox.md` untouched.

**In flight (later seat, 2026-07-19 — planning-only, TIME-SENSITIVE) — DIST-9:**
- PR #255 (`claude/dist-9-pre-eap-sprint-plan`) adds a single planning doc,
  `docs/launch/pre-eap-sprint-plan.md` — a one-page wind-down plan for the ~2
  days of write access before the **2026-07-21 EAP read-only cutover**. It splits
  **AGENT-LANDS-THESE** (repo work that needs the write seat, in priority order:
  DIST-9 itself, the DIST-2 owner-publish-hour sequencer, BOOK-6 proofread
  tooling, DIST-5 microsite — all owner-veto-filtered, none pre-approved) from
  **OWNER-CLICKS-THESE** (publish clicks that survive the cutover but compete for
  owner attention — the webhook trio GitHub D6 / Slack D20 / Shopify D19 →
  Webhook Verifier Bundle unlock, then the API-robustness four → API Robustness
  Bundle, then membership D11 + template-pack D21 → Ship-It Bundle — batched into
  one pre-cutover session, mirroring CATALOG's advisory publish order). Honest
  about what read-only means for autonomy (no repo landing; owner clicks still
  work) and about the real freeze/gate state: ⚑B/⚑D were UNFROZEN 2026-07-11
  (ORDER 003 real-path gate PR #16 `912da3e`; inbox stays `status: new` by the
  append-only protocol, not a live freeze), while native-speaker proofread /
  LENGTH-BAND-PREP / R5 stay owner-only. Grounded in #254 and the live
  OWNER-QUEUE; no invented deadlines or metrics. One Cross-product index link in
  `docs/launch/README.md` for the docs-gate. Planning/docs-only, reversible; no
  SKU, no publish surface, no OWNER-QUEUE row; the seat performed no
  publish/spend/account action. `control/inbox.md` untouched.

**⚑ Owner-queue (paste-ready, all owner-only):**
1. ~8 publish clicks — nothing live yet — per
   [`../docs/publishing/OWNER-QUEUE.md`](../docs/publishing/OWNER-QUEUE.md)
   (authoritative; decisions renumber on insert). The 2 bundles auto-unblock once
   their components publish.
2. Delete leftover remote branch `probe/push-access-check-2026-07-17` (agents are
   403-walled on branch delete).
3. LENGTH-BAND-PREP one-word ratify (unblocks Night Kiln NL omnibus + NL
   narration).
4. Native-speaker NL proofread (unblocks Salt Bell / Wire Garden NL editions).
5. R5 yes/no — authorize/decline the `_api-hardening-core` refactor of the 8
   shipped kits.

**Next-2 (baton):**
1. R5 `_api-hardening-core` extraction — PENDING owner nod (regression risk to
   shipped kits, zero revenue pre-publish).
2. R6+ roadmap items owner-gated — full ranked list at
   [`../docs/ideas/2026-07-18-next-wave-roadmap.md`](../docs/ideas/2026-07-18-next-wave-roadmap.md).

kit: v1.17.0
