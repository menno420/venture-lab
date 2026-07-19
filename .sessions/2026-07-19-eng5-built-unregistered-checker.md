# Session — ENG-5: built-but-unregistered checker

> **Status:** `complete`

- **📊 Model:** Claude Opus (4.x family) · high · test writing
- **started (date -u):** Sun Jul 19 08:37 UTC 2026
- **branch:** `claude/eng5-built-unregistered-checker`
- **base:** `main@1da8222`
- **purpose:** implement roadmap item **ENG-5** — a REQUIRED guard that pins the
  storefront **inventory-to-registry correspondence**. A SKU lives in three
  independent places (BUILT on disk under `candidates/<sku>/dist/`,
  LAUNCH-REGISTERED under `docs/launch/<sku>/`, and QUEUE/CATALOG-REGISTERED via
  `docs/publishing/vetting/<sku>.md` + a row in `docs/launch/CATALOG.md`) and
  nothing yet asserts they agree. Two drift classes strand the owner's click path:
  a kit **BUILT-BUT-UNREGISTERED** (finished, packaged inventory that no owner
  publish step will ever surface — the headline ENG-5 case) and a launch row
  **REGISTERED-BUT-MISSING-ARTIFACT** (an owner click that dead-links or ships an
  incomplete product). This slice closes both.
- **mechanism (not hand-fabricated):** the guard reads the three registries off
  the live tree and cross-checks set membership — no re-implementation of any
  generated format. The "BUILT" signal is a candidate carrying a `dist/`
  packaged-artifact dir, which crisply separates a real product from a book-lane /
  WIP-intake / notes candidate dir (none carry `dist/`).
- **scope (files):** NEW `scripts/check_built_registered.py` (the guard,
  stdlib-only, exit 0 clean / non-zero on drift with an itemized report, `--root`
  for fixtures), NEW `scripts/test_check_built_registered.py` (unittest: live-tree
  green + built-unregistered catch + registered-missing-artifact catch + exemption
  + catalog-ref-token + empty-skip), CI wiring in `.github/workflows/kit-tests.yml`
  (new REQUIRED `built-registered-guard` job mirroring the
  `owner-queue-idempotence-guard` job), plus the claim and this card.
- **known-current-state (reported, not papered over):** two launch rows carry no
  `candidates/<sku>/dist/` build, and both are intentional per the repo's own docs
  — `bundle-starter` (a compositional bundle-listing scaffold; the two shippable
  bundles DO carry a build dir and are checked normally) and `photo-packs` (an
  owner-gated lane `docs/launch/CATALOG.md` explicitly calls "Out of scope here").
  Adding a catalog row or a build dir for either would invent artifacts that
  contradict the repo's scoping, so they are allowlisted **with the reason** in the
  guard, which then flags any OTHER built-but-unregistered / registered-but-missing
  item. No real (unexpected) drift was found; no registry entries were invented.
- **verify:** `python3 scripts/check_built_registered.py` (exit 0 on the live
  tree) · `cd scripts && python3 -m unittest test_check_built_registered -v`
  · `python3 bootstrap.py check --strict` (exit 0, advisories only).

## 💡 Session idea

💡 **The "is this candidate a storefront SKU?" question is answered by inferring
from directory shape across THREE places — promote it to ONE machine-readable SKU
registry and have every surface validate against that instead.** This guard's
"BUILT" signal is a heuristic: a `candidates/<sku>/dist/` packaged-artifact dir.
It works today because every real product packages to `dist/` and every book-lane
/ WIP candidate does not — but the heuristic is load-bearing and undocumented
anywhere but this script, and it already needs two hand-maintained allowlists
(`BUNDLE_TEMPLATES`, `OWNER_GATED_LANES`) to encode "this launch row is
intentionally not a packaged SKU". A markdown-only guide SKU, or a product that
ships as a single file rather than a `dist/`, would slip the built-check silently.
The generalization: add a tiny authoritative `sku-registry` (extend
`project.index.json`, or a new `docs/publishing/SKU-REGISTRY.md` table) that names
each storefront SKU ONCE with its lane + expected artifacts + owner-gated flag,
and have **this guard, `CATALOG.md`, and `derive_owner_queue.py` all validate
against it** — three-way set inference collapses to "does each surface match the
registry", the allowlists become declared registry rows (`gated: true`), and the
`dist/` heuristic becomes an explicit per-SKU `artifact:` field. Guard recipe:
add the registry file + a `load_registry()` in a shared `scripts/sku_registry.py`,
have `check_built_registered.py::collect` read the SKU universe from it instead of
globbing dir names, and add a `test_*` catch-case per surface (registry lists a
SKU no surface carries → guard fires). That turns "built but nobody registered it"
from a shape-inference into a one-line registry omission the guard names exactly.

## previous-session review

previous-session review: `.sessions/2026-07-19-eng6-owner-queue-idempotence-guard.md`
(PR #261, `1da8222`) — added the REQUIRED `owner-queue-idempotence-guard` pinning
that the generated `OWNER-QUEUE.md` is byte-identical to a fresh regeneration. That
guard secures the *internal consistency of the generated queue*; this ENG-5 slice
sits one level up and secures the *inventory-to-registry correspondence that feeds
it* — so a packet that regenerates cleanly (ENG-6 green) but describes a SKU whose
build artifacts are missing, or a kit built with no packet at all, now also reds.
I mirrored #261's job shape exactly (checker-on-live-tree step + `working-directory:
scripts` unittest step, born-red card + claim discipline), and deliberately followed
its example of NOT inventing registry entries to force a green — #261 regenerated
nothing because the tree was already idempotent; I invented no catalog rows because
the only two gaps (`bundle-starter`, `photo-packs`) are intentional per the repo's
own scoping and are allowlisted with reasons instead.

## Work log

- 2026-07-19T08:37Z — Branch `claude/eng5-built-unregistered-checker` from
  origin/main (`1da8222`); collision check clean (no prior
  `control/claims/eng5-built-unregistered-checker` entry). Read the ENG-5 spec of
  record (`docs/ideas/2026-07-19-execution-roadmap.md` line 80 + the veto-menu
  §ENG-5 framing) and mapped the three on-disk registries. Claim + this born-red
  card committed. Build begins.
- 2026-07-19T08:4xZ — **Build.** Added `scripts/check_built_registered.py`
  (reads the three registries off the live tree, cross-checks membership, exit 0
  clean / 1 on drift with an itemized report, `--root` for fixtures) +
  `scripts/test_check_built_registered.py` (12 tests: live-tree-green +
  saw-real-built-SKUs sanity + built-but-unregistered catch + three
  registered-but-missing catches + two exemption cases + catalog-ref-token
  robustness + empty-skip). Wired a new REQUIRED `built-registered-guard` job into
  `.github/workflows/kit-tests.yml` (checker on the live tree + unittest),
  mirroring the `owner-queue-idempotence-guard` job. Verified against the live
  tree: 22 built SKUs, all registered; 24 launch rows, all with artifacts.
- 2026-07-19T08:4xZ — **Verification.** Checker EXIT 0 on the live tree; `python3
  -m unittest test_check_built_registered -v` 12/12 OK; `bootstrap.py check
  --strict` EXIT 0 (born-red HOLD + pre-existing seat-digest / model-line
  advisories only — no new failure). Reverted the local
  `.substrate/guard-fires.jsonl` telemetry append to keep the PR scoped. No real
  (unexpected) drift found; no registry entries invented — the two known gaps
  (`bundle-starter`, `photo-packs`) are intentional and allowlisted with reasons.
- 2026-07-19T08:4xZ — Flip to `complete` (this commit): Status badge, 📊 Model
  line (family-level, task-class `test writing`), one 💡 idea, previous-session
  review, all `[[fill:]]` slots resolved. Post-flip `bootstrap.py check --strict`
  EXIT 0 (advisories only). Born-red HOLD clears.
