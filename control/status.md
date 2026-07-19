# Venture Lab — status log (neutral snapshot)
updated: 2026-07-19T07:32:38Z

> The `control/*` manager↔lane message-bus remains **retired**. This file is a
> neutral status pointer, not a source of truth or an order. The successor reads
> [`../docs/current-state.md`](../docs/current-state.md),
> [`../docs/NEXT-TASKS.md`](../docs/NEXT-TASKS.md),
> [`../docs/launch/CATALOG.md`](../docs/launch/CATALOG.md), and
> [`../docs/ideas/2026-07-18-next-wave-roadmap.md`](../docs/ideas/2026-07-18-next-wave-roadmap.md).

**Where the tree is (neutral facts):**
- `main` HEAD is `5d439bf` (PR #257). **Zero open PRs** — the queue is clear.
- `python3 bootstrap.py check --strict` is **green (exit 0)** at this HEAD
  (advisories only, pre-existing).

**Overnight merge wave (all merged green):**
- Venture **#242–#257** landed overnight: the CORS Preflight Test Kit SKU (#242)
  and its OWNER-QUEUE fold + D-ref resync (#244, #245), four cluster lead magnets
  and the distribution playbook (#243, #246, #249, #250, #251), the veto-ready
  planning menu (#247), the catalog-D-ref and funnel-coverage guards (#248, #256),
  funnel/kill-clock decision docs (#252, #253), the current-state ledger refresh
  (#254), the pre-EAP sprint plan (#255), and the legacy-`claims/`-dir retirement
  (#257). Per-PR detail lives in each PR body and `docs/current-state.md`.
- Pointer: trading-strategy **#152** (cross-round meta-analysis) landed in its own
  sibling repo, not here.

**Status-doc freshness:**
- These control/status docs were previously stamped around **#253** and are now
  **caught up to #257** — the earlier per-PR "in flight" list is retired now that
  all of #242–#257 are merged. `docs/current-state.md` (refreshed in #254) remains
  the authoritative ledger.

**Next-2 (baton, pointers — not orders):**
1. The **veto-ready menu** (`docs/ideas/2026-07-18-veto-ready-menu.md`, #247) is
   being groomed into an execution roadmap — the owner's line-by-line veto is the
   filter; survivors become claimed slices. Full ranked backlog in
   [`../docs/ideas/2026-07-18-next-wave-roadmap.md`](../docs/ideas/2026-07-18-next-wave-roadmap.md).
2. Two **time-sensitive owner steps** are on the clock: the live Stripe Webhook
   Test Kit **T+7 checkpoint is due 2026-07-19** (see
   [`../docs/launch/funnel-diagnostic.md`](../docs/launch/funnel-diagnostic.md) and
   [`../docs/launch/kill-clock-decision-packet.md`](../docs/launch/kill-clock-decision-packet.md)),
   and the **EAP read-only cutover is 2026-07-21** (repo-landing needs the write
   seat before then; owner publish clicks survive the cutover — see
   [`../docs/launch/pre-eap-sprint-plan.md`](../docs/launch/pre-eap-sprint-plan.md)).

kit: v1.17.0
