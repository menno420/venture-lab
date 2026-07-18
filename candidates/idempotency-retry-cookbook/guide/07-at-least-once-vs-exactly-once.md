# 7 · At-least-once vs exactly-once: dedup at the consumer

Everything so far has been about the *caller* retrying safely. This chapter is the
other side: when you are the *consumer* of an at-least-once channel — a message
queue, a webhook, an event stream — retries elsewhere in the system mean you
**will** receive duplicates, and your job is to process each logical event once
anyway. The good news: it's chapter 2's idea, moved to the receiving end.

## The three delivery guarantees

- **At-most-once** — every message delivered zero or one times. No duplicates,
  but messages can be *lost* (a crash after dequeue, before processing, drops
  it). Rarely acceptable for anything that matters.
- **At-least-once** — every message delivered one or more times. Nothing is lost,
  but you can get **duplicates** (the producer retried, or the broker redelivered
  because your ack was lost). This is what almost every real queue and webhook
  system gives you: SQS, most Kafka setups, Stripe/GitHub/Shopify webhooks.
- **Exactly-once *delivery*** — the appealing fiction. True exactly-once delivery
  across an unreliable network is, in the general case, impossible: the same
  ambiguous-ack problem from chapter 1 means the sender can never be *sure* the
  receiver got it, so a correct sender must sometimes resend. What real systems
  provide is **effectively-once *processing*** — at-least-once delivery plus
  consumer-side deduplication so duplicates are harmless.

The practical stance: **assume at-least-once, design the consumer to be
idempotent.** Don't chase a delivery guarantee the network can't give; make
duplicate delivery a non-event.

## Dedup at the consumer is idempotency, received-side

The mechanism is chapter 2 with the roles swapped. Every message needs a **stable
dedup id** — a unique identifier that is the *same* across redeliveries of the
same logical event:

- A queue message id or a producer-assigned message id (many brokers provide
  one).
- A webhook event id (Stripe `evt_…`, GitHub's `X-GitHub-Delivery`, etc.) — the
  same id is resent on redelivery.
- Failing those, a deterministic hash of the event's identifying content — the
  same `fingerprint(...)` idea from `recipes/idempotency_store.py`.

Then the consumer keeps a **seen-set** (a table/store of processed ids) and, for
each message: check if the id is already processed; if so, ack and drop it; if
not, process it, record the id, ack. The `IdempotencyStore` sketch models exactly
this pattern — `begin` reserves the id (so a concurrent duplicate hits the
in-flight lock), the work runs once, `complete` records it, and a later duplicate
replays/drops instead of reprocessing.

## Make the check-and-record atomic with the work

The subtle failure: check "seen?", it's not, start processing, crash before
recording the id → the redelivery reprocesses. To be truly effectively-once, the
"record the dedup id" and the "commit the side effect" must be **atomic** — ideally
the same database transaction:

```
BEGIN
  INSERT dedup_id  -- unique constraint; fails if already processed
  <do the side effect>
COMMIT             -- both land or neither does
```

If the insert violates the unique constraint, this is a duplicate — roll back and
ack. If the transaction commits, the work and its dedup record are durable
together, so no redelivery can double-process. When the side effect is in a
*different* system than the dedup store (you can't share a transaction), fall back
to: reserve the id first (in-flight lock), make the side effect itself idempotent
(an idempotency key on the downstream call — chapter 2 again), and record on
success. Idempotency composes; that's why it's the whole book's spine.

## Ack semantics tie it together

- **Ack only after the work + dedup record are durable.** Ack-then-process loses
  messages on a crash (you promised the broker you were done). Process-then-ack is
  the at-least-once contract — and the reason you get duplicates (a lost ack ⇒
  redelivery), which is exactly what the dedup handles.
- **Duplicates from a lost ack are normal, not a bug.** Your consumer's
  correctness must not depend on acks never being lost; it depends on the
  seen-set.

## The one-line rule

> Treat every consumer as if it will see every message more than once, and make
> the second time a no-op. At-least-once delivery + an idempotent consumer =
> effectively-once processing — which is the strongest guarantee you can actually
> keep.

**Sources.** RFC 9110 §9.2.2 (idempotency as the property that makes repeats
safe); Google, *Site Reliability Engineering*, "Data Processing Pipelines" /
"Managing Critical State" on at-least-once and consumer dedup; the widely
documented webhook-redelivery model with a stable delivery/event id (Stripe
`evt_…` idempotent event handling; GitHub `X-GitHub-Delivery`) as public examples
of stable dedup ids; the general distributed-systems result that exactly-once
*delivery* is unattainable while effectively-once *processing* is achievable via
idempotent consumers. Shipped recipe: `recipes/idempotency_store.py` (the same
`begin`/`complete` reserve-and-record used consumer-side).
