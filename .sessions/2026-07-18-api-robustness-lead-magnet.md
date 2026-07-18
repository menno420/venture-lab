# Session — API-robustness lead-magnet article + dev-cluster distribution drafts (distribution-first, no spend)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only
- **started (date -u):** Sat Jul 18 21:29 UTC 2026
- **branch:** `claude/api-robustness-lead-magnet`
- **base:** `main@3d295b2` (born-red first cut off `4137691`; branch rebuilt
  clean on fresh `main` after the shared-clone HEAD collision — see work log)
- **purpose:** the binding constraint in this repo is REVENUE/DISTRIBUTION, not
  inventory — 1 LIVE SKU with 0 organic sales + 18 publish-READY SKUs that are
  undiscovered (see `docs/launch/CATALOG.md`). Every dev-tool kit's intake names
  "a free dev.to/Hashnode article on the pain" as its top-of-funnel channel, but
  NO such free discovery asset exists for the API/webhook test-kit cluster. This
  slice creates it: a genuinely useful, free, dev.to/Hashnode/Show-HN-ready
  article teaching the shared pain of the test-kit cluster (non-idempotent
  webhook handlers, missing signature verification, retry storms, unbounded
  pagination, missing rate-limit headers, the CORS+Authorization footgun), then
  channel drafts that funnel to the two four-pack bundles first (higher AOV) and
  the singles second. Docs/markdown-only, reversible, NO owner spend/publish/
  account action performed by the seat — posting stays an owner-gated
  paste-and-post like every other launch asset.
- **honesty bar (repo rule):** NO fabricated metrics, NO invented testimonials,
  NO "used by X companies," NO fake benchmark numbers — real technical substance,
  soft honest funnel. Matches the tone of existing `docs/launch/` copy.
- **scope (files):** NEW `docs/launch/api-robustness-lead-magnet.md`; EDIT
  `docs/launch/distribution-drafts.md` (add dev-cluster channel drafts), EDIT
  `docs/launch/CATALOG.md` (register the lead magnet as the dev-cluster funnel-top
  asset), EDIT `docs/current-state.md` (fold in the honest stale-count fix:
  "10 publish-READY" → the CATALOG.md-fresh count). Born-red card holds
  substrate-gate red until the completion flip.

## 💡 Session idea

💡 **A `scripts/check_funnel_assets.py` advisory that proves each kit's named
top-of-funnel actually exists.** Every dev-tool kit's intake/listing names "a
free dev.to/Hashnode article on the pain" as its top-of-funnel channel — but
until this slice, no such article existed for the API/webhook cluster; the gap
was invisible because nothing checks it. The fix is a tiny stdlib checker that,
for each `candidates/*/` kit, greps its vetting/listing copy for the funnel-top
channel it claims and asserts the referenced discovery asset (a
`docs/launch/*lead-magnet*` / article) actually exists and links back to the
kit's bundle+singles — emitting a `funnel-asset-missing` advisory (never
exit-affecting, same class as the claims/kill-clock linters) when a kit promises
a discovery channel it never shipped. That turns "the kits are built but
undiscovered" — the repo's own binding constraint — from a prose observation
into a standing, greppable signal, and it's the natural mechanical sibling of
the storefront-catalog and bundle-manifest derive scripts: don't hand-track the
drift-prone funnel-coverage table, derive it. Guard recipe: new
`scripts/check_funnel_assets.py` (glob `candidates/*/`, read each
`docs/publishing/vetting/<kit>.md` §-intake for the channel phrase, resolve the
named `docs/launch/` asset), wired as an advisory into `bootstrap.py check`
alongside `check_kill_clocks.py` / `lint_owner_gates.py`; test target a fixture
kit with a missing funnel asset asserting the one advisory fires.

## previous-session review

previous-session review: `.sessions/2026-07-18-cors-preflight-test-kit.md`
(PR #242, ORDER 016 — the CORS Preflight Test Kit $29, a new sellable) — a clean,
honest slice that did the hard things right: a stdlib-only `cptk.py`+`cptk.js`
harness with a correct/naive reference pair, a 37-test HTTP real-path suite, a
byte-reproducible bundle, and the correct restraint of NOT regenerating
OWNER-QUEUE.md (it renumbers shared decision IDs) — flagging the regen as an
explicit owner follow-up rather than smuggling a renumber into the PR. Its one
real cost landed on me, not on it: it ran in this SAME shared clone and switched
the git HEAD out from under a parallel session, so its commits briefly landed on
my branch and mine on its — a worktree-isolation gap in the dispatch, not a
defect in the kit. The lesson for the next multi-session night is mechanical:
parallel sellable-build sessions in one repo need separate git worktrees (or
serialized checkouts), because a shared HEAD makes "commit to my own branch" a
race, not a guarantee.

## Work log

- 2026-07-18 — Branch `claude/api-robustness-lead-magnet` from origin/main
  (`4137691`); collision check clean (no existing `control/claims/` entry, no
  open PR covering the dev-cluster lead magnet). Claim + born-red card committed
  (first commit), pushed. Build begins.
- 2026-07-18T21:3xZ — Built the payload: the free lead-magnet article, the
  dev-cluster distribution drafts, the CATALOG funnel-top registration, and the
  honest current-state count fix (10→18 READY, citing CATALOG.md). Committed.
- 2026-07-18T21:4xZ — **Shared-clone collision + recovery.** A parallel CORS-kit
  session ran in this SAME clone and switched the git HEAD between branches
  mid-build, so its commits landed on my remote branch and my payload commit
  landed on its local branch; its PR #242 then merged to `main` independently. My
  own content was never lost — both my commits were isolated, clean diffs
  (preserved as rescue tags). Per coordinator direction (the collision was a
  dispatch/worktree-isolation gap, not my work): rebuilt the branch clean on
  fresh `origin/main` (`3d295b2`, which now includes #242), cherry-picked my
  born-red and payload commits (both applied with zero conflict — anchors intact
  on new main), re-added the heartbeat, and force-pushed with lease to replace
  the polluted remote. Verified the PR #243 diff carries ONLY my files and ZERO
  `candidates/cors-*` / cptk pollution.
- 2026-07-18T21:4xZ — Flip to `complete` (this commit): Status badge, 📊 Model
  line, one 💡 idea, previous-session review, all `[[fill:]]` slots resolved.
  `python3 bootstrap.py check --strict` EXIT 0 (advisories only). Born-red HOLD
  clears.
