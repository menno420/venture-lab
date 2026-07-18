#!/usr/bin/env python3
"""Rate-Limit Test Kit (rltk) — point it at your own API endpoint and prove your
server-side rate limiter behaves correctly: requests under the limit succeed,
the first request past the limit returns 429 with a valid Retry-After, the
RateLimit-* headers are consistent, and the window actually resets when it says
it will.

Stdlib only. No pip install, no build step. Python 3.8+. No account, no vendor.

This is NOT a webhook signature kit and NOT the idempotency kit — it tests
THROTTLING correctness (429 + Retry-After + RateLimit-* + window reset). The 429
+ Retry-After semantics are RFC 6585 §4 / RFC 9110 §10.2.3; the RateLimit-Limit/
Remaining/Reset fields follow the IETF draft "RateLimit header fields for HTTP"
(and the legacy X-RateLimit-* convention). See fixtures/PROVENANCE.md — the
draft fields are NOT yet an RFC, and the kit says so.

Properties checked (each PASS/FAIL against YOUR endpoint):

  1. under-limit         The first `limit` requests inside a window return 2xx.
                         Throttling before the limit is a FAIL (limit under-set).
  2. over-limit          Request `limit`+1 within the window returns 429. A 2xx
                         there is an off-by-one quota leak (your "100/hr" allows
                         101).
  3. retry-after         The 429 carries a `Retry-After` that is positive, sane
                         delay-seconds OR a future HTTP-date. Missing / 0 /
                         negative / absurd is a FAIL (clients can't time a retry).
  4. headers             RateLimit-*/X-RateLimit-* (when present) are consistent:
                         Limit is a positive int, Remaining decrements and hits 0
                         at the boundary, Reset points into the future.
  5. window-reset        After the advertised reset elapses, requests succeed
                         again. A limiter that never resets is a FAIL.
  6. retry-after-honored The advertised Retry-After matches when the service
                         actually resumes: still 429 before it, 2xx after it
                         (within tolerance).

`rltk demo` runs all six against the bundled reference stubs — the CORRECT one
(all pass) and the deliberately NAIVE one (flagged) — with ZERO accounts and a
loud banner, so you can see the checks working before you point them at your app.
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from email.utils import parsedate_to_datetime
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_PRIMARY = "api_ping"
DEFAULT_LIMIT = 5
DEFAULT_WINDOW = 1.2          # seconds — reset/settle fallback when no Retry-After
DEFAULT_MAX_DELAY = 3600      # seconds — a Retry-After larger than this is "insane"
TOLERANCE = 0.4              # seconds of slack added to a timed wait


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def load_manifest() -> dict:
    manifest = json.loads((FIXTURES_DIR / "MANIFEST.json").read_text(encoding="utf-8"))
    manifest.pop("_comment", None)
    return manifest


def _entry_for(stem: str) -> dict:
    stem = stem[:-5] if stem.endswith(".json") else stem
    manifest = load_manifest()
    if stem not in manifest:
        raise SystemExit(
            f"error: fixture {stem!r} has no entry in fixtures/MANIFEST.json — "
            f"run `rltk list` to see bundled fixtures."
        )
    return manifest[stem]


def load_fixture(stem: str) -> bytes:
    stem = stem[:-5] if stem.endswith(".json") else stem
    p = FIXTURES_DIR / (stem + ".json")
    if not p.exists():
        raise SystemExit(f"error: fixture not found: {stem}. Run `rltk list`.")
    return p.read_bytes()


def method_for(stem: str) -> str:
    return _entry_for(stem).get("method", "GET").upper()


def path_for(stem: str) -> str:
    return _entry_for(stem)["path"]


def content_type_for(stem: str) -> str:
    return _entry_for(stem).get("content_type", "application/json")


def list_fixtures():
    return sorted(load_manifest().keys())


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def fire(base_url, method, path, body=None, content_type="application/json",
         timeout=10.0):
    """Fire one request. Returns (status, headers_lower, body_text). A dropped
    connection yields status 0 so a crashing endpoint is a FAIL, not an
    exception. `headers_lower` is a case-insensitive dict of response headers."""
    url = base_url.rstrip("/") + path
    data = body if (method in ("POST", "PUT", "PATCH") and body) else None
    req = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, _lower_headers(resp.headers), resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, _lower_headers(e.headers), e.read().decode("utf-8", "replace")
    except OSError as e:
        return 0, {}, f"<no HTTP response: {e}>"


def _lower_headers(headers) -> dict:
    out = {}
    if headers is None:
        return out
    for k, v in headers.items():
        out[k.lower()] = v
    return out


def reset(base_url) -> bool:
    """Best-effort: POST /_debug/reset (the bundled stubs support it). Returns
    True on a 200. A real endpoint without that route returns non-200 and the
    caller falls back to --settle."""
    s, _, _ = fire(base_url, "POST", "/_debug/reset", body=b"{}")
    return s == 200


def _fresh_window(base_url, settle):
    """Start a property from a clean window: reset the bundled stub, or (against a
    real endpoint) sleep `settle` seconds to let the current window roll over."""
    if not reset(base_url) and settle > 0:
        time.sleep(settle)


def is_2xx(s: int) -> bool:
    return 200 <= s < 300


def _fixture_call(fixture):
    return method_for(fixture), path_for(fixture), load_fixture(fixture), content_type_for(fixture)


def _rl(headers, *names):
    for n in names:
        if n in headers:
            return headers[n]
    return None


def _fire_until_429(base_url, fixture, cap):
    """Fire up to `cap` requests; return (statuses, the_429_headers_or_None)."""
    method, path, body, ct = _fixture_call(fixture)
    statuses = []
    hdrs_429 = None
    for _ in range(cap):
        s, h, _b = fire(base_url, method, path, body, ct)
        statuses.append(s)
        if s == 429:
            hdrs_429 = h
            break
    return statuses, hdrs_429


def _parse_retry_after(headers, max_delay):
    """Return (ok, detail, delay_seconds_or_None). Accepts positive sane
    delay-seconds OR a future HTTP-date (RFC 9110 §10.2.3)."""
    ra = _rl(headers, "retry-after")
    if ra is None:
        return False, "the 429 carried NO Retry-After header — a client has no idea when to retry", None
    ra = ra.strip()
    if ra.lstrip("-").isdigit():
        secs = int(ra)
        if secs <= 0:
            return False, f"Retry-After is {secs} (must be positive)", None
        if secs > max_delay:
            return False, f"Retry-After is {secs}s — larger than the sane cap ({max_delay}s)", None
        return True, f"Retry-After: {secs}s (positive, sane delay-seconds)", secs
    try:
        when = parsedate_to_datetime(ra)
    except (TypeError, ValueError, OverflowError):
        return False, f"Retry-After {ra!r} is neither delay-seconds nor a valid HTTP-date", None
    import datetime as _dt
    now = _dt.datetime.now(when.tzinfo) if when.tzinfo else _dt.datetime.now()
    delta = (when - now).total_seconds()
    if delta <= 0:
        return False, f"Retry-After HTTP-date {ra!r} is in the PAST", None
    if delta > max_delay:
        return False, f"Retry-After HTTP-date is {int(delta)}s out — larger than the sane cap", None
    return True, f"Retry-After: {ra!r} (future HTTP-date, ~{int(delta)}s)", delta


# --------------------------------------------------------------------------- #
# Properties — each returns (passed: bool, detail: str)
# --------------------------------------------------------------------------- #
def check_under_limit(base_url, fixture, limit=DEFAULT_LIMIT, settle=0.0):
    """The first `limit` requests inside a window must all return 2xx."""
    _fresh_window(base_url, settle)
    method, path, body, ct = _fixture_call(fixture)
    statuses = [fire(base_url, method, path, body, ct)[0] for _ in range(limit)]
    throttled = [i + 1 for i, s in enumerate(statuses) if s == 429]
    if throttled:
        return False, (f"request #{throttled[0]} of the first {limit} was throttled (429) — "
                       f"the endpoint 429s BEFORE its own limit (statuses {statuses}).")
    if all(is_2xx(s) for s in statuses):
        return True, f"the first {limit} requests all returned 2xx (statuses {statuses})"
    return False, f"a request under the limit did not return 2xx (statuses {statuses})"


def check_over_limit(base_url, fixture, limit=DEFAULT_LIMIT, settle=0.0):
    """Request `limit`+1 within the window must return 429 (no off-by-one)."""
    _fresh_window(base_url, settle)
    method, path, body, ct = _fixture_call(fixture)
    statuses = [fire(base_url, method, path, body, ct)[0] for _ in range(limit + 1)]
    early = [i + 1 for i, s in enumerate(statuses[:limit]) if s == 429]
    if early:
        return False, (f"request #{early[0]} was throttled BEFORE the limit of {limit} "
                       f"(statuses {statuses}).")
    last = statuses[limit]
    if last == 429:
        return True, f"request #{limit + 1} correctly returned 429 (statuses {statuses})"
    if is_2xx(last):
        return False, (f"request #{limit + 1} was ACCEPTED (HTTP {last}) — off-by-one quota leak: "
                       f"a limit of {limit} let {limit + 1} through (statuses {statuses}).")
    return False, f"request #{limit + 1} returned HTTP {last} (expected 429): statuses {statuses}"


def check_retry_after(base_url, fixture, limit=DEFAULT_LIMIT, settle=0.0,
                      max_delay=DEFAULT_MAX_DELAY):
    """The 429 must carry a valid, positive, sane Retry-After."""
    _fresh_window(base_url, settle)
    statuses, hdrs = _fire_until_429(base_url, fixture, cap=limit + 6)
    if hdrs is None:
        return False, (f"no 429 in {len(statuses)} requests — the endpoint did not enforce a limit, "
                       f"so there is no Retry-After to check (statuses {statuses}).")
    ok, detail, _secs = _parse_retry_after(hdrs, max_delay)
    return ok, detail


def check_headers(base_url, fixture, limit=DEFAULT_LIMIT, settle=0.0):
    """RateLimit-*/X-RateLimit-* (when present) must be internally consistent."""
    _fresh_window(base_url, settle)
    method, path, body, ct = _fixture_call(fixture)
    remainings, limits, resets, saw_any = [], [], [], False
    for _ in range(limit):
        _s, h, _b = fire(base_url, method, path, body, ct)
        lim = _rl(h, "ratelimit-limit", "x-ratelimit-limit")
        rem = _rl(h, "ratelimit-remaining", "x-ratelimit-remaining")
        rst = _rl(h, "ratelimit-reset", "x-ratelimit-reset")
        if lim is not None or rem is not None or rst is not None:
            saw_any = True
        if lim is not None:
            limits.append(lim)
        if rem is not None and rem.lstrip("-").isdigit():
            remainings.append(int(rem))
        if rst is not None and rst.lstrip("-").isdigit():
            resets.append(int(rst))
    if not saw_any:
        return True, "endpoint emits no RateLimit-*/X-RateLimit-* headers (optional per the draft) — nothing to check"
    # Limit: a positive integer.
    if limits and not all(v.lstrip("-").isdigit() and int(v) > 0 for v in limits):
        return False, f"RateLimit-Limit is not a positive integer ({limits})"
    # Remaining: must decrement across the burst and reach 0 by the last success.
    if not remainings:
        return False, "RateLimit-Remaining is present but non-numeric — a client cannot read its budget"
    if any(remainings[i + 1] > remainings[i] for i in range(len(remainings) - 1)):
        return False, f"RateLimit-Remaining did not decrement monotonically ({remainings})"
    if remainings[-1] >= remainings[0] and len(remainings) > 1:
        return False, (f"RateLimit-Remaining never decreased across {len(remainings)} requests "
                       f"({remainings}) — it is stuck; a client can't see itself running out.")
    if remainings[-1] != 0:
        return False, (f"RateLimit-Remaining did not reach 0 at the limit boundary "
                       f"(ended at {remainings[-1]}, values {remainings}).")
    # Reset: must point into the future (delta-seconds, or an absolute epoch).
    if not resets:
        return False, "RateLimit-Reset is present but non-numeric — a client can't tell when the window resets"
    bad = _reset_not_future(resets[0])
    if bad:
        return False, bad
    return True, (f"headers consistent: Limit ok, Remaining {remainings[0]}→{remainings[-1]} (hits 0 at "
                  f"the boundary), Reset points to the future")


def _reset_not_future(value: int):
    """Return an error string if the Reset value does not indicate the future,
    else None. Heuristic: a value > 1e9 is treated as an absolute UNIX epoch
    (must be > now); otherwise it is delta-seconds (must be > 0)."""
    if value > 1_000_000_000:
        if value <= int(time.time()):
            return f"RateLimit-Reset {value} is an absolute timestamp in the PAST (stale reset)"
        return None
    if value <= 0:
        return f"RateLimit-Reset {value} is not positive — the window never resets"
    return None


def check_window_reset(base_url, fixture, limit=DEFAULT_LIMIT, settle=0.0,
                       window=DEFAULT_WINDOW, max_delay=DEFAULT_MAX_DELAY):
    """After the advertised reset elapses, requests must succeed again."""
    _fresh_window(base_url, settle)
    statuses, hdrs = _fire_until_429(base_url, fixture, cap=limit + 6)
    if hdrs is None:
        return False, f"no 429 in {len(statuses)} requests — cannot test reset (no enforced limit)."
    ok, _detail, secs = _parse_retry_after(hdrs, max_delay)
    wait = (secs if ok and secs else window) + TOLERANCE
    time.sleep(wait)
    method, path, body, ct = _fixture_call(fixture)
    s, _h, _b = fire(base_url, method, path, body, ct)
    if is_2xx(s):
        return True, f"after ~{wait:.1f}s the window reset and a request succeeded again (HTTP {s})"
    return False, (f"still throttled (HTTP {s}) ~{wait:.1f}s after the advertised reset — the window "
                   f"did not reset when it said it would.")


def check_retry_after_honored(base_url, fixture, limit=DEFAULT_LIMIT, settle=0.0,
                              max_delay=DEFAULT_MAX_DELAY):
    """The advertised Retry-After must match when the service actually resumes."""
    _fresh_window(base_url, settle)
    statuses, hdrs = _fire_until_429(base_url, fixture, cap=limit + 6)
    if hdrs is None:
        return False, f"no 429 in {len(statuses)} requests — nothing to honour (no enforced limit)."
    ok, detail, secs = _parse_retry_after(hdrs, max_delay)
    if not ok or not secs:
        return False, (f"the 429 carried no usable Retry-After ({detail}) — a client cannot honour a "
                       f"delay it was never given.")
    method, path, body, ct = _fixture_call(fixture)
    # Before the advertised delay elapses the service must still be throttled.
    s_before, _h, _b = fire(base_url, method, path, body, ct)
    if is_2xx(s_before):
        return False, (f"the service resumed (HTTP {s_before}) IMMEDIATELY, before the advertised "
                       f"Retry-After of {secs}s elapsed — the advertised delay overstates the wait.")
    # After the advertised delay (plus slack) it must resume.
    time.sleep(secs + TOLERANCE)
    s_after, _h2, _b2 = fire(base_url, method, path, body, ct)
    if is_2xx(s_after):
        return True, (f"still 429 before the {secs}s Retry-After, 2xx after it (within tolerance) — "
                      f"the advertised delay is honoured.")
    return False, (f"still throttled (HTTP {s_after}) after waiting the advertised {secs}s Retry-After — "
                   f"the delay understates the real wait; a client that trusts it still gets 429s.")


# --------------------------------------------------------------------------- #
# Runner / reporting
# --------------------------------------------------------------------------- #
def _print_result(name, passed, detail):
    print(f"[{'PASS' if passed else 'FAIL'}] {name:20s} {detail}")


def run_suite(base_url, fixture, limit, settle, window, max_delay):
    checks = [
        ("under-limit", lambda: check_under_limit(base_url, fixture, limit, settle)),
        ("over-limit", lambda: check_over_limit(base_url, fixture, limit, settle)),
        ("retry-after", lambda: check_retry_after(base_url, fixture, limit, settle, max_delay)),
        ("headers", lambda: check_headers(base_url, fixture, limit, settle)),
        ("window-reset", lambda: check_window_reset(base_url, fixture, limit, settle, window, max_delay)),
        ("retry-after-honored", lambda: check_retry_after_honored(base_url, fixture, limit, settle, max_delay)),
    ]
    failures = 0
    for name, fn in checks:
        passed, detail = fn()
        _print_result(name, passed, detail)
        if not passed:
            failures += 1
    return failures


# --------------------------------------------------------------------------- #
# CLI commands
# --------------------------------------------------------------------------- #
def cmd_check(args) -> int:
    print(f"Rate-Limit Test Kit — checking {args.url}")
    print(f"  fixture: {args.fixture} ({method_for(args.fixture)} {path_for(args.fixture)})   "
          f"assumed limit: {args.limit}/window")
    print(f"  (set --limit to your window budget; --window <seconds> is the reset "
          f"fallback; --settle <seconds> starts each check in a fresh window on a\n"
          f"   real endpoint without a debug-reset route)\n")
    failures = run_suite(args.url, args.fixture, args.limit, args.settle, args.window, args.max_delay)
    print()
    if failures == 0:
        print("ALL PROPERTIES PASS — this endpoint's rate limiter behaves correctly.")
        return 0
    print(f"{failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.")
    return 1


def _single(args, fn, name, *extra) -> int:
    passed, detail = fn(args.url, args.fixture, *extra)
    _print_result(name, passed, detail)
    return 0 if passed else 1


def cmd_under_limit(args):
    return _single(args, check_under_limit, "under-limit", args.limit, args.settle)


def cmd_over_limit(args):
    return _single(args, check_over_limit, "over-limit", args.limit, args.settle)


def cmd_retry_after(args):
    return _single(args, check_retry_after, "retry-after", args.limit, args.settle, args.max_delay)


def cmd_headers(args):
    return _single(args, check_headers, "headers", args.limit, args.settle)


def cmd_window_reset(args):
    return _single(args, check_window_reset, "window-reset", args.limit, args.settle, args.window, args.max_delay)


def cmd_retry_after_honored(args):
    return _single(args, check_retry_after_honored, "retry-after-honored", args.limit, args.settle, args.max_delay)


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled fixtures (docs-derived request templates — see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        e = manifest[stem]
        print(f"  {stem:14s}  {e.get('method','GET'):5s} {e.get('path','?'):14s}  "
              f"{e.get('content_type','application/json')}  — {e.get('note','')}")
    return 0


def cmd_demo(args) -> int:
    """Run the whole suite against the bundled reference stubs — zero accounts."""
    import stub_handler
    import stub_handler_naive
    import threading

    print("=" * 72)
    print("  RLTK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.")
    print("  NO real endpoint, NO accounts, NO money. This proves the kit works")
    print("  before you point `rltk check --url` at your own app.")
    print("=" * 72)

    limit, window_ms = 5, 800
    window_s = window_ms / 1000.0
    correct = stub_handler.serve(0, limit=limit, window_ms=window_ms, header_style="both")
    naive = stub_handler_naive.serve(0, limit=limit, window_ms=window_ms)
    cport = correct.server_address[1]
    nport = naive.server_address[1]
    threading.Thread(target=correct.serve_forever, daemon=True).start()
    threading.Thread(target=naive.serve_forever, daemon=True).start()
    try:
        print(f"\n--- CORRECT stub (limit {limit}/{window_ms}ms) — expect ALL PASS ---")
        cf = run_suite(f"http://127.0.0.1:{cport}", DEFAULT_PRIMARY, limit, 0.0, window_s, DEFAULT_MAX_DELAY)
        print(f"\n--- NAIVE stub (off-by-one, no Retry-After, stale headers) — expect the kit to FLAG it ---")
        nf = run_suite(f"http://127.0.0.1:{nport}", DEFAULT_PRIMARY, limit, 0.0, window_s, DEFAULT_MAX_DELAY)
    finally:
        correct.shutdown()
        naive.shutdown()

    print("\n" + "=" * 72)
    if cf == 0 and nf > 0:
        print(f"  DEMO OK: correct stub passed all 6; naive stub flagged on {nf} property(ies).")
        print("  The kit distinguishes a correct limiter from a broken one.")
        print("=" * 72)
        return 0
    print(f"  DEMO UNEXPECTED: correct failures={cf}, naive failures={nf} (expected 0 and >0).")
    print("=" * 72)
    return 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="rltk",
        description="Rate-Limit Test Kit — prove your endpoint's rate limiter is correct.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp, window=False, max_delay=False):
        sp.add_argument("--url", required=True, help="your endpoint base, e.g. http://localhost:8000")
        sp.add_argument("--fixture", default=DEFAULT_PRIMARY, help=f"fixture name (default {DEFAULT_PRIMARY})")
        sp.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                        help=f"requests allowed per window (default {DEFAULT_LIMIT}; read from RateLimit-Limit if you don't know it)")
        sp.add_argument("--settle", type=float, default=0.0,
                        help="seconds to wait before a burst to start in a fresh window (real endpoints without /_debug/reset)")
        if window:
            sp.add_argument("--window", type=float, default=DEFAULT_WINDOW,
                            help=f"window length in seconds — the reset-wait fallback when there's no Retry-After (default {DEFAULT_WINDOW})")
        if max_delay:
            sp.add_argument("--max-delay", type=int, default=DEFAULT_MAX_DELAY, dest="max_delay",
                            help=f"a Retry-After larger than this many seconds is treated as insane (default {DEFAULT_MAX_DELAY})")

    c = sub.add_parser("check", help="run all six properties against your endpoint")
    common(c, window=True, max_delay=True)
    c.set_defaults(func=cmd_check)

    u = sub.add_parser("under-limit", help="the first `limit` requests return 2xx")
    common(u)
    u.set_defaults(func=cmd_under_limit)

    o = sub.add_parser("over-limit", help="request limit+1 returns 429 (no off-by-one)")
    common(o)
    o.set_defaults(func=cmd_over_limit)

    r = sub.add_parser("retry-after", help="the 429 carries a valid, positive, sane Retry-After")
    common(r, max_delay=True)
    r.set_defaults(func=cmd_retry_after)

    h = sub.add_parser("headers", help="RateLimit-*/X-RateLimit-* are consistent")
    common(h)
    h.set_defaults(func=cmd_headers)

    w = sub.add_parser("window-reset", help="the window resets after the advertised delay")
    common(w, window=True, max_delay=True)
    w.set_defaults(func=cmd_window_reset)

    k = sub.add_parser("retry-after-honored", help="the advertised Retry-After matches when service resumes")
    common(k, max_delay=True)
    k.set_defaults(func=cmd_retry_after_honored)

    sub.add_parser("demo", help="run all six against the bundled stubs (zero accounts)").set_defaults(func=cmd_demo)
    sub.add_parser("list", help="list bundled fixtures").set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
