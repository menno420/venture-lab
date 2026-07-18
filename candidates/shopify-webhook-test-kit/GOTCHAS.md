# Shopify webhook-signing gotchas — the one-page checklist

The failure modes that repeatedly break first Shopify integrations. Each maps
to a kit command that proves your handler is not making the mistake. Sources:
Shopify's own docs, cited in `fixtures/PROVENANCE.md` (reconstructed
2026-07-17).

## 1. Verify the RAW body bytes — base64, NOT hex, constant-time

`X-Shopify-Hmac-Sha256` is the **base64** (not hex) HMAC-SHA256 of the raw
request body, keyed with your app's **client secret** (the API secret key, or
the shared secret shown in the admin). The classic bugs:

- **Re-serialized / re-parsed body.** Parsing the JSON and re-encoding it before
  hashing produces different bytes (key order, whitespace, unicode escaping).
  Shopify's docs say it outright: capture the raw body **before** it's parsed,
  and hash exactly those bytes.
- **Hex instead of base64.** Slack/GitHub use hex; Shopify uses base64. A hex
  digest never matches Shopify's header.
- **`==` comparison.** Use a constant-time compare
  (`hmac.compare_digest`, `crypto.timingSafeEqual`), never `==`.
- **Wrong secret.** The webhook secret is your app's client secret (or the
  admin's shared secret) — NOT the Admin API access token (`shpat_…`) and NOT
  the API key.

**Check it:** `shwtk fire --forge` (wrong secret, must be rejected),
`shwtk fire --tamper` (body mutated after signing, must be rejected), and
`shwtk vector` (proves the kit's own base64 HMAC path + Python/Node parity).

## 2. There is NO timestamp — dedupe on the webhook id, don't look for a clock

Unlike Slack (which signs `v0:{timestamp}:{body}` and wants a ±300s window) and
Stripe (`t=…,v1=…`), Shopify signs the **raw body only**. There is no timestamp
in the signature and **no replay window to enforce** — so don't waste time
looking for one, and don't reject on a missing timestamp header. Shopify DOES
retry deliveries, so the real duplicate-handling job is to **dedupe on the
`X-Shopify-Webhook-Id` header** (the same id is re-sent on a retry).

**Check it:** the bundled `stub_handler.py` returns the `X-Shopify-Webhook-Id`
so you can wire your own dedupe; there is deliberately no `--stale` mode because
Shopify's scheme has no timestamp (see `fixtures/PROVENANCE.md`).

## 3. Fail CLOSED on a missing signature header

If a request arrives with no `X-Shopify-Hmac-Sha256`, it did not come from
Shopify — reject it (401). The common bug is `if header: verify()`, which
silently accepts anything unsigned. A configured webhook ALWAYS carries the
HMAC header.

**Check it:** `shwtk fire --unsigned` (no signature header — must be rejected
with 4xx).

## 4. Don't crash on a malformed signature header

A signature header that isn't valid base64 is hostile input, not a server bug.
If you call `base64_decode(header)` with no error handling, bad input throws and
your endpoint 500s (or drops the connection) — a denial-of-service anyone can
trigger. Decode defensively and return 401 on garbage.

**Check it:** `shwtk fire --malformed` (an invalid-base64 header — must be a
clean 4xx, never a 5xx crash or a dropped connection).

## 5. Route on the TOPIC header, and ack fast

Shopify puts the event type in the `X-Shopify-Topic` **header**
(`orders/create`, `products/update`, `app/uninstalled`, …), not a field in the
body. Route on the header **after** verifying the signature. Shopify expects a
fast 2xx and **retries** anything it doesn't get one for — so acknowledge
immediately, do heavy work out-of-band, and dedupe on `X-Shopify-Webhook-Id`.
Also handle `app/uninstalled` (a mandatory lifecycle topic): it's your cue to
purge the shop's data.

**Check it:** `shwtk fire --fixture products_update` and
`--fixture app_uninstalled` (both delivered with the real `X-Shopify-Topic`
header); the bundled `stub_handler.py` acks 2xx and echoes the routed topic.
