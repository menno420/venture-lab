# Session — Shopify Webhook Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Fri Jul 17 23:51:33 UTC 2026
- **branch:** `claude/shopify-webhook-test-kit-2026-07-17` (PR TBD)
- **base:** `main@732ae02`
- **purpose:** build the **Shopify Webhook Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — the N+1 analog of the LIVE Stripe Webhook Test Kit and the
  just-shipped Slack Webhook Test Kit. A stdlib-only, account-free verifier for
  Shopify's webhook signing (`X-Shopify-Hmac-Sha256` = base64 of
  `HMAC-SHA256(client_secret, raw_request_body)` — base64, NOT hex, over the raw
  body DIRECTLY with no timestamp basestring, constant-time compare), shipped
  with vendored real-shape fixtures (`orders/create` / `products/update` /
  `app/uninstalled`), a correct example handler, an HTTP-layer real-path test
  suite (true-pass + tamper-fail + wrong-secret-fail + malformed-base64-fail), a
  byte-reproducible buyer bundle, and a §7 owner-gate publish packet. The build
  ENDS at a queued owner ⚑ publish click (rail 13 / CONSTITUTION §13) — no
  publish, no spend, no accounts performed by the seat.
- **session:** Mirrors the proven Stripe/GitHub/Slack kit scaffold exactly (file
  set, evidence bar, packaging, listing/vetting shape) with the Shopify-specific
  differences called out honestly: the digest is base64 (not hex like Slack's
  `v0=`), signed over the raw body with NO timestamp (so there is no
  stale/replay mode and no challenge handshake), and Shopify publishes no fixed
  known-answer HMAC constant (so the `vector` command is an honest kit-internal
  known-answer + cross-language parity proof, not a reproduction of a vendor
  constant). Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-17T23:51Z — Branch `claude/shopify-webhook-test-kit-2026-07-17` from
  origin/main (732ae02); collision check clean (`control/claims/` has no
  shopify-webhook-test-kit claim, no open PR covering it). Born-red card
  committed (first commit), pushed. Build begins.
