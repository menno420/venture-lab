# Session — Slack Webhook Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
- **started (date -u):** Fri Jul 17 22:47:58 UTC 2026
- **branch:** `claude/slack-webhook-test-kit-2026-07-17` (PR TBD)
- **base:** `main@37cf9fd`
- **purpose:** build the **Slack Webhook Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — the N+1 analog of the LIVE Stripe Webhook Test Kit and the
  built GitHub Webhook Test Kit. A stdlib-only, account-free verifier for Slack's
  request-signing (`X-Slack-Signature` `v0=` HMAC over
  `v0:{timestamp}:{raw_body}`, 300s replay window, constant-time compare),
  shipped with vendored real-shape fixtures (url_verification / event_callback /
  slash-command + interactive), a correct example handler, an HTTP-layer
  real-path test suite (true-pass + tamper-fail + stale-timestamp-fail), a
  byte-reproducible buyer bundle, and a §7 owner-gate publish packet. The build
  ENDS at a queued owner ⚑ publish click (rail 13 / CONSTITUTION §13) — no
  publish, no spend, no accounts performed by the seat.
- **session:** Mirrors the proven Stripe/GitHub kit scaffold exactly (file set,
  evidence bar, packaging, listing/vetting shape). Born-red card holds the
  substrate-gate red until the deliberate completion flip.

## 💡 Session idea

💡 The three webhook kits (Stripe/GitHub/Slack) now share ~80% of their
scaffold by copy — the byte-reproducible allow-list `package.sh`, the
`_insecure_handler` HTTP test scaffold, the `normal_fire_pass`/`rejected_fire_pass`
verdict pair, and the PROVENANCE discipline (pinned per-fixture sha256 + a docs
citation per fact). Extract a tiny `candidates/_webhook-kit-core/` the kits
inherit — plus a `provenance_lint.py` that FAILS a kit whose fixture lacks a
pinned sha256 or a cited source — so kit N+3 (SNS? Twilio? Shopify?) is a
fixtures-and-scheme diff, not a re-implementation, and the honesty bar is
machine-enforced rather than reviewer-trusted. Pairs with a **"Webhook Verifier
Trio" bundle listing** (~$59 vs $87 buying all three) once GWTK + this Slack kit
go live behind the proven SWTK — one storefront page, three zips, the
cross-sell the intakes already name as first-ten channel 2.

## previous-session review

previous-session review: `.sessions/2026-07-17-restamp-current-state.md` (#218)
— it did the surgical `docs/current-state.md` HEAD restamp cleanly and proposed
a CI `LAST-VERIFIED-HEAD` guard so hand-maintained stamps fail loud instead of
rotting. Good instinct, and the same anti-rot principle is why THIS build never
hand-edits `OWNER-QUEUE.md`: it regenerates the queue from the §7 packet via
`scripts/derive_owner_queue.py`, so the owner's click list can't silently drift
from the product truth.
