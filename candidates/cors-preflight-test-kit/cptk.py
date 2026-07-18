#!/usr/bin/env python3
"""CORS Preflight Test Kit (cptk) — point it at your own API endpoint and prove
your server-side CORS configuration behaves correctly: the cross-origin OPTIONS
preflight returns an ok status, Access-Control-Allow-Origin matches the request
Origin (with Vary: Origin when it echoes a specific origin), the preflight
advertises the method and headers the browser asked for, credentials are never
paired with a wildcard origin, and the server does NOT reflect an arbitrary
Origin back (the open-CORS security hole).

Stdlib only. No pip install, no build step. Python 3.8+. No account, no vendor.

This is NOT a webhook signature kit, NOT the idempotency kit, NOT the rate-limit
kit, NOT the pagination kit, and NOT the JWT auth kit — it tests a DIFFERENT
problem class: the BROWSER CROSS-ORIGIN (CORS) contract your server emits. The
behaviour it checks follows the WHATWG Fetch Standard "CORS protocol" and MDN's
CORS documentation. See fixtures/PROVENANCE.md — every property is cited.

Properties checked (each PASS/FAIL against YOUR endpoint):

  1. preflight-status  The cross-origin OPTIONS preflight returns an ok status
                       (200 or 204). A 404/405/500 preflight means the browser
                       never sends the real request.
  2. allow-origin      Both the preflight AND the actual response carry an
                       Access-Control-Allow-Origin matching the request Origin
                       (or `*`). When it echoes the SPECIFIC origin (not `*`),
                       Vary: Origin must be present, or a shared cache can serve
                       one origin's response to another.
  3. allow-methods     The preflight's Access-Control-Allow-Methods covers the
                       method the client asked for (Access-Control-Request-Method).
  4. allow-headers     The preflight's Access-Control-Allow-Headers covers every
                       header the client asked for (Access-Control-Request-Headers),
                       case-insensitively. Flags the Fetch-spec gotcha that a
                       literal `*` does NOT cover Authorization.
  5. credentials       If Access-Control-Allow-Credentials: true is present, the
                       Allow-Origin must be a SPECIFIC origin (not `*`) and the
                       Allow-Methods/Allow-Headers must not be the literal `*` —
                       browsers reject `*` + credentials.
  6. reflect-guard     A disallowed probe origin must NOT be reflected into
                       Access-Control-Allow-Origin (blindly echoing any Origin is
                       an open-CORS hole: any website can read authenticated
                       responses), and `*` + credentials is flagged.

`cptk demo` runs all six against the bundled reference stubs — the CORRECT one
(all pass) and the deliberately NAIVE one (flagged) — with ZERO accounts and a
loud banner, so you can see the checks working before you point them at your app.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
DEFAULT_PRIMARY = "api_json_post"
# A probe origin the reflect-guard check sends: it must not be on any real
# allowlist, so a server that echoes it back is reflecting arbitrarily.
DEFAULT_BAD_ORIGIN = "https://cptk-probe.invalid"


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
            f"run `cptk list` to see bundled fixtures."
        )
    return manifest[stem]


def load_fixture(stem: str) -> bytes:
    stem = stem[:-5] if stem.endswith(".json") else stem
    p = FIXTURES_DIR / (stem + ".json")
    if not p.exists():
        raise SystemExit(f"error: fixture not found: {stem}. Run `cptk list`.")
    return p.read_bytes()


def method_for(stem: str) -> str:
    return _entry_for(stem).get("method", "GET").upper()


def path_for(stem: str) -> str:
    return _entry_for(stem)["path"]


def content_type_for(stem: str) -> str:
    return _entry_for(stem).get("content_type", "application/json")


def request_headers_for(stem: str) -> str:
    """The Access-Control-Request-Headers value a browser would send in the
    preflight for this request (the non-simple request headers)."""
    return _entry_for(stem).get("request_headers", "")


def list_fixtures():
    return sorted(load_manifest().keys())


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def fire(base_url, method, path, headers=None, body=None,
         content_type="application/json", timeout=10.0):
    """Fire one request with an explicit header dict. Returns (status,
    headers_lower, body_text). A dropped connection yields status 0 so a
    crashing endpoint is a FAIL, not an exception. `headers_lower` is a
    case-insensitive dict of RESPONSE headers."""
    url = base_url.rstrip("/") + path
    data = body if (method in ("POST", "PUT", "PATCH") and body) else None
    req = urllib.request.Request(url, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", content_type)
    for k, v in (headers or {}).items():
        if v is not None:
            req.add_header(k, v)
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


def is_2xx(s: int) -> bool:
    return 200 <= s < 300


def preflight(base_url, path, origin, req_method, req_headers):
    """Fire the CORS preflight: an OPTIONS with Origin +
    Access-Control-Request-Method (+ -Request-Headers when non-empty)."""
    h = {"Origin": origin, "Access-Control-Request-Method": req_method}
    if req_headers:
        h["Access-Control-Request-Headers"] = req_headers
    return fire(base_url, "OPTIONS", path, headers=h)


def actual(base_url, method, path, origin, body=None, content_type="application/json"):
    """Fire the real (non-OPTIONS) request carrying the Origin header."""
    return fire(base_url, method, path, headers={"Origin": origin},
                body=body, content_type=content_type)


def _fixture_call(fixture):
    return (method_for(fixture), path_for(fixture), load_fixture(fixture),
            content_type_for(fixture), request_headers_for(fixture))


def _split_list(value):
    """Split a comma-separated CORS header value into a stripped list."""
    if value is None:
        return []
    return [p.strip() for p in value.split(",") if p.strip()]


def _vary_has_origin(headers) -> bool:
    return any(v.lower() == "origin" for v in _split_list(headers.get("vary")))


# --------------------------------------------------------------------------- #
# Properties — each returns (passed: bool, detail: str)
# --------------------------------------------------------------------------- #
def check_preflight_status(base_url, fixture, origin):
    """The cross-origin OPTIONS preflight must return an ok status (200/204)."""
    method, path, _body, _ct, req_headers = _fixture_call(fixture)
    status, _h, _b = preflight(base_url, path, origin, method, req_headers)
    if status in (200, 204):
        return True, f"the OPTIONS preflight returned {status} (ok — the browser will proceed to the real request)"
    if status == 0:
        return False, "the OPTIONS preflight got no HTTP response (endpoint down or refused the connection)"
    return False, (f"the OPTIONS preflight returned {status} (needs 200 or 204) — a browser treats a non-ok "
                   f"preflight as a failure and never sends the real request; many frameworks 404/405 OPTIONS "
                   f"by default until CORS is wired.")


def _acao_ok(headers, origin, phase):
    """Assert Access-Control-Allow-Origin on ONE response. Returns (ok, detail)."""
    acao = headers.get("access-control-allow-origin")
    if acao is None:
        return False, (f"the {phase} carried NO Access-Control-Allow-Origin — the browser blocks the "
                       f"cross-origin request (this is the #1 CORS error).")
    acao = acao.strip()
    if acao == "*":
        return True, f"the {phase} allows `*` (any origin)"
    if acao == origin:
        if not _vary_has_origin(headers):
            return False, (f"the {phase} echoes the specific origin ({origin}) but is missing `Vary: Origin` — "
                           f"a shared cache can serve this origin's Allow-Origin to a DIFFERENT origin, breaking "
                           f"CORS for everyone behind the cache.")
        return True, f"the {phase} echoes {origin} with Vary: Origin"
    return False, (f"the {phase} Access-Control-Allow-Origin is {acao!r}, which is neither the request origin "
                   f"({origin}) nor `*` — the browser blocks the request.")


def check_allow_origin(base_url, fixture, origin):
    """Both the preflight and the actual response must allow the request Origin,
    and echo Vary: Origin when they name the specific origin."""
    method, path, body, ct, req_headers = _fixture_call(fixture)
    ps, ph, _pb = preflight(base_url, path, origin, method, req_headers)
    if ps not in (200, 204):
        return False, (f"cannot check Allow-Origin: the OPTIONS preflight returned {ps} (see preflight-status).")
    ok, detail = _acao_ok(ph, origin, "preflight")
    if not ok:
        return False, detail
    _as, ah, _ab = actual(base_url, method, path, origin, body, ct)
    ok2, detail2 = _acao_ok(ah, origin, "actual response")
    if not ok2:
        return False, detail2
    return True, f"Access-Control-Allow-Origin correct on preflight AND actual response ({detail}; {detail2})"


def check_allow_methods(base_url, fixture, origin):
    """The preflight's Access-Control-Allow-Methods must cover the requested method."""
    method, path, _body, _ct, req_headers = _fixture_call(fixture)
    ps, ph, _pb = preflight(base_url, path, origin, method, req_headers)
    if ps not in (200, 204):
        return False, f"cannot check Allow-Methods: the OPTIONS preflight returned {ps} (see preflight-status)."
    acam = ph.get("access-control-allow-methods")
    if acam is None:
        return False, (f"the preflight carried NO Access-Control-Allow-Methods — the browser blocks the "
                       f"{method} request (a common 'I set Allow-Origin and thought that was enough' bug).")
    allowed = {m.upper() for m in _split_list(acam)}
    if "*" in allowed:
        return True, f"the preflight allows `*` methods (note: `*` is invalid with credentials — see the credentials check)"
    if method.upper() in allowed:
        return True, f"the preflight's Access-Control-Allow-Methods ({acam}) covers {method}"
    return False, (f"the preflight's Access-Control-Allow-Methods ({acam}) does NOT include {method} — "
                   f"the browser blocks the request.")


def check_allow_headers(base_url, fixture, origin):
    """The preflight's Access-Control-Allow-Headers must cover every requested header."""
    method, path, _body, _ct, req_headers = _fixture_call(fixture)
    requested = [h.lower() for h in _split_list(req_headers)]
    if not requested:
        return True, "this request sends no non-simple headers, so the browser asks for none — nothing to check"
    ps, ph, _pb = preflight(base_url, path, origin, method, req_headers)
    if ps not in (200, 204):
        return False, f"cannot check Allow-Headers: the OPTIONS preflight returned {ps} (see preflight-status)."
    acah = ph.get("access-control-allow-headers")
    if acah is None:
        return False, (f"the preflight carried NO Access-Control-Allow-Headers, but the request asks for "
                       f"{', '.join(requested)} — the browser blocks it (the classic 'works in curl, fails in "
                       f"the browser' bug when a custom header like Authorization or Content-Type isn't allowed).")
    allowed = [h.lower() for h in _split_list(acah)]
    allowed_set = set(allowed)
    # Fetch-spec gotcha: a literal `*` does NOT cover Authorization.
    if "*" in allowed_set:
        if "authorization" in requested:
            return False, ("Access-Control-Allow-Headers is `*`, but the request asks for Authorization — per the "
                           "Fetch standard the `*` wildcard does NOT cover Authorization; it must be named "
                           "explicitly. The browser blocks this request.")
        return True, "the preflight allows `*` headers (covers the requested headers; note: `*` excludes Authorization)"
    missing = [h for h in requested if h not in allowed_set]
    if missing:
        return False, (f"the preflight's Access-Control-Allow-Headers ({acah}) is missing {', '.join(missing)} — "
                       f"the browser blocks the request.")
    return True, f"the preflight's Access-Control-Allow-Headers covers every requested header ({', '.join(requested)})"


def check_credentials(base_url, fixture, origin):
    """If Access-Control-Allow-Credentials: true is set, Allow-Origin must be a
    specific origin (not `*`) and Allow-Methods/Headers must not be the literal `*`."""
    method, path, body, ct, req_headers = _fixture_call(fixture)
    ps, ph, _pb = preflight(base_url, path, origin, method, req_headers)
    _as, ah, _ab = actual(base_url, method, path, origin, body, ct)
    saw_creds = False
    for phase, headers in (("preflight", ph), ("actual response", ah)):
        acac = headers.get("access-control-allow-credentials")
        if acac is None or acac.strip().lower() != "true":
            continue
        saw_creds = True
        acao = (headers.get("access-control-allow-origin") or "").strip()
        if acao == "*":
            return False, (f"the {phase} sets Access-Control-Allow-Credentials: true together with "
                           f"Access-Control-Allow-Origin: * — browsers REJECT this combination; echo the specific "
                           f"origin instead.")
        if acao == "":
            return False, (f"the {phase} sets Access-Control-Allow-Credentials: true but no Allow-Origin — a "
                           f"credentialed request needs the specific origin echoed.")
        acam = (headers.get("access-control-allow-methods") or "").strip()
        acah = (headers.get("access-control-allow-headers") or "").strip()
        if acam == "*":
            return False, (f"the {phase} sets credentials: true with Access-Control-Allow-Methods: * — the `*` "
                           f"wildcard is invalid under credentials; list the methods explicitly.")
        if acah == "*":
            return False, (f"the {phase} sets credentials: true with Access-Control-Allow-Headers: * — the `*` "
                           f"wildcard is invalid under credentials; list the headers explicitly.")
    if not saw_creds:
        return True, ("endpoint does not enable credentialed CORS (no Access-Control-Allow-Credentials: true) — "
                      "nothing to check (credentials are optional).")
    return True, ("Access-Control-Allow-Credentials: true is correctly paired with a specific origin (not `*`) "
                  "and explicit methods/headers")


def check_reflect_guard(base_url, fixture, origin, bad_origin=DEFAULT_BAD_ORIGIN):
    """A disallowed probe origin must NOT be reflected into Allow-Origin."""
    method, path, body, ct, req_headers = _fixture_call(fixture)
    ps, ph, _pb = preflight(base_url, path, bad_origin, method, req_headers)
    _as, ah, _ab = actual(base_url, method, path, bad_origin, body, ct)
    for phase, headers in (("preflight", ph), ("actual response", ah)):
        acao = headers.get("access-control-allow-origin")
        if acao is None:
            continue
        acao = acao.strip()
        acac = (headers.get("access-control-allow-credentials") or "").strip().lower()
        if acao == bad_origin:
            return False, (f"the {phase} REFLECTS an arbitrary Origin ({bad_origin}) back into "
                           f"Access-Control-Allow-Origin — this is open CORS: any website can read your "
                           f"authenticated responses. Validate the Origin against an allowlist instead of "
                           f"echoing it.")
        if acao == "*" and acac == "true":
            return False, (f"the {phase} answers a disallowed origin with Access-Control-Allow-Origin: * AND "
                           f"credentials: true — an open, credentialed CORS hole (browsers reject `*`+credentials, "
                           f"but the intent is unsafe).")
    return True, (f"a disallowed probe origin ({bad_origin}) is NOT reflected — the server validates Origin "
                  f"against an allowlist rather than echoing it")


# --------------------------------------------------------------------------- #
# Runner / reporting
# --------------------------------------------------------------------------- #
def _print_result(name, passed, detail):
    print(f"[{'PASS' if passed else 'FAIL'}] {name:18s} {detail}")


def run_suite(base_url, fixture, origin, bad_origin=DEFAULT_BAD_ORIGIN):
    checks = [
        ("preflight-status", lambda: check_preflight_status(base_url, fixture, origin)),
        ("allow-origin", lambda: check_allow_origin(base_url, fixture, origin)),
        ("allow-methods", lambda: check_allow_methods(base_url, fixture, origin)),
        ("allow-headers", lambda: check_allow_headers(base_url, fixture, origin)),
        ("credentials", lambda: check_credentials(base_url, fixture, origin)),
        ("reflect-guard", lambda: check_reflect_guard(base_url, fixture, origin, bad_origin)),
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
    print(f"CORS Preflight Test Kit — checking {args.url}")
    print(f"  fixture: {args.fixture} ({method_for(args.fixture)} {path_for(args.fixture)})   "
          f"origin: {args.origin}")
    print(f"  (--origin is the browser origin your app is served from; --bad-origin is the disallowed "
          f"probe the reflect-guard check sends, default {DEFAULT_BAD_ORIGIN})\n")
    failures = run_suite(args.url, args.fixture, args.origin, args.bad_origin)
    print()
    if failures == 0:
        print("ALL PROPERTIES PASS — this endpoint's CORS configuration behaves correctly for this origin.")
        return 0
    print(f"{failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.")
    return 1


def _single(args, fn, name, *extra) -> int:
    passed, detail = fn(args.url, args.fixture, args.origin, *extra)
    _print_result(name, passed, detail)
    return 0 if passed else 1


def cmd_preflight_status(args):
    return _single(args, check_preflight_status, "preflight-status")


def cmd_allow_origin(args):
    return _single(args, check_allow_origin, "allow-origin")


def cmd_allow_methods(args):
    return _single(args, check_allow_methods, "allow-methods")


def cmd_allow_headers(args):
    return _single(args, check_allow_headers, "allow-headers")


def cmd_credentials(args):
    return _single(args, check_credentials, "credentials")


def cmd_reflect_guard(args):
    return _single(args, check_reflect_guard, "reflect-guard", args.bad_origin)


def cmd_list(args) -> int:
    manifest = load_manifest()
    if not manifest:
        print("(no fixtures found)")
        return 1
    print("bundled fixtures (docs-derived request templates — see fixtures/PROVENANCE.md):")
    for stem in sorted(manifest):
        e = manifest[stem]
        print(f"  {stem:14s}  {e.get('method','GET'):6s} {e.get('path','?'):12s}  "
              f"headers=[{e.get('request_headers','')}]  — {e.get('note','')}")
    return 0


def cmd_demo(args) -> int:
    """Run the whole suite against the bundled reference stubs — zero accounts."""
    import stub_handler
    import stub_handler_naive
    import threading

    allowed = "https://app.example.com"
    bad = "https://evil.example"
    print("=" * 72)
    print("  CPTK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.")
    print("  NO real endpoint, NO accounts, NO money. This proves the kit works")
    print("  before you point `cptk check --url` at your own app.")
    print(f"  allowed origin: {allowed}   disallowed probe: {bad}")
    print("=" * 72)

    correct = stub_handler.serve(0, allowed_origins=[allowed])
    naive = stub_handler_naive.serve(0)
    cport = correct.server_address[1]
    nport = naive.server_address[1]
    threading.Thread(target=correct.serve_forever, daemon=True).start()
    threading.Thread(target=naive.serve_forever, daemon=True).start()
    try:
        print(f"\n--- CORRECT stub (allowlist = {allowed}) — expect ALL PASS ---")
        cf = run_suite(f"http://127.0.0.1:{cport}", DEFAULT_PRIMARY, allowed, bad)
        print(f"\n--- NAIVE stub (reflects any origin, no Vary, no Allow-Methods/Headers) — expect the kit to FLAG it ---")
        nf = run_suite(f"http://127.0.0.1:{nport}", DEFAULT_PRIMARY, allowed, bad)
    finally:
        correct.shutdown()
        naive.shutdown()

    print("\n" + "=" * 72)
    if cf == 0 and nf > 0:
        print(f"  DEMO OK: correct stub passed all 6; naive stub flagged on {nf} property(ies).")
        print("  The kit distinguishes a correct CORS config from a broken one.")
        print("=" * 72)
        return 0
    print(f"  DEMO UNEXPECTED: correct failures={cf}, naive failures={nf} (expected 0 and >0).")
    print("=" * 72)
    return 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cptk",
        description="CORS Preflight Test Kit — prove your endpoint's CORS configuration is correct.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp, bad_origin=False):
        sp.add_argument("--url", required=True, help="your endpoint base, e.g. http://localhost:8000")
        sp.add_argument("--origin", required=True,
                        help="the browser origin your app is served from, e.g. https://app.example.com")
        sp.add_argument("--fixture", default=DEFAULT_PRIMARY, help=f"fixture name (default {DEFAULT_PRIMARY})")
        if bad_origin:
            sp.add_argument("--bad-origin", default=DEFAULT_BAD_ORIGIN, dest="bad_origin",
                            help=f"a disallowed probe origin for the reflect-guard check (default {DEFAULT_BAD_ORIGIN})")

    c = sub.add_parser("check", help="run all six properties against your endpoint")
    common(c, bad_origin=True)
    c.set_defaults(func=cmd_check)

    s = sub.add_parser("preflight-status", help="the OPTIONS preflight returns an ok status (200/204)")
    common(s)
    s.set_defaults(func=cmd_preflight_status)

    o = sub.add_parser("allow-origin", help="Allow-Origin matches the request Origin (+ Vary: Origin)")
    common(o)
    o.set_defaults(func=cmd_allow_origin)

    m = sub.add_parser("allow-methods", help="the preflight's Allow-Methods covers the requested method")
    common(m)
    m.set_defaults(func=cmd_allow_methods)

    h = sub.add_parser("allow-headers", help="the preflight's Allow-Headers covers the requested headers")
    common(h)
    h.set_defaults(func=cmd_allow_headers)

    cr = sub.add_parser("credentials", help="credentials: true is never paired with a `*` origin/methods/headers")
    common(cr)
    cr.set_defaults(func=cmd_credentials)

    r = sub.add_parser("reflect-guard", help="a disallowed origin is NOT reflected (no open CORS)")
    common(r, bad_origin=True)
    r.set_defaults(func=cmd_reflect_guard)

    sub.add_parser("demo", help="run all six against the bundled stubs (zero accounts)").set_defaults(func=cmd_demo)
    sub.add_parser("list", help="list bundled fixtures").set_defaults(func=cmd_list)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
