# Session — DIST-3 "why zero sales" funnel diagnostic (= REV-2, live Stripe SKU)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · medium · docs-only
- **started (date -u):** Sat Jul 18 23:45 UTC 2026
- **closed (date -u):** Sat Jul 18 23:50 UTC 2026
- **PR:** #252 — <https://github.com/menno420/venture-lab/pull/252>
- **branch:** `claude/dist-3-funnel-diagnostic`
- **base:** `main@25f1444`
- **purpose:** REV-2 / DIST-3 off the veto-ready menu
  (`docs/ideas/2026-07-18-veto-ready-menu.md`) — before the **T+7 checkpoint
  (2026-07-19, tomorrow)** and the **T+14 kill rule (2026-07-26)**, write an
  honest, repo-grounded diagnostic of the ONE live listing's funnel: is
  zero-sales a **traffic** problem, a **listing-copy** problem, or a **price**
  problem — and what is the **cheapest owner-executed test of each**. The one
  piece of analysis directly tied to a live revenue decision. Diagnostic doc
  only — NO live change, NO listing edit, NO spend, NO publish.
- **live SKU under diagnosis:** **Stripe Webhook Test Kit — $29**, LIVE on
  Gumroad since **2026-07-12T16:25Z** (T), funnel top = a free dev.to gotcha
  article live since 2026-07-12T17:18Z. Source of truth:
  `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`,
  `docs/launch/CATALOG.md` (LIVE row + kill-clock caveat).
- **honesty bar (repo TRUTH rule):** NO invented metrics. The repo has NO
  sales/traffic numbers — Gumroad views/sales are owner-dashboard-only and agent
  surfaces do NOT see them (LAUNCH-LOG "Measurement plan"). Where a number is
  absent, the doc says "not measured — here is the cheapest way to measure it"
  rather than guessing. Only agent-visible engagement signal = dev.to public
  reactions/comments.
- **scope (files):** NEW `docs/launch/funnel-diagnostic.md` (`reference` badge);
  EDIT `docs/launch/README.md` (one reachable index link so the docs-gate
  passes). Pairs with the upcoming MISC-3 live-SKU kill-clock decision packet.
  Born-red card holds the substrate-gate red until the completion flip.

## 💡 Session idea

💡 **Teach `scripts/check_kill_clocks.py` to print a one-line pointer to this
diagnostic on the DUE day.** The advisory checker already emits "SWTK T+7 DUE
today 2026-07-19" when run with `--today` (per
`.sessions/2026-07-13-night-killclock-advisory.md`), but the owner reading that
line still has to *find* the evidence to act on it. A tiny, exit-0-preserving
addition — when a kill-clock line fires DUE/OVERDUE for a SKU that has a
`docs/launch/funnel-diagnostic.md` (or a future per-SKU diagnostic), append
`→ see docs/launch/funnel-diagnostic.md` to that line — would wire the *alarm*
to its *diagnosis* with zero new grammar and no determinism cost (the pointer is
a static string, not an impure input). It closes the same "beautifully-built,
undiscoverable artifact" gap the agent-ops lead magnet names: this doc is only
useful if the owner reaches it exactly when the clock fires, and the checker is
the one thing that already runs on that schedule. Pairs cleanly with the MISC-3
kill-clock packet — the checker points at the diagnostic, the diagnostic points
at the decision packet.

## previous-session review

previous-session review: this slice picks up the #242–#251 distribution-first
baton — **DIST-1 #249** (the reusable lead-magnet playbook), **LM-1 #250**
(membership/boilerplate cluster magnet), and **LM-2 #251** (AI-Novella cluster
magnet). That series correctly diagnosed the binding constraint as
REVENUE/DISTRIBUTION, not inventory (1 LIVE SKU + 0 organic sales + ~18
publish-READY SKUs), and built the *top* of the funnel — free discovery articles
to pull traffic in. This slice turns that same lens on the one place the funnel
is already fully wired and live: instead of adding a fourth magnet, it asks the
harder question those cards implied but never answered — *given the funnel is
live, why is the number still zero, and which stage is actually broken.* Two
disciplines carried forward from the #249 card: (1) keep the diff to a single
docs slice + one reachable README link (tight-diff, no new SKU, no publish
surface), and (2) hold the honesty bar hard — where #249/#250/#251 refused
invented testimonials and benchmark numbers, this card refuses invented *funnel
metrics*, stating "not measured (owner-dashboard-only)" wherever the repo is
genuinely dark rather than guessing a conversion rate. The one improvement over
the baton: those cards ended at "owner posts it"; this one ends at "owner reads
two dashboards, ~5 min, $0" — the cheapest possible next action, sized to
tomorrow's T+7 clock.

## Work log

- 2026-07-18 — Branch `claude/dist-3-funnel-diagnostic` from `origin/main`
  (`25f1444`, includes #249/#250/#251); clean base verified. Read the live-SKU
  evidence (LAUNCH-LOG, LISTING, CATALOG kill-clock caveat, kill-clock advisory,
  article/test-purchase logs). Born-red card committed (first commit, `b2c0901`),
  pushed; PR #252 opened READY. Build begins.
- 2026-07-18 — Built the payload: `docs/launch/funnel-diagnostic.md` (traffic vs
  copy vs price, cheapest owner-executed test of each, no invented metrics),
  linked from `docs/launch/README.md` (Cross-product) for reachability. Committed
  `3123dee`, pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #252 added to
  `control/status.md` (`updated:` bumped; other sections + `control/inbox.md`
  untouched). Committed `4222371`, pushed.
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8`), one genuine 💡 idea, previous-session review
  acknowledging the DIST-1 #249 / LM-1 #250 / LM-2 #251 baton, all `[[fill:]]`
  slots resolved. Pre-flip `python3 bootstrap.py check --strict` was EXIT 1 =
  the expected born-red HOLD (in-progress card only; no docs-gate/catalog-dref
  failure); this flip clears the HOLD. This is the last commit, releasing the
  landing workflow.
