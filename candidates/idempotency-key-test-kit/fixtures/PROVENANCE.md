# Fixture provenance

**Honest statement up front:** the request bodies in this directory are
**docs-derived** — reconstructed from the documented request shapes in Stripe's
API / idempotency documentation — **not** captured from a live API. No account
was created, no API key was used, and no real charge, order, or customer was
created to build this kit (this repo's no-new-accounts rule). Every idempotency
behaviour this kit checks is cited below to a public source, so a buyer can audit
each claim. Where a value is illustrative (a demo amount, a fake token, a demo
customer ref) it carries a clearly-fake test value — never a real credential.

> Reconstructed 2026-07-18 (UTC). Payload shapes are representative subsets of
> the documented example shapes; they are REQUEST bodies (POST payloads), not
> webhook deliveries.

## Honest scope: whose model does this kit test?

There are two relevant sources, and they cover different things:

- **The IETF draft — "The Idempotency-Key HTTP Header Field"**
  (`draft-ietf-httpapi-idempotency-key-header`, IETF HTTP APIs working group).
  This standardises the **header name** (`Idempotency-Key`) and the *intent*: a
  client attaches an idempotency key so that retrying a request is safe (the
  server performs the operation at most once for a given key). Crucially, the
  draft is deliberately **light on exact status codes** — it establishes the
  header and the semantics, not a single mandated error code for every edge.

- **Stripe's idempotency documentation** (`https://docs.stripe.com/api/idempotent_requests`
  and the idempotency guide). Stripe is the most widely-deployed concrete
  implementation of this header, and its behaviour is what most developers mean
  by "idempotency keys". Its documented model:
  - Sending the **same key + same request** returns the **stored original
    response** (the operation is not performed a second time).
  - Reusing a key with a **different request body** returns an **error** (the
    keys are fingerprinted against the first request's parameters).
  - Keys are **scoped per account/endpoint** and stored responses **expire**
    (Stripe documents a 24-hour retention window).
  - Concurrent requests with the same key are handled with an in-flight lock
    (Stripe documents returning a **409 Conflict** while an original request is
    still in progress).

**This kit tests the Stripe-style model and says so.** Where a specific status
code is asserted (409/422 for a key-reuse conflict, 400 for a missing key under
a `required` policy), that follows Stripe's widely-used behaviour, not a hard
requirement of the IETF draft — a buyer whose API documents *different* codes
should adjust the expectation (the harness's `missing-key` mode is already
configurable for exactly this reason, and the conflict check accepts either 409
or 422). The kit is deliberately honest that "correct idempotency" here means
"correct per the documented Stripe-style contract", not "the one true RFC".

## The properties this kit checks (and their sources)

| Property | What the kit asserts | Source |
|---|---|---|
| **replay** | same key + same body ⇒ the **stored original response** is replayed (same resource id); the side effect runs **once** | Stripe: "sending the same idempotency key… returns the same result" |
| **mismatch** | same key + a **different** body ⇒ rejected (**409/422**) | Stripe: keys are fingerprinted; reuse with different params is an error |
| **distinct-keys** | two **different** keys + same body ⇒ two independent resources | Stripe: idempotency is keyed on the header, per endpoint |
| **concurrent** | two in-flight same-key requests ⇒ **one** side effect (in-flight lock; loser replays or gets 409) | Stripe: concurrent requests return 409 while the original is in progress |
| **missing-key** | no key ⇒ your **documented** policy (`required` ⇒ 4xx, or `passthrough` ⇒ 2xx) | Configurable — the IETF draft does not mandate one behaviour |

## The fixtures (docs-derived request shapes)

| File | Method · path | Role | sha256 of the vendored file |
|---|---|---|---|
| `charge_basic.json` | `POST /charges` | primary payload — the safe-retry / replay / concurrency subject; shape follows Stripe's Charge create params (`amount`, `currency`, `source`, `description`, `metadata`) | `7f4414be99faac83cd2c9171973ebdb00a5a1519bffe5fb5bdd2cb23508b8c40` |
| `charge_mismatch.json` | `POST /charges` | a **different body** on the **same** endpoint (a different `amount`) — the same-key-different-body conflict subject | `aca5f89df96715633bb9a671a8991f00bcdd3074b0950a9ea41e1f3818634994` |
| `order_create.json` | `POST /orders` | a **second endpoint** — demonstrates that keys are scoped per (method, path) | `cc655285cd52c37b532fc5863245f4b24e86a220bea7a1a391e0e69d71a4d53d` |

`MANIFEST.json` (kit-authored, not vendored — sha256
`51910067e9b24d71e640864ed937687d6422b07673882306c606626dbec073cd`) maps each
fixture stem to the HTTP method, path, and Content-Type a real request of that
shape carries. The `Idempotency-Key` travels in the request **header** the
client sends; the endpoint keys its store on **(method, path, key)**, so the
manifest gives the harness the method + path to fire each fixture at.

## What is illustrative, not wire-captured

Field names and structure are reconstructed from the documented example shapes,
truncated to a representative subset; they were **not** captured from a live API
call, and no account, key, charge, order, or customer was created to produce
them. Amounts, tokens, customer refs, and order refs are clearly-fake test
values — none is a real credential or record. The reference stubs
(`stub_handler.py` / `stub_handler_naive.py`) are the kit's own code, not vendor
code; the naive stub exists specifically so the test suite can prove the harness
catches a broken (no-dedup) implementation. The `.env.example` names optional
configuration only; no secret value ships in this kit.
