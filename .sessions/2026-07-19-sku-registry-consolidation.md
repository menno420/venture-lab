# Session — SKU-registry consolidation (behavior-preserving de-duplication)

> **Status:** `complete`

![status](https://img.shields.io/badge/status-complete-brightgreen)

- **📊 Model:** Claude Opus (4.x family) · high · feature build
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
- 2026-07-19T09:2xZ — **Build.** Added `scripts/sku_registry.py` (the authoritative
  source: enumeration + built/registered/funnel facts + the two allowlists with their
  verbatim reasons + `REQUIRED_ROLES`). Refactored `check_built_registered.py` (its
  `collect()` now draws every fact from the module; `_catalog_refs` re-exported for its
  test) and `check_funnel_assets.py` (imports `built_skus` / `missing_roles` /
  `_launch_files` / `REQUIRED_ROLES` from the module) — both re-export the same
  module-local names so their tests are byte-for-byte unchanged. Added
  `scripts/test_sku_registry.py` (17 tests). Wired a REQUIRED `sku-registry-module-tests`
  job into `.github/workflows/kit-tests.yml` mirroring the guard-test step pattern; YAML
  validated (24 jobs). Left ENG-6/7/8 untouched (no SKU inference to share).
- 2026-07-19T09:2xZ — **Verification (hard — this is a refactor).** All FIVE guards
  EXIT 0 on the live tree (`check_built_registered`, `check_funnel_assets`,
  `check_owner_queue_idempotent`, `check_owner_queue_staleness`, `check_docs_links`).
  Every existing guard test passes UNCHANGED: `test_check_built_registered` 12,
  `test_check_funnel_assets` 14, `test_check_owner_queue_idempotent` 7,
  `test_check_owner_queue_staleness` 20, `test_check_docs_links` 20; new
  `test_sku_registry` 17 — 90 total, all OK. `python3 bootstrap.py check --strict`
  EXIT 1 ONLY on the born-red HOLD (card in-progress) — no finding from this slice; the
  `.substrate/guard-fires.jsonl` telemetry append reverted so the tree stays clean. No
  behavior, invariant, or message string changed — only the SOURCE of the inference.
- 2026-07-19T09:2xZ — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level, task-class `feature build`), one 💡 idea, previous-session review, all
  `[[fill:]]` slots resolved. Born-red HOLD clears → `check --strict` returns EXIT 0.

## 💡 Session idea

💡 **`sku_registry.py` now consolidates the INFERENCE, but the SKU universe is still
inferred from directory SHAPE — take the last step the ENG-5 💡 named and back these
functions with a DECLARED registry file so the `dist/` heuristic and the two
allowlists become reviewable rows.** This session collapsed the duplication: `is_built`,
the registry roots, and the allowlists live in one place instead of two. But
`iter_skus`/`is_built` still answer "is this a storefront SKU?" by globbing
`candidates/<sku>/dist/` — a load-bearing heuristic that works only because every real
product happens to package to `dist/` and every book-lane/WIP candidate happens not to.
A markdown-only guide SKU, or a product that ships as a single file, would slip the
built-check silently, and the `BUNDLE_TEMPLATES`/`OWNER_GATED_LANES` exemptions are still
hand-maintained frozensets rather than declared facts. Guard recipe: add
`docs/publishing/SKU-REGISTRY.md` (a table: sku · lane · expected-artifact · gated?),
add `load_registry(root)` to `scripts/sku_registry.py` that parses it, have `iter_skus`
read the SKU universe from the registry (falling back to the dir-glob only when the file
is absent, so it stays behavior-compatible), turn the two allowlists into `gated: true`
rows, and add a meta-guard `test_*` catch-case (registry lists a SKU no surface carries →
guard fires; a `candidates/<sku>/dist/` with no registry row → guard fires). That is the
behavior-CHANGING follow-up this behavior-PRESERVING consolidation deliberately deferred,
and it makes `check_built_registered.py`, `CATALOG.md`, and `derive_owner_queue.py` all
validate against ONE declared source instead of three-way set inference — the exact
convergence the ENG-4, ENG-5, and ENG-8 cards each asked for.

## previous-session review

previous-session review: `.sessions/2026-07-19-eng8-docs-freshness-checker.md` (PR #265,
`10e0151`) — the FINAL slice of the ENG-4→ENG-8 pipeline-safety lane, adding the REQUIRED
`docs-links-guard` (INV-1 dead links in the un-gated root/`control/` docs; INV-2 `#anchor`
resolution across root + `control/` + `docs/`) scoped precisely to the gap the bootstrap
docs-gate leaves, with zero duplication of it. Exemplary work, and its own 💡 is the
mandate for THIS session: it observed that the five lane guards each hard-code a private,
script-local answer to "which files am I responsible for" (ENG-4/5's SKU roots among
them) and asked for them to "converge into one repo-consistency manifest, not five
parallel per-guard ones." I took the ENG-4/ENG-5 slice of that convergence — the
duplicated SKU/built/registered inference — and collapsed it into `scripts/sku_registry.py`,
following ENG-8's three best habits directly: (1) **reuse so the guards can't drift** —
where ENG-8 mirrored the bootstrap gate's OWN normalisation rather than re-deriving it, I
made both guards import ONE definition of "built"/"registered" so they can never disagree;
(2) **prove non-vacuity** — ENG-8 asserted its live run checked >0 links AND >0 anchors; my
`test_sku_registry` asserts the live tree really has built SKUs, launch rows, and vetting
packets, so a regression can't pass as a silent empty tree; (3) **honestly scope what you
leave alone** — ENG-8 documented every excluded dir with a reason; I documented that
ENG-6/7 (generator-domain, `gen.DEFAULT_VETTING_DIR`) and ENG-8 (no SKU inference) share
nothing and left all three untouched rather than manufacturing a coupling. ENG-8's 💡
imagined a full repo-consistency manifest spanning all five guards; my 💡 above narrows
that to the concrete next step for the SKU half — a declared `SKU-REGISTRY.md` backing the
module this session created — which is the natural capstone once the inference has one home.

