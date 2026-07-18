# Marketplace listing copy — CORS Preflight Test Kit v0.1

> **Status:** `reference`

**Title:** CORS Preflight Test Kit — prove your CORS is neither broken nor wide open

**Short description (≤200 chars):** Point it at your endpoint and prove your CORS:
preflight ok, Allow-Origin + Vary, Allow-Methods/Headers cover the request,
credentials never with `*`, and no arbitrary-origin reflection. Stdlib only. No
account.

**Price:** $29 (one-time)

## Description

CORS is easy to get wrong in two opposite, equally bad directions. Get it too tight
and every browser request dies with *"No 'Access-Control-Allow-Origin' header is
present"* — or the preflight 404s because your framework doesn't answer `OPTIONS`,
or you set `Access-Control-Allow-Origin` but forgot `Access-Control-Allow-Methods` /
`-Allow-Headers`, so the JSON POST with an `Authorization` header is blocked. Get it
too loose and your server reflects **any** `Origin` back with
`Access-Control-Allow-Credentials: true` — now any website on the internet can make
a credentialed request from a victim's browser and read the authenticated response.
None of this shows up in `curl` or in a same-origin unit test, because neither ever
sends a cross-origin `Origin` header.

The CORS Preflight Test Kit points at your own API endpoint, fires the exact
cross-origin preflight (`OPTIONS`) and actual request a browser would, and proves
the six properties a correct CORS configuration must satisfy — runnable in
milliseconds, no vendor account, no live API, no headless browser, stdlib only. It
is **not** a webhook-signature kit, the Idempotency Key Test Kit, the Rate-Limit
Test Kit, the Pagination Test Kit, or the JWT Auth Test Kit; it tests a distinct
problem class: the browser cross-origin (CORS) contract. The behaviour it checks
follows the WHATWG Fetch Standard "CORS protocol" and MDN's CORS documentation.

- **Preflight returns ok.** The cross-origin `OPTIONS` preflight returns 200 or 204
  — not the 404/405 many frameworks send until CORS is wired.
- **Allow-Origin + Vary.** Both the preflight and the actual response echo your
  origin (or `*`), and when they echo the specific origin they send `Vary: Origin`
  so a shared cache never leaks one origin's grant to another.
- **Allow-Methods & Allow-Headers cover the request.** The preflight advertises the
  method and every header the browser asked for — including `Authorization`, which a
  literal `*` does **not** cover (a real, little-known Fetch-spec gotcha).
- **Credentials done right.** `Access-Control-Allow-Credentials: true` is never
  paired with `Access-Control-Allow-Origin: *` — browsers reject that combination.
- **No open reflection.** A disallowed probe origin is **not** reflected back — the
  server validates `Origin` against an allowlist instead of echoing anything.

## What makes it a *test* kit, not a blog post

It ships **two reference endpoints**: a correct allowlist-based one and a
deliberately naive one (reflects any origin, no `Vary`, no `Allow-Methods` /
`-Allow-Headers` on the preflight). Run `cptk demo` and watch the harness pass all
six against the correct config and *flag* the naive one on `allow-origin` (missing
`Vary`), `allow-methods`, `allow-headers`, and `reflect-guard`. That correct/broken
pair is the proof the checks actually distinguish a good CORS config from a broken
one — and the kit is honest that two of the six properties (`preflight-status`,
`credentials`) don't distinguish the two, so it never overclaims.

Runs in Python or Node, entirely from the standard library. No `pip install`, no
`npm install`, no account required to run any of it.

## What's inside

- The harness in two languages: `cptk.py` (Python) and `cptk.js` (Node), same
  commands (`check`, `preflight-status`, `allow-origin`, `allow-methods`,
  `allow-headers`, `credentials`, `reflect-guard`, `demo`, `list`).
- A **correct** reference endpoint (`stub_handler.py`) you can read — an
  allowlist-based CORS handler that answers the preflight with `204` + echoed
  `Access-Control-Allow-Origin` + `Vary: Origin` + `-Allow-Methods` +
  `-Allow-Headers` + `-Allow-Credentials`, and returns no CORS headers for an origin
  off its allowlist.
- A **naive** endpoint (`stub_handler_naive.py`) with the classic bugs, shipped so
  the suite can prove the harness catches them.
- Two docs-derived request templates + `PROVENANCE.md` documenting every property's
  source (the WHATWG Fetch Standard CORS protocol + MDN CORS), with a pinned sha256
  per fixture.
- An HTTP-layer real-path test suite (`test_http_realpath.py`, 37 tests) — every
  request fired over real HTTP against a reference endpoint, no timed waits.
- A one-page `GOTCHAS.md` checklist and a `QUICKSTART.md`.

## Requirements

- Python 3.8+ or Node 14+.
- No account, no dependencies, no build step, no browser.
- No secret values live in the kit; `.env.example` names optional config only.

## What it does NOT do (so you know what you're buying)

- It does **not** verify webhook signatures / HMAC (the Webhook Test Kits), test
  idempotency / safe-retry (the Idempotency Key Test Kit), throttling (the Rate-Limit
  Test Kit), result-set integrity (the Pagination Test Kit), or token security (the
  JWT Auth Test Kit). This is a distinct problem class: the browser CORS contract.
- It does **not** drive a real browser. It fires the exact cross-origin preflight and
  request a browser would and checks the response headers against the rules a browser
  enforces — at the HTTP layer, with no headless-browser dependency.
- It does **not** cover Private Network Access
  (`Access-Control-Allow-Private-Network`) — a separate, newer mechanism left out of
  scope. It asserts the core CORS protocol every browser has enforced for years.
- It tests CORS for the **origin you name** plus one disallowed probe — not your
  entire allowlist or per-route policy matrix. Run it once per origin/route you care
  about.
- The `credentials` property only asserts something when your endpoint sets
  `Access-Control-Allow-Credentials: true`; a non-credentialed public API using
  `Access-Control-Allow-Origin: *` passes `credentials` and `reflect-guard` with a
  note. Two properties (`preflight-status`, `credentials`) honestly do not
  distinguish the correct config from the naive one — the kit says so.
- The fixtures are **docs-derived** request templates (cited in `PROVENANCE.md`),
  not captures from a live API. The `demo` runs entirely in-process — no account, no
  network beyond localhost, no money.

## FAQ

**Doesn't my framework's CORS middleware already handle this?**
Often — if it's configured correctly. The bugs are in the configuration: a
forgotten `OPTIONS` route, a missing `Vary: Origin`, an `Allow-Headers` list that
doesn't include `Authorization` (or uses `*`, which excludes it), a `*` origin
paired with credentials, or an "echo the origin" shortcut with no allowlist (open
CORS). This kit fires exactly those cases at *your* endpoint and tells you which one
you're hitting.

**Why not just read the Fetch standard / MDN?**
You should — and the correct behaviour is a few dozen lines once you know the
contract. What you're paying for is the harness that proves *your* endpoint honours
it (including the two footguns almost everyone hits), plus the correct/naive
reference pair that demonstrates the checks catch a broken config. The free
substitute is real; the kit is the done, runnable version.

**Refunds / support / license:** [owner-to-set — storefront defaults; suggested:
14-day no-questions refund, single-developer license, email support best-effort.]

---

## PROVENANCE-FOOTER

Every claim above is checkable against the committed source (blob `file@sha` at
build time, branch `claude/cors-preflight-test-kit`):

- `candidates/cors-preflight-test-kit/cptk.py@865a59dc405e0fd7ecbfbcc721a01c971f06777d`
  — the harness (six properties, demo, list).
- `candidates/cors-preflight-test-kit/cptk.js@aaa251eab8e2defe11cd15baa0318c69f1d4010c`
  — the Node parity port (same six properties + demo).
- `candidates/cors-preflight-test-kit/stub_handler_naive.py@ac087d3bad8c2b410b05ae23b586e5c40d15d0ae`
  — the deliberately broken reference endpoint (reflects any origin, no Vary, no
  Allow-Methods/Headers — the value proof).
- `candidates/cors-preflight-test-kit/test_http_realpath.py@c7097ea9078e6a363210089cf4f440c3a61716bf`
  — the 37-test HTTP real-path suite (correct all-pass; naive flagged on 4
  properties; preflight-status + credentials honestly non-distinguishing).
- `candidates/cors-preflight-test-kit/GOTCHAS.md@3551bf8185b7a57d94c4ad3f7524ed3342c4d177`
  — the seven failure modes, each mapped to a kit command.
- `candidates/cors-preflight-test-kit/fixtures/PROVENANCE.md@955b2a62467444ff55294a8bf133805fbee91b7a`
  — the honest source statement (Fetch standard + MDN) + per-fixture sha256.
- `candidates/cors-preflight-test-kit/dist/cors-preflight-test-kit-v0.1.zip@67807c9871ba7305d1d1f43aeb1bc63e79c99b60`
  — the buyer bundle (sha256
  `5c754e4432385d8c3b3f892a5ff572ddcf0e13cb0e07ee0dad522705be0b6c29`, 35,779 bytes,
  13 content files; byte-reproducible via `package.sh`).
