# 5 · Retry budgets & circuit breakers: cap the blast radius

Backoff and jitter (chapter 4) space out retries so they don't land as one spike.
But they don't *limit the total*: during a broad outage, every request fails,
every one retries up to its attempt limit, and the aggregate retry load can still
dwarf the normal traffic — the multiplicative amplification from chapter 1. Two
mechanisms cap the total effort: a **retry budget** limits how many retries you
issue relative to real traffic, and a **circuit breaker** stops calling a
dependency that is clearly down. Both ship in `recipes/retry.py`.

## Per-request attempt caps are not enough

"Retry up to 4 times" bounds a single request but not the system. If a dependency
goes fully down and every one of a thousand in-flight requests retries 4 times,
that is up to 4,000 extra calls onto the thing that is already failing — piled on
by the very clients waiting for it to recover. The attempt cap is necessary
(always have one) but it is a per-request limit, and outages are a whole-fleet
event. You need a limit that sees the aggregate.

## Retry budgets: bound retries as a *ratio* of requests

A retry budget caps retries as a fraction of total requests, so retries can never
become more than a small percentage of your load no matter how much is failing.
The model in the recipe is the gRPC-style **token bucket** (also called retry
throttling):

- Every **request** deposits `token_ratio` tokens into a bucket capped at `max`.
- Every **retry** withdraws one token.
- A retry is allowed only while the balance is `>= 1`.

In steady state this permits roughly **one retry per `1/token_ratio` requests**
(e.g. `token_ratio = 0.1` ⇒ at most ~10% of requests get retried). When a
dependency is *healthy*, most requests succeed without retrying, the bucket stays
full, and the occasional retry is always permitted. When it is *broadly down*,
few requests succeed to refill the bucket, retries drain it fast, and further
retries are **denied** — so the client fails fast instead of amplifying the
outage. The budget self-tunes to the failure rate.

`RetryBudget(max_tokens, token_ratio)` in the recipe implements exactly this;
`call_with_retry` calls `on_request()` per attempt and checks `allow_retry()`
before each retry, stopping early when the budget says no. The test
`test_budget_starves_under_sustained_retries` shows a sustained-failure workload
draining to a hard ceiling instead of retrying unboundedly.

> Google's SRE book recommends exactly this shape: a **per-client retry budget**
> (they cite bounding retries to ~10% of requests) plus **not retrying at
> multiple layers** of the stack, because retries at layer 1 × layer 2 × layer 3
> multiply. Retry at one layer, budget it, and let the error propagate.

## Circuit breakers: stop knocking on a dead door

A circuit breaker is a state machine wrapping a dependency so that once it is
clearly failing, calls **fail fast** without even being attempted — giving the
dependency room to recover and giving the caller an instant, cheap error instead
of a slow timeout. Three states (`CircuitBreaker` in the recipe):

- **CLOSED** — normal. Calls pass through; consecutive failures are counted.
- **OPEN** — after `fail_threshold` consecutive failures, the breaker opens.
  Calls are rejected immediately (`CircuitOpen`) for a `cooldown` window. No load
  reaches the ailing dependency; callers get a fast, honest failure.
- **HALF-OPEN** — after the cooldown, one trial call is allowed through. If it
  **succeeds**, the breaker closes (recovered). If it **fails**, it re-opens for
  another cooldown. This is how the breaker discovers recovery without
  re-stampeding: exactly one probe, not the whole herd.

The tests `test_opens_after_threshold_then_probes` and
`test_half_open_failure_reopens` walk both transitions with an injected clock, so
the cooldown logic is verified without real waiting.

## How the two compose

They solve different halves of the same problem and belong together:

- The **breaker** is a *fast* circuit: it reacts to a run of failures and cuts
  off a specific dead dependency entirely, so you stop paying timeout latency and
  stop adding load.
- The **budget** is a *slow* governor: even while the breaker is closed and calls
  are mostly working, it guarantees retries stay a small fraction of traffic, so
  a partial degradation (some calls failing, not all) still can't amplify.

`call_with_retry(fn, budget=..., breaker=...)` wires both around the classified,
backed-off retry loop: the breaker gates *whether to call at all*, the budget
gates *whether a failure earns a retry*, and chapter 4's jitter decides *how long
to wait* when it does. Together they bound the blast radius: an outage produces a
fast wall of cheap failures, not a self-sustaining retry storm.

**Sources.** Google, *Site Reliability Engineering*, "Handling Overload" and
"Addressing Cascading Failures" (per-client retry budgets ~10%, avoid retrying at
multiple layers, request-level amplification); the gRPC retry design
(`grpc/proposal` A6, "retry throttling" token-bucket) for the request-deposit /
retry-withdraw budget model; Michael Nygard, *Release It!* (the Circuit Breaker
pattern and its CLOSED/OPEN/HALF-OPEN states); Martin Fowler, "CircuitBreaker".
Shipped recipe: `recipes/retry.py` (`RetryBudget`, `CircuitBreaker`,
`call_with_retry`) and the corresponding `test_recipes.py` cases.
