# 4 · Backoff & jitter: don't retry in lockstep

Once you know a failure is retryable (chapter 3), the question is *when*. Retry
immediately and you hammer a struggling dependency. Retry on a fixed exponential
schedule and every client that failed together retries together — the thundering
herd from chapter 1. The fix is exponential backoff to grow the gaps, plus
**jitter** to break the synchronization. This chapter is the math;
`recipes/backoff.py` is the runnable version and `test_recipes.py` checks the
bounds.

## Exponential backoff (necessary, not sufficient)

Wait longer after each failure so a dependency has room to recover:

```
delay(attempt) = min(cap, base * 2 ** (attempt - 1))
```

With `base = 100ms`, `cap = 20s`: 100ms, 200ms, 400ms, 800ms, … capped at 20s.
The cap keeps a long outage from producing absurd multi-minute waits. This is
`exponential_delay(attempt, base, cap)` in the recipe.

Exponential backoff alone fixes the *rate* of one client's retries but not the
*correlation* between many clients. If a thousand callers all failed at `t=0`,
they all retry at `t=100ms`, then all at `t=300ms`, … The load arrives in
synchronized spikes exactly as tall as the herd. Backoff without jitter just
schedules the stampede politely.

## Jitter: randomize within the window

Jitter adds randomness so retries **spread out** across time instead of landing
together. The canonical treatment is the AWS Architecture blog *Exponential
Backoff And Jitter* (Marc Brooker), which simulated the variants and measured
which actually reduced contention. Three forms, all in the recipe:

**Full jitter (the recommended default):**
```
delay = uniform(0, min(cap, base * 2 ** (attempt - 1)))
```
Pick a random wait anywhere in `[0, exponential_ceiling]`. This maximally
de-synchronizes the herd — two clients almost never pick the same delay. Mean
wait is half the ceiling. Downside: occasionally retries very soon. This is
`full_jitter(...)`.

**Equal jitter (keep a guaranteed minimum):**
```
temp  = min(cap, base * 2 ** (attempt - 1))
delay = temp/2 + uniform(0, temp/2)
```
Half the ceiling guaranteed, jitter over the other half. Never retries instantly,
still de-correlates. `equal_jitter(...)`.

**Decorrelated jitter (fewest total calls in the AWS sim):**
```
delay = min(cap, uniform(base, prev_delay * 3))
```
Feed the *previous* delay back in, so the window grows from where the last wait
landed rather than from a fixed ladder. Seed the first call with
`prev_delay = base`. In the AWS simulation this completed the work with the
fewest total client calls. `decorrelated_jitter(...)`.

## Why jitter prevents the thundering herd (the intuition + the proof)

Un-jittered, N clients that fail together produce N retries in the same instant
at every step — the arrival process is a sum of *identical* schedules, so the
peak is N. Full jitter turns each client's next retry into a uniform draw over a
window of width W; the expected number landing in any small interval `dt` is
`N · dt / W`, i.e. the herd is *smeared* across the whole window instead of
piling on one point. Bigger W (later attempts) smears harder. The peak load drops
from "all N at once" to "roughly N/W per unit time" — which is the entire game
when the dependency's problem was too much concurrent load.

The shipped test `test_jitter_actually_de_synchronizes` makes this concrete: two
independent clients drawing full-jitter delays collide **zero** times across a
thousand draws, whereas the un-jittered `exponential_delay` would return the
identical value every time. That is the herd, broken, in one assertion.

## Practical defaults

- **base:** 100-200ms for user-facing calls; higher for background work.
- **cap:** a few seconds to ~30s depending on how long a caller can wait.
- **jitter:** full jitter is the safe default; decorrelated jitter if you want
  the lowest total call count and can carry the previous delay.
- **Always cap the number of attempts too** (chapter 5) — backoff decides the
  gap; the budget and attempt-count decide when to stop.
- **Never sleep on the request thread in a way that blocks a whole worker pool
  under load** — that itself is a cascading-failure amplifier.

The recipe's delay functions are pure (they return seconds; they don't sleep) and
take an injectable RNG, so you can unit-test your schedule and plug the value into
`retry.call_with_retry`, which floors it by any server-supplied `Retry-After`
(chapter 6).

**Sources.** AWS Architecture Blog, *Exponential Backoff And Jitter* (Marc
Brooker) — the full-/equal-/decorrelated-jitter formulas and the simulation
result that decorrelated jitter minimizes total calls; Google, *Site Reliability
Engineering*, "Addressing Cascading Failures" (why synchronized retries amplify
load); RFC 9110 §7.6.3 relationship to `Retry-After` timing. Shipped recipe:
`recipes/backoff.py` and the `test_recipes.py` jitter-bound + de-sync tests.
