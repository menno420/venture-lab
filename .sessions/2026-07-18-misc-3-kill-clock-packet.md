# Session — MISC-3 live-SKU kill-clock decision packet

> **Status:** `complete`

- **📊 Model:** opus-4.8 · medium · docs-only
- **started (date -u):** Sat Jul 18 23:53 UTC 2026
- **closed (date -u):** Sat Jul 18 23:56 UTC 2026
- **PR:** #253 — <https://github.com/menno420/venture-lab/pull/253>
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

💡 **A `scripts/check_kill_clocks.py` "decision-packet reachable?" assertion for
DUE/OVERDUE live SKUs.** The DIST-3 card (#252) already proposed teaching the
advisory checker to append `→ see docs/launch/funnel-diagnostic.md` on the DUE
day; this packet is the natural second half of that pointer. A tiny,
exit-0-preserving addition: when a kill-clock line fires DUE/OVERDUE for a LIVE
SKU, also assert a `docs/launch/kill-clock-decision-packet.md` (or a future
per-SKU packet) *exists and is index-reachable*, and append
`→ decide: docs/launch/kill-clock-decision-packet.md` to the line. The chain then
becomes complete and self-checking: the **clock** fires → the **diagnostic**
explains why the number is what it is → the **decision packet** turns that into a
keep/iterate/delist call — each hop a static-string pointer, no new grammar, no
determinism cost. It closes the "beautifully-built, undiscoverable artifact" gap
(named in the agent-ops lead magnet): a two-minute decision packet is only worth
writing if the owner reaches it exactly when the 2026-07-26 clock fires, and the
checker is the one thing already scheduled to run on that day.

## previous-session review

previous-session review: this slice takes the last hand-off in the #249–#252
distribution-first baton and closes its loop. **DIST-1 #249** distilled the
reusable lead-magnet playbook; **LM-1 #250** and **LM-2 #251** built the
membership and AI-Novella cluster funnel-tops (pulling traffic *in*); **DIST-3
#252** then turned that same lens on the one place the funnel is already fully
wired and live and asked *why is the number still zero — traffic, copy, or
price.* Each of those cards ended one step short of a decision: #249–#251 stopped
at "owner posts it," and #252 stopped at "owner reads two dashboards, ~5 min,
$0 — and that read tells the T+14 call." This card is that T+14 call, pre-written:
it consumes #252's diagnosis instead of re-deriving it (references, never
duplicates — the one-writer discipline the whole baton kept), and it carries the
same two disciplines forward: a tight single-doc diff + one reachable README link
(no new SKU, no publish surface, no OWNER-QUEUE renumber), and the honesty bar
held hard — where #249–#252 refused invented testimonials, benchmarks, and funnel
metrics, this packet **quotes the kill rule verbatim** rather than paraphrasing a
threshold, and marks every absent datum "not measured (owner-dashboard-only)."
The one improvement over the baton: those cards each pointed *forward* to the next
artifact; this one is the terminal node the chain was aiming at — clock →
diagnostic → decision — so the 💡 above proposes wiring the checker to make that
whole chain reachable on the day it matters.

## Work log

- 2026-07-18 — Branch `claude/misc-3-kill-clock-packet` from `origin/main`
  (`cb4ef3a`, includes #249–#252); clean base verified,
  `docs/launch/funnel-diagnostic.md` (#252) present. Read the kill-rule sources
  (LAUNCH-LOG "Kill rule (concrete dates)", SWTK §7 KILL-CHECK, OWNER-QUEUE ⏲
  line), the funnel diagnostic this packet consumes, and the DISTRIBUTION-PLAYBOOK
  voice. Born-red card committed (first commit `143808b`), pushed; PR #253 opened
  READY. Build begins.
- 2026-07-18 — Built the payload: `docs/launch/kill-clock-decision-packet.md`
  (`reference` badge) — (a) the kill rule quoted verbatim from LAUNCH-LOG.md, (b)
  the exact evidence to check pointing at the DIST-3 funnel diagnostic's
  traffic/copy/price hypotheses, (c) keep/iterate/delist each with concrete
  consequences, (d) an owner-only action checklist; linked from
  `docs/launch/README.md` (Cross-product) for reachability. Committed `e76e29c`,
  pushed.
- 2026-07-18 — Heartbeat: neutral in-flight pointer for PR #253 added to
  `control/status.md` (`updated:` bumped; other sections + `control/inbox.md`
  untouched). Committed `e24f0a6`, pushed.
- 2026-07-18 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8`), one genuine 💡 idea, previous-session review
  acknowledging the DIST-1 #249 / LM-1 #250 / LM-2 #251 / DIST-3 #252 baton, all
  `[[fill:]]` slots resolved. Pre-flip `python3 bootstrap.py check --strict` was
  EXIT 1 = the expected born-red HOLD (in-progress card only; no
  docs-gate/catalog-dref failure); this flip clears the HOLD. Last commit,
  releasing the landing workflow.
