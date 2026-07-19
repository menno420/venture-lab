# Session — DIST-9: pre-EAP-read-only publish sprint plan

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · idea/planning
- **started (date -u):** Sun Jul 19 00:07 UTC 2026
- **branch:** `claude/dist-9-pre-eap-sprint-plan`
- **base:** `main@6b1b8a8`
- **purpose:** the Claude Code Projects EAP goes **read-only 2026-07-21** (~2
  days from now). Repo *work* must land before then — after the cutover the
  autonomous seat can no longer write, merge, or update docs. Owner *publish
  clicks* do NOT need the seat (they are Gumroad/account actions, independent of
  EAP write) but they compete for finite owner attention. This slice lands
  DIST-9 from the veto-ready menu (#247): a one-page
  `docs/launch/pre-eap-sprint-plan.md` that (a) lists the highest-leverage
  **agent-buildable** slices to land in the remaining write window, in priority
  order, and (b) front-loads the owner's highest-leverage **publish clicks** —
  the webhook trio (GitHub D6, Slack D20, Shopify D19) → Webhook Verifier Bundle
  unlock — into a single pre-cutover session so they aren't scattered. It is
  honest about "what happens to autonomy on the 21st" (read-only = no repo
  landing; owner clicks still work) and grounds every number in the refreshed
  current state (#254) and the live OWNER-QUEUE, without inventing deadlines or
  claiming items ready that aren't.
- **honesty bar (TRUTH):** no invented deadlines, no claiming a backlog spec is
  "ready" when it is an owner-veto-filtered proposal, no over-stating the
  freeze/gate state. The plan cites real SHAs, real D-numbers, and the real
  OWNER-QUEUE. Where a funnel stage is dark (Gumroad views/sales are
  owner-dashboard-only) it says so rather than guessing.
- **scope (files):** NEW `docs/launch/pre-eap-sprint-plan.md`; EDIT
  `docs/launch/README.md` (one Cross-product index link so the docs-gate reaches
  it). Plan/docs-only, reversible; no SKU, no publish surface, no OWNER-QUEUE
  row; the seat performs no publish/spend/account action. Born-red card holds
  substrate-gate red until the completion flip.

## 💡 Session idea

💡 **A tiny `scripts/derive_bundle_unlocks.py` advisory that derives the
single-SKU-publish → bundle-unlock dependency graph from `OWNER-QUEUE.md` §2
bundle click-runs, so the "publish trio → bundle" sequences stop being
hand-copied.** This slice's OWNER-CLICKS-THESE list (webhook trio D6/D20/D19 →
Webhook Verifier Bundle; API-robustness four → API Robustness Bundle; D11+D21 →
Ship-It Bundle) is the *same* dependency graph already spelled out by hand in
three places — `CATALOG.md`'s "Recommended publish order", the bundle click-runs
in `OWNER-QUEUE.md` §2, and (once DIST-2 lands) `OWNER-LAUNCH-HOUR.md`. Every
OWNER-QUEUE renumber (the #244 CORS fold shifted D5→D6, D18→D19, D19→D20…, and
#245 had to hand-resync the bundle D-refs) is a chance for these hand-copied
sequences to drift out of sync with the queue — exactly the mispoint class the
`catalog-dref-guard` (#248) now catches for *cross-refs* but not for *ordering*.
The fix: parse each `### <Bundle> …` §2 block, read its "execute the <Kit>
publish click — blocking … queued OWNER-QUEUE D<n>" rows into a `bundle →
[blocking D-numbers]` map, and emit a `bundle-unlock-order` advisory (never
exit-affecting, same class as `check_kill_clocks.py`) when a doc's stated
publish-order sequence for a bundle disagrees with the derived blocking set —
turning the "which clicks unlock which bundle, in what order" question from a
hand-maintained list into a standing derived signal. Natural sibling of the
per-cluster funnel-coverage checker idea (agent-ops card) and the D-ref guard
(#248): D-ref guard checks *resolution*, this checks *ordering*.

## previous-session review

previous-session review: this slice picks up the distribution-first baton that
#249–#254 carried and closes its planning loop. #249 (DISTRIBUTION-PLAYBOOK),
#250/#251 (the membership + AI-Novella lead magnets) built the top-of-funnel
discovery assets; #252 (funnel diagnostic) and #253 (kill-clock decision packet)
pre-chewed the live SKU's T+7/T+14 call; #254 refreshed `current-state.md` to
HEAD `7d5229f` with the 64-item veto menu as the standing backlog. DIST-9 is the
meta-layer above all of them: with ~2 write days left before the 2026-07-21
read-only cutover, it says *which* of that backlog to land and *which* owner
clicks to batch — and it consumes, rather than re-derives, #252/#253 (the T+7/T+14
call needs no repo work, it's already owner-ready) and #254's counts. The
hard-won lesson I carried forward from the #249–#253 series: honest freeze/gate
state matters more than a tidy narrative — so this plan explicitly reconciles the
append-only `control/inbox.md` ORDER 003 "frozen" text against the repo's real
"UNFROZEN 2026-07-11" state, rather than restating a stale freeze. The one thing
I'd flag forward: the OWNER-CLICKS-THESE sequence is hand-derived from CATALOG +
OWNER-QUEUE (the 💡 above is the mechanical fix for that drift risk).

## Work log

- 2026-07-19 — Branch `claude/dist-9-pre-eap-sprint-plan` from `origin/main`
  (`6b1b8a8`, #254 HEAD); clean base confirmed. Born-red card committed (first
  commit `741d05e`), pushed. PR #255 opened READY. Build begins.
- 2026-07-19 — Built the payload: `docs/launch/pre-eap-sprint-plan.md` (one-page
  AGENT-LANDS-THESE vs OWNER-CLICKS-THESE split, honest read-only-autonomy and
  freeze/gate sections, webhook-trio → bundle-unlock click sequence) + one
  Cross-product index link in `docs/launch/README.md`. Committed (`b4ca918`),
  pushed. Diff verified to carry only the 2 intended files (+ card).
- 2026-07-19 — Heartbeat: neutral in-flight pointer for PR #255 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed
  (`936d162`), pushed.
- 2026-07-19 — `python3 bootstrap.py check --strict` pre-flip = the born-red HOLD
  only (in-progress Status + unresolved auto-draft slots); all non-hold checks pass,
  advisories are non-gating and pre-existing.
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8`), one 💡 idea, previous-session review acknowledging
  the #249–#254 baton, all auto-draft slots resolved, guard-fires ledger delta
  committed. Re-ran `bootstrap.py check --strict` EXIT 0 (advisories only). Born-red
  HOLD clears; last commit releases auto-merge.
