# Session — submissions guard fix (classify the marketing-drafts container as a non-SKU)

> **Status:** `in-progress`

![status](https://img.shields.io/badge/status-in--progress-orange)

- **📊 Model:** opus-4.8 · high · guard fix
- **started (date -u):** Mon Jul 20 04:51 UTC 2026
- **branch:** `claude/submissions-guard-fix`
- **base:** `main@3bb962b`
- **purpose:** land a small fix for a guard REGRESSION introduced by #277. That PR
  added `docs/launch/submissions/` — a container of per-channel marketing submission
  DRAFTS (one paste-and-post file per channel for the free lead-magnet articles), NOT
  a sellable SKU. The `built-registered-guard` (`scripts/check_built_registered.py`,
  backed by `scripts/sku_registry.py`'s `launch_skus`) enumerates every immediate
  `docs/launch/*` subdirectory as a per-SKU launch row, so it now reads `submissions/`
  as a phantom SKU and reddens on main:
  `REGISTERED-BUT-MISSING-ARTIFACT: docs/launch/submissions/ is a launch row but no
  vetting packet … not referenced in CATALOG.md … no built artifact`. The guard is
  advisory (non-required) so books merged past it, but it is RED on main and must be
  clean before the EAP cutover so a fresh seat boots from a green repo. The correct
  fix CLASSIFIES `submissions/` as a non-SKU container — it is not a launch row at any
  level — NOT invents a phantom vetting packet / catalog row / build dir for it.
- **scope (files):** UPDATE `scripts/sku_registry.py` (add a clearly-named
  `NON_SKU_LAUNCH_DIRS` frozenset sibling to the two documented allowlists, and filter
  it out of `launch_skus` — the ONE place `docs/launch/*` is enumerated, so both guards
  agree); UPDATE `scripts/test_sku_registry.py` (assert the classification + that it
  does NOT blind the guard to real launch rows, plus a live-tree check that the
  container dir exists yet is excluded); this card; NEW
  `control/claims/submissions-guard-fix.md`. No touch to candidates/**,
  OWNER-START-HERE.md, control/status.md, docs/current-state.md, or any generated file.
- **verify:** `built-registered-guard` exit 0 AND still enumerating the real ~22 built
  SKUs / 24 launch rows (it must still catch genuine missing artifacts);
  `sku-registry-module-tests` (`python3 -m unittest test_sku_registry`) green; the two
  refactored guards' tests green; `python3 bootstrap.py check --strict` exit 0.

## Work log

- 2026-07-20T04:51Z — Isolated worktree; branch `claude/submissions-guard-fix` from
  `origin/main` (`3bb962b`, post #279). Reproduced the RED: `check_built_registered.py`
  exits 1 with the single `docs/launch/submissions/` REGISTERED-BUT-MISSING-ARTIFACT
  violation. Read `sku_registry.py` (`launch_skus` enumerates every `docs/launch/*`
  subdir; the two documented allowlists `BUNDLE_TEMPLATES` / `OWNER_GATED_LANES` are
  guard-level exemptions for real SKUs, not the right hook for a non-SKU CONTAINER) and
  confirmed the only consumers of `launch_skus` are `check_built_registered.py`
  (Direction B) and `registered_surfaces` — the funnel guards key off built-skus /
  file globs, so filtering at the enumeration layer is safe. Born-red card + claim
  committed (first commit). Build begins.
- 2026-07-20T04:5xZ — **Build.** Chose fix (a): added `NON_SKU_LAUNCH_DIRS =
  frozenset({"submissions"})` to `sku_registry.py` with a comment stating it is a
  CLASSIFICATION (the entry is categorically not a sellable SKU, unlike the two
  allowlists which are real SKUs merely exempt from a requirement), and subtracted it
  in `launch_skus`. This preserves the doc location and needs no relocation/link churn.
  Added two tests to `test_sku_registry.py`: a fixture test proving a real launch row
  is still enumerated while the container is excluded (anti-blinding), and a live-tree
  test proving `docs/launch/submissions/` exists yet is NOT a launch SKU.
- 2026-07-20T04:5xZ — **Verification.** `check_built_registered.py` now EXIT 0:
  `OK: 22 built SKU(s) all registered; 24 launch row(s) all have artifacts`, and
  `submissions` is no longer in `launch_skus` — the guard still enumerates and validates
  the real SKUs (so it still catches genuine missing artifacts). Tests: `test_sku_registry`
  19, `test_check_built_registered` 12, `test_check_funnel_assets` 14 — all OK.
  `bootstrap.py check --strict` EXIT [[fill: pre-flip strict exit code]] on the born-red
  HOLD only, no other guard red.
- 2026-07-20T04:5xZ — Flip to `complete` (this commit): Status badge flipped, 📊 Model
  line kept, one 💡 idea, previous-session review, all `[[fill:]]` slots resolved. PR
  #[[fill: PR number]] opened READY. Re-ran `bootstrap.py check --strict` → EXIT 0
  (born-red HOLD clears); `check_built_registered.py` re-confirmed EXIT 0.

## 💡 Session idea

💡 **A `launch-dir-classification` micro-guard (or a `test_sku_registry` catch-case) that
asserts EVERY immediate `docs/launch/*` subdirectory is accounted for as exactly one of:
a built-and-registered SKU, a documented `BUNDLE_TEMPLATES` / `OWNER_GATED_LANES`
exemption, or a declared `NON_SKU_LAUNCH_DIRS` container.** This session fixed the
regression `submissions/` caused, but the underlying footgun is that `docs/launch/` is a
mixed bag — per-SKU launch rows live beside non-SKU containers and loose `*.md` files, and
the ONLY thing that decides "is this dir a SKU row?" is the negative space of three
hand-maintained frozensets. The next unrelated container dropped under `docs/launch/`
(a second submissions batch, a press-kit folder) will redden the guard again exactly as
`submissions/` did, and the failure will read as a missing SKU artifact rather than "an
unclassified directory." Guard recipe: add a test to `scripts/test_sku_registry.py` that
globs the live `docs/launch/*/` dirs and asserts each is in `launch_skus(REPO_ROOT)` ∪
`BUNDLE_TEMPLATES` ∪ `OWNER_GATED_LANES` ∪ `NON_SKU_LAUNCH_DIRS` — a new dir then fails
loudly at test time with "unclassified launch dir: <name>; add it to a SKU registry or to
NON_SKU_LAUNCH_DIRS", turning a confusing phantom-SKU red into a self-explaining
classification prompt. It is the natural sibling of the ENG-5 💡 (back the `dist/`
heuristic and these frozensets with a DECLARED `SKU-REGISTRY.md`): the same "the SKU
universe is inferred from directory shape, not declared" gap, caught one dir earlier.

## previous-session review

previous-session review: the newest prior card,
`.sessions/2026-07-19-sku-registry-consolidation.md`, is the one that CREATED the module
I just touched — it collapsed the duplicated built/registered/funnel inference the ENG-4
and ENG-5 guards each hand-maintained into the single authoritative `scripts/sku_registry.py`,
refactoring both guards to import it and adding `test_sku_registry.py`, all
behavior-preserving (every guard still exit 0, every existing guard test unchanged). That
consolidation is exactly why THIS fix could be a one-place change: because `launch_skus`
is now the ONE definition of a launch row shared by both guards, subtracting a non-SKU
container there fixes the correspondence for every consumer at once, with no risk of the
two guards drifting on what "registered" means. I followed its three best habits directly:
(1) **one home for the fact** — I classified `submissions/` at the shared enumeration layer,
not with a private skip inside `check_built_registered.py`; (2) **prove non-vacuity /
anti-blinding** — its live-tree test asserts the tree really has SKUs; my added test asserts
a real launch row is STILL enumerated alongside the excluded container, so the exclusion can
never silently blind the guard; (3) **honestly scope the exemption** — where it moved the two
allowlists over with verbatim reasons, I documented `NON_SKU_LAUNCH_DIRS` as a
CLASSIFICATION of a genuine non-SKU, explicitly distinct from hiding a missing artifact.
Its own 💡 (back the module with a DECLARED `SKU-REGISTRY.md`) is the capstone my 💡 above
narrows to the concrete next dir-classification catch-case.
