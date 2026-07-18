# Quickstart — Shopify Webhook Test Kit v0.1

Three minutes from unzip to a green check on your own handler. Stdlib only —
no `pip install`, no `npm install`, no Shopify store.

## 0. Prove the kit itself (offline, no server)

```
python3 shwtk.py vector      # or: node shwtk.js vector
```

Expect `PASS` — the kit recomputes its pinned known-answer (a fixed secret +
body → `uhRiDuW3…`) and confirms the Python and Node ports agree. (Shopify
publishes no fixed known-answer constant of its own, so this vector is the
kit's — see `fixtures/PROVENANCE.md`.) If this fails, re-download the kit.

## 1. Set your webhook secret in the environment

Copy `.env.example` to `.env` and fill in your app's **webhook signing secret**
— your app's **client secret** (Partners dashboard → your app → Client
credentials) for API-created webhooks, or the shared secret shown in the
Shopify admin for admin-created webhooks. Then export it — the kit reads the
NAME from the env and never stores the value:

```
export SHOPIFY_WEBHOOK_SECRET=your_webhook_secret_here
```

(It is NOT the Admin API access token `shpat_…` and NOT the API key.)

## 2. Start a handler

Either your own handler, or the bundled correct example:

```
SHOPIFY_WEBHOOK_SECRET=$SHOPIFY_WEBHOOK_SECRET python3 stub_handler.py 8000
```

It listens on `http://127.0.0.1:8000`.

## 3. Fire the happy path

```
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create
```

Expect `PASS` (HTTP 2xx). Try the other topics too:

```
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture products_update
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture app_uninstalled
```

## 4. Fire the hostile path (this is the point)

Each of these must be REJECTED (4xx) by a correct handler:

```
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --forge
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --unsigned
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --tamper
python3 shwtk.py fire --url http://localhost:8000/webhooks/shopify --fixture orders_create --malformed
```

If any of these prints `FAIL`, your handler is accepting requests it should
refuse (or crashing on bad input) — see `GOTCHAS.md` for the fix.

## 5. Run the kit's own test suite

```
python3 -m unittest -v
```

Every request is signed with the real scheme and POSTed over actual HTTP to a
handler on an ephemeral port. All green = the kit is intact on your machine.

---

Next: read `GOTCHAS.md` (one page, five failure modes) and adapt
`stub_handler.py` into your framework of choice.
