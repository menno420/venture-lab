# Session — CORS Preflight Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · feature build
- **started (date -u):** Sat Jul 18 21:09 UTC 2026
- **branch:** `claude/cors-preflight-test-kit`
- **base:** `main@4137691`
- **purpose:** build the **CORS Preflight Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — a NEW sellable in the API-robustness kit family, a genuinely
  DIFFERENT problem class from the four webhook signature kits, the idempotency kit,
  the rate-limit kit, the pagination kit, and the JWT auth kit. Where the webhook
  kits verify an inbound provider *signature*, the idempotency kit verifies a
  *safe-retry / exactly-once* contract, the rate-limit kit verifies a *throttling*
  contract, the pagination kit verifies *result-set integrity*, and the JWT kit
  verifies *verifier security*, this kit verifies a buyer's OWN endpoint's
  **browser CORS contract**: that a cross-origin `OPTIONS` preflight returns an ok
  status, that `Access-Control-Allow-Origin` matches the request `Origin` (with
  `Vary: Origin` when it echoes a specific origin), that `Access-Control-Allow-Methods`
  covers the requested method, that `Access-Control-Allow-Headers` covers every
  requested header (including the `Authorization`-is-not-covered-by-`*` Fetch-spec
  footgun), that `Access-Control-Allow-Credentials: true` is never paired with a
  `*` origin, and that the server does NOT reflect an arbitrary Origin (the
  open-CORS security hole). Stdlib-only (`http.server` + `urllib`), account-free,
  runs with a loud DEMO banner against bundled reference stubs. Ships: a CORRECT
  reference stub (pins an origin allowlist, echoes the origin + `Vary: Origin`,
  advertises methods/headers, sets credentials with a specific origin, refuses to
  reflect unknown origins), a deliberately NAIVE/broken stub (reflects any origin,
  omits `Vary`, omits `Access-Control-Allow-Methods`/`-Headers` on the preflight)
  so the suite can PROVE it catches the bugs, a `cptk.py` harness (+ `cptk.js` Node
  parity) that a buyer points at their own endpoint, an HTTP-layer real-path test
  suite (deterministic, no waiting), docs-derived request-template fixtures +
  PROVENANCE (cited to the WHATWG Fetch Standard CORS protocol + MDN CORS), a
  byte-reproducible buyer bundle, and a §7 owner-gate publish packet. The build ENDS
  at a queued owner ⚑ publish click (rail 13 / CONSTITUTION §13) — no publish, no
  spend, no accounts by the seat.
- **session:** Mirrors the proven rate-limit-/pagination-/jwt-auth-test-kit scaffold
  (the closest templates — same correct-stub + naive-stub value-proof pattern) but
  is a genuinely DIFFERENT product: browser CORS correctness, not signature
  verification, throttling, dedup, result-set integrity, or token forgery. The value
  proof is built in — the CORRECT stub passes all six properties and the NAIVE stub
  is FLAGGED on the missing-`Vary`, missing-methods, missing-headers, and
  arbitrary-origin-reflection bugs, so the kit demonstrably distinguishes a correct
  CORS config from a broken one, and is HONEST that two properties (preflight-status,
  credentials) do NOT distinguish the two stubs. Honest scope carried in PROVENANCE +
  the listing: this tests server-emitted CORS response headers at the HTTP layer
  (what a browser preflight/request would check) — it does NOT drive a real browser,
  and does NOT cover Private Network Access (`Access-Control-Allow-Private-Network`);
  fixtures are docs-derived request templates, not live captures. Born-red card holds
  the substrate-gate red until the deliberate completion flip.
- **local verify:** `python3 -m unittest test_http_realpath -v` → `Ran 37 tests ... OK`
  (green from source AND from the extracted zip in a clean dir); `node cptk.js demo`
  → correct config all-6-pass, naive config flagged on 4; `python3 bootstrap.py
  check --strict` → **EXIT 0** (advisories only — no hard finding; reachability
  clean after the CATALOG link).
- **bundle sha256:** `5c754e4432385d8c3b3f892a5ff572ddcf0e13cb0e07ee0dad522705be0b6c29`
  (35,779 bytes, 13 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild produced the identical sha).
- **final commits:** `c2d20e3` (claim + born-red card) → `a001329` (SKU payload:
  harness ×2 + stubs + 37-test suite + docs + bundle + CI job + CATALOG row) →
  `1b28a52` (status heartbeat) → this flip commit (born-red → complete). Note: the
  payload/heartbeat commits first landed on a sibling worker's branch after a
  shared-worktree branch switch and were cherry-picked back onto this branch; the
  sibling branch `claude/api-robustness-lead-magnet` still carries copies (flagged
  to the coordinator — no force-push).

## 💡 Session idea

💡 **CORS is the one API-robustness kit whose failure a browser can *demonstrate* —
so it's the family's natural free lead magnet: ship a tiny static HTML page (one
`fetch()` + a textarea for the user's endpoint URL and origin) that runs the same
six checks the CLI does, live, in the visitor's own browser, and prints the exact
PASS/FAIL lines.** Every other kit needs a terminal to show its value; CORS is the
only one where the pain (a real red `blocked by CORS policy` console error, or a
green "your API reflects any origin — here's the exploit") reproduces in a browser
tab with zero install. That page IS the distribution: it's the interactive demo the
dev.to gotcha article embeds, the thing that ranks for "test my cors" / "cors
checker", and the top-of-funnel that sells not just this $29 kit but the whole
API-robustness line by proving the catalog's checks are real. Two honest caveats to
respect if built: (a) a browser page can only run the checks the browser itself
permits (it can't set a forbidden `Origin` header — the browser sets that from the
page's own origin — so the hosted checker tests CORS *from the checker's origin*,
which is a genuine and useful signal but narrower than the CLI's arbitrary
`--origin`/`--bad-origin`; say so plainly, and keep the full CLI as the paid
product); (b) it must stay a pure client-side page (no proxy backend) or it stops
being "runs in your browser" and becomes a service to run. This is the same
"free-tool-as-lead-magnet → paid-kit" play the sibling worker's
`api-robustness-lead-magnet` claim gestures at — CORS is the single best kit to
anchor it on, because its check is the only one that survives being run from a
sandboxed browser tab.

## previous-session review

previous-session review: `.sessions/2026-07-18-jwt-auth-test-kit.md` (PR for the JWT
Auth Test Kit, the fifth API-robustness kit). Strong and the cleanest template to
mirror: its correct/naive stub pair is the load-bearing value proof and its card is
exemplary about naming what the kit does NOT rest on (the explicit no-RS256-signature-math
boundary). This CORS kit inherited that discipline — the honesty burden here was
scoping (server-emitted headers at the HTTP layer, NOT a real browser, NOT Private
Network Access), and the two-non-signal honesty (`preflight-status` + `credentials`
don't distinguish the stubs). One nit that recurs across all six sibling cards
(idempotency #233, rate-limit #236, pagination #237, jwt): every one flags the
`_api-hardening-core` extraction as overdue, and every one records the same
off-taxonomy `📊 Model:` payload the check advisories nag about (`claude-opus-4-8
family` / `high effort` / freeform task-class) — this card deliberately files the
taught form (`opus-4.8 · high · feature build`) so it lands clean in the PL-004
dataset instead of adding a seventh drift row.
