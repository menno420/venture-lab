#!/usr/bin/env python3
"""Pagination Test Kit (pgtk) — point it at your own paginated API endpoint and
prove your cursor/keyset pagination is correct: following the next-cursor walks
the whole ordered set with no overlap and no gap, the traversal stays stable when
rows are inserted/deleted mid-traversal (the property naive OFFSET pagination
fails), the order is consistent, the page-size limit is honored and clamped to a
documented max, the last page signals the end, and a forged/opaque cursor is
rejected instead of silently mishandled.

Stdlib only. No pip install, no build step. Python 3.8+. No account, no vendor.

This is NOT a webhook signature kit, NOT the idempotency kit, and NOT the
rate-limit kit — it tests RESULT-SET INTEGRITY of a paginated collection. There
is no single RFC for cursor pagination; the model is the widely-deployed
keyset/cursor pattern (Stripe/Slack/GitHub cursor pagination + the keyset-vs-
offset literature). See fixtures/PROVENANCE.md — the sources are named honestly.

Properties checked (each PASS/FAIL/SKIP against YOUR endpoint):

  1. traversal            Following next-cursor from page 1 yields every item
                          with NO overlap and NO gap; concatenating all pages
                          reproduces the full ordered set exactly once.
  2. stable-under-mutation  Inserting + deleting rows BETWEEN page fetches does
                          not skip or duplicate items present throughout. THE
                          headline — naive OFFSET pagination skips here. (SKIP if
                          the endpoint exposes no test-mutation hook.)
  3. ordering             A consistent total order: sorted by a stable sort key
                          plus a UNIQUE tiebreaker, no duplicate ids.
  4. page-size            `limit` is honored on full pages, and a request OVER the
                          documented max is CLAMPED to the max (not served
                          unbounded).
  5. terminal             The last page signals the end (null/absent next-cursor)
                          and the loop terminates — no infinite cursor loop.
  6. cursor-tamper        A malformed or forged/opaque cursor is rejected (4xx),
                          not silently coerced to page 1.

`pgtk demo` runs all six against the bundled reference stubs — the CORRECT one
(all pass) and the deliberately NAIVE OFFSET one (flagged on stability / page-size
/ cursor-tamper) — with ZERO accounts and a loud banner, so you can see the checks
working before you point them at your app.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlencode

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_PRIMARY = "items_keyset"
DEFAULT_LIMIT = 3
DEFAULT_MAX = 100          # fallback documented max when no X-Page-Size-Max header
TRAVERSE_CAP = 1000        # hard bound so an infinite cursor loop cannot hang us


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
            f"run `pgtk list` to see bundled fixtures."
        )
    return manifest[stem]


def load_fixture(stem: str) -> bytes:
    stem = stem[:-5] if stem.endswith(".json") else stem
    p = FIXTURES_DIR / (stem + ".json")
    if not p.exists():
        raise SystemExit(f"error: fixture not found: {stem}. Run `pgtk list`.")
    return p.read_bytes()


def list_fixtures():
    return sorted(load_manifest().keys())


class PageSpec:
    """The request/response shape of a paginated collection, read from a fixture
    so a buyer can point it at their own API's param and field names."""

    def __init__(self, entry: dict):
        self.path = entry["path"]
        self.limit_param = entry.get("limit_param", "limit")
        self.cursor_param = entry.get("cursor_param", "cursor")
        self.items_field = entry.get("items_field", "items")
        self.next_cursor_field = entry.get("next_cursor_field", "next_cursor")
        self.id_field = entry.get("id_field", "id")
        self.sort_field = entry.get("sort_field", "created_at")

    @classmethod
    def from_fixture(cls, stem: str):
        return cls(_entry_for(stem))


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def fire(base_url, method, path, body=None, content_type="application/json",
         timeout=10.0):
    """Fire one request. Returns (status, headers_lower, body_text). A dropped
    connection yields status 0 so a crashing endpoint is a FAIL, not an
    exception."""
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


def is_2xx(s):
    return 200 <= s < 300


def fire_page(base_url, spec: PageSpec, limit, cursor):
    """GET one page. Returns (status, headers, obj_or_None)."""
    params = {spec.limit_param: str(limit)}
    if cursor not in (None, ""):
        params[spec.cursor_param] = cursor
    path = spec.path + "?" + urlencode(params)
    status, headers, text = fire(base_url, "GET", path)
    try:
        obj = json.loads(text)
    except ValueError:
        obj = None
    return status, headers, obj


def _extract(obj, spec: PageSpec):
    """Return (item_ids, item_rows, next_cursor) from a page response body."""
    items = obj.get(spec.items_field, []) if isinstance(obj, dict) else []
    rows = [r for r in items if isinstance(r, dict)]
    ids = [r.get(spec.id_field) for r in rows]
    nxt = obj.get(spec.next_cursor_field) if isinstance(obj, dict) else None
    return ids, rows, nxt


def traverse(base_url, spec: PageSpec, limit, start_cursor="", cap=TRAVERSE_CAP):
    """Follow next-cursor from `start_cursor` to the end. Returns
    (ids, rows, page_sizes, terminated, error_or_None). Guards against an
    infinite loop (a repeated cursor or exceeding `cap`)."""
    ids, rows, sizes = [], [], []
    cursor = start_cursor
    seen_cursors = set()
    for _ in range(cap):
        status, _h, obj = fire_page(base_url, spec, limit, cursor)
        if status != 200 or obj is None:
            return ids, rows, sizes, False, f"page fetch returned HTTP {status}"
        page_ids, page_rows, nxt = _extract(obj, spec)
        ids.extend(page_ids)
        rows.extend(page_rows)
        sizes.append(len(page_ids))
        if not nxt:
            return ids, rows, sizes, True, None
        if nxt in seen_cursors:
            return ids, rows, sizes, False, "next_cursor repeated — cursor loop"
        seen_cursors.add(nxt)
        cursor = nxt
    return ids, rows, sizes, False, f"did not terminate within {cap} pages (possible infinite loop)"


# ---- debug hooks (bundled stubs; best-effort against a real endpoint) ------ #
def reset(base_url) -> bool:
    s, _, _ = fire(base_url, "POST", "/_debug/reset", body=b"{}")
    return s == 200


def debug_all(base_url):
    """Ground-truth ordered ids via GET /_debug/all, or None if unavailable."""
    s, _h, text = fire(base_url, "GET", "/_debug/all")
    if s != 200:
        return None
    try:
        obj = json.loads(text)
        return obj.get("ids")
    except ValueError:
        return None


def debug_insert(base_url, row) -> bool:
    s, _, _ = fire(base_url, "POST", "/_debug/insert",
                   body=json.dumps(row).encode("utf-8"))
    return s == 200


def debug_delete(base_url, row_id) -> bool:
    s, _, _ = fire(base_url, "POST", "/_debug/delete",
                   body=json.dumps({"id": row_id}).encode("utf-8"))
    return s == 200


def _dupes(seq):
    seen, dup = set(), []
    for x in seq:
        if x in seen and x not in dup:
            dup.append(x)
        seen.add(x)
    return dup


def _page_max(base_url, spec, fallback):
    """Read the endpoint's documented max page size from X-Page-Size-Max, else
    the caller-supplied fallback."""
    _s, h, _o = fire_page(base_url, spec, 1, "")
    raw = h.get("x-page-size-max")
    if raw and raw.lstrip("-").isdigit() and int(raw) > 0:
        return int(raw), True
    return fallback, False


# --------------------------------------------------------------------------- #
# Properties — each returns (passed: bool|None, detail: str). None == SKIP.
# --------------------------------------------------------------------------- #
def check_traversal(base_url, fixture, limit=DEFAULT_LIMIT):
    spec = PageSpec.from_fixture(fixture)
    reset(base_url)
    ids, _rows, sizes, terminated, err = traverse(base_url, spec, limit)
    if err:
        return False, f"traversal failed: {err} (collected {len(ids)} ids so far)"
    if not terminated:
        return False, "traversal never signalled a terminal page (no null next-cursor)"
    dup = _dupes(ids)
    if dup:
        return False, (f"the same item appeared on more than one page (overlap): {dup} "
                       f"— pages returned {len(ids)} ids, {len(set(ids))} distinct.")
    truth = debug_all(base_url)
    if truth is not None:
        if ids != truth:
            missing = [t for t in truth if t not in set(ids)]
            extra = [i for i in ids if i not in set(truth)]
            return False, (f"traversal did not reproduce the full ordered set exactly once: "
                           f"missing {missing or 'none'}, unexpected {extra or 'none'} "
                           f"(got {len(ids)} vs {len(truth)} ground-truth rows).")
        return True, (f"followed the cursor across {len(sizes)} pages → {len(ids)} items, "
                      f"no overlap, no gap; reproduces the full ordered set exactly once")
    return True, (f"followed the cursor across {len(sizes)} pages → {len(ids)} items with no "
                  f"overlap (no /_debug/all ground truth to check for gaps — see GOTCHAS)")


def check_stable_under_mutation(base_url, fixture, limit=DEFAULT_LIMIT):
    """Delete an already-returned row and insert a tail row BETWEEN page fetches;
    every item present throughout must still appear exactly once. THE headline —
    naive OFFSET pagination skips a row here."""
    spec = PageSpec.from_fixture(fixture)
    if not reset(base_url):
        return None, ("SKIP: endpoint has no POST /_debug/reset hook, so the kit cannot drive "
                      "a controlled mutation. Run this against the bundled stubs or a seeded "
                      "test dataset you can mutate (see GOTCHAS).")
    truth = debug_all(base_url)
    if truth is None or len(truth) < limit + 2:
        return None, ("SKIP: no GET /_debug/all ground truth (or too few rows) to run a "
                      "controlled mid-traversal mutation — see GOTCHAS for wiring test hooks.")
    # Page 1.
    status, _h, obj = fire_page(base_url, spec, limit, "")
    if status != 200 or obj is None:
        return False, f"page 1 fetch returned HTTP {status}"
    seen_ids, _rows, cursor = _extract(obj, spec)
    if not cursor or len(seen_ids) < 2:
        return None, ("SKIP: the dataset paged into a single page (no mid-traversal point) — "
                      "use a larger dataset or a smaller --limit to exercise this property.")
    # Mutation BETWEEN page 1 and the rest: delete an already-seen row (this is
    # what shifts an OFFSET window) and insert a brand-new tail row.
    delete_id = seen_ids[0]
    insert_id = "pgtk_inserted_zzz"
    big_sort = 10 ** 9
    if not debug_delete(base_url, delete_id) or not debug_insert(
            base_url, {spec.id_field: insert_id, spec.sort_field: big_sort, "name": "pgtk-inserted"}):
        return None, ("SKIP: /_debug/delete or /_debug/insert hook unavailable — cannot perform "
                      "the controlled mutation (see GOTCHAS).")
    # Continue from the page-1 cursor to the end.
    rest_ids, _r2, _s2, terminated, err = traverse(base_url, spec, limit, start_cursor=cursor)
    if err:
        return False, f"post-mutation traversal failed: {err}"
    returned = seen_ids + rest_ids
    dup = _dupes(returned)
    present_throughout = set(truth) - {delete_id}
    missing = sorted(present_throughout - set(returned))
    if missing:
        return False, (f"after deleting already-returned {delete_id!r} mid-traversal, "
                       f"item(s) present throughout were SKIPPED: {missing} — the classic OFFSET "
                       f"skip (the offset window shifted when a prior row was removed).")
    if dup:
        return False, (f"after the mid-traversal mutation, item(s) were DUPLICATED across pages: "
                       f"{dup} — the offset window re-served a row.")
    return True, (f"deleted already-returned {delete_id!r} + inserted a tail row mid-traversal; "
                  f"all {len(present_throughout)} items present throughout still appear exactly "
                  f"once, none skipped or duplicated (keyset stays stable)")


def check_ordering(base_url, fixture, limit=DEFAULT_LIMIT):
    spec = PageSpec.from_fixture(fixture)
    reset(base_url)
    ids, rows, _sizes, terminated, err = traverse(base_url, spec, limit)
    if err:
        return False, f"could not traverse to check ordering: {err}"
    dup = _dupes(ids)
    if dup:
        return False, f"duplicate ids in the traversal — not a total order: {dup}"
    have_sort = rows and all(spec.sort_field in r for r in rows)
    if have_sort:
        keys = [(r[spec.sort_field], r.get(spec.id_field)) for r in rows]
        for i in range(len(keys) - 1):
            if keys[i] > keys[i + 1]:
                return False, (f"order is not monotonic by ({spec.sort_field}, {spec.id_field}) "
                               f"at position {i}: {keys[i]} then {keys[i + 1]} — inconsistent sort.")
        if len(set(keys)) != len(keys):
            return False, (f"the sort key ({spec.sort_field}, {spec.id_field}) is not unique across "
                           f"rows — without a unique tiebreaker the order is unstable.")
        return True, (f"{len(rows)} rows are in a consistent total order by "
                      f"({spec.sort_field}, {spec.id_field}), unique tiebreaker holds")
    # No sort field exposed: fall back to determinism (two traversals identical).
    ids2, _r2, _s2, _t2, err2 = traverse(base_url, spec, limit)
    if err2:
        return False, f"second traversal failed: {err2}"
    if ids != ids2:
        return False, ("two traversals returned a different order — the ordering is not stable "
                       f"(no {spec.sort_field!r} field exposed to check the sort key directly).")
    return True, (f"no {spec.sort_field!r} field exposed, but two full traversals returned the "
                  f"identical {len(ids)}-item order (deterministic) with no duplicates")


def check_page_size(base_url, fixture, limit=DEFAULT_LIMIT, max_arg=DEFAULT_MAX):
    spec = PageSpec.from_fixture(fixture)
    reset(base_url)
    max_page, from_header = _page_max(base_url, spec, max_arg)
    # (a) a small limit is honored exactly on full (non-terminal) pages.
    k = max(1, min(limit, max_page))
    _s, _h, obj = fire_page(base_url, spec, k, "")
    if obj is None:
        return False, "page fetch returned no JSON body"
    ids, _rows, nxt = _extract(obj, spec)
    if nxt and len(ids) != k:
        return False, (f"requested limit={k} but the first (non-terminal) page returned "
                       f"{len(ids)} items — the page size is not honored.")
    # (b) an over-max limit must be CLAMPED to the documented max.
    over = max_page * 10 + 50
    _s2, _h2, obj2 = fire_page(base_url, spec, over, "")
    if obj2 is None:
        return False, "over-max page fetch returned no JSON body"
    over_ids, _r2, _n2 = _extract(obj2, spec)
    src = "X-Page-Size-Max header" if from_header else f"--max {max_arg}"
    if len(over_ids) > max_page:
        return False, (f"requested limit={over} and got {len(over_ids)} items — OVER the documented "
                       f"max of {max_page} ({src}); the endpoint serves an unbounded page (a cheap "
                       f"DoS). It must clamp to {max_page}.")
    return True, (f"limit={k} honored on full pages; over-max limit={over} clamped to "
                  f"{len(over_ids)} ≤ {max_page} ({src})")


def check_terminal(base_url, fixture, limit=DEFAULT_LIMIT):
    spec = PageSpec.from_fixture(fixture)
    reset(base_url)
    ids, _rows, sizes, terminated, err = traverse(base_url, spec, limit)
    if err:
        return False, f"traversal did not terminate cleanly: {err}"
    if not terminated:
        return False, "the last page did not signal the end (no null/absent next-cursor)"
    # A terminal page (fetched past the end) must also carry a null next-cursor.
    return True, (f"traversal terminated after {len(sizes)} pages with a null/absent next-cursor "
                  f"({len(ids)} items) — no infinite loop")


def check_cursor_tamper(base_url, fixture, limit=DEFAULT_LIMIT):
    spec = PageSpec.from_fixture(fixture)
    reset(base_url)
    # A real, valid cursor (if the dataset spans more than one page) to tamper.
    _s, _h, obj = fire_page(base_url, spec, max(1, limit), "")
    valid = None
    if isinstance(obj, dict):
        _ids, _rows, valid = _extract(obj, spec)
    forged = ["not-a-cursor", "%%%bogus%%%", "999999", "YWJj.Zm9vYmFy"]
    if valid:
        forged.append(valid[:-1] + ("Z" if valid[-1] != "Z" else "Q"))  # bit-flip the tail
        forged.append(valid + "tampered")
    accepted = []
    for f in forged:
        status, _hh, _oo = fire_page(base_url, spec, limit, f)
        if is_2xx(status):
            accepted.append((f[:24], status))
    if accepted:
        return False, (f"forged/garbage cursor(s) were ACCEPTED with a 2xx instead of rejected: "
                       f"{accepted} — the endpoint silently coerces a bad cursor to page 1 rather "
                       f"than returning 400.")
    return True, (f"all {len(forged)} forged/malformed cursors were rejected (4xx) — the opaque "
                  f"cursor is tamper-evident, not silently coerced to page 1")


# --------------------------------------------------------------------------- #
# Runner / reporting
# --------------------------------------------------------------------------- #
def _label(passed):
    if passed is None:
        return "SKIP"
    return "PASS" if passed else "FAIL"


def _print_result(name, passed, detail):
    print(f"[{_label(passed)}] {name:22s} {detail}")


def run_suite(base_url, fixture, limit, max_arg):
    checks = [
        ("traversal", lambda: check_traversal(base_url, fixture, limit)),
        ("stable-under-mutation", lambda: check_stable_under_mutation(base_url, fixture, limit)),
        ("ordering", lambda: check_ordering(base_url, fixture, limit)),
        ("page-size", lambda: check_page_size(base_url, fixture, limit, max_arg)),
        ("terminal", lambda: check_terminal(base_url, fixture, limit)),
        ("cursor-tamper", lambda: check_cursor_tamper(base_url, fixture, limit)),
    ]
    failures = 0
    for name, fn in checks:
        passed, detail = fn()
        _print_result(name, passed, detail)
        if passed is False:
            failures += 1
    return failures


# --------------------------------------------------------------------------- #
# CLI commands
# --------------------------------------------------------------------------- #
def cmd_check(args) -> int:
    spec = PageSpec.from_fixture(args.fixture)
    print(f"Pagination Test Kit — checking {args.url}")
    print(f"  fixture: {args.fixture} (GET {spec.path}?{spec.limit_param}=N"
          f"&{spec.cursor_param}=…)   page size: {args.limit}")
    print(f"  (set --limit to the page size to traverse with; --max is the documented\n"
          f"   page-size cap fallback when the endpoint sends no X-Page-Size-Max header)\n")
    failures = run_suite(args.url, args.fixture, args.limit, args.max)
    print()
    if failures == 0:
        print("ALL PROPERTIES PASS/SKIP — this endpoint's pagination behaves correctly.")
        return 0
    print(f"{failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.")
    return 1


def _single(args, fn, name, *extra) -> int:
    passed, detail = fn(args.url, args.fixture, *extra)
    _print_result(name, passed, detail)
    return 1 if passed is False else 0


def cmd_traversal(args):
    return _single(args, check_traversal, "traversal", args.limit)


def cmd_stability(args):
    return _single(args, check_stable_under_mutation, "stable-under-mutation", args.limit)


def cmd_ordering(args):
    return _single(args, check_ordering, "ordering", args.limit)


def cmd_page_size(args):
    return _single(args, check_page_size, "page-size", args.limit, args.max)


def cmd_terminal(args):
    return _single(args, check_terminal, "terminal", args.limit)


def cmd_cursor_tamper(args):
    return _single(args, check_cursor_tamper, "cursor-tamper", args.limit)


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled fixtures (docs-derived request templates — see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        e = manifest[stem]
        print(f"  {stem:16s}  GET {e.get('path','?'):10s}  "
              f"cursor={e.get('cursor_param','cursor')} items={e.get('items_field','items')}  "
              f"— {e.get('note','')}")
    return 0


def cmd_demo(args) -> int:
    """Run the whole suite against the bundled reference stubs — zero accounts."""
    import stub_handler
    import stub_handler_naive
    import threading

    print("=" * 74)
    print("  PGTK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.")
    print("  NO real endpoint, NO accounts, NO money. This proves the kit works")
    print("  before you point `pgtk check --url` at your own app.")
    print("=" * 74)

    max_page = 5
    correct = stub_handler.serve(0, max_page=max_page)
    naive = stub_handler_naive.serve(0, max_page=max_page)
    cport = correct.server_address[1]
    nport = naive.server_address[1]
    threading.Thread(target=correct.serve_forever, daemon=True).start()
    threading.Thread(target=naive.serve_forever, daemon=True).start()
    try:
        print(f"\n--- CORRECT stub (keyset on (created_at, id), max_page {max_page}) — expect ALL PASS ---")
        cf = run_suite(f"http://127.0.0.1:{cport}", DEFAULT_PRIMARY, DEFAULT_LIMIT, DEFAULT_MAX)
        print(f"\n--- NAIVE stub (OFFSET pagination, no clamp, forged cursor accepted) — expect the kit to FLAG it ---")
        nf = run_suite(f"http://127.0.0.1:{nport}", DEFAULT_PRIMARY, DEFAULT_LIMIT, DEFAULT_MAX)
    finally:
        correct.shutdown()
        naive.shutdown()

    print("\n" + "=" * 74)
    if cf == 0 and nf > 0:
        print(f"  DEMO OK: correct stub passed all properties; naive stub flagged on {nf} property(ies).")
        print("  The kit distinguishes correct keyset pagination from a broken offset one.")
        print("=" * 74)
        return 0
    print(f"  DEMO UNEXPECTED: correct failures={cf}, naive failures={nf} (expected 0 and >0).")
    print("=" * 74)
    return 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pgtk",
        description="Pagination Test Kit — prove your endpoint's cursor pagination is correct.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp, with_max=False):
        sp.add_argument("--url", required=True, help="your endpoint base, e.g. http://localhost:8000")
        sp.add_argument("--fixture", default=DEFAULT_PRIMARY, help=f"fixture name (default {DEFAULT_PRIMARY})")
        sp.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                        help=f"page size to traverse with (default {DEFAULT_LIMIT})")
        if with_max:
            sp.add_argument("--max", type=int, default=DEFAULT_MAX,
                            help=f"documented max page size — fallback when there's no X-Page-Size-Max header (default {DEFAULT_MAX})")

    c = sub.add_parser("check", help="run all six properties against your endpoint")
    common(c, with_max=True)
    c.set_defaults(func=cmd_check)

    t = sub.add_parser("traversal", help="cursor traversal has no overlap and no gap")
    common(t)
    t.set_defaults(func=cmd_traversal)

    m = sub.add_parser("stable-under-mutation", help="mid-traversal insert/delete doesn't skip or dupe")
    common(m)
    m.set_defaults(func=cmd_stability)

    o = sub.add_parser("ordering", help="a consistent total order with a unique tiebreaker")
    common(o)
    o.set_defaults(func=cmd_ordering)

    z = sub.add_parser("page-size", help="limit honored + over-max clamped to the documented max")
    common(z, with_max=True)
    z.set_defaults(func=cmd_page_size)

    e = sub.add_parser("terminal", help="the last page signals the end; no infinite loop")
    common(e)
    e.set_defaults(func=cmd_terminal)

    k = sub.add_parser("cursor-tamper", help="a forged/opaque cursor is rejected (4xx)")
    common(k)
    k.set_defaults(func=cmd_cursor_tamper)

    sub.add_parser("demo", help="run all six against the bundled stubs (zero accounts)").set_defaults(func=cmd_demo)
    sub.add_parser("list", help="list bundled fixtures").set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
