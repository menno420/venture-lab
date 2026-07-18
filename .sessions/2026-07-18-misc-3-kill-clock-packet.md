# Session — MISC-3 live-SKU kill-clock decision packet

> **Status:** `in-progress`

- **📊 Model:** [[fill: model line at flip]]
- **started (date -u):** Sat Jul 18 23:53 UTC 2026
- **closed (date -u):** [[fill: close time at flip]]
- **PR:** [[fill: PR number + URL at flip]]
- **branch:** `claude/misc-3-kill-clock-packet`
- **base:** `main@cb4ef3a`
- **purpose:** MISC-3 off the veto-ready menu
  (`docs/ideas/2026-07-18-veto-ready-menu.md`) — the live Stripe kit's **T+14
  kill rule fires 2026-07-26**. Write a pre-written decision packet so the
  owner's keep / iterate / delist call at the clock is a **two-minute read, not a
  cold re-derivation**: the kill rule exactly as written in the repo, the exact
  evidence to check before deciding (pointing at the DIST-3 funnel diagnostic's
  traffic-vs-copy-vs-price hypotheses), each option with its concrete
  consequences, and an owner-only action checklist. Decision packet doc only —
  NO live change, NO listing edit, NO price change, NO spend, NO publish. The
  decision is **owner-only, never auto-executed**.
- **live SKU under decision:** **Stripe Webhook Test Kit — $29**, LIVE on
  Gumroad since **2026-07-12T16:25Z** (T). Kill rule source of truth:
  `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md` ("Kill rule (concrete
  dates)"); the ⚑E/⏲ checkpoints are also carried in
  `docs/publishing/vetting/stripe-webhook-test-kit.md` (§7 KILL-CHECK) and
  `docs/publishing/OWNER-QUEUE.md`.
- **pairs with (#252):** consumes `docs/launch/funnel-diagnostic.md` (DIST-3 /
  REV-2, merged #252) — the diagnostic *diagnoses* traffic vs copy vs price;
  this packet is the *decision* that diagnosis informs. This packet **references,
  never duplicates**, the diagnostic.
- **honesty bar (repo TRUTH rule):** NO invented metrics. Gumroad views/sales
  are owner-dashboard-only and agent surfaces do NOT see them (LAUNCH-LOG
  "Measurement plan"). The kill rule is **quoted as actually written** — no
  invented thresholds. Where a datum is absent the packet says **"not measured
  (owner-dashboard-only)"** rather than guessing.
- **scope (files):** NEW `docs/launch/kill-clock-decision-packet.md`
  (`reference` badge); EDIT `docs/launch/README.md` (one reachable index link so
  the docs-gate passes). Born-red card holds the substrate-gate red until the
  completion flip.

## 💡 Session idea

[[fill: one genuine idea at flip]]

## previous-session review

[[fill: prev-session review remark at flip — DIST-1/LM-1/LM-2/DIST-3 (#249–#252) baton]]

## Work log

- 2026-07-18 — Branch `claude/misc-3-kill-clock-packet` from `origin/main`
  (`cb4ef3a`, includes #249–#252); clean base verified,
  `docs/launch/funnel-diagnostic.md` (#252) present. Read the kill-rule sources
  (LAUNCH-LOG "Kill rule (concrete dates)", SWTK §7 KILL-CHECK, OWNER-QUEUE ⏲
  line), the funnel diagnostic this packet consumes, and the DISTRIBUTION-PLAYBOOK
  voice. Born-red card committed (first commit), pushed; PR opened READY. Build
  begins.
