# Session — Storefront Catalog + positioning/comparison asset (conversion)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Sat Jul 18 16:48:19 UTC 2026
- **branch:** `claude/storefront-catalog-2026-07-18`
- **base:** `main@aee9a08`
- **purpose:** build ONE conversion-focused, cross-SKU **storefront catalog**
  (`docs/launch/CATALOG.md`) and land it as ONE PR. This is a NEW launch ASSET,
  not a new SKU — it COMPLEMENTS the existing per-SKU listing copy, it does not
  rewrite or duplicate it. It gives the owner a single storefront-facing
  positioning + comparison surface across the 14 software/guide/writing SKUs +
  the 2 bundles: a comparison table (name · price · value · buyer · category ·
  status · queue decision #), a per-SKU positioning block with the DIY-alternative
  buy-vs-build angle, a bundles & cross-sell map with the discount math, and an
  advisory recommended publish order. No new publish surface: the build adds NO
  §7 vetting packet and does NOT regen OWNER-QUEUE (an asset adds zero owner
  clicks). No publish, no spend, no accounts performed by the seat — the asset
  stays in-repo.
- **session:** Prices + publish status + queue decision numbers are pulled from
  `docs/publishing/OWNER-QUEUE.md` (the generated, authoritative queue) and the
  LIVE-SKU fact from `docs/current-state.md`; positioning is DERIVED from each
  SKU's own listing copy (target buyer + one-line value + DIY angle), never
  copied prose. Hard-gated items (the two bundles) are marked honestly. Born-red
  card holds substrate-gate red until the completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-18T16:48Z — Branch `claude/storefront-catalog-2026-07-18` from
  origin/main (`aee9a08`); collision check clean (no `control/claims/` catalog
  claim, no existing `docs/launch/CATALOG.md`, no open PR covering it). Born-red
  card committed (first commit), pushed. Survey + build begin.
