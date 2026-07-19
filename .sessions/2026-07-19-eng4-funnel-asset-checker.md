# Session — ENG-4: per-kit funnel-asset completeness checker

> **Status:** `complete`

- **📊 Model:** Claude Opus (4.x family) · high · test writing
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
- **known-current-state (reported, not papered over):** NO missing-asset finding.
  All 22 built kits carry both required funnel roles — 20 under the modern
  `listing-copy.md` + `owner-actions.md` scheme, and the two flagship launches
  (`stripe-webhook-test-kit`, `agent-fleet-field-manual`) under the legacy
  `LISTING.md` + `publish-owner-action.md` scheme, which the role-satisfied-by-any-
  accepted-filename design accepts without a per-kit exception. So NO per-name
  allowlist was needed, and NO sales/landing copy was invented to force a green —
  the guard reflects the real tree and reds only a FUTURE regression (a new built
  kit shipping without one of the two roles, or a role file deleted).
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
- 2026-07-19T08:5xZ — **Build.** Added `scripts/check_funnel_assets.py` (reads the
  built-kit set off `candidates/<sku>/dist/`, then asserts each kit's
  `docs/launch/<sku>/` folder satisfies both required funnel ROLES, each accepting
  either naming convention; exit 0 clean / 1 with a per-kit missing-role list;
  `--root` for fixtures) + `scripts/test_check_funnel_assets.py` (14 tests:
  live-tree-green + saw-real-built-SKUs + missing-landing-copy catch +
  missing-owner-actions catch + missing-both catch + modern/legacy/mixed naming +
  non-built-out-of-scope + built-no-launch-folder-not-double-reported + two skip
  cases). Wired a new REQUIRED `funnel-assets-guard` job into
  `.github/workflows/kit-tests.yml` (checker on the live tree + unittest),
  mirroring the `built-registered-guard` (#262) job. Verified: 22 built kits, all
  funnel-complete.
- 2026-07-19T08:5xZ — **Verification.** Checker EXIT 0 on the live tree; `python3
  -m unittest test_check_funnel_assets -v` 14/14 OK; `bootstrap.py check --strict`
  EXIT 1 = the designed born-red HOLD only (this card was still in-progress) plus
  pre-existing seat-digest / model-line advisories on OTHER cards — no new failure
  from this slice. Reverted the local `.substrate/guard-fires.jsonl` telemetry
  append to keep the PR scoped. No missing-asset finding; no funnel assets invented.
- 2026-07-19T08:5xZ — Flip to `complete` (this commit): Status badge, 📊 Model
  line (family-level, task-class `test writing`), one 💡 idea, previous-session
  review, all `[[fill:]]` slots resolved. Born-red HOLD clears.

## 💡 Session idea

💡 **The two funnel ROLES are inferred from filename conventions that already
forked once (`listing-copy.md`/`owner-actions.md` vs `LISTING.md`/
`publish-owner-action.md`) — promote the funnel-asset contract to a declared
per-lane manifest so a THIRD convention can't silently satisfy nothing.** This
guard tolerates the two live schemes by accepting either filename per role, which
is correct for today — but the accepted-filename lists are hand-maintained in
`REQUIRED_ROLES`, and a future kit that names its owner doc `publish.md` or
`OWNER-ACTIONS.md` would red as "missing owner publish action" even though the
asset exists, OR (worse, if someone appeases the red by widening the list without
thought) a genuinely-missing asset could be masked by an over-broad glob. The
generalization pairs with the ENG-5 card's SKU-registry idea: give each lane
(test-kit / cookbook / bundle / book) a declared funnel-asset manifest — role name
→ the ONE canonical filename that lane uses — and have the intake/adopt step that
scaffolds a launch folder WRITE those exact names, so the convention is enforced at
creation, not merely tolerated at check time. Guard recipe: add a
`docs/publishing/FUNNEL-MANIFEST.md` (or a `funnel:` block per SKU in the
SKU-REGISTRY the ENG-5 card proposes), have `check_funnel_assets.py::REQUIRED_ROLES`
load from it keyed by the kit's lane, and add a `test_*` catch-case (manifest names
a role file the folder lacks → guard fires; a folder file not in any manifest role →
advisory, not red). That converts "which filenames count as the funnel" from a
script-local constant the next convention will outgrow into a declared, scaffold-
enforced contract.

## previous-session review

previous-session review: `.sessions/2026-07-19-eng5-built-unregistered-checker.md`
(PR #262, `66b5bae`) — added the REQUIRED `built-registered-guard` asserting every
packaged candidate is launch-REGISTERED (its `docs/launch/<sku>/` dir exists, plus
a vetting packet + a catalog row). That guard proves the funnel folder EXISTS; this
ENG-4 slice sits one level DOWN and proves the folder is COMPLETE — so a kit that
passes ENG-5 (folder present) but whose landing copy or owner-actions doc is missing
now also reds. I reused #262's exact `dist/` "built" signal (via the same
`BUILD_MARKER` semantics) so the two guards can never disagree on what "shippable"
means, and mirrored its job shape (checker-on-live-tree step + `working-directory:
scripts` unittest step, born-red card + claim discipline). I also followed its
deliberate example of NOT inventing artifacts to force a green: #262 allowlisted two
intentional gaps with reasons; here the two flagship kits' legacy naming is absorbed
by the role-any-filename design rather than a per-kit exception, and no launch copy
was fabricated — the current tree was already complete.
