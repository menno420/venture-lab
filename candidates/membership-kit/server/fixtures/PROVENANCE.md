# Stripe fixture provenance

These fixtures are real-shape `checkout.session.completed` **event** payloads
used by `../test_http_realpath.py` to drive the webhook over real HTTP. They are
committed so the payment path is tested against the exact bytes Stripe sends —
not a hand-simplified stand-in.

## Files

| File | What it is |
|------|------------|
| `checkout_session_completed.json` | The **real live shape**: top-level `data.object.customer_email` is `null`; the buyer's address is at `data.object.customer_details.email` (`jenny.rosen@example.com`). This is what a normal Stripe Checkout completion looks like. |
| `checkout_session_completed_legacy_email.json` | The legacy / guest-with-prefill case: `data.object.customer_email` is populated (`guest.buyer@example.com`) in addition to `customer_details.email`. Exercises the fallback extraction path. |

## The key real-shape fact this fix depends on

Live `checkout.session.completed` events carry **`customer_email: null`** at the
top level, with the buyer's email at **`customer_details.email`**. Code that only
reads `customer_email` grants nothing on a real payment. The fix prefers
`customer_details.email` and falls back to top-level `customer_email` (legacy).

Note: the real `object` discriminator value is the string `"checkout.session"`
(with a dot), not `checkout_session`.

## Field-name verification

Field names were verified against Stripe's own SDK source and the OpenAPI spec on
`raw.githubusercontent.com` (not paraphrased from memory):

- Checkout Session object fields (`customer_details`, `customer_email`, `id`,
  `object`, `payment_status`, `status`, `success_url`):
  https://raw.githubusercontent.com/stripe/stripe-go/master/checkout_session.go
- Event envelope fields (`type`, `data.object`, `api_version`, `livemode`):
  https://raw.githubusercontent.com/stripe/stripe-go/master/event.go
- Cross-checked against the Stripe OpenAPI spec:
  https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.json

`docs.stripe.com` returns **HTTP 403** through the agent proxy, so the published
web docs could not be fetched. The `stripe-go` SDK source (generated from the
same OpenAPI spec Stripe publishes) was used as the authoritative reference.

## Webhook signature scheme (used by the tests)

Stripe signs webhooks with a header:

```
Stripe-Signature: t=<unix_timestamp>,v1=<hex_hmac>
```

where `<hex_hmac>` is the hex-encoded **HMAC-SHA256** of the bytes
`"{t}.{raw_body}"` (the unix timestamp, a literal `.`, then the exact raw request
body bytes), keyed by the endpoint's `whsec_...` signing secret. A header may
carry multiple `v1=` signatures (secret rotation); a match against any one is
valid. Stripe also rejects timestamps outside a tolerance window (default 300s).

Scheme source:
https://raw.githubusercontent.com/stripe/stripe-go/master/webhook/client.go

`../app.py:verify_stripe_signature()` re-implements exactly this scheme using only
the Python standard library (`hmac`, `hashlib`, `time`) so the real signature path
is testable with a fake test secret and no live keys and no `stripe` package.
