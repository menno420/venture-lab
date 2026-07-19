# Session — SKU-registry consolidation (behavior-preserving de-duplication)

> **Status:** `in-progress`

- **📊 Model:** `[[fill: family-level model line]]`
- **started (date -u):** Sun Jul 19 09:24 UTC 2026
- **branch:** `claude/sku-registry-consolidation`
- **base:** `main@10e0151` (post #261 ENG-6 / #262 ENG-5 / #263 ENG-4 / #264 ENG-7 / #265 ENG-8 — the ENG-4→ENG-8 pipeline-safety lane is fully merged)
- **purpose:** collapse the DUPLICATED SKU/registry inference that the ENG-4 and
  ENG-5 guards each maintained independently into ONE authoritative shared module,
  and refactor those guards to import it. This is the capstone the ENG-4, ENG-5, and
  ENG-8 session cards each independently proposed (💡 "one machine-readable SKU
  registry"): three cards converged on it, so it is a real de-duplication, not churn.
- **the duplication (mapped before moving anything):** `check_built_registered.py`
  (ENG-5) and `check_funnel_assets.py` (ENG-4) each hand-maintained their OWN copy of
  the same facts: the registry roots (`CANDIDATES_DIR_REL = "candidates"`,
  `LAUNCH_DIR_REL = "docs/launch"`), the `dist/` `BUILD_MARKER` (the "built/shippable"
  signal — the ENG-4 docstring even says it copies ENG-5's marker "so the two guards
  can never disagree"), the `_subdirs` helper, and the built-sku enumeration
  (ENG-5's `collect()` built-set == ENG-4's `built_skus()`). ENG-5 additionally owns
  the launch/vetting/catalog enumeration + the two allowlists (`BUNDLE_TEMPLATES`,
  `OWNER_GATED_LANES`) + `_catalog_refs`; ENG-4 owns the funnel `REQUIRED_ROLES` +
  `_launch_files` + `missing_roles`. A repo-structure change (new build marker, moved
  launch root) meant editing the same fact in two files in lockstep, and any drift
  would silently make the two guards disagree about what "built" means.
- **what does NOT share and is deliberately LEFT UNTOUCHED:** ENG-6
  (`check_owner_queue_idempotent.py`) and ENG-7 (`check_owner_queue_staleness.py`) do
  NO candidates/launch/built/catalog inference — they import `derive_owner_queue` and
  source their vetting-dir path from `gen.DEFAULT_VETTING_DIR` (the generator's domain,
  correctly reused there — pulling it into this module would invent a new coupling and
  risk behavior). ENG-8 (`check_docs_links.py`) has no SKU inference at all. Per the
  "do not touch a guard that shares nothing" rule, all three are left alone.
- **scope (files):** NEW `scripts/sku_registry.py` (the ONE authoritative source:
  `iter_skus` / `is_built` / `built_skus` / `launch_skus` / `vetting_skus` /
  `catalog_refs` / `registered_surfaces` / `launch_files` / `missing_roles` /
  `funnel_roles`, plus the registry constants, `BUILD_MARKER`, the two allowlists with
  their verbatim documented reasons, and `REQUIRED_ROLES`); REFACTORED
  `scripts/check_built_registered.py` + `scripts/check_funnel_assets.py` to import from
  it (re-exporting the same module-local names so their tests are unchanged); NEW
  `scripts/test_sku_registry.py` (unittest: enumeration, built/registered/funnel facts,
  allowlist values, catalog whole-token match, fixture-root isolation, live-tree
  non-vacuity); CI wiring in `.github/workflows/kit-tests.yml` (new REQUIRED
  `sku-registry-module-tests` job mirroring the guard-test step pattern); plus the
  claim and this card.
- **behavior-preserving contract:** every guard produces the SAME verdict on the
  current tree (all still exit 0) and every existing guard test passes UNCHANGED. The
  module's functions reproduce the exact inference the guards previously did inline —
  the allowlists and their comments moved over verbatim; no invariant or message
  string changed, only the SOURCE of the inference.
- **verify:** all five guards exit 0 on the live tree · every existing guard test
  passes unchanged · `test_sku_registry` passes · `python3 bootstrap.py check --strict`
  exit 0 (revert any `.substrate/guard-fires.jsonl` append).

## Work log

- 2026-07-19T09:24Z — Branch `claude/sku-registry-consolidation` from origin/main
  (`10e0151`, post #261–#265). Read all five guards + their tests, mapped the exact
  duplication (above), confirmed ENG-6/7/8 share nothing, and read the ENG-4/5/8 💡
  ideas describing the intended SKU-registry manifest. Claim + this born-red card
  committed. Build begins.
- `[[fill: build + verification + flip-to-complete log entries]]`

## 💡 Session idea

`[[fill: one genuine idea]]`

## previous-session review

`[[fill: review of the ENG-8 #265 card]]`
