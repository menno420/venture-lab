# Session — ENG-5: built-but-unregistered checker

> **Status:** `in-progress`

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

💡 [[fill: session idea — flip step]]

## previous-session review

previous-session review: [[fill: previous-session review — flip step]]

## Work log

- 2026-07-19T08:37Z — Branch `claude/eng5-built-unregistered-checker` from
  origin/main (`1da8222`); collision check clean (no prior
  `control/claims/eng5-built-unregistered-checker` entry). Read the ENG-5 spec of
  record (`docs/ideas/2026-07-19-execution-roadmap.md` line 80 + the veto-menu
  §ENG-5 framing) and mapped the three on-disk registries. Claim + this born-red
  card committed. Build begins.
