# 1 · Why naive retries are dangerous

A network call failed. The obvious fix is to try again. That single instinct,
applied without the guard rails in this cookbook, is how a payment gets charged
twice, how a queue quietly duplicates every message under load, and how a brief
blip on one dependency becomes a self-inflicted outage across your whole fleet.
This chapter is the threat model; the rest of the book is the defenses.

## The retry looks safe because the failure lies to you

The core problem: **a failed response is not the same as a failed operation.**
When a `POST /charges` call times out, exactly one of two things happened, and
the client cannot tell which:

1. the request never reached the server (safe to retry), or
2. the request reached the server, the side effect ran, and the *response* was
   lost on the way back (retrying charges the card again).

A timeout, a dropped connection, a 502 from a load balancer that already
forwarded your request upstream — all of these look identical to the caller and
all can hide a side effect that already happened. This is why "just retry on
error" is unsafe for any request that isn't naturally idempotent: the ambiguous
failure is the *common* case, not the edge case.

## Three failure modes

**Double side effects (the double charge).** Retrying a non-idempotent write
after an ambiguous failure runs the side effect twice: two charges, two orders,
two shipping labels, two "welcome" emails. The fix is not "retry less" — it is to
make the write *idempotent* so a retry is a no-op, which is exactly what an
idempotency key buys you (chapter 2).

**Retry storms (the thundering herd).** A dependency slows down. Every client
times out at roughly the same moment and retries at roughly the same moment. The
retries land as a synchronized spike — often *larger* than the original traffic,
because each caller now sends its original request plus its retries. The
dependency, already struggling, now gets hit harder, so more calls fail, so more
retries fire. Without jitter (chapter 4), retry budgets (chapter 5), and a
circuit breaker (chapter 5), a recoverable slowdown becomes a full outage that
the retries themselves sustain. Google's SRE book calls this out directly:
retries stack multiplicatively across the layers of a system, so a naive retry at
each of three layers can amplify load by an order of magnitude.

**Wasted work on errors that will never succeed.** Retrying a `400 Bad Request`
or a `403 Forbidden` cannot help — the request is malformed or unauthorized and
will fail identically every time. Retrying it just burns your retry budget,
delays the inevitable error the caller needs to see, and, at scale, looks like an
attack on your own dependency. Retryability is a property of the *error*, not a
default (chapter 3).

## What "safe retry" actually requires

Retrying safely is not one trick; it is a small stack of cooperating decisions,
and this cookbook is one chapter per layer:

- **Make the write idempotent** so a retry can't double-execute — idempotency
  keys, server-side (ch.2).
- **Retry only retryable errors** — 429/408 and 5xx and transport failures;
  never an ordinary 4xx (ch.3).
- **Space the retries with backoff + jitter** so they don't resynchronize into a
  herd (ch.4).
- **Cap the total retry effort** with a retry budget and a circuit breaker so a
  broad failure can't turn your fleet into the load that keeps it down (ch.5).
- **Honor the server's `Retry-After`** instead of guessing when it told you when
  (ch.6).
- **Design the consumer to dedup**, because at-least-once delivery means
  duplicates are a *when*, not an *if* (ch.7).

The dangerous version skips all six and just loops on failure. Every property in
this book exists because one of those three failure modes bit somebody in
production.

## This teaches the patterns; the kits test your implementation

This cookbook is the *why* and the *how*. Two companion products are the
*prove-it*: the **Idempotency Key Test Kit** fires real-shape requests at an
endpoint you own and reports PASS/FAIL on the exactly-once contract (chapter 2's
subject), and the **Rate-Limit Test Kit** does the same for 429 + `Retry-After`
behaviour (chapter 6's subject). Read here; verify there. See the "pairs with"
note in the README.

**Sources.** RFC 9110 (*HTTP Semantics*) §9.2.2 on idempotent methods and the
retry-safety of method semantics; RFC 9110 §15.5/§15.6 on 4xx vs 5xx meaning;
Google, *Site Reliability Engineering* (O'Reilly, free at sre.google/books),
"Handling Overload" and "Addressing Cascading Failures" on retry amplification
and thundering herds; the IETF draft *The Idempotency-Key HTTP Header Field*
(`draft-ietf-httpapi-idempotency-key-header`) for the safe-retry intent of
idempotency keys. Companion kits:
`candidates/idempotency-key-test-kit/README.md` @ `c1bf40a`,
`candidates/rate-limit-test-kit/README.md` @ `dfec52e` in
`menno420/venture-lab`.
