# Fixture provenance

The JSON files in this directory are **real-shape** Stripe event fixtures: every
field NAME and type was verified against Stripe's own SDK source, not written from
memory. The whole point of the kit is to test handlers against the bytes Stripe
actually sends — a hand-simplified stand-in would hide the exact gotchas the kit
exists to catch.

> `docs.stripe.com` returns **HTTP 403** through the agent proxy used to build
> this kit, so the authoritative reference is the `stripe-go` SDK source
> (generated from the same OpenAPI spec Stripe publishes) on
> `raw.githubusercontent.com`. Field names are copied from the Go struct
> `json:"..."` tags.

## Files

| File | Event type | Exercises |
|---|---|---|
| `checkout_session_completed.json` | `checkout.session.completed` | the null `customer_email` → `customer_details.email` gotcha |
| `checkout_session_completed_legacy_email.json` | `checkout.session.completed` | the legacy/guest path where top-level `customer_email` is populated and `customer_details` is null |
| `payment_intent_succeeded.json` | `payment_intent.succeeded` | a second high-value event, for handlers that key off the PaymentIntent |

## The real-shape fact the kit depends on

On a normal Checkout completion the top-level `customer_email` is **`null`**; the
buyer's email address is at `customer_details.email`. A handler that reads only
`event.data.object.customer_email` silently drops the sale. The legacy fixture
covers the older/guest-prefill case where `customer_email` IS set — a correct
handler must read `customer_details.email` first and fall back to `customer_email`.

## Field-name verification (stripe-go @ master)

Every field name in these fixtures was checked against these sources:

- CheckoutSession + CheckoutSessionCustomerDetails — `https://raw.githubusercontent.com/stripe/stripe-go/master/checkout_session.go`
- Event envelope (`id`, `object`, `api_version`, `created`, `type`, `livemode`, `pending_webhooks`, `request`, `data.object`) — `https://raw.githubusercontent.com/stripe/stripe-go/master/event.go`
- PaymentIntent — `https://raw.githubusercontent.com/stripe/stripe-go/master/paymentintent.go`
- OpenAPI spec (cross-check) — `https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.json`

Verified verbatim `json:` tags include: on the session object `customer_email`,
`customer_details` (sub-fields `address`, `business_name`, `email`,
`individual_name`, `name`, `phone`, `tax_exempt`, `tax_ids`), `success_url`,
`payment_status`, `status`, `amount_total`, `amount_subtotal`, `currency`, `mode`,
`customer`, `payment_intent`, `created`, `livemode`, `metadata`; on the envelope
`data.object` carries the resource (stripe-go `EventData` marshals its
`Raw json.RawMessage` to the wire name `object`); on the PaymentIntent `id`,
`object`, `amount`, `amount_received`, `currency`, `status`, `customer`, `created`,
`livemode`, `metadata`, `latest_charge`.

### What is illustrative, not verified

Field **names and types** are SDK-verified. The **values** (ids, the
`example.com`/`example.net` email addresses, amounts, timestamps, `api_version`
strings) are realistic illustrative examples, not captured from a live account.
`customer_details.address` is `null` (a valid real shape — Stripe returns null when
billing-address collection is off) so no address sub-field appears unverified. No
fixture contains any real customer data or secret.

## Webhook signature scheme

The kit signs each fixture with the real Stripe-Signature scheme, verified against
`https://raw.githubusercontent.com/stripe/stripe-go/master/webhook/client.go`:

- header: `Stripe-Signature: t=<unix_ts>,v1=<hex>`
- `<hex>` = lowercase hex HMAC-SHA256, key = the endpoint's `whsec_` secret,
  message = `f"{t}." + raw_body` (the exact request bytes)
- default timestamp tolerance: `300` seconds (`DefaultTolerance = 300 * time.Second`)
- multiple `v1=` values may appear during secret rotation; verify against any via a
  constant-time compare (`hmac.compare_digest`)
