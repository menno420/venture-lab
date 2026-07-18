# Idempotency Key Test Kit v0.1

Prove your API's `Idempotency-Key` handling is correct — that a safe retry
triggers the side effect **exactly once**, so a network blip never charges a
customer twice. Stdlib only, no dependencies, no vendor account, no live API.

This is **not** a webhook signature kit. It does not verify HMAC signatures — it
tests the **dedup / safe-retry contract** of an endpoint you own: the property
that makes `POST /charges` safe to retry. Behaviour specifics follow Stripe's
widely-used model (the header itself is the subject of the IETF draft *The
Idempotency-Key HTTP Header Field*); see `fixtures/PROVENANCE.md`.

## The five properties it checks

Point `ikt` at your endpoint and it reports PASS/FAIL for each:

1. **replay** — same key + same body → your endpoint replays the **stored
   original response** (same resource id); the side effect runs **once**. A
   retry that mints a *new* resource id is a double side effect (a double
   charge).
2. **mismatch** — same key + a **different** body → rejected (**409/422**).
   Accepting it silently returns a stale result or double-executes.
3. **distinct-keys** — two **different** keys + the same body → two independent
   resources. Collapsing them means you're keying on the body, not the
   `Idempotency-Key`.
4. **concurrent** — two in-flight requests with the same key → **one** side
   effect (an in-flight lock); the loser replays the stored response or gets a
   409. Two resources means no lock — a retry-storm double charge.
5. **missing-key** — no key header → your **documented** policy: `required`
   (reject 4xx) or `passthrough` (process without idempotency, 2xx). You tell
   the kit which; it never guesses silently.

## Quickstart

Zero setup — run the built-in demo first (no accounts, no endpoint of your own):

```
python3 ikt.py demo        # or: node ikt.js demo
```

It spins up two bundled reference stubs in-process — a **correct** one (all five
properties PASS) and a deliberately **naive** one with no dedup (the kit FLAGS
it) — and prints a server-side side-effect counter proving exactly-once. This is
the kit's value proof: it distinguishes correct idempotency from a broken
implementation.

Then point it at your own endpoint:

```
# start your app (or the bundled correct reference stub) listening locally:
python3 stub_handler.py 8000

# run all five properties against it:
python3 ikt.py check --url http://localhost:8000 --missing-key-mode required
```

Run a single property:

```
python3 ikt.py replay        --url http://localhost:8000
python3 ikt.py mismatch      --url http://localhost:8000
python3 ikt.py distinct-keys --url http://localhost:8000
python3 ikt.py concurrent    --url http://localhost:8000 --n 4
python3 ikt.py missing-key   --url http://localhost:8000 --mode required
python3 ikt.py list
```

`ikt.js` mirrors every command via Node (stdlib only, Node 14+):

```
node ikt.js check --url http://localhost:8000 --missing-key-mode required
node ikt.js demo
```

## What's inside

- The harness in two languages: `ikt.py` (Python) and `ikt.js` (Node), same
  commands (`check`, the five single-property checks, `demo`, `list`).
- A **correct** reference endpoint (`stub_handler.py`) you can adapt — an
  in-memory store keyed on `(method, path, Idempotency-Key)` holding a
  request-fingerprint + the stored response, a **per-key in-flight lock**,
  fingerprint-mismatch rejection (422), a configurable missing-key policy, and a
  `GET /_debug/side_effects` counter.
- A deliberately **naive** endpoint (`stub_handler_naive.py`) with no dedup —
  the "double charge on retry" bug in the flesh, shipped so the test suite can
  prove the harness catches it.
- Three docs-derived request fixtures (`charge_basic`, `charge_mismatch`,
  `order_create`) + `PROVENANCE.md` citing every behaviour and pinning a sha256
  per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 20 tests) — every
  request POSTed over real HTTP, with a side-effect counter that proves
  exactly-once on the correct stub and over-execution on the naive one.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## How it detects a double side effect

The kit does not need to see inside your server. It fires a retry and compares
the **response**: a correct idempotent endpoint replays the *stored* response, so
the resource id is identical; a naive one runs the operation again, so a *new*
id comes back. The bundled reference stubs additionally expose a
`GET /_debug/side_effects` counter that the kit's own test suite reads to assert
exactly-once directly — but the harness's verdicts against *your* endpoint come
purely from observing the HTTP responses, so it works against any implementation.

## Run the kit's own tests

```
python3 -m unittest -v
```

Every request is POSTed over actual HTTP to a reference stub on an ephemeral
port. All green = the kit is intact on your machine.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC — that's the Webhook Test
  Kits. This is a different problem class: dedup / safe-retry.
- It does **not** talk to Stripe or any live API, create an account, or move
  money. The `demo` runs entirely in-process.
- It does **not** validate your business logic — only the idempotency edge
  behaviour of your endpoint.
- It tests the **Stripe-style model**. The IETF draft standardises the header,
  not one mandated status code, so the exact codes (409/422 for a conflict, 400
  for a missing key under `required`) follow Stripe's documented behaviour. If
  your API documents different codes, adjust the expectation — the `missing-key`
  mode is configurable and the conflict check accepts 409 or 422.
- **Expiry** (stored responses time out — Stripe documents 24h) is documented in
  `GOTCHAS.md` but not asserted against a live endpoint (it would require
  waiting out the TTL). The in-process properties the kit *can* prove, it proves.
- The fixtures are **docs-derived** (cited file-by-file in `PROVENANCE.md`), not
  captures from a live API.

## Requirements

- Python 3.8+ (for `ikt.py`, the stubs, the tests) or Node 14+ (for `ikt.js`).
- No account, no `pip install`, no `npm install`.
- No secret values live in this kit; `.env.example` names optional config only.
