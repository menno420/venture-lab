# Stripe Webhook Test Kit v0.1

Test your Stripe webhook handler against the event shapes Stripe really sends — stdlib only, no dependencies.

The kit signs vendored real-shape Stripe events with the actual `Stripe-Signature`
scheme and fires them over HTTP at your local webhook endpoint, then checks your
handler the way Stripe actually behaves. It catches the specific gotchas that
repeatedly break first Stripe integrations — not toy payloads written from memory.

## Quickstart

1. Start your webhook handler (or the bundled example) listening locally. To run
   the bundled example handler:

   ```
   SWTK_WEBHOOK_SECRET=whsec_your_signing_secret python3 stub_handler.py 8000
   ```

   The signing secret is read from the environment — never hardcode it.

2. List the bundled fixtures:

   ```
   python3 swtk.py list
   ```

3. Fire a correctly-signed event at your endpoint (PASS = handler returns 2xx):

   ```
   SWTK_WEBHOOK_SECRET=whsec_your_signing_secret \
     python3 swtk.py fire --url http://localhost:8000/webhook --fixture checkout_session_completed
   ```

4. Fire a forged event (PASS = handler REJECTS it with 4xx — proves signature
   verification is actually running):

   ```
   SWTK_WEBHOOK_SECRET=whsec_your_signing_secret \
     python3 swtk.py fire --url http://localhost:8000/webhook --fixture checkout_session_completed --forge
   ```

5. Show where the buyer email actually lives on an event:

   ```
   python3 swtk.py check-email --fixture checkout_session_completed
   ```

6. Lint a `success_url` for placeholders Stripe won't expand:

   ```
   python3 swtk.py lint-url "https://you/success?session_id={CHECKOUT_SESSION_ID}"
   ```

### Node port

`swtk.js` mirrors the same four commands via Node (stdlib only, Node 14+):

```
node swtk.js list
node swtk.js fire --url http://localhost:8000/webhook --fixture checkout_session_completed
node swtk.js check-email --fixture checkout_session_completed
node swtk.js lint-url "https://you/success?session_id={CHECKOUT_SESSION_ID}"
```

## What it checks

1. **fire** — your handler ACCEPTS a correctly-signed real event (HTTP 2xx).
2. **fire --forge** — your handler REJECTS a forged/badly-signed event (HTTP 4xx)
   instead of silently accepting it. A 2xx here means anyone who knows your
   endpoint URL can post fake events.
3. **check-email** — the buyer email is read from `customer_details.email`;
   top-level `customer_email` is `null` on a normal Checkout completion (the #1
   gotcha this kit exists for).
4. **lint-url** — your `success_url` uses ONLY `{CHECKOUT_SESSION_ID}`. Anything
   else (e.g. `{CHECKOUT_EMAIL}`) is a placeholder Stripe never expands, so it
   lands in the buyer's browser verbatim.

## Run the kit's own tests

The kit ships with an HTTP-layer real-path test suite (every event is signed and
POSTed over real HTTP to a handler on an ephemeral port):

```
python3 -m unittest -v
```

## What it does NOT do

Be clear about the boundaries:

- It does **not** talk to the real Stripe API, your database, or any live account.
- It does **not** validate your business logic — only the webhook edge behaviour.
- It is **not** a "battle-tested payments" library, and **not** a substitute for
  Stripe's own CLI (`stripe listen`), which forwards real events from your account.

What it *does* is check the specific real-shape gotchas that repeatedly break first
Stripe integrations: the null `customer_email`, an invalid `success_url`
placeholder, missing signature verification, and the timestamp tolerance.

## Where the shapes come from

See `fixtures/PROVENANCE.md` — every field name and type in the fixtures was
verified against Stripe's own SDK source, and the signature scheme against
`stripe-go`'s `webhook/client.go`. No fixture contains real customer data.

## Requirements

- Python 3.8+ (for `swtk.py`, `stub_handler.py`, tests) or Node 14+ (for `swtk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this repo — the signing secret is read from an env var.
