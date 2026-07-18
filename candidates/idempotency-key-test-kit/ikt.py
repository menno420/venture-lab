#!/usr/bin/env python3
"""Idempotency Key Test Kit (ikt) — point it at your own POST endpoint and prove
your `Idempotency-Key` handling is correct: safe retries trigger the side effect
EXACTLY ONCE, key reuse with a different body is rejected, concurrent retries
don't double-execute, and keys are scoped per endpoint.

Stdlib only. No pip install, no build step. Python 3.8+. No account, no vendor.

This is NOT a webhook signature kit — it does not verify HMAC signatures. It
tests the DEDUP / SAFE-RETRY contract of an API's `Idempotency-Key` support,
the property that stops a network retry from charging a customer twice.

Behaviour specifics follow Stripe's widely-used model; the header itself is the
subject of the IETF draft "The Idempotency-Key HTTP Header Field". See
fixtures/PROVENANCE.md for the cited sources.

Properties checked (each is PASS/FAIL against YOUR endpoint):

  1. replay        Same key + same body → the STORED original response is
                   replayed (same resource id); the side effect runs ONCE. A
                   retry that mints a NEW resource id is a double side effect.
  2. mismatch      Same key + a DIFFERENT body → rejected (409/422). Accepting
                   it silently returns a stale result or double-executes.
  3. distinct-keys Two DIFFERENT keys + the same body → two independent
                   resources. Collapsing them means the endpoint keys on the
                   body, not the Idempotency-Key.
  4. concurrent    Two in-flight requests with the same key → ONE side effect
                   (in-flight lock); the loser replays the stored response or
                   gets a 409. Two resources means no lock — a retry-storm
                   double charge.
  5. missing-key   No key header → your DOCUMENTED policy: `required` (4xx) or
                   `passthrough` (2xx, processed without idempotency). You tell
                   the kit which; it never guesses silently.

`ikt demo` runs all five against the bundled reference stubs — the CORRECT one
(all pass) and the deliberately NAIVE one (flagged) — with ZERO accounts and a
loud banner, so you can see the checks working before you point them at your app.
"""
import argparse
import json
import sys
import threading
import urllib.error
import urllib.request
import uuid
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
IDEMPOTENCY_HEADER = "Idempotency-Key"
DEFAULT_ID_FIELD = "id"
DEFAULT_PRIMARY = "charge_basic"
DEFAULT_VARIANT = "charge_mismatch"


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #
def load_manifest() -> dict:
    """fixture stem -> {"method", "path", "content_type", ...} (fixtures/MANIFEST.json)."""
    manifest = json.loads((FIXTURES_DIR / "MANIFEST.json").read_text(encoding="utf-8"))
    manifest.pop("_comment", None)
    return manifest


def _entry_for(stem: str) -> dict:
    stem = stem[:-5] if stem.endswith(".json") else stem
    manifest = load_manifest()
    if stem not in manifest:
        raise SystemExit(
            f"error: fixture {stem!r} has no entry in fixtures/MANIFEST.json — "
            f"add its method/path/content_type. Run `ikt list` to see bundled fixtures."
        )
    return manifest[stem]


def fixture_file(stem: str) -> Path:
    stem = stem[:-5] if stem.endswith(".json") else stem
    p = FIXTURES_DIR / (stem + ".json")
    if p.exists():
        return p
    raise SystemExit(f"error: fixture not found: {stem}. Run `ikt list` to see bundled fixtures.")


def load_fixture(stem: str) -> bytes:
    """The RAW request body bytes for a fixture (exactly as sent on the wire)."""
    return fixture_file(stem).read_bytes()


def path_for(stem: str) -> str:
    return _entry_for(stem)["path"]


def content_type_for(stem: str) -> str:
    return _entry_for(stem).get("content_type", "application/json")


def list_fixtures():
    return sorted(load_manifest().keys())


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def new_key() -> str:
    """A fresh idempotency key for a scenario run."""
    return "ikt_" + uuid.uuid4().hex


def post(base_url: str, path: str, body: bytes, content_type: str,
         key=None, timeout: float = 10.0):
    """POST body to base_url + path with an optional Idempotency-Key.
    Returns (status_code, body_text). A dropped connection yields status 0 so a
    crashing endpoint is a FAIL, not an exception."""
    url = base_url.rstrip("/") + path
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", content_type)
    if key is not None:
        req.add_header(IDEMPOTENCY_HEADER, key)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except OSError as e:
        return 0, f"<no HTTP response: {e}>"


def get(base_url: str, path: str, timeout: float = 10.0):
    """GET base_url + path. Returns (status_code, body_text). Used by `demo` to
    read the reference stubs' /_debug/side_effects counter."""
    url = base_url.rstrip("/") + path
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except OSError as e:
        return 0, f"<no HTTP response: {e}>"


def resource_id(body_text: str, id_field: str):
    """The resource identifier from a response body, or the whole body when the
    field is absent (so two responses can still be compared for identity)."""
    try:
        data = json.loads(body_text)
    except (ValueError, json.JSONDecodeError):
        return ("<raw>", body_text)
    if isinstance(data, dict) and id_field in data:
        return ("id", data[id_field])
    return ("<raw>", body_text)


def is_2xx(status: int) -> bool:
    return 200 <= status < 300


# --------------------------------------------------------------------------- #
# Properties — each returns (passed: bool, detail: str)
# --------------------------------------------------------------------------- #
def check_replay(base_url, fixture, id_field=DEFAULT_ID_FIELD):
    """Same key + same body → stored response replayed; side effect runs once."""
    path, ct, body = path_for(fixture), content_type_for(fixture), load_fixture(fixture)
    key = new_key()
    s1, b1 = post(base_url, path, body, ct, key=key)
    if not is_2xx(s1):
        return False, f"first request was not accepted (HTTP {s1}) — cannot test replay: {b1[:160]}"
    s2, b2 = post(base_url, path, body, ct, key=key)
    if not is_2xx(s2):
        return False, (f"the retry (same key + same body) was rejected (HTTP {s2}); a safe "
                       f"retry must replay the stored response, not error: {b2[:160]}")
    id1, id2 = resource_id(b1, id_field), resource_id(b2, id_field)
    if id1 == id2:
        return True, f"retry replayed the stored response ({id1[0]}={id1[1]!r}); exactly one side effect"
    return False, (f"the retry created a DIFFERENT resource ({id1[1]!r} → {id2[1]!r}) — the side "
                   f"effect ran TWICE. A retried charge would double-charge.")


def check_mismatch(base_url, fixture, variant):
    """Same key + different body → rejected (409/422)."""
    path, ct = path_for(fixture), content_type_for(fixture)
    body, vbody = load_fixture(fixture), load_fixture(variant)
    if body == vbody:
        return False, f"cannot test: fixture {fixture!r} and variant {variant!r} have identical bodies"
    key = new_key()
    s1, b1 = post(base_url, path, body, ct, key=key)
    if not is_2xx(s1):
        return False, f"first request was not accepted (HTTP {s1}) — cannot test mismatch: {b1[:160]}"
    s2, b2 = post(base_url, path, vbody, ct, key=key)
    if s2 in (409, 422):
        return True, f"same key + different body correctly rejected (HTTP {s2})"
    if is_2xx(s2):
        return False, (f"same key + a DIFFERENT body was ACCEPTED (HTTP {s2}) — key reuse with a "
                       f"mismatched payload must be rejected (409/422), not silently served/executed.")
    return False, f"same key + different body returned HTTP {s2} (expected 409/422): {b2[:160]}"


def check_distinct_keys(base_url, fixture, id_field=DEFAULT_ID_FIELD):
    """Two different keys + same body → two independent resources (per-key scope)."""
    path, ct, body = path_for(fixture), content_type_for(fixture), load_fixture(fixture)
    s1, b1 = post(base_url, path, body, ct, key=new_key())
    s2, b2 = post(base_url, path, body, ct, key=new_key())
    if not (is_2xx(s1) and is_2xx(s2)):
        return False, f"one of two distinct-key requests was rejected (HTTP {s1}, {s2}) — cannot test scoping"
    id1, id2 = resource_id(b1, id_field), resource_id(b2, id_field)
    if id1 != id2:
        return True, f"two different keys produced two resources ({id1[1]!r}, {id2[1]!r}) — keys are scoped"
    return False, (f"two DIFFERENT keys collapsed to one resource ({id1[1]!r}) — the endpoint is "
                   f"keying on the request body, not the Idempotency-Key.")


def check_concurrent(base_url, fixture, n=2, id_field=DEFAULT_ID_FIELD):
    """Two in-flight requests, same key + same body → one side effect."""
    path, ct, body = path_for(fixture), content_type_for(fixture), load_fixture(fixture)
    key = new_key()
    results = [None] * n

    def fire(i):
        results[i] = post(base_url, path, body, ct, key=key)

    threads = [threading.Thread(target=fire, args=(i,)) for i in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    ok = [r for r in results if r and is_2xx(r[0])]
    conflicts = [r for r in results if r and r[0] == 409]
    distinct = {resource_id(b, id_field) for _, b in ok}
    if not ok:
        return False, f"no concurrent request succeeded (statuses {[r[0] for r in results]})"
    if len(distinct) <= 1:
        extra = f", {len(conflicts)} got 409" if conflicts else ""
        return True, (f"{len(results)} concurrent same-key requests → ONE side effect "
                      f"(1 distinct resource{extra})")
    ids = [d[1] for d in distinct]
    return False, (f"{len(results)} concurrent same-key requests created {len(distinct)} resources "
                   f"({ids}) — no in-flight lock; a retry storm double-executes.")


def check_missing_key(base_url, fixture, mode):
    """No key header → documented policy: required (4xx) or passthrough (2xx)."""
    path, ct, body = path_for(fixture), content_type_for(fixture), load_fixture(fixture)
    s, b = post(base_url, path, body, ct, key=None)
    if mode == "required":
        if 400 <= s < 500:
            return True, f"missing key correctly rejected (HTTP {s}) under the `required` policy"
        return False, (f"missing key was NOT rejected (HTTP {s}) though the policy is `required` — "
                       f"a keyless request must fail closed (400): {b[:160]}")
    if mode == "passthrough":
        if is_2xx(s):
            return True, f"missing key processed (HTTP {s}) under the `passthrough` policy"
        return False, f"missing key returned HTTP {s} though the policy is `passthrough` (expected 2xx): {b[:160]}"
    raise SystemExit(f"error: unknown missing-key mode {mode!r} (use `required` or `passthrough`)")


# --------------------------------------------------------------------------- #
# Runner / reporting
# --------------------------------------------------------------------------- #
def _print_result(name, passed, detail):
    verdict = "PASS" if passed else "FAIL"
    print(f"[{verdict}] {name:14s} {detail}")


def run_suite(base_url, fixture, variant, missing_key_mode):
    """Run all five properties; return the number of failures."""
    checks = [
        ("replay", lambda: check_replay(base_url, fixture)),
        ("mismatch", lambda: check_mismatch(base_url, fixture, variant)),
        ("distinct-keys", lambda: check_distinct_keys(base_url, fixture)),
        ("concurrent", lambda: check_concurrent(base_url, fixture)),
        ("missing-key", lambda: check_missing_key(base_url, fixture, missing_key_mode)),
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
    print(f"Idempotency Key Test Kit — checking {args.url}")
    print(f"  primary fixture: {args.fixture} (POST {path_for(args.fixture)})   "
          f"variant: {args.variant}")
    print(f"  missing-key policy assumed: {args.missing_key_mode}  "
          f"(set --missing-key-mode to match your documented behaviour)\n")
    failures = run_suite(args.url, args.fixture, args.variant, args.missing_key_mode)
    print()
    if failures == 0:
        print("ALL PROPERTIES PASS — this endpoint's Idempotency-Key handling is correct.")
        return 0
    print(f"{failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.")
    return 1


def _single(args, fn, *extra) -> int:
    passed, detail = fn(args.url, args.fixture, *extra)
    _print_result(fn.__name__.replace("check_", "").replace("_", "-"), passed, detail)
    return 0 if passed else 1


def cmd_replay(args):
    return _single(args, check_replay)


def cmd_mismatch(args):
    return _single(args, check_mismatch, args.variant)


def cmd_distinct_keys(args):
    return _single(args, check_distinct_keys)


def cmd_concurrent(args):
    return _single(args, check_concurrent, args.n)


def cmd_missing_key(args):
    return _single(args, check_missing_key, args.mode)


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled fixtures (docs-derived request payloads — see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        e = manifest[stem]
        print(f"  {stem:16s}  {e.get('method','POST'):4s} {e.get('path','?'):12s}  "
              f"{e.get('content_type','application/json')}  — {e.get('note','')}")
    return 0


def cmd_demo(args) -> int:
    """Run the whole suite against the bundled reference stubs — zero accounts."""
    import stub_handler
    import stub_handler_naive

    print("=" * 72)
    print("  IKT DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.")
    print("  NO real endpoint, NO accounts, NO money. This proves the kit works")
    print("  before you point `ikt check --url` at your own app.")
    print("=" * 72)

    # A small execution delay makes the two concurrent requests genuinely
    # overlap, so the in-flight lock (correct) vs its absence (naive) is real.
    correct = stub_handler.serve(0, require_key=True, delay_ms=60)
    naive = stub_handler_naive.serve(0, delay_ms=60)
    cport = correct.server_address[1]
    nport = naive.server_address[1]
    threading.Thread(target=correct.serve_forever, daemon=True).start()
    threading.Thread(target=naive.serve_forever, daemon=True).start()
    try:
        print(f"\n--- CORRECT stub (http://127.0.0.1:{cport}) — expect ALL PASS ---")
        cf = run_suite(f"http://127.0.0.1:{cport}", DEFAULT_PRIMARY, DEFAULT_VARIANT, "required")
        _, cnt = get(f"http://127.0.0.1:{cport}", "/_debug/side_effects")
        print(f"        (side-effect counter on the correct stub: {cnt})")

        print(f"\n--- NAIVE stub (http://127.0.0.1:{nport}) — expect the kit to FLAG it ---")
        nf = run_suite(f"http://127.0.0.1:{nport}", DEFAULT_PRIMARY, DEFAULT_VARIANT, "required")
        _, ncnt = get(f"http://127.0.0.1:{nport}", "/_debug/side_effects")
        print(f"        (side-effect counter on the naive stub: {ncnt} — it over-executed)")
    finally:
        correct.shutdown()
        naive.shutdown()

    print("\n" + "=" * 72)
    if cf == 0 and nf > 0:
        print(f"  DEMO OK: correct stub passed all 5; naive stub flagged on {nf} property(ies).")
        print("  The kit distinguishes correct idempotency from a broken (no-dedup) one.")
        print("=" * 72)
        return 0
    print(f"  DEMO UNEXPECTED: correct failures={cf}, naive failures={nf} (expected 0 and >0).")
    print("=" * 72)
    return 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ikt",
        description="Idempotency Key Test Kit — prove your endpoint's Idempotency-Key handling.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_url_fixture(sp):
        sp.add_argument("--url", required=True, help="your endpoint base, e.g. http://localhost:8000")
        sp.add_argument("--fixture", default=DEFAULT_PRIMARY, help=f"fixture name (default {DEFAULT_PRIMARY})")

    c = sub.add_parser("check", help="run all five properties against your endpoint")
    add_url_fixture(c)
    c.add_argument("--variant", default=DEFAULT_VARIANT,
                   help=f"a DIFFERENT-body fixture for the mismatch check (default {DEFAULT_VARIANT})")
    c.add_argument("--missing-key-mode", default="required", choices=["required", "passthrough"],
                   dest="missing_key_mode",
                   help="your documented policy for a request with NO Idempotency-Key")
    c.set_defaults(func=cmd_check)

    r = sub.add_parser("replay", help="same key + same body → stored response replayed (exactly once)")
    add_url_fixture(r)
    r.set_defaults(func=cmd_replay)

    m = sub.add_parser("mismatch", help="same key + different body → rejected (409/422)")
    add_url_fixture(m)
    m.add_argument("--variant", default=DEFAULT_VARIANT, help=f"the different-body fixture (default {DEFAULT_VARIANT})")
    m.set_defaults(func=cmd_mismatch)

    d = sub.add_parser("distinct-keys", help="two different keys + same body → two resources (scoping)")
    add_url_fixture(d)
    d.set_defaults(func=cmd_distinct_keys)

    n = sub.add_parser("concurrent", help="two in-flight same-key requests → one side effect")
    add_url_fixture(n)
    n.add_argument("--n", type=int, default=2, help="how many concurrent requests (default 2)")
    n.set_defaults(func=cmd_concurrent)

    k = sub.add_parser("missing-key", help="no key header → your documented policy")
    add_url_fixture(k)
    k.add_argument("--mode", default="required", choices=["required", "passthrough"],
                   help="your documented policy for a keyless request")
    k.set_defaults(func=cmd_missing_key)

    sub.add_parser("demo", help="run all five against the bundled stubs (zero accounts)").set_defaults(func=cmd_demo)
    sub.add_parser("list", help="list bundled fixtures").set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
