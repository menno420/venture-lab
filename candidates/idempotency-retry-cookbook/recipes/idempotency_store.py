"""idempotency_store.py — server-side idempotency-key store sketch (stdlib only).

The property that makes a non-idempotent write (POST /charges) safe to retry:
the server keys the operation on a caller-supplied ``Idempotency-Key``, stores a
*fingerprint of the request* plus *the response it produced*, and on a replay
returns the stored response instead of running the side effect twice.

This is a single-process, in-memory reference sketch — enough to show the four
load-bearing rules, small enough to read in one sitting. A production store puts
this in a shared, atomic backend (Redis SETNX / a unique DB constraint) so the
``begin`` step is a real distributed lock; the RULES are identical. Chapter 02 of
the guide walks each one, and cross-references the Idempotency Key Test Kit,
which exercises exactly these behaviours over real HTTP against an endpoint you
own.

Behaviour modeled on the Stripe-style ``Idempotency-Key`` semantics that the IETF
draft *The Idempotency-Key HTTP Header Field* standardizes; see PROVENANCE.md.

The four rules:
  1. same key + same request  -> REPLAY the stored response; side effect runs once.
  2. same key + different req  -> MISMATCH: reject (409/422); never serve a stale
     or double result.
  3. key seen, still running   -> IN-PROGRESS: a concurrent retry hits an in-flight
     lock; it must not start a second side effect.
  4. expired key               -> treated as new (keys are retained for a TTL, not
     forever).
"""

from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Callable

__all__ = [
    "IdempotencyMismatch",
    "IdempotencyInProgress",
    "fingerprint",
    "IdempotencyStore",
]

# Recommended retention: Stripe keys expire after 24h; keep yours long enough to
# cover the client's entire retry budget and then some. See ch.02.
DEFAULT_TTL_SECONDS = 24 * 60 * 60


class IdempotencyMismatch(Exception):
    """Same key, different request body -> the caller reused a key. Map to 422
    (or 409). Rule 2: serving the stored response here would silently answer the
    wrong question; running the new body would break the key's promise."""


class IdempotencyInProgress(Exception):
    """Same key, original request still executing -> a concurrent retry. Map to
    409. Rule 3: the loser must not launch a second side effect; it retries and
    replays once the original completes."""


def fingerprint(method: str, path: str, body: Any) -> str:
    """A stable SHA-256 over (method, path, canonical body).

    ``body`` is canonicalized with sorted keys + tight separators so semantically
    equal JSON fingerprints identically regardless of key order or whitespace.
    Bytes/str bodies are hashed as-is. This is what rule 2 compares: a differing
    fingerprint under the same key is a mismatch.
    """
    if isinstance(body, bytes):
        raw = body
    elif isinstance(body, str):
        raw = body.encode("utf-8")
    else:
        raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256()
    digest.update(method.upper().encode("ascii"))
    digest.update(b"\x00")
    digest.update(path.encode("utf-8"))
    digest.update(b"\x00")
    digest.update(raw)
    return digest.hexdigest()


class IdempotencyStore:
    """In-memory idempotency store. Not thread-safe by itself in a way that
    survives multiple processes — ``begin`` models the atomic reserve-or-read a
    real backend must provide (SETNX / INSERT ... ON CONFLICT). The rules it
    enforces are the portable part."""

    def __init__(self, ttl_seconds: int = DEFAULT_TTL_SECONDS, clock: Callable[[], float] = time.time):
        self._ttl = ttl_seconds
        self._clock = clock
        self._records: dict[str, dict[str, Any]] = {}

    def _live_record(self, key: str) -> dict[str, Any] | None:
        rec = self._records.get(key)
        if rec is None:
            return None
        if self._clock() - rec["ts"] > self._ttl:  # rule 4: expired -> gone
            del self._records[key]
            return None
        return rec

    def begin(self, key: str, fp: str) -> tuple[str, Any]:
        """Atomically reserve ``key`` for this request, or resolve the replay.

        Returns:
          ("run", None)         -> caller is first; run the side effect, then
                                   call ``complete(key, response)``.
          ("replay", response)  -> stored response for an identical earlier
                                   request; return it, run NOTHING (rule 1).
        Raises:
          IdempotencyMismatch   -> same key, different body (rule 2).
          IdempotencyInProgress -> original still running (rule 3).
        """
        rec = self._live_record(key)
        if rec is None:
            # Reserve. In a real backend this is the atomic step that must fail
            # for the loser of a concurrent race (so exactly one caller "runs").
            self._records[key] = {"fp": fp, "response": None, "ts": self._clock()}
            return ("run", None)
        if rec["fp"] != fp:
            raise IdempotencyMismatch("idempotency key reused with a different request")
        if rec["response"] is None:
            raise IdempotencyInProgress("original request for this key is still in flight")
        return ("replay", rec["response"])

    def complete(self, key: str, response: Any) -> None:
        """Record the response for ``key`` so future replays return it. Call this
        exactly once, after the side effect succeeds."""
        rec = self._records.get(key)
        if rec is None:
            # Reserved slot expired mid-flight (pathological); re-create so a
            # follow-up retry can still replay rather than double-execute.
            self._records[key] = {"fp": None, "response": response, "ts": self._clock()}
            return
        rec["response"] = response
        rec["ts"] = self._clock()

    def abort(self, key: str) -> None:
        """Release a reservation whose side effect FAILED before producing a
        response, so an honest retry is allowed to run rather than being wedged
        behind a permanent in-progress lock."""
        rec = self._records.get(key)
        if rec is not None and rec["response"] is None:
            del self._records[key]
