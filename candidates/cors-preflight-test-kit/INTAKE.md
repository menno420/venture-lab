# CORS Preflight Test Kit — intake (ORDER 016 build, 2026-07-18)

> A stdlib-only local test harness + docs-derived request templates that lets any
> developer verify their server-side CORS configuration behaves correctly — the
> cross-origin preflight returns an ok status, `Access-Control-Allow-Origin`
> matches the `Origin` (with `Vary: Origin` when echoed), the preflight advertises
> the requested method and headers, credentials are never paired with a `*`
> origin, and the server does NOT reflect an arbitrary origin — at the HTTP layer,
> in milliseconds, with no live API, no account, and no real browser.

## What it is

The webhook-/idempotency-/rate-limit-/pagination-/JWT-test-kit **packaging
pattern** (stdlib harness + docs-derived fixtures + a correct reference stub + a
deliberately naive stub + HTTP real-path suite + byte-reproducible bundle + §7
owner-gate packet, proven across the LIVE Stripe kit, the GitHub/Slack/Shopify
kits, and the Idempotency/Rate-Limit/Pagination/JWT kits) applied to a **new,
genuinely different problem class**: the **browser cross-origin (CORS) contract**,
NOT signature verification, NOT dedup/safe-retry, NOT throttling, NOT result-set
integrity, NOT token security. Where the webhook kits verify an *inbound* provider
signature, the idempotency kit a *stateful safe-retry* contract, the rate-limit
kit a *throttling* contract, the pagination kit *result-set integrity*, and the
JWT kit *verifier security*, this kit verifies a buyer's OWN endpoint's *browser
CORS* contract. Ships as: a CORRECT reference endpoint (allowlist-based CORS
handler: 204 preflight, echoed `Access-Control-Allow-Origin` + `Vary: Origin` +
`-Allow-Methods` + `-Allow-Headers` + `-Allow-Credentials`, and no CORS headers for
an off-allowlist origin), a deliberately NAIVE endpoint (reflects any origin, no
`Vary`, no `Allow-Methods`/`Allow-Headers` on the preflight) so the suite can PROVE
the harness catches the bugs, a language-agnostic harness (Python `cptk.py` + Node
`cptk.js`) a buyer points at their own endpoint, two docs-derived request templates
+ `PROVENANCE.md`, a 37-test HTTP real-path suite, and `package.sh` →
`dist/cors-preflight-test-kit-vX.Y.zip`.

## Provenance of this build

Built under **ORDER 016** (live owner overnight/continued autonomous-build
authorization, reaffirmed by the live owner turn 2026-07-18) as a NEW sellable in
the API-robustness kit family. It **reuses the kit scaffold's structure** (file
set, evidence bar, packaging, listing/vetting grammar — closest templates are the
Rate-Limit and JWT kits, which have the same correct-stub + naive-stub evidence
pattern) but is **not** an N+1 of any existing line — it is a distinct product in a
distinct problem class, so the scoring below is an analog estimate inherited from
the dev-tool kit line, not a fresh ideation re-score.

## Scoring (kill-rule intake rubric, inherited weights — analog estimate)

| Axis | W | Score (analog to the sibling kits) |
|---|---|---|
| Distribution | 35% | 3.5 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **≈3.70 — BUILD (dev-tool kit line, new problem class)** |

Distribution scores **higher** than the throttling/pagination/dedup siblings on one
honest structural point: CORS is one of the highest search-intent pains in web
development (*"cors error"*, *"cors preflight failed"*, *"no access-control-allow-origin
header"* are perennial top-of-search queries), and the pain is felt by **both**
front-end and back-end developers — the widest audience in the family. That is a
distribution *lever*, not proof of sales: the concentrated dev-tool channel is the
same one where the live Stripe kit has 0 organic sales, so the conservative revenue
line stays $0 absent seeding.

## Kill-rule fields (provisional — bound at this INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on a free "your CORS reflects any
  origin / your `*` doesn't cover Authorization" gotcha article within **30 days of
  publish**, else ledgered negative (same bar as the sibling kits).
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the vetting packet
  once the publish click is DONE-flipped):** **T+7** funnel checkpoint · **T+30**
  kill-rule deadline (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to/Hashnode article on the exact "your CORS is either broken in the
  browser or wide open — here's how to tell in 30 seconds" pain ⚑; (2) cross-link
  from the sibling dev-tool listings — the JWT/idempotency/rate-limit/webhook kits
  (adjacent buyer: a developer hardening a browser-facing API needs correct CORS
  AND safe retries AND correct throttling AND a verifier that can't be bypassed) ⚑;
  (3) Gumroad Discover ⚑. Distinct angle vs the siblings: this is the
  *browser-facing edge* of API robustness — the pair to the server-internal
  concerns (throttling, dedup) and the inbound-signature concern.
- **Max agent-effort budget:** ≤80k tokens to a buildable v0.1 zip.
- **Conservative revenue estimate:** $29 one-time. Conservative first-90-day:
  0–5 sales ($0–$145). Zero distribution = $0 — the proven sibling (Stripe kit)
  has 0 organic sales as of the last check; expect the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click; unverified until
  first sale.

## Why this might fail

CORS is a well-documented pattern, most web frameworks ship a CORS middleware, and
the correct configuration is a few dozen lines once you know the contract. The paid
delta is the same shape as the sibling kits' delta: a runnable harness that tests a
buyer's OWN endpoint against the properties a browser enforces + the correct/naive
reference pair that demonstrably catches a broken config + the docs discipline. A
free blog post substitutes substantially. One honest structural plus: the two worst
CORS outcomes — a config that silently blocks every browser request, and one that
silently reflects any origin (open CORS) — are invisible to `curl` and to a
same-origin unit test, and this kit fires the exact cross-origin preflight + request
a browser would and reports both failure modes in milliseconds, with no
headless-browser dependency. The $29 price sits on catalog precedent (the sibling
kits at $29), not measured CORS-specific willingness-to-pay, and distribution is the
same owner-gated channel where the Stripe kit has produced 0 organic sales so far.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/cors-preflight-test-kit.md` (the
derive script compiles it into `docs/publishing/OWNER-QUEUE.md`); the HOW detail
lives in `docs/launch/cors-preflight-test-kit/owner-actions.md`. Nothing here is
performed by any agent: no publish, no spend, no accounts — the build ENDS at the
queued owner ⚑ publish click (rail 13 / CONSTITUTION §13).

## Build artifact (verified 2026-07-18)

- Buyer bundle `dist/cors-preflight-test-kit-v0.1.zip` @ sha256
  `5c754e4432385d8c3b3f892a5ff572ddcf0e13cb0e07ee0dad522705be0b6c29`
  (35,779 bytes, 13 content files), byte-reproducible via `package.sh`
  (unconditional double rebuild produced the identical sha; the committed dist IS
  that build). The 37-test real-path HTTP suite is green from source AND from the
  extracted zip in a clean dir; `node cptk.js demo` shows the correct config
  all-pass and the naive config flagged on 4 properties; real-secret-shape scan
  **0 hits**.
