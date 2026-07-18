# Session — Storefront Catalog + positioning/comparison asset (conversion)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · launch asset (content)
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

💡 **A `scripts/derive_catalog.py` that machine-emits the comparison table from
the vetting packets + OWNER-QUEUE**, so the one drift-prone artifact in this
asset — the price/status/decision-# table — can never fall out of sync with the
authoritative queue. Today the CATALOG.md table hand-transcribes 16 rows of
price, publish status, and D-number from `OWNER-QUEUE.md`; the moment a packet's
price changes or a new SKU lands (as Slack/Shopify/Auto-Merge-Enabler did *after*
current-state's "10 READY" stamp — the exact drift this catalog had to reconcile
by hand), the table silently lies. The fix is a tiny stdlib script that reads
each `docs/publishing/vetting/*.md` §3 price + §7 ⚑ block (or re-parses the
already-derived OWNER-QUEUE) and regenerates *only* the fenced comparison-table
block between two HTML-comment markers, leaving the hand-written positioning
prose untouched — plus a catalog-coverage assertion that FAILS in CI if a
publish-READY SKU exists in the queue but is absent from the table, or if a
table price/status/D-# drifts from the queue. Pair it with a **per-SKU
conversion-checklist** (a short "does this listing answer: who / what problem /
buy-vs-DIY / cross-sell?" rubric applied to each listing-copy file) so the
positioning prose has a quality floor too. This is the same "machine-derive the
one genuinely drift-prone table, don't hand-maintain it" instinct the #231
bundle card applied to `MANIFEST.json` and the night-kiln audio card applied to
the per-chapter runtime table — three lanes now independently converging on it,
which is the strongest signal it's the next consolidation slice.

## previous-session review

previous-session review: `.sessions/2026-07-18-webhook-verifier-bundle.md`
(PR #231, slice-1 — the **Webhook Verifier Bundle $79** hard-gated bundle SKU) —
an honest, precedent-disciplined bundle build that mirrored the Ship-It hard-gate
exactly (numbered §7 steps carry no ⚑, so the queue derives zero D-items; the
blocking component-publish checkboxes come first and name the real D-numbers
GitHub D5 / Slack D14 / Shopify D13; price cited as $116 → $79 with the discount
math stated, $37 / ~32%), and went one honest step beyond precedent by shipping a
**byte-reproducible assembly zip** (four component zips verbatim, double-rebuild
identical to sha `28f61d8…`) with an 8-test assembly/inventory check wired into
CI, rather than Ship-It's N/A-artifact stance. Its correct call to **regen
OWNER-QUEUE** there (+1 HARD-GATED sequence) is the exact mirror-opposite of this
catalog's correct call to **not** regen: a bundle IS a new publish surface (it
adds owner clicks), a cross-SKU positioning asset is not — the same "does this
add owner clicks?" test, answered oppositely and correctly in each. Its 💡 (a
manifest-driven auto-growing bundle so kit N+5 joins by a one-line edit) is the
same derive-the-drift-prone-table instinct this card's 💡 applies to the catalog
comparison table — the two compose cleanly.

## Work log

- 2026-07-18T16:48Z — Branch `claude/storefront-catalog-2026-07-18` from
  origin/main (`aee9a08`); collision check clean (no `control/claims/` catalog
  claim, no existing `docs/launch/CATALOG.md`, no open PR covering it). Born-red
  card committed (first commit), pushed. Survey + build begin.
- 2026-07-18T16:5xZ — Surveyed `current-state.md` + `OWNER-QUEUE.md` (D1–D15
  prices/status) + all 16 listing-copy/LISTING files. Confirmed no catalog doc
  existed (`docs/launch/CATALOG.md` is new; `the-seed-catalogue-courtship.md` is
  an unrelated book packet). Wrote `docs/launch/CATALOG.md` (comparison table +
  per-SKU positioning with buy-vs-DIY angle + bundles/cross-sell map + advisory
  publish order + `file@sha` provenance) and a one-line cross-link from
  `docs/launch/README.md`. No §7 packet, no OWNER-QUEUE regen (asset = zero
  publish surface). `bootstrap.py check --strict`: zero dead links on CATALOG.md;
  only reds are the born-red HOLD (this card) + the advisory ORDER-016
  claims-collision shared by the sibling branches. Claim (second commit) +
  CATALOG (third commit) pushed. PR #232 opened READY. Card flipped `complete`
  (this commit).
