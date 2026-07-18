# Idempotency-Key gotchas — the one-page checklist

The failure modes that repeatedly break first `Idempotency-Key` implementations.
Each maps to a kit command that proves your endpoint is not making the mistake.
Behaviour follows Stripe's widely-used model; sources cited in
`fixtures/PROVENANCE.md`.

## 1. A retry must return the STORED response — not re-execute

The whole point of an idempotency key is that a client can safely retry a
request that timed out, and the operation happens **exactly once**. The classic
bug: on the second (retried) request the handler runs the operation again and
creates a second resource — a second charge. Correct behaviour is to look up the
key, find the stored original response, and **replay it byte-for-byte** without
touching the side effect.

**Check it:** `ikt replay` — fires the same key + same body twice and confirms
the second response carries the *same* resource id (one side effect), not a new
one.

## 2. Same key + a DIFFERENT body is an error (409/422), never a silent replay

Idempotency keys are **fingerprinted** against the first request's body. If a
client reuses a key with a *different* payload, that is a bug on the client's
side and must be surfaced — return **422** (or 409), not the old stored result
and not a fresh execution. Silently returning the stored response hides a real
mistake; silently executing double-charges. The fingerprint is over the raw
request body (this kit uses sha256 of the raw bytes).

**Check it:** `ikt mismatch` — sends the same key with a different body and
confirms a 409/422, not a 2xx.

## 3. Key the store on the header, per endpoint — not on the body

Idempotency must be keyed on the `Idempotency-Key` **header**, scoped per
endpoint (per method + path, and in real systems per account). Two *different*
keys with the same body are two distinct operations and must both execute. A
handler that dedupes on a body hash instead of the key will wrongly collapse two
legitimate requests into one — a **dropped** operation, the mirror image of the
double-charge bug.

**Check it:** `ikt distinct-keys` — two different keys + the same body must
produce two resources. (The bundled reference stub also keys on the path, so the
*same* key on `POST /charges` and `POST /orders` is two independent effects.)

## 4. Concurrency needs an in-flight lock

Two requests with the same key can arrive **at the same time** (the client's
retry races the original that was actually still in flight). Without a per-key
lock, both pass the "is it in the store yet?" check before either has written,
and both execute — a double charge under a retry storm. Correct handlers take a
per-key lock (or an atomic "insert if absent" in Redis/Postgres): the first
executes and stores; the second waits, finds the stored response, and replays it
(or returns **409 Conflict** while the original is still in progress).

**Check it:** `ikt concurrent --n 4` — fires several same-key requests
simultaneously and confirms only **one** side effect (one distinct resource);
409s on the losers are fine.

## 5. Decide the missing-key policy, and mind expiry + storage

- **Missing key.** A request with no `Idempotency-Key` needs a *documented*
  policy: reject it (400) if the key is mandatory, or process it without
  idempotency if the key is optional. Don't leave it undefined. `ikt missing-key
  --mode required|passthrough` checks the one you chose.
- **Expiry.** Stored responses **expire** (Stripe documents a 24-hour window). A
  key replayed *after* expiry will execute again — so idempotency protects
  against retries within the window, not indefinitely. This kit documents it but
  does not assert it against a live endpoint (it would require waiting out the
  TTL); size your store's TTL to your client's retry horizon.
- **Storage.** The reference stub uses an in-memory dict for clarity; a real
  multi-process deployment needs a shared store (Redis/Postgres) with an atomic
  insert and a TTL, or the in-flight lock in gotcha #4 does not hold across
  workers.

**Check it:** `ikt missing-key` for the policy; expiry/storage are design notes
(no live assertion) — see the store implementation in `stub_handler.py`.

---

Run all five at once with `ikt check --url … --missing-key-mode …`, and see them
distinguish a correct endpoint from a broken one with `ikt demo`.
