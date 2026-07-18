# 6 · Honoring `Retry-After` and rate-limit headers

When a server returns `429 Too Many Requests` or `503 Service Unavailable`, it
often tells you *exactly when to come back* in a `Retry-After` header. Ignoring it
and falling back to your own backoff is, at best, guessing when you were handed
the answer — and at worst, retrying sooner than the server said, which keeps you
throttled and turns a rate-limit event into a storm. This chapter is how to parse
and honor it; `recipes/retry.py` (`parse_retry_after`, and the floor logic in
`call_with_retry`) is the runnable version. The companion **Rate-Limit Test Kit**
tests that *your own* endpoint emits these headers correctly.

## `Retry-After` has two forms (RFC 9110 §10.2.3)

The header value is either:

1. **delay-seconds** — a non-negative integer number of seconds:
   `Retry-After: 120` ("come back in 2 minutes").
2. **an HTTP-date** — an absolute time:
   `Retry-After: Wed, 21 Oct 2026 07:28:00 GMT` ("come back at this instant").

`parse_retry_after` handles both: an all-digits value is delay-seconds; otherwise
it is parsed as an HTTP-date (via the stdlib `email.utils.parsedate_to_datetime`)
and converted to a seconds delay from now, **clamped at zero** so a stale or past
date never yields a negative wait. Anything it can't parse — `"soon"`, an empty
value — returns `None`, and the caller falls back to computed backoff rather than
trusting garbage. The tests cover all three: integer, future/past date, and
unparseable.

## Use the server's delay as a *floor* over your backoff

The rule the recipe encodes:

```
delay = full_jitter(attempt, base, cap)      # chapter 4
if retry_after is not None:
    delay = max(delay, retry_after)          # never retry sooner than told
```

Take the **larger** of your computed backoff and the server's `Retry-After`. Two
reasons it's a floor, not a replacement:

- **Never retry *sooner* than the server said.** If it said 30s and your backoff
  says 400ms, honoring 30s is mandatory — retrying at 400ms just earns another
  429. `max(...)` guarantees you never undercut it.
- **Still apply jitter when the server said nothing (or said "0").** If many
  clients all got `Retry-After: 30`, they'd all retry at exactly +30s — a
  synchronized herd again. Keeping your jittered value as the other side of the
  `max` means that when the server's floor is small or absent, chapter 4's
  de-synchronization still applies. (Some designs even add a little jitter *on
  top* of `Retry-After`; at minimum, don't strip it.)

The shipped test `test_retry_after_floors_the_delay` sets `base`/`cap` tiny so
the computed jitter is well under the header's 5s and asserts the actual sleep is
`>= 5s` — the floor dominates exactly when it should.

## The rate-limit headers next to it

Alongside `Retry-After`, throttling responses often carry the draft
`RateLimit-Limit` / `RateLimit-Remaining` / `RateLimit-Reset` fields (or the
legacy `X-RateLimit-*` convention) describing your quota and when it resets. A
well-behaved client can read `Remaining` and *slow down before* hitting the
limit, rather than sprinting into a 429 and reacting. Two honesty notes:

- The `RateLimit-*` field family is an **IETF draft, not yet an RFC** — treat it
  as advisory and don't hard-depend on exact semantics across vendors.
- `429` itself and its `Retry-After` are stable standards: `429` is RFC 6585 §4,
  `Retry-After` is RFC 9110 §10.2.3.

This is precisely the contract the **Rate-Limit Test Kit** verifies on the
*server* side — that the 429 lands at the right boundary, that `Retry-After` is
present and sane, and that the service actually resumes when it said it would. If
you build the endpoint, that kit proves it; this chapter is how the *client*
should consume what a correct endpoint emits.

## Checklist

- Parse both `Retry-After` forms; clamp past dates to 0; treat unparseable as
  absent.
- Honor it as a **floor**: `max(computed_backoff, retry_after)`.
- Keep jitter alive so an absent/small `Retry-After` doesn't resynchronize the
  herd.
- Read `RateLimit-Remaining` where present to pace *before* the 429 — but don't
  hard-depend on the draft fields.
- Never retry a 429 with no delay — that's a storm accelerant, not a retry.

**Sources.** RFC 9110 (*HTTP Semantics*) §10.2.3 (`Retry-After`: delay-seconds or
HTTP-date); RFC 6585 §4 (`429 Too Many Requests`); the IETF draft *RateLimit
header fields for HTTP* (`draft-ietf-httpapi-ratelimit-headers`) for the
`RateLimit-*` fields, explicitly a draft; the stdlib
`email.utils.parsedate_to_datetime` for HTTP-date parsing. Shipped recipe:
`recipes/retry.py` (`parse_retry_after` + the `max(delay, retry_after)` floor).
Companion: `candidates/rate-limit-test-kit/README.md` @ `dfec52e` and
`candidates/rate-limit-test-kit/fixtures/PROVENANCE.md` @ `dfec52e` in
`menno420/venture-lab`.
