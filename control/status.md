# Venture Lab — status log (neutral snapshot)
updated: 2026-07-19T09:35:10Z

> The `control/*` manager↔lane message-bus remains **retired**. This file is a
> neutral status pointer, not a source of truth or an order. The successor reads
> [`../docs/current-state.md`](../docs/current-state.md),
> [`../docs/NEXT-TASKS.md`](../docs/NEXT-TASKS.md),
> [`../docs/launch/CATALOG.md`](../docs/launch/CATALOG.md), and
> [`../docs/ideas/2026-07-19-execution-roadmap.md`](../docs/ideas/2026-07-19-execution-roadmap.md).

**Where the tree is (neutral facts):**
- `main` HEAD is `4a89e46` — "Consolidate the guards' duplicated SKU/registry
  inference into one authoritative module (behavior-preserving) (#266)". **Zero
  open PRs** from this session — the queue is clear.
- `python3 bootstrap.py check --strict` is **green (exit 0)** at this HEAD
  (advisories only, pre-existing).

**Today's merge wave (2026-07-19, all merged green via merge-on-green landing):**
- **#258** — repo hygiene / stale-claim prune.
- **#259** — execution roadmap groomed from the veto-ready menu.
- **#260** — owner-steps refresh (consolidated publish click-path).
- **#261** — ENG-6 owner-queue-idempotence guard.
- **#262** — ENG-5 built-but-unregistered checker.
- **#263** — ENG-4 funnel-assets checker.
- **#264** — ENG-7 owner-queue-staleness checker.
- **#265** — ENG-8 docs-links freshness checker.
- **#266** — SKU/registry consolidation into one authoritative module
  (behavior-preserving).
- Per-PR detail lives in each PR body and `docs/current-state.md`.

**What now guards the owner click-path:**
- Six REQUIRED CI guards run over the owner path — `owner-queue-idempotence`,
  `built-registered`, `funnel-assets`, `owner-queue-staleness`, `docs-links`,
  and `sku-registry-module-tests`.
- The guards now share one authoritative helper, `scripts/sku_registry.py`,
  instead of each re-deriving SKU/registry inference.

**Backlog (honest):**
- The high-leverage autonomous-safe backlog is **spent**. Remaining autonomous
  items are lower-leverage upkeep — e.g. MISC-1 fresh-seat boot hardening, which
  stays **deferred as speculative** (no concrete failure has been identified).
- Everything revenue-moving is **owner-gated** on the publish clicks in
  [`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md).

**Next-2 (baton, pointers — not orders):**
1. The **owner-steps list**
   ([`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md))
   is on the clock: the live **Stripe SWTK T+7 checkpoint is due today
   (2026-07-19)**, and the **pre-EAP publish clicks** want doing before the
   **2026-07-21 read-only cutover**.
2. The **execution roadmap**
   ([`../docs/ideas/2026-07-19-execution-roadmap.md`](../docs/ideas/2026-07-19-execution-roadmap.md))
   holds the next autonomous-safe pick if the owner wants more building.

kit: v1.17.0
