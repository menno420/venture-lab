# Session — DIST-9: pre-EAP-read-only publish sprint plan

> **Status:** `in-progress`

- **📊 Model:** [[fill: family · effort · task-class at flip]]
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

[[fill: one genuine idea at flip]]

## previous-session review

[[fill: prev-session review remark at flip — acknowledge the #249–#254 baton]]

## Work log

- 2026-07-19 — Branch `claude/dist-9-pre-eap-sprint-plan` from `origin/main`
  (`6b1b8a8`, #254 HEAD); clean base confirmed. Born-red card committed (first
  commit), pushed. PR opened READY. Build begins.
- [[fill: doc commit + heartbeat + flip log at flip]]
