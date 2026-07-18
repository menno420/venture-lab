# Fixture provenance

**Honest statement up front:** the request bodies in this directory were
**reconstructed from Shopify's official published documentation**, not captured
from a live Shopify store. No Shopify store was created, no app was installed,
and no live webhook subscription was connected to build this kit (this repo's
no-new-accounts rule). Every field name, shape, and signing fact below is cited
to the Shopify docs page it was taken from, so a buyer can audit each claim
against Shopify's own documentation. Where a value is illustrative (a demo
order id, a demo shop domain), it carries a clearly-fake test value — never a
real credential, order, or customer.

> Fetched/reconstructed 2026-07-17 (UTC). Citations are to `shopify.dev`
> documentation pages by title + path. The payload shapes reproduced here are
> the documented example shapes on those pages, truncated to a representative
> subset of fields.

## The signature scheme (from Shopify's docs)

Source: **shopify.dev — "Subscribe to webhooks / Verify a webhook"**
(`https://shopify.dev/docs/apps/build/webhooks/subscribe/https#verify-a-webhook`):

- Header: `X-Shopify-Hmac-SHA256: <base64>` where `<base64>` is the
  **base64-encoded** (NOT hex) **HMAC-SHA256** digest of the **raw request
  body**, keyed with **your app's client secret** (the "API secret key" for
  webhooks created via the API; or the shared secret shown in the Shopify admin
  for admin-created webhooks). HTTP header names are case-insensitive
  (RFC 7230 §3.2); Shopify documents the header as `X-Shopify-Hmac-SHA256` and
  this kit sends `X-Shopify-Hmac-Sha256` — the same header.
- **No basestring, no timestamp.** Unlike Slack (`v0:{timestamp}:{body}`) and
  Stripe (`t=…,v1=…`), the Shopify HMAC is computed over the **raw request body
  bytes directly**. There is no signed timestamp and therefore **no replay
  window baked into the signature** — so this kit has **no `--stale` mode** and
  Shopify webhooks have **no challenge/handshake** (so no challenge command
  either). Shopify's own guidance for duplicate/replay handling is to **dedupe
  on the `X-Shopify-Webhook-Id` header**, not a timestamp check.
- **Raw body, before parsing.** Shopify's docs are explicit: "Capture the raw
  body before it's parsed" — parsing then re-serialising the JSON changes the
  bytes and breaks verification. Hash the exact bytes received.
- **Constant-time compare.** Shopify's reference snippet compares with
  `crypto.timingSafeEqual()` — never `==`. This kit's example handler decodes
  the base64 header and compares the raw digest bytes with
  `hmac.compare_digest`.

### No vendor known-answer constant — the kit's `vector` is its own

Shopify's docs publish the verification **method** (code in Node/Ruby/etc.) but
**do not publish a fixed known-answer example** (a specific secret + specific
body + expected base64 output) the way Slack's "Verifying requests from Slack"
page does. Rather than fabricate a Shopify-attributed constant, this kit ships a
**kit-internal** known-answer vector, honestly labelled as such:

- secret: `shwtk_test_client_secret_v0_1_not_a_real_secret` (a fake test value)
- body: `{"id":123456789,"topic":"orders/create","note":"shwtk known-answer vector"}`
- expected `X-Shopify-Hmac-Sha256`: `uhRiDuW3C3+o+mLcijsFK2jv0FwIloa+C4O5MQzK6w0=`

`shwtk.py vector` and `shwtk.js vector` recompute this locally and compare, so a
buyer can prove the kit's HMAC-SHA256 + base64 path end to end and confirm the
Python and Node ports agree byte-for-byte — offline, in one command. It is a
**self-consistency + cross-language** proof, not a reproduction of a
Shopify-published value (Shopify publishes none).

## The fixtures (reconstructed from documented example shapes)

| File | Content-Type of a real request | X-Shopify-Topic | Reconstructed from (shopify.dev) | sha256 of the vendored file |
|---|---|---|---|---|
| `orders_create.json` | `application/json` | `orders/create` | "Webhooks / webhook topics — `orders/create`" + the REST Admin **Order** resource shape (`id`, `admin_graphql_api_id`, `name`, `email`, `financial_status`, `line_items[]`, `customer`, `shipping_address`) | `5791e615be3421d64fdec3ad815fa1b8c4ef9d02918ed6d31d5766645052bd01` |
| `products_update.json` | `application/json` | `products/update` | "Webhooks / webhook topics — `products/update`" + the REST Admin **Product** resource shape (`id`, `title`, `handle`, `status`, `variants[]`, `options[]`, `images[]`) | `0f3e829593ba792a823152d81b76a5ea0e75c3ae86cd04b7c5cd061669f9302a` |
| `app_uninstalled.json` | `application/json` | `app/uninstalled` | "Webhooks / mandatory + app lifecycle topics — `app/uninstalled`" — the payload is the **Shop** object (`id`, `name`, `myshopify_domain`, `plan_name`, …); Shopify delivers this so your app can purge the shop's data | `a3b39559c3b40a57ff1414b4467649ddfa9240885ab97f1a04f0901b1d7713f8` |

`MANIFEST.json` (kit-authored, not vendored — sha256
`9111a4753640e74c721766dd3dd39ac75548844cb06730004b10227ba3e9aed2`) maps each
fixture stem to the `Content-Type` **and** the `X-Shopify-Topic` a real Shopify
webhook of that shape carries. Shopify puts the topic in a **header**, not the
body, and the signature covers the **raw body as sent**, so the kit needs this
manifest to fire each fixture the way Shopify would deliver it.

## The other webhook headers (from Shopify's docs)

Shopify attaches these headers to every webhook POST (the kit models them on
`fire`, with illustrative values):

- `X-Shopify-Topic` — the topic, e.g. `orders/create`.
- `X-Shopify-Hmac-Sha256` — the base64 HMAC-SHA256 described above.
- `X-Shopify-Shop-Domain` — the sending shop, e.g.
  `example-store.myshopify.com`.
- `X-Shopify-Webhook-Id` — a unique delivery id; **dedupe on it** because
  Shopify retries and re-sends the same id.
- `X-Shopify-Api-Version` — the API version of the payload, e.g. `2026-07`.
- (`X-Shopify-Event-Id`, `X-Shopify-Triggered-At` also appear on real
  deliveries; not required for verification and not modelled here.)

Content-Type of a Shopify webhook delivery is `application/json`; the body is
the JSON document, and the HMAC covers those raw JSON bytes.

## What is illustrative, not wire-captured

Payload field names and structure are reconstructed from Shopify's published
example shapes (cited above), truncated to a representative subset; they were
**not** captured from a live Shopify delivery in this build, and no live store,
app, or webhook subscription was created to produce them. Ids, tokens, emails,
domains, and the demo `X-Shopify-Webhook-Id` are clearly-fake test values —
none is a real credential, order, customer, or shop. The `.env.example` names
the environment variable to hold your real secret; no secret value ships in
this kit.
