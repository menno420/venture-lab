# 3 · Retryable vs non-retryable errors

Retryability is a property of the *specific failure*, not a default you apply to
everything that isn't a 2xx. Retry the wrong things and you burn your budget on
requests that can never succeed, hammer a dependency that told you to stop, and
turn a client bug into what looks like a denial-of-service attack on your own
API. This chapter is the classification; `recipes/retry.py`
(`is_retryable_status`, `is_idempotent_method`) encodes it.

## The one rule for status codes

**Retry 5xx and the two-and-a-half retryable 4xx; never retry any other 4xx.**

- **5xx — retry (with backoff).** `500`, `502`, `503`, `504` mean the server or
  an intermediary failed to handle a request that may well be fine. These are the
  canonical transient failures. `503 Service Unavailable` and `429` may carry a
  `Retry-After` telling you when — honor it (ch.6).
- **429 Too Many Requests — retry, but honor `Retry-After`.** You were throttled.
  The request is fine; you sent it too fast. Back off — ideally exactly as long
  as the server's `Retry-After` says (RFC 6585 §4). Retrying a 429 *immediately*
  is how a rate-limit event becomes a retry storm.
- **408 Request Timeout — retry.** The server gave up waiting for the request;
  sending it again is reasonable.
- **425 Too Early — retry (situational).** The server declined to process a
  replayed early-data request; retrying without early data is the fix.
- **Every other 4xx — do NOT retry.** `400` (malformed), `401` (unauthenticated),
  `403` (forbidden), `404` (not found), `409` (conflict), `422` (validation) all
  describe something wrong with *the request itself*. It will fail identically on
  retry. Surface the error; don't loop on it. (A `401` may warrant one
  token-refresh-then-retry, but that's a re-auth step, not a blind retry.)

`RETRYABLE_STATUS` in the recipe is exactly `{408, 425, 429, 500, 502, 503,
504}`. The test suite asserts both directions: those retry, and `400/401/403/404/
409/422` do not.

## Transport failures are retryable — but mind the ambiguity

Errors that never produced an HTTP status — connection refused, connection reset,
DNS failure, a read timeout — are generally retryable: often the request never
reached the server. But a timeout is the ambiguous case from chapter 1: the
request *may* have been processed. So:

- **Connection refused / DNS failure / connect timeout** → the request almost
  certainly didn't land → retry freely.
- **Read timeout / reset after the request was sent** → the side effect *might*
  have run → only retry safely if the operation is idempotent (chapter 2's key
  makes it so). This is why the recipe pairs classification with
  `is_idempotent_method`.

## Method matters: don't blind-retry a non-idempotent write

RFC 9110 §9.2.2 defines `GET`, `HEAD`, `PUT`, `DELETE`, `OPTIONS`, `TRACE` as
idempotent — applying them once or many times has the same effect, so they are
safe to retry on an ambiguous failure. `POST` is **not** idempotent by default.
The rule:

> Retry an idempotent method on a retryable error freely. Retry a non-idempotent
> method (`POST`) **only** when an idempotency key makes the server treat the
> replay as a no-op (chapter 2).

`is_idempotent_method("POST")` is `False`; `is_idempotent_method("POST",
has_idempotency_key=True)` is `True`. That boolean is the whole safety gate for
retrying writes.

## Put it together

The client's decision for each failure is a short pipeline:

1. Did it produce a status? If yes and it's not in `RETRYABLE_STATUS` → **fail
   fast**, surface the error.
2. Is the method safe to retry (idempotent, or carrying an idempotency key)? If
   no → **fail fast** rather than risk a double side effect.
3. Otherwise → **retry**, with backoff + jitter (ch.4), inside a budget + breaker
   (ch.5), honoring any `Retry-After` (ch.6).

Classification first, mechanism second. A perfect backoff schedule applied to a
`400` is still just a slow way to fail.

**Sources.** RFC 9110 (*HTTP Semantics*) §9.2.2 (idempotent methods), §15.5
(4xx client errors — meaning of 400/401/403/404/409/422), §15.6 (5xx server
errors); RFC 6585 §4 (`429 Too Many Requests` and its `Retry-After`); RFC 8470
(`425 Too Early`, HTTP early data). Shipped recipe: `recipes/retry.py`
(`RETRYABLE_STATUS`, `is_retryable_status`, `IDEMPOTENT_METHODS`,
`is_idempotent_method`).
