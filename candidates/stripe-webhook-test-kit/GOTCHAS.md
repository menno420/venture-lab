# Stripe webhook gotchas checklist

The traps that break first Stripe integrations, and the fix for each. One screen.

1. **`customer_email` is null on `checkout.session.completed`.**
   On a normal Checkout completion the top-level `customer_email` is `null`; the
   buyer's address is at `customer_details.email`. Reading only `customer_email`
   silently drops the sale.
   **Fix:** read `customer_details.email` first, fall back to `customer_email`.

2. **`success_url` only expands `{CHECKOUT_SESSION_ID}`.**
   Any other placeholder (e.g. `{CHECKOUT_EMAIL}`) is passed through literally —
   the buyer's browser lands on a URL with a raw `{CHECKOUT_EMAIL}` in it.
   **Fix:** use only `{CHECKOUT_SESSION_ID}`, then resolve the buyer server-side
   from the session id.

3. **Verify the `Stripe-Signature` header.**
   It is HMAC-SHA256 over `"{t}." + raw_body`, keyed by your `whsec_` secret. A
   handler that skips verification accepts forged events from anyone who knows the
   endpoint URL.
   **Fix:** recompute the HMAC, constant-time compare against each `v1=`, reject on
   mismatch.

4. **Enforce the 300-second timestamp tolerance.**
   Without it, a captured request can be replayed indefinitely.
   **Fix:** reject events whose `t=` timestamp is more than 300s from now.

5. **Sign/verify over the RAW request bytes.**
   Re-serialising the JSON (different key order or whitespace) changes the bytes
   and breaks the signature.
   **Fix:** verify against the exact body received; do not parse-then-reserialise
   before verifying.

6. **Return 2xx fast, and process idempotently.**
   Stripe retries on any non-2xx, so slow or failing handlers get the same event
   again.
   **Fix:** acknowledge quickly, dedupe on `event.id`, and do heavy work
   out-of-band.
