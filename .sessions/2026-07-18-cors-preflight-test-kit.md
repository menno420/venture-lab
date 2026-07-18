# Session — CORS Preflight Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill: family-level model · effort · task-class at flip]]
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
- **local verify:** [[fill: unittest pass line + test count + bootstrap check EXIT at flip]]
- **bundle sha256:** [[fill: dist zip sha256 + byte count at flip]]
- **final commits:** [[fill: commit list at flip]]

## 💡 Session idea

💡 [[fill: one genuine idea at flip]]

## previous-session review

previous-session review: [[fill: pointer + one-line remark on the prior session card at flip]]
