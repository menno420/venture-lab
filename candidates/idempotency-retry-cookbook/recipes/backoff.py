"""backoff.py — exponential backoff + jitter reference recipe (stdlib only).

Small, correct, dependency-free functions you can lift into a client. Every
delay function takes an injectable ``rng`` (default: the module ``random``) so
it is deterministic under test — see ``test_recipes.py``. None of these sleep;
they return a delay in seconds for the caller to sleep on. That keeps the math
unit-testable and lets you plug the value into ``retry.call_with_retry`` (or your
own loop) however you schedule waits.

The jitter variants follow the widely-cited AWS Architecture blog
"Exponential Backoff And Jitter" (Marc Brooker). The one-line takeaway of that
piece: adding jitter is not a nicety — synchronized clients retrying on the same
un-jittered exponential schedule reconverge into a thundering herd, and
*decorrelated* jitter completed the simulated workload with the fewest calls and
lowest spread. Chapter 04 of the guide walks the formulas and the reasoning.
"""

from __future__ import annotations

import random

__all__ = [
    "exponential_delay",
    "full_jitter",
    "equal_jitter",
    "decorrelated_jitter",
]


def exponential_delay(attempt: int, base: float, cap: float) -> float:
    """Un-jittered capped exponential backoff for a 1-based ``attempt``.

    ``base * 2**(attempt-1)``, clamped to ``cap``. attempt 1 -> base, attempt 2
    -> 2*base, attempt 3 -> 4*base, ... This is the DANGEROUS-alone schedule:
    every client that failed at the same instant retries at the same instant.
    Use it only as the ceiling the jitter functions randomize under.
    """
    if attempt < 1:
        raise ValueError("attempt is 1-based; got %r" % (attempt,))
    if base <= 0 or cap <= 0:
        raise ValueError("base and cap must be positive")
    # 2**(attempt-1) can get large; clamp before multiplying to avoid overflow.
    exp = min(attempt - 1, 32)
    return min(cap, base * (2 ** exp))


def full_jitter(attempt: int, base: float, cap: float, rng: random.Random = random) -> float:
    """Full jitter: ``uniform(0, exponential_delay(...))``.

    The AWS blog's recommended default. Spreads retries across the whole window
    ``[0, cap_for_this_attempt]``, which maximally de-synchronizes a herd at the
    cost of occasionally retrying very soon. Mean delay is half the exponential
    ceiling.
    """
    return rng.uniform(0.0, exponential_delay(attempt, base, cap))


def equal_jitter(attempt: int, base: float, cap: float, rng: random.Random = random) -> float:
    """Equal jitter: half the exponential ceiling, plus jitter over the other half.

    ``temp/2 + uniform(0, temp/2)``. Keeps a guaranteed minimum wait (never
    retries instantly) while still de-correlating — a middle ground between
    un-jittered and full jitter.
    """
    temp = exponential_delay(attempt, base, cap)
    return temp / 2.0 + rng.uniform(0.0, temp / 2.0)


def decorrelated_jitter(
    prev_delay: float, base: float, cap: float, rng: random.Random = random
) -> float:
    """Decorrelated jitter: ``min(cap, uniform(base, prev_delay*3))``.

    Feeds the previous delay back in, so the window grows from where the last
    wait landed rather than from a fixed exponential ladder. In the AWS
    simulation this variant finished the work in the fewest total calls. Seed the
    first call with ``prev_delay=base``.
    """
    if base <= 0 or cap <= 0:
        raise ValueError("base and cap must be positive")
    lo = base
    hi = max(base, prev_delay * 3.0)
    return min(cap, rng.uniform(lo, hi))
