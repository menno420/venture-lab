"""test_recipes.py — self-test for the cookbook's reference recipes.

Stdlib only, offline, deterministic (a seeded RNG, an injected clock, and a
recording fake sleeper — no wall-clock waits). Proves the shipped snippets are
correct, not just parseable.

Run from this directory:

    python3 -m unittest test_recipes -v
"""

from __future__ import annotations

import random
import unittest
from datetime import datetime, timezone

import backoff
import idempotency_store as store
import retry


class BackoffTests(unittest.TestCase):
    def test_exponential_ladder_and_cap(self):
        self.assertEqual(backoff.exponential_delay(1, 0.1, 100), 0.1)
        self.assertAlmostEqual(backoff.exponential_delay(2, 0.1, 100), 0.2)
        self.assertAlmostEqual(backoff.exponential_delay(3, 0.1, 100), 0.4)
        # cap clamps
        self.assertEqual(backoff.exponential_delay(40, 1.0, 30.0), 30.0)

    def test_exponential_rejects_bad_input(self):
        with self.assertRaises(ValueError):
            backoff.exponential_delay(0, 0.1, 1.0)
        with self.assertRaises(ValueError):
            backoff.exponential_delay(1, 0, 1.0)

    def test_full_jitter_within_window(self):
        rng = random.Random(1234)
        for attempt in range(1, 8):
            ceiling = backoff.exponential_delay(attempt, 0.1, 20.0)
            for _ in range(50):
                d = backoff.full_jitter(attempt, 0.1, 20.0, rng)
                self.assertGreaterEqual(d, 0.0)
                self.assertLessEqual(d, ceiling)

    def test_equal_jitter_keeps_minimum(self):
        rng = random.Random(7)
        for attempt in range(1, 8):
            ceiling = backoff.exponential_delay(attempt, 0.1, 20.0)
            for _ in range(50):
                d = backoff.equal_jitter(attempt, 0.1, 20.0, rng)
                self.assertGreaterEqual(d, ceiling / 2.0)  # never retries instantly
                self.assertLessEqual(d, ceiling)

    def test_decorrelated_jitter_bounds(self):
        rng = random.Random(99)
        prev = 0.1
        for _ in range(200):
            d = backoff.decorrelated_jitter(prev, 0.1, 20.0, rng)
            self.assertGreaterEqual(d, 0.1)      # never below base
            self.assertLessEqual(d, 20.0)        # never above cap
            prev = d

    def test_jitter_actually_de_synchronizes(self):
        # Two "clients" with independent RNGs should NOT land on the same delay
        # the way un-jittered backoff would. (The whole point of ch.04.)
        a, b = random.Random(1), random.Random(2)
        collisions = sum(
            1
            for _ in range(1000)
            if backoff.full_jitter(3, 0.1, 20.0, a) == backoff.full_jitter(3, 0.1, 20.0, b)
        )
        self.assertEqual(collisions, 0)


class IdempotencyStoreTests(unittest.TestCase):
    def setUp(self):
        self.now = [1000.0]
        self.s = store.IdempotencyStore(ttl_seconds=100, clock=lambda: self.now[0])
        self.fp = store.fingerprint("POST", "/charges", {"amount": 500, "currency": "usd"})

    def test_fingerprint_is_order_insensitive(self):
        a = store.fingerprint("POST", "/charges", {"amount": 500, "currency": "usd"})
        b = store.fingerprint("post", "/charges", {"currency": "usd", "amount": 500})
        self.assertEqual(a, b)  # method case + key order don't matter
        c = store.fingerprint("POST", "/charges", {"amount": 501, "currency": "usd"})
        self.assertNotEqual(a, c)  # a different body IS a different fingerprint

    def test_rule1_replay_runs_side_effect_once(self):
        side_effects = []

        def handle(key):
            decision, replay = self.s.begin(key, self.fp)
            if decision == "replay":
                return replay
            side_effects.append(key)              # the "charge"
            resp = {"id": "ch_1", "amount": 500}
            self.s.complete(key, resp)
            return resp

        first = handle("k-1")
        second = handle("k-1")                     # the retry
        self.assertEqual(first, second)            # same stored response
        self.assertEqual(side_effects, ["k-1"])    # charged exactly once

    def test_rule2_mismatch_rejected(self):
        self.s.begin("k-2", self.fp)
        self.s.complete("k-2", {"id": "ch_2"})
        other = store.fingerprint("POST", "/charges", {"amount": 999, "currency": "usd"})
        with self.assertRaises(store.IdempotencyMismatch):
            self.s.begin("k-2", other)             # same key, different body -> 409/422

    def test_rule3_in_flight_lock(self):
        decision, _ = self.s.begin("k-3", self.fp)
        self.assertEqual(decision, "run")          # first caller reserved it
        with self.assertRaises(store.IdempotencyInProgress):
            self.s.begin("k-3", self.fp)           # concurrent retry, not yet complete

    def test_rule4_expiry_then_new(self):
        self.s.begin("k-4", self.fp)
        self.s.complete("k-4", {"id": "ch_4"})
        self.now[0] += 101                          # push past the 100s TTL
        decision, _ = self.s.begin("k-4", self.fp)
        self.assertEqual(decision, "run")          # expired -> treated as new

    def test_abort_releases_failed_reservation(self):
        self.s.begin("k-5", self.fp)
        self.s.abort("k-5")                         # side effect failed pre-response
        decision, _ = self.s.begin("k-5", self.fp)
        self.assertEqual(decision, "run")          # retry may proceed, not wedged


class RetryClassificationTests(unittest.TestCase):
    def test_retryable_status_set(self):
        for code in (408, 425, 429, 500, 502, 503, 504):
            self.assertTrue(retry.is_retryable_status(code))
        for code in (200, 201, 400, 401, 403, 404, 409, 422):
            self.assertFalse(retry.is_retryable_status(code))

    def test_idempotent_method_gate(self):
        self.assertTrue(retry.is_idempotent_method("GET"))
        self.assertTrue(retry.is_idempotent_method("PUT"))
        self.assertFalse(retry.is_idempotent_method("POST"))
        # a POST carrying an idempotency key IS safe to retry
        self.assertTrue(retry.is_idempotent_method("POST", has_idempotency_key=True))


class RetryAfterTests(unittest.TestCase):
    def test_delay_seconds(self):
        self.assertEqual(retry.parse_retry_after("120"), 120.0)
        self.assertEqual(retry.parse_retry_after("0"), 0.0)

    def test_http_date(self):
        now = datetime(2026, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        # 60 seconds in the future
        self.assertAlmostEqual(
            retry.parse_retry_after("Thu, 01 Jan 2026 00:01:00 GMT", now=now), 60.0, places=0
        )
        # a past date clamps to 0, never negative
        self.assertEqual(
            retry.parse_retry_after("Wed, 31 Dec 2025 23:59:00 GMT", now=now), 0.0
        )

    def test_garbage_is_none(self):
        self.assertIsNone(retry.parse_retry_after("soon"))
        self.assertIsNone(retry.parse_retry_after(""))
        self.assertIsNone(retry.parse_retry_after(None))


class RetryBudgetTests(unittest.TestCase):
    def test_budget_starves_under_sustained_retries(self):
        b = retry.RetryBudget(max_tokens=10, token_ratio=0.1)
        # Drain the initial 10 tokens with retries (each request deposits 0.1).
        allowed = 0
        for _ in range(200):
            b.on_request()
            if b.allow_retry():
                allowed += 1
        # Can't be unbounded: ~ initial 10 + 0.1/req refill, far below 200.
        self.assertLess(allowed, 40)
        self.assertGreaterEqual(allowed, 10)

    def test_budget_refills_when_traffic_succeeds(self):
        b = retry.RetryBudget(max_tokens=10, token_ratio=0.5)
        for _ in range(100):        # healthy traffic, no retries taken
            b.on_request()
        self.assertEqual(b.balance, 10.0)   # refilled to cap, not overflowing


class CircuitBreakerTests(unittest.TestCase):
    def test_opens_after_threshold_then_probes(self):
        clock = [0.0]
        cb = retry.CircuitBreaker(fail_threshold=3, cooldown=30.0, clock=lambda: clock[0])
        for _ in range(3):
            cb.before_call()
            cb.on_failure()
        self.assertEqual(cb.state, "open")
        with self.assertRaises(retry.CircuitOpen):
            cb.before_call()                # rejected fast while open
        clock[0] += 31                       # cooldown elapses
        cb.before_call()                     # transitions to half-open, allows a trial
        self.assertEqual(cb.state, "half_open")
        cb.on_success()                      # trial passed
        self.assertEqual(cb.state, "closed")

    def test_half_open_failure_reopens(self):
        clock = [0.0]
        cb = retry.CircuitBreaker(fail_threshold=2, cooldown=10.0, clock=lambda: clock[0])
        cb.before_call(); cb.on_failure()
        cb.before_call(); cb.on_failure()
        self.assertEqual(cb.state, "open")
        clock[0] += 11
        cb.before_call()                     # half-open
        cb.on_failure()                      # trial failed -> back to open
        self.assertEqual(cb.state, "open")


class CallWithRetryTests(unittest.TestCase):
    def setUp(self):
        self.slept: list[float] = []

    def _sleep(self, d):
        self.slept.append(d)

    def test_succeeds_after_transient_failures(self):
        calls = []

        def fn(attempt):
            calls.append(attempt)
            if attempt < 3:
                raise retry.RetryableError("503")
            return "ok"

        out = retry.call_with_retry(
            fn, max_attempts=5, base=0.1, cap=1.0, rng=random.Random(0), sleep=self._sleep
        )
        self.assertEqual(out, "ok")
        self.assertEqual(calls, [1, 2, 3])
        self.assertEqual(len(self.slept), 2)      # slept between the 3 attempts

    def test_fatal_is_not_retried(self):
        calls = []

        def fn(attempt):
            calls.append(attempt)
            raise retry.FatalError("400")

        with self.assertRaises(retry.FatalError):
            retry.call_with_retry(fn, max_attempts=5, sleep=self._sleep)
        self.assertEqual(calls, [1])              # one and done
        self.assertEqual(self.slept, [])

    def test_exhaustion_raises_with_cause(self):
        def fn(attempt):
            raise retry.RetryableError("still 503")

        with self.assertRaises(retry.RetryExhausted) as ctx:
            retry.call_with_retry(fn, max_attempts=3, sleep=self._sleep)
        self.assertIsInstance(ctx.exception.__cause__, retry.RetryableError)
        self.assertEqual(len(self.slept), 2)      # slept between 3 attempts, not after last

    def test_retry_after_floors_the_delay(self):
        def fn(attempt):
            if attempt == 1:
                raise retry.RetryableError("429", retry_after=5.0)
            return "ok"

        # base/cap tiny so computed jitter is < 5; Retry-After must dominate.
        retry.call_with_retry(
            fn, max_attempts=3, base=0.001, cap=0.01, rng=random.Random(0), sleep=self._sleep
        )
        self.assertEqual(len(self.slept), 1)
        self.assertGreaterEqual(self.slept[0], 5.0)

    def test_budget_denial_stops_retries_early(self):
        spent = retry.RetryBudget(max_tokens=1, token_ratio=0.0001)
        spent.balance = 0.0                        # no tokens: no retry permitted
        calls = []

        def fn(attempt):
            calls.append(attempt)
            raise retry.RetryableError("503")

        with self.assertRaises(retry.RetryExhausted):
            retry.call_with_retry(fn, max_attempts=5, budget=spent, sleep=self._sleep)
        self.assertEqual(calls, [1])               # first try, then budget denied
        self.assertEqual(self.slept, [])


if __name__ == "__main__":
    unittest.main()
