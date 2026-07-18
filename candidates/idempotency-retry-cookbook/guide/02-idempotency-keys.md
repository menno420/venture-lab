# 2 · Idempotency keys: make the retry a no-op

Chapter 1's worst failure mode is the double charge: an ambiguous failure on a
non-idempotent write, retried, runs the side effect twice. The fix is not to
retry more carefully — it is to make the write *idempotent* so that a retry
literally cannot execute twice. That is what an idempotency key does, and this
chapter is how to build the server side correctly. The runnable sketch is
`recipes/idempotency_store.py`; the companion **Idempotency Key Test Kit** tests
these exact behaviours over HTTP against an endpoint you own.

## The contract in one paragraph

The client attaches a unique `Idempotency-Key` header to a mutating request. The
server, keyed on that value, performs the operation **at most once**: the first
request runs the side effect and stores its response; any later request with the
same key returns the *stored* response instead of running the side effect again.
A retry after an ambiguous failure is therefore safe — either the first attempt
never landed (the retry is the first real execution) or it did (the retry replays
the stored result). Either way the card is charged once.

That is the intent the IETF draft *The Idempotency-Key HTTP Header Field*
standardizes. The draft deliberately fixes the **header and the semantics**, not
one mandated status code for every edge — so the concrete behaviours below follow
the widely-deployed Stripe-style model, and you should match your own API's
documented codes where they differ. Say which model you implement; don't leave a
buyer guessing.

## Generating the key: the client's job

- **Unique per logical operation, stable across its retries.** Generate the key
  **once, before the first attempt** (a UUIDv4 is the common choice), and reuse
  the *same* key for every retry of that operation. A fresh key per retry defeats
  the whole mechanism — each looks like a new operation.
- **Opaque and high-entropy.** The server treats it as a bare token. Don't encode
  meaning a client could collide on; don't derive it from a low-entropy field two
  requests could share.

## Storing on the server: fingerprint + response

For each key the server stores two things:

1. **A fingerprint of the request** — a hash over the method, path, and a
   canonicalized body (`recipes/idempotency_store.py` uses SHA-256 over
   `method\0path\0canonical-json`, with sorted keys so key order and whitespace
   don't change the hash). This is what catches key reuse.
2. **The response it produced** — status, body, and any headers a replay must
   return byte-for-byte.

The reserve step must be **atomic**: exactly one concurrent caller may create the
record and become the one that runs the side effect. In the in-memory sketch that
is a dict insert; in production it is a Redis `SET key val NX` or a database
`INSERT ... ON CONFLICT DO NOTHING` / a unique constraint. Without atomicity, two
simultaneous retries both see "no record" and both charge — the exact bug the key
was supposed to prevent.

## The four rules the store enforces

The sketch models these; the test kit checks them:

1. **Same key + same request → replay.** Return the stored response; run the side
   effect **zero** additional times. A retry that mints a *new* resource id is a
   double side effect wearing a success code.
2. **Same key + a different request → mismatch.** The fingerprints differ, so the
   caller reused a key for a different operation. Reject it — **409 Conflict** or
   **422 Unprocessable Entity** in the Stripe-style model. Silently replaying the
   old response answers the wrong question; silently running the new body breaks
   the key's one-operation promise.
3. **Key seen, original still running → in-progress.** A concurrent retry arrives
   before the first attempt finished. It must hit an in-flight lock (Stripe
   documents a **409** here), not launch a second side effect. It retries and
   replays once the original completes.
4. **Expired key → treated as new.** Keys are retained for a TTL, not forever
   (Stripe documents a **24-hour** window). Retain at least as long as your
   client's entire retry budget could run, plus margin; after that the slot is
   reclaimed and a same-key request is a fresh operation.

## Scoping and expiry

- **Scope keys per account (and usually per endpoint).** Two tenants must be able
  to use the same key value without colliding; the stored key is effectively
  `(account, [endpoint], key)`.
- **Expire on a documented TTL.** Publish it, and make it comfortably longer than
  the longest retry schedule a client following chapter 4-5 could produce, so a
  legitimate slow retry still replays rather than re-charging.
- **Release failed reservations.** If the side effect fails *before* producing a
  storable response, release the reservation (`abort` in the sketch) so an honest
  retry can run — otherwise the operation is wedged behind a permanent
  in-progress lock. Only store a response you actually want replayed.

## The client half is just chapter 3-6

An idempotency key makes a `POST` safe to retry, but it doesn't tell the client
*when* to retry — that is the retryable-error classification (ch.3), the backoff
(ch.4), the budget and breaker (ch.5), and honoring `Retry-After` (ch.6). The key
and the retry policy are two halves of one design: `retry.is_idempotent_method`
in `recipes/retry.py` encodes exactly this — a bare `POST` is not retry-safe, but
a `POST` carrying an idempotency key is.

**Sources.** IETF draft *The Idempotency-Key HTTP Header Field*
(`draft-ietf-httpapi-idempotency-key-header`, IETF HTTP APIs WG) for the header
and at-most-once intent; Stripe's idempotency documentation
(`https://docs.stripe.com/api/idempotent_requests` and the idempotent-requests
guide) for the concrete fingerprint / 409-in-progress / 24-hour-expiry model;
RFC 9110 §9.2.2 (idempotent methods) and §15.5.10/§15.5.21 (409/422). Shipped
recipe: `recipes/idempotency_store.py`. Companion:
`candidates/idempotency-key-test-kit/README.md` @ `c1bf40a` and
`candidates/idempotency-key-test-kit/fixtures/PROVENANCE.md` @ `c1bf40a` in
`menno420/venture-lab`.
