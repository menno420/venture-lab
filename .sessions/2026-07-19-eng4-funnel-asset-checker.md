# Session — ENG-4: per-kit funnel-asset completeness checker

> **Status:** `in-progress`

- **📊 Model:** [[fill: family-level model line at close-out]]
- **started (date -u):** Sun Jul 19 08:50 UTC 2026
- **branch:** `claude/eng4-funnel-asset-checker`
- **base:** `main@66b5bae`
- **purpose:** implement roadmap item **ENG-4** — a REQUIRED guard that pins
  per-KIT **funnel-asset completeness**. ENG-5 (#262) proved every packaged
  candidate (`candidates/<sku>/dist/`) is launch-REGISTERED (its
  `docs/launch/<sku>/` dir exists); it does not look INSIDE that dir. This slice
  sits one level down: for each shippable (built) kit, assert its
  `docs/launch/<sku>/` funnel folder carries the FULL required asset set — a
  landing/sales-copy doc AND an owner-publish-action doc — so a kit whose landing
  copy or owner-actions doc is missing can't ship as a dead owner click path.
- **required asset set (inferred from the live tree, not assumed):** every one of
  the 22 built kits carries exactly two funnel roles, under one of two naming
  conventions — the modern majority (`listing-copy.md` + `owner-actions.md`, 20
  kits) and the legacy/flagship scheme (`LISTING.md` + `publish-owner-action.md`,
  used by the two most-developed launches `stripe-webhook-test-kit` and
  `agent-fleet-field-manual`). Both map to the SAME two funnel roles, so the guard
  requires each ROLE satisfied by ANY of its accepted filenames, not one exact
  file. `one-pager.md`, `readme-buy-snippet.md`, `gotcha-article.md`, chapter
  excerpts, `LAUNCH-LOG.md` appear on only a subset — they are enrichments, so
  they are OPTIONAL, not required.
- **scope (files):** NEW `scripts/check_funnel_assets.py` (the guard, stdlib-only,
  exit 0 clean / non-zero with a per-kit itemized list of MISSING funnel roles,
  `--root` for fixtures), NEW `scripts/test_check_funnel_assets.py` (unittest:
  live-tree green + synthetic missing-asset catches + naming-convention +
  enrichment-optional + skip/edge cases), CI wiring in
  `.github/workflows/kit-tests.yml` (new REQUIRED `funnel-assets-guard` job
  mirroring the `built-registered-guard` job), plus the claim and this card.
- **known-current-state (to be reported, not papered over):** [[fill: confirm at
  build — expected: no missing-asset finding; every built kit has both funnel
  roles; no allowlist needed; no marketing copy invented]].
- **verify:** `python3 scripts/check_funnel_assets.py` (exit 0 on the live tree)
  · `cd scripts && python3 -m unittest test_check_funnel_assets -v` · `python3
  bootstrap.py check --strict` (exit 0, advisories only).

## Work log

- 2026-07-19T08:50Z — Branch `claude/eng4-funnel-asset-checker` from origin/main
  (`66b5bae`, post #261/#262). Read the ENG-4 spec of record
  (`docs/ideas/2026-07-19-execution-roadmap.md` line 81 + the veto-menu §ENG-4
  framing), the ENG-5 #262 guard/test/CI it mirrors, and the live
  `docs/launch/<sku>/` funnel folders across all 22 built kits to infer the
  canonical required asset set. Claim + this born-red card committed. Build begins.
