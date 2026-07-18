# Rate-limiter gotchas — the one-page checklist

The failure modes that repeatedly break first rate-limiter implementations. Each
maps to a kit command that proves your endpoint is not making the mistake. The
429 + `Retry-After` behaviour is RFC 6585 §4 / RFC 9110 §10.2.3; the
`RateLimit-*` headers follow the IETF draft (sources cited in
`fixtures/PROVENANCE.md`).

## 1. The off-by-one: your "N per window" actually allows N+1

The classic bug is `count <= limit + 1` (or checking the limit *after*
incrementing but *before* comparing) so the `limit`+1'th request slips through
before the 429 kicks in. On a quota that gates cost or abuse, letting one extra
request per window through is a real leak. Correct: the `limit`+1'th request in a
window returns **429 Too Many Requests**.

**Check it:** `rltk over-limit --limit N` — fires `N`+1 requests and confirms the
last one is a 429, and `rltk under-limit --limit N` — confirms the first `N` are
not throttled early.

## 2. A 429 with no Retry-After (or a useless one)

RFC 6585 says a 429 **MAY** carry `Retry-After`, and in practice it must, or the
client is flying blind: it either hammers you immediately (making things worse) or
backs off far too long. Just as bad: `Retry-After: 0`, a negative value, a
non-numeric string, or an HTTP-date already in the past. Correct: a **positive,
sane** delay-seconds, or an HTTP-date in the future (RFC 9110 §10.2.3 defines both
forms).

**Check it:** `rltk retry-after --limit N` — drives the endpoint to a 429 and
validates the `Retry-After` value (present, positive, sane, or a future date).

## 3. RateLimit-* headers that lie

If you advertise a budget with `RateLimit-Limit` / `RateLimit-Remaining` /
`RateLimit-Reset` (or the legacy `X-RateLimit-*`), they must be **internally
consistent** or they mislead every well-behaved client that reads them:

- `Remaining` must **decrement** each request and reach **0 exactly at the 429
  boundary** — not sit stuck at the limit (a client can't see itself running out).
- `Reset` must point into the **future** — not a stale constant timestamp already
  in the past (a common copy-paste bug), and not `0`.
- `Limit` must be a positive integer that matches the budget you actually enforce.

These headers are **optional** (the spec is a draft) — an endpoint that emits none
is fine. But if you emit them, get them right.

**Check it:** `rltk headers --limit N` — reads the headers across a burst and
flags a stuck `Remaining`, a past/zero `Reset`, or a `Remaining` that never hits
0. (No headers at all → passes with a note.)

## 4. A window that doesn't reset — or resets on a schedule it won't admit

The point of a window is that it **reopens**. A limiter that counts forever (a
misconfigured leaky/token bucket that never refills) locks the client out
permanently. And a limiter whose `Retry-After` says "wait 30s" but actually
resumes at 90s (or never) has trained the client to trust a lie — the client
retries at 30s, gets another 429, and either loops or gives up.

**Check it:** `rltk window-reset --limit N --window W` — exhausts the limit, waits
out the advertised reset, and confirms a request succeeds again.
`rltk retry-after-honored --limit N` — confirms the service is still throttled
just **before** the advertised `Retry-After` and resumes just **after** it, within
tolerance.

## 5. Two honest non-signals (and the scope of the test)

- **`under-limit` and `window-reset` don't distinguish a broken limiter from a
  correct one on their own.** A limiter with an off-by-one still serves the first
  `limit` requests, and still resets its window — so those two properties pass on
  both the correct and the naive reference stub. The distinguishing failures are
  `over-limit`, `retry-after`, `headers`, and `retry-after-honored`. The kit says
  this out loud rather than overclaiming (`stub_handler_naive.py` documents which
  bugs each property does and doesn't catch).
- **Scope.** This kit tests the externally-visible contract for the **caller it
  is** — one bucket, one client. It does not test per-user/per-IP fairness,
  cross-node consistency of a distributed limiter, or which algorithm you chose
  (fixed-window, token bucket, sliding log). Those are design decisions; the kit
  checks that whatever you built returns the right 429s, headers, and resets.

---

Run all six at once with `rltk check --url … --limit N`, and see them distinguish
a correct limiter from a broken one with `rltk demo`.
