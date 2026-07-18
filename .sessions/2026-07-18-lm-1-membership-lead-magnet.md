# Session — LM-1: membership/boilerplate cluster free lead-magnet article (distribution-first, no spend)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only
- **started (date -u):** Sat Jul 18 23:28 UTC 2026
- **branch:** `claude/lm-1-membership-lead-magnet`
- **base:** `main@e8d688e`
- **purpose:** the binding constraint in this repo is REVENUE/DISTRIBUTION, not
  inventory — 1 LIVE SKU with 0 organic sales + ~18 publish-READY SKUs that are
  built-but-undiscovered (see `docs/launch/CATALOG.md`). Two clusters already have
  their free top-of-funnel teaching article: the dev/webhook + API-robustness
  cluster (PR #243, `api-robustness-lead-magnet.md`) and the agent-ops / fleet
  cluster (PR #246, `agent-ops-lead-magnet.md`). The **membership / boilerplate
  cluster** (Membership-Site Boilerplate Kit $49 → Stripe Webhook Test Kit $29
  LIVE → Ship-It Bundle $59) already has channel copy in
  `docs/launch/distribution-drafts.md`, but it has **no funnel-top teaching
  article** — the one uncovered high-leverage cluster. This slice writes it, using
  `docs/launch/DISTRIBUTION-PLAYBOOK.md` (merged as DIST-1 / PR #249) as the
  fill-in-the-blank template.
- **honesty bar (repo rule):** NO fabricated metrics, NO invented testimonials,
  NO "used by X companies," NO fake benchmark numbers — real technical substance,
  soft honest funnel. Matches the disclaimer close of the shipped
  `docs/launch/api-robustness-lead-magnet.md` and `docs/launch/agent-ops-lead-magnet.md`.
- **scope (files):** NEW `docs/launch/membership-lead-magnet.md` — a free,
  standalone teaching article titled around "The seven things every paid-membership
  site gets wrong about Stripe webhooks and access control," teaching seven real
  membership/Stripe failure modes (forged webhook grants, double-grant on retry,
  no grace period on a failed payment, boolean access flags vs. derived
  subscription state, fragile webhook-driven revocation with no reconcile,
  out-of-order webhook re-grants, keying membership off the email) — each as
  **The failure. / Why it bites in production. / The fix.** — with a soft honest
  footer funnelling to the Ship-It Bundle → Membership Kit + Stripe Webhook Test
  Kit → The False-Green Test Trap. EDIT `docs/launch/README.md` (add one
  Cross-product index link so the docs-gate reachability check passes). Per the
  task, channel drafts already exist in `distribution-drafts.md` and are
  cross-referenced, NOT duplicated. Born-red card holds substrate-gate red until
  the completion flip.

## 💡 Session idea

💡 **Audit the Membership-Site Boilerplate Kit against the seven failure modes
this magnet teaches, and either close the gaps or state coverage honestly in the
kit's scope — so the free article never teaches a fix the paid product doesn't
embody.** The magnet's whole credibility (and the funnel's honesty bar) rests on
the paid kit actually delivering the fixes the article preaches. Per
`docs/launch/CATALOG.md`, the Membership Kit today ships fail-closed HMAC
verification (§1), idempotent grants (§2), and a deny-when-unpaid gate — but the
article also teaches four fixes the kit's described scope does *not* clearly
cover: grace-period / dunning tolerance (§3), deriving access from subscription
`status` + `current_period_end` rather than a boolean (§4), reconcile-on-a-schedule
so a dropped `subscription.deleted` self-heals (§5), and order-independent writes
so a late `subscription.updated` can't re-grant (§6), plus keying off `cus_…`/`sub_…`
not email (§7). That's a latent funnel-honesty risk: a buyer arrives from the
article expecting all seven and finds three. The fix is a small, greppable audit
— a `docs/launch/membership-kit/COVERAGE.md` table mapping each of the seven
failure modes to the kit file/test that embodies it (or an explicit "not in v0.2,
DIY" row) — which both keeps the "honest v0.2" scope statement truthful and turns
"what should the kit's next version add" into a mechanical checklist (§3–§7 are
the natural v0.3 backlog). Sibling of the per-KIT/per-CLUSTER funnel-coverage
ideas on the api-robustness and agent-ops cards, but pointed *inward*: those check
that a cluster has a magnet; this checks that the magnet's promises and the SKU's
delivery actually match.

## previous-session review

previous-session review: `.sessions/2026-07-18-dist-1-distribution-playbook.md`
(DIST-1 / PR #249 — `docs/launch/DISTRIBUTION-PLAYBOOK.md`), the direct baton this
slice picks up: #249 lifted the recipe PRs #243 and #246 each ran by hand into a
fill-in-the-blank playbook, and this slice is its **first consumer** — I followed
its Step-1 skeleton (teaching-first title, `reference` badge in the first 12 lines,
five-to-seven failure modes each in the failure/why/fix shape, a bundle-first soft
footer, fill tokens left unresolved) end to end, which is exactly the "third
cluster is fill-in-the-blank instead of re-derived" outcome #249 promised. The one
place I deliberately diverged from the playbook's four-part recipe: per this task's
explicit scope, the membership cluster *already* has channel drafts and a CATALOG
cross-sell entry (from the earlier #242–248 wave), so I cross-referenced
`distribution-drafts.md` rather than appending a duplicate section and did not
re-register in CATALOG — keeping the diff a clean single-purpose "add the missing
teaching article" slice rather than re-running steps already done. The #242–248
baton (CORS kit #242, the api-robustness magnet #243, the owner-queue/D-ref
resync/guard chain #244/#245/#248, the agent-ops magnet #246, the veto-ready menu
#247) is the merged base this branched from; the D-ref guard #248 in particular is
why I touched no CATALOG D-refs here.

## Work log

- 2026-07-18 — Branch `claude/lm-1-membership-lead-magnet` from `origin/main`
  (`e8d688e`, includes DIST-1 / PR #249's `DISTRIBUTION-PLAYBOOK.md`). Collision
  check clean (no `control/claims/` entry and no open PR covering the membership
  lead magnet; PRs #243/#246 covered the dev and agent-ops clusters). Born-red
  card committed (first commit), pushed. Build begins.
- 2026-07-18 — Built the payload: the free membership/boilerplate lead-magnet
  article (`docs/launch/membership-lead-magnet.md`, seven failure modes) plus one
  Cross-product index link in `docs/launch/README.md` so the docs-gate
  reachability check reaches it. Per task scope, channel drafts in
  `distribution-drafts.md` were cross-referenced, NOT duplicated, and CATALOG was
  left untouched (the membership cross-sell entry already exists from the
  #242–248 wave). `git diff --stat origin/main` confirmed the diff carries only
  the card + article + README link (+ the telemetry guard-fires delta). Committed,
  pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #250 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed,
  pushed.
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8`), one 💡 idea, previous-session review acknowledging
  the DIST-1 #249 + #242–248 baton, all `[[fill:]]` slots resolved.
  `python3 bootstrap.py check --strict` EXIT 0 (only advisory model-line notes on
  other seats' cards remain). Born-red HOLD clears; this is the last commit and
  releases auto-merge.
