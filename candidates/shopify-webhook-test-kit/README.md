# Shopify Webhook Test Kit v0.1

Test your Shopify webhook handler against the requests Shopify really sends —
stdlib only, no dependencies, no Shopify store, no app install, no tunnel.

The kit signs real-shape Shopify webhook bodies with the actual
`X-Shopify-Hmac-Sha256` scheme (`base64(HMAC-SHA256(client_secret, raw_body))` —
**base64, not hex**, over the **raw request body directly**, with **no**
timestamp basestring) and fires them over HTTP at your local endpoint, then
checks your handler the way Shopify actually behaves: forged, unsigned,
tampered-body, and malformed-base64 signature, plus topic routing over the real
`X-Shopify-Topic` header. It catches the specific gotchas that repeatedly break
first Shopify integrations — not toy payloads written from memory.

## Quickstart

1. Start your handler (or the bundled example) listening locally. To run the
   bundled example handler:

   ```
   SHOPIFY_WEBHOOK_SECRET=your_webhook_secret python3 stub_handler.py 8000
   ```

   The secret is read from the environment — never hardcode it.

2. Prove the kit's own HMAC implementation against its pinned known-answer
   (offline, no server needed):

   ```
   python3 shwtk.py vector
   ```

3. List the bundled fixtures (and their topics):

   ```
   python3 shwtk.py list
   ```

4. Fire a correctly-signed webhook at your endpoint (PASS = handler returns
   2xx):

   ```
   SHOPIFY_WEBHOOK_SECRET=your_webhook_secret \
     python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create
   ```

5. Fire the hostile variants (PASS = handler REJECTS each with 4xx — proves
   verification is actually running and fails closed):

   ```
   python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --forge
   python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --unsigned
   python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --tamper
   python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --malformed
   ```

6. Fire the other topics (topic travels in the `X-Shopify-Topic` header, not the
   body):

   ```
   python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture products_update
   python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture app_uninstalled
   ```

### Node port

`shwtk.js` mirrors the same three commands via Node (stdlib only, Node 14+):

```
node shwtk.js vector
node shwtk.js list
node shwtk.js fire --url http://localhost:8000/webhooks/shopify --fixture orders_create
node shwtk.js fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --tamper
```

## What it checks

1. **fire** — your handler ACCEPTS a correctly-signed real webhook (HTTP 2xx),
   with the real header set (`X-Shopify-Hmac-Sha256`, `X-Shopify-Topic`,
   `X-Shopify-Shop-Domain`, `X-Shopify-Webhook-Id`, `X-Shopify-Api-Version`).
2. **fire --forge** — your handler REJECTS a wrong-secret webhook (4xx)
   instead of silently accepting it. A 2xx here means anyone who knows your
   URL can post fake webhooks.
3. **fire --unsigned** — your handler REJECTS a webhook with no
   `X-Shopify-Hmac-Sha256` header: a missing signature must fail closed.
4. **fire --tamper** — signs the real body, then mutates it before sending:
   your handler REJECTS it because it hashes the RAW bytes it received, not a
   re-parsed / re-serialised copy.
5. **fire --malformed** — sends a syntactically INVALID base64 in the signature
   header: your handler REJECTS it cleanly (4xx) without crashing. A naive
   `base64_decode(header)` with no error handling 500s (or drops the
   connection) here — bad input must never take your endpoint down.
6. **vector** — recomputes the kit's pinned known-answer (secret + body →
   `uhRiDuW3…`) and confirms the Python and Node ports agree. NOTE: Shopify
   does not publish a fixed known-answer constant, so this vector is the kit's
   own (see `fixtures/PROVENANCE.md`), not a reproduction of a vendor value.

## Run the kit's own tests

The kit ships with an HTTP-layer real-path test suite (every request is signed
and POSTed over real HTTP to a handler on an ephemeral port):

```
python3 -m unittest -v
```

## What it does NOT do

Be clear about the boundaries:

- It does **not** talk to the real Shopify API, create a store, install an app,
  or touch any live shop.
- It does **not** validate your business logic — only the request edge
  behaviour (HMAC verification, raw-body handling, malformed-input safety,
  topic routing).
- It is **not** a substitute for Shopify's CLI `app dev` webhook forwarding or a
  tunnel (Cloudflare / ngrok), which forward REAL webhooks from a live app —
  this kit is for testing your handler locally *before* (and without) wiring
  one.
- If you use Shopify's official libraries (`@shopify/shopify-api`,
  `shopify_api` gem), they can verify the HMAC for you — this kit is for
  handlers you hand-roll outside those helpers.
- The bundled fixtures are **reconstructed from Shopify's official
  documentation** (see `fixtures/PROVENANCE.md`), not captures from a live
  store; three topic shapes ship in v0.1 (`orders/create`, `products/update`,
  `app/uninstalled`).

## How Shopify signing differs from Slack/Stripe

- **Base64, not hex.** The header value is the base64 digest, not a lowercase
  hex string.
- **Raw body only — no timestamp.** Shopify hashes the raw body directly. There
  is no signed timestamp, so **no replay window** is baked into the signature
  (this kit has no `--stale` mode) and there is **no challenge handshake**.
  Dedupe replays on the `X-Shopify-Webhook-Id` header instead.
- **The topic is a header.** Routing keys off `X-Shopify-Topic`, not a `type`
  field in the body.

See `fixtures/PROVENANCE.md` for the docs citations behind every one of these
facts, and `GOTCHAS.md` for the failure modes each maps to.

## Requirements

- Python 3.8+ (for `shwtk.py`, `stub_handler.py`, tests) or Node 14+
  (for `shwtk.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit — the signing secret is read from an env
  var (`SHOPIFY_WEBHOOK_SECRET` by default).
