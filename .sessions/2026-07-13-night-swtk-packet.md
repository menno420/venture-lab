# Session — Night run: Stripe Webhook Test Kit catalog parity (ORDER 008, PRODUCT #4)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #4 of the 2026-07-13 night run — assess whether the Stripe Webhook Test Kit ($29) needs a publish click queued, and bring it to catalog parity with the packet-era products (dist freshness proof, ARTIFACT sha line, listing parity) WITHOUT queueing a duplicate click if it is already live.
- **started (date -u):** Mon Jul 13 01:36:24 UTC 2026
- **closed (date -u):** (in progress)

## Scope

- Verdict first: is SWTK already published/live? (`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md` says yes — verify and cite before doing anything.)
- If live: NO §7 packet unless the derive grammar supports a no-click disposition (read `scripts/derive_owner_queue.py` first); parity work only — double rebuild + sha compare, test suite run, listing-vs-artifact check, clean-dir unzip + secret scan, ARTIFACT sha line in the launch docs.
- Landing per `docs/products/TEMPLATE.md`: born-red card first, claim second, work commits with evidence, strict check, ender flip + claim delete, PR READY, ≤2 CI polls, leave OPEN.
