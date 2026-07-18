"""retry.py — client-side safe-retry executor reference recipe (stdlib only).

Ties the other recipes together into one small, correct retry loop:

  * error CLASSIFICATION — retry only what is safe to retry (429/408 + 5xx +
    transport errors); never retry an ordinary 4xx (ch.03);
  * BACKOFF + JITTER between attempts (imports ``backoff.full_jitter``, ch.04);
  * a RETRY BUDGET — a gRPC-style token bucket that caps the *ratio* of retries
    to requests, so a broad outage can't turn every client into a retry storm
    (ch.05);
  * a CIRCUIT BREAKER — stop hammering a dead dependency; fail fast while it is
    down, probe once on a cooldown (ch.05);
  * honoring ``Retry-After`` — use the server's stated delay as a floor over the
    computed backoff (ch.06, ties to the Rate-Limit Test Kit).

Everything schedulable is injectable (``rng``, ``sleep``, ``clock``) so the whole
thing runs deterministically and instantly under test — see ``test_recipes.py``.

Semantics of ``Retry-After`` follow RFC 9110 §10.2.3 (delay-seconds OR an
HTTP-date); 429 is RFC 6585 §4. See PROVENANCE.md for exact citations.
"""

from __future__ import annotations

import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Callable

from backoff import full_jitter

__all__ = [
    "RetryableError",
    "FatalError",
    "RetryExhausted",
    "CircuitOpen",
    "RETRYABLE_STATUS",
    "IDEMPOTENT_METHODS",
    "is_retryable_status",
    "is_idempotent_method",
    "parse_retry_after",
    "RetryBudget",
    "CircuitBreaker",
    "call_with_retry",
]

# The only status codes worth retrying. Note the 4xx exceptions: 408 Request
# Timeout, 425 Too Early, 429 Too Many Requests. Every other 4xx is the client's
# fault and will fail identically on retry — retrying it just wastes the budget
# and can look like an attack. (ch.03)
RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503, 504})

# Methods RFC 9110 defines as idempotent. A non-idempotent POST is only safe to
# retry when an Idempotency-Key makes the server treat the replay as a no-op —
# see idempotency_store.py and ch.02.
IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE"})


def is_retryable_status(status: int) -> bool:
    return status in RETRYABLE_STATUS


def is_idempotent_method(method: str, has_idempotency_key: bool = False) -> bool:
    """Safe to retry this method? True for RFC-idempotent methods, or for any
    method carrying an idempotency key (which makes the retry a server-side
    no-op)."""
    return has_idempotency_key or method.upper() in IDEMPOTENT_METHODS


class RetryableError(Exception):
    """A transient failure worth retrying (a 5xx, a 429/408, a connection reset,
    a timeout). Optionally carries ``retry_after`` seconds parsed from the
    response header."""

    def __init__(self, message: str = "", retry_after: float | None = None):
        super().__init__(message)
        self.retry_after = retry_after


class FatalError(Exception):
    """A non-retryable failure (a 4xx that isn't 408/425/429, a validation
    error). Propagates immediately — retrying cannot help."""


class RetryExhausted(Exception):
    """Raised when every attempt failed (budget spent, attempts used, or breaker
    open). ``__cause__`` is the last underlying error."""


class CircuitOpen(Exception):
    """The breaker is open; the call was rejected without touching the
    dependency."""


def parse_retry_after(value: str, now: datetime | None = None) -> float | None:
    """Parse a ``Retry-After`` header into a non-negative seconds delay.

    RFC 9110 §10.2.3 allows two forms: delay-seconds (an integer) or an
    HTTP-date. Returns ``None`` for an unparseable/absurd value so the caller
    falls back to computed backoff rather than trusting garbage.
    """
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    if value.isdigit():
        return float(value)
    try:
        when = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when is None:
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    if now is None:
        now = datetime.now(timezone.utc)
    return max(0.0, (when - now).total_seconds())


class RetryBudget:
    """gRPC-style retry throttle: a token bucket capping the *ratio* of retries
    to requests. Every request deposits ``token_ratio`` tokens (up to ``max``);
    every retry withdraws 1. Retries are allowed only while the balance is >= 1,
    so a total outage (where nothing succeeds to refill much) quickly starves
    retries and prevents a self-inflicted storm. Steady state permits roughly one
    retry per ``1/token_ratio`` requests."""

    def __init__(self, max_tokens: float = 100.0, token_ratio: float = 0.1):
        if max_tokens <= 0 or token_ratio <= 0:
            raise ValueError("max_tokens and token_ratio must be positive")
        self.max = float(max_tokens)
        self.ratio = float(token_ratio)
        self.balance = float(max_tokens)

    def on_request(self) -> None:
        self.balance = min(self.max, self.balance + self.ratio)

    def allow_retry(self) -> bool:
        if self.balance >= 1.0:
            self.balance -= 1.0
            return True
        return False


_CLOSED, _OPEN, _HALF_OPEN = "closed", "open", "half_open"


class CircuitBreaker:
    """Minimal three-state breaker. CLOSED: calls pass, failures counted. At
    ``fail_threshold`` consecutive failures -> OPEN: calls rejected fast for
    ``cooldown`` seconds. After cooldown -> HALF_OPEN: one trial call allowed; its
    success closes the breaker, its failure re-opens it. ``clock`` is injectable
    for testing."""

    def __init__(self, fail_threshold: int = 5, cooldown: float = 30.0, clock: Callable[[], float] = time.monotonic):
        self.fail_threshold = fail_threshold
        self.cooldown = cooldown
        self._clock = clock
        self.state = _CLOSED
        self.failures = 0
        self._opened_at: float | None = None

    def before_call(self) -> None:
        """Call before dispatching. Raises ``CircuitOpen`` while open + within
        cooldown; transitions OPEN -> HALF_OPEN once the cooldown elapses."""
        if self.state == _OPEN:
            assert self._opened_at is not None
            if self._clock() - self._opened_at >= self.cooldown:
                self.state = _HALF_OPEN
            else:
                raise CircuitOpen("circuit breaker is open")

    def on_success(self) -> None:
        self.failures = 0
        self.state = _CLOSED
        self._opened_at = None

    def on_failure(self) -> None:
        self.failures += 1
        if self.state == _HALF_OPEN or self.failures >= self.fail_threshold:
            self.state = _OPEN
            self._opened_at = self._clock()


def call_with_retry(
    fn: Callable[[int], object],
    *,
    max_attempts: int = 4,
    base: float = 0.1,
    cap: float = 20.0,
    budget: RetryBudget | None = None,
    breaker: CircuitBreaker | None = None,
    rng: random.Random = random,
    sleep: Callable[[float], None] = time.sleep,
) -> object:
    """Call ``fn(attempt)`` with classification + backoff + budget + breaker.

    ``fn`` receives the 1-based attempt number and must either return a value
    (success), raise ``RetryableError`` (transient — will be retried), or raise
    ``FatalError`` (non-retryable — propagates). On a retryable error the delay is
    ``full_jitter(...)``, floored by the error's ``retry_after`` if present. Stops
    when attempts run out, the budget denies a retry, or the breaker opens —
    raising ``RetryExhausted`` (or ``CircuitOpen``) with the last error as cause.
    """
    last_exc: BaseException | None = None
    for attempt in range(1, max_attempts + 1):
        if breaker is not None:
            breaker.before_call()  # may raise CircuitOpen
        if budget is not None:
            budget.on_request()
        try:
            result = fn(attempt)
        except FatalError:
            # A client error is not a transport failure; don't trip the breaker.
            raise
        except RetryableError as exc:
            last_exc = exc
            if breaker is not None:
                breaker.on_failure()
            if attempt == max_attempts:
                break
            if budget is not None and not budget.allow_retry():
                break
            delay = full_jitter(attempt, base, cap, rng)
            if exc.retry_after is not None:
                delay = max(delay, exc.retry_after)  # honor the server's floor
            sleep(delay)
            continue
        else:
            if breaker is not None:
                breaker.on_success()
            return result
    raise RetryExhausted("retries exhausted") from last_exc
