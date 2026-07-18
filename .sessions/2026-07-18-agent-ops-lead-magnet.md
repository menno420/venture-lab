# Session — Agent-ops cluster lead-magnet article + agent-ops distribution drafts (distribution-first, no spend)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only
- **started (date -u):** Sat Jul 18 22:20 UTC 2026
- **branch:** `claude/agent-ops-lead-magnet`
- **base:** `main@5358fb0`
- **purpose:** the binding constraint in this repo is REVENUE/DISTRIBUTION, not
  inventory — 1 LIVE SKU with 0 organic sales + ~18 publish-READY SKUs that are
  built-but-undiscovered (see `docs/launch/CATALOG.md`). PR #243 shipped the free
  top-of-funnel discovery article for the dev-tool (webhook + API-robustness)
  cluster. The next-highest-leverage cluster with NO free discovery asset is the
  **agent-ops / fleet cluster** — the widest cluster by SKU count and the only one
  anchored by a $39 guide (Agent Fleet Field Manual) plus five supporting SKUs
  (Multi-Agent Control-Plane Pack $29, Owner-Click Queue Kit $19, Agent-Workflow
  Template Pack $19 PWYW, the Merge-Wall $19 + Auto-Merge Enabler $19 cookbooks,
  Kill-Rule Intake Kit $15). Membership/template-pack channel copy already exists
  in `distribution-drafts.md`; the dev cluster's lead magnet already exists. This
  slice builds the agent-ops cluster's missing top-of-funnel: a genuinely useful,
  free, dev.to/Hashnode/Show-HN-ready article teaching the shared pain of running
  autonomous coding-agent fleets (agents that overstate/self-certify, collide when
  parallel, can't land their own green PRs, and spend/publish without a human), then
  channel drafts that funnel soft-and-honest to the Field Manual + the supporting
  SKUs. Docs/markdown-only, reversible; NO owner spend/publish/account action —
  posting stays an owner-gated paste-and-post (OWNER-ACTION) like every launch asset.
- **honesty bar (repo rule):** NO fabricated metrics, NO invented testimonials,
  NO "used by X companies," NO fake benchmark numbers — real technical substance,
  soft honest funnel. Matches the tone of the shipped
  `docs/launch/api-robustness-lead-magnet.md` and the rest of `docs/launch/` copy.
- **scope (files):** NEW `docs/launch/agent-ops-lead-magnet.md`; EDIT
  `docs/launch/distribution-drafts.md` (add an agent-ops-cluster channel-drafts
  section — Show HN / r/ExperiencedDevs + r/LLMDevs teaser / dev.to intro — without
  disturbing existing sections), EDIT `docs/launch/CATALOG.md` (register the article
  as the agent-ops-cluster funnel-top asset, matching the dev-cluster funnel-top row
  format). Born-red card holds substrate-gate red until the completion flip.

## 💡 Session idea

💡 **A `docs/launch/FUNNEL-MAP.md` (derived, not hand-kept) that asserts every
SKU cluster has exactly one live funnel-top discovery asset — and flags the ones
that don't.** Two clusters now have a free lead magnet (dev/api-robustness via PR
#243, agent-ops via this slice); membership/template has channel copy but no
teaching article; AI Novella has neither. Right now "which clusters are covered"
lives only in the prose of `CATALOG.md`'s cross-sell section and is drift-prone —
the next cluster's magnet author has to re-derive the coverage gap by reading the
whole catalog (exactly what this slice did by hand). The fix is a tiny stdlib
deriver that reads the CATALOG cross-sell clusters, resolves each cluster's
claimed `*-lead-magnet.md` / funnel-top link, and emits a `funnel-cluster-uncovered`
advisory (never exit-affecting, same class as the claims/kill-clock linters) for
any cluster with no free discovery asset — turning "which cluster is the next
highest-leverage magnet target" from a manual catalog read into a standing,
greppable signal, and giving the distribution-first roadmap a mechanical
coverage table instead of a prose one. Guard recipe: new
`scripts/check_funnel_coverage.py` (parse `docs/launch/CATALOG.md` §"Cross-sell
clusters", for each `*-cluster` bullet resolve the linked `docs/launch/*lead-magnet*`
asset, advisory-warn on a cluster with a bundle/singles list but no funnel-top
link), wired into `bootstrap.py check` alongside `check_kill_clocks.py`; test
target a fixture catalog with one covered + one uncovered cluster asserting the
one advisory fires. (Natural sibling of the funnel-asset-per-kit idea logged on
the api-robustness card — that one checks per-KIT, this checks per-CLUSTER.)

## previous-session review

previous-session review: `.sessions/2026-07-18-api-robustness-lead-magnet.md`
(PR #243 — the free dev-cluster lead magnet, the direct predecessor in this
distribution-first series). It set the template this slice reused wholesale: an
honest, metrics-free teaching article (six failure modes, each The failure / Why
the test misses it / The fix) closing on a bundle-first soft funnel, with the
matching channel drafts and a CATALOG funnel-top registration. Its hard-won
lesson — parallel sellable-build sessions in one shared clone race on a shared git
HEAD, so each needs its own worktree/clone — is exactly why this slice ran in an
ISOLATED fresh clone from the first command; no HEAD collision occurred here. The
one thing I'd flag forward: #243 also folded a `docs/current-state.md` stale-count
fix into its diff; this slice deliberately kept scope tighter (launch docs +
control scaffolding only) so the diff stays a clean single-purpose docs slice.

## Work log

- 2026-07-18 — Branch `claude/agent-ops-lead-magnet` from `origin/main`
  (`5358fb0`); collision check clean (no existing `control/claims/` entry for the
  agent-ops lead magnet, no open PR covering it — PR #243 covered the DEV cluster
  only). Claim + born-red card committed (first commit), pushed. Build begins.
- 2026-07-18 — Built the payload: the free agent-ops lead-magnet article, the
  agent-ops-cluster distribution drafts (existing sections untouched), and the
  CATALOG funnel-top registration. `git diff --stat origin/main` verified to carry
  ONLY the 5 intended files (payload + claim + card). Committed, pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #246 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed,
  pushed.
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level), one 💡 idea, previous-session review, all `[[fill:]]` slots
  resolved. `python3 bootstrap.py check --strict` EXIT 0 (advisories only). Born-red
  HOLD clears.
