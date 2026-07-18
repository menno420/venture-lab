# Venture Lab — status log (neutral snapshot)
updated: 2026-07-18T22:22:10Z

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
