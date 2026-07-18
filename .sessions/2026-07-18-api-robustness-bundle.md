# Session — API Robustness Bundle $79 (hard-gated bundle → ready-pending component publishes)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · bundle build
- **started (date -u):** Sat Jul 18 19:15 UTC 2026
- **branch:** `claude/api-robustness-bundle-2026-07-18`
- **base:** `main@2fb86bf`
- **purpose:** bundle the FOUR own-endpoint API-robustness test kits (Idempotency
  Key + Rate-Limit + Pagination + JWT Auth, $29 each) into ONE discounted
  storefront SKU — the **API Robustness Bundle** — and land it as ONE PR. Unlike
  the individual kits this lands **HARD-GATED (ready-pending-publish):** a
  storefront bundle references its component products, so it cannot be created
  (owner-click-ready) until the not-yet-published component kits are live. The
  gate is on the Idempotency (D6) / JWT Auth (D7) / Pagination (D13) /
  Rate-Limit (D16) publish clicks. Mirrors the existing hard-gated **Webhook
  Verifier Bundle** precedent exactly. The build ENDS at the queued owner ⚑
  publish sequence (rail 13 / CONSTITUTION §13) — no publish, no spend, no
  accounts performed by the seat.
- **session:** Mirrors the Webhook Verifier Bundle hard-gate precedent exactly:
  numbered §7 steps carry no ⚑ so the queue derives zero D-items, the blocking
  component-publish checkboxes come first and name the real D-numbers
  (Idempotency D6 / JWT D7 / Pagination D13 / Rate-Limit D16), and the price is
  the cited $79 vs $116 with the discount math ($37 / 31.9%). Like the webhook
  bundle it ships a real byte-reproducible assembly zip (four component zips
  verbatim + docs) with an assembly/inventory check wired into CI, rather than an
  N/A-artifact stance — the pins are asserted both on disk and inside the built
  zip. This is the second four-kit discount SKU and the own-endpoint sibling to
  the webhook (inbound-edge) bundle. Born-red card holds substrate-gate red until
  this completion flip.

## 💡 Session idea

💡 **The catalog now carries TWO four-kit bundles and EIGHT $29 dev-tool kits
built from the same correct-vs-broken-stub + HTTP-real-path + byte-reproducible-
zip scaffold. The next consolidation slice is a `candidates/_api-hardening-core/`
extraction that BOTH bundles' assembly + all eight kits' build discipline derive
from — and, once it exists, a top-of-funnel "API Reliability Suite" mega-bundle
that spans both four-packs (all 8 kits) at a deeper anchor.** Two moves, in
dependency order. (1) **Extract `_api-hardening-core/`** — the eight kits (four
webhook + four own-endpoint) are now eight near-copies of: a loopback HTTP
harness that starts a reference stub and drives fixtures, a correct-stub /
naive-stub pair, a `package.sh` (allow-list + fixed mtime + sorted + `zip -X`),
and a PROVENANCE shape. That is ~8× the surface for the same bug to land eight
times. A shared `_api-hardening-core/` (the harness + the package/repro helper +
a fixtures-schema contract) that each kit imports turns "add kit N+9" into "drop
a fixtures-and-property diff," and turns a scaffold fix into one edit, not eight.
This is the shopify card's #227 `_webhook-kit-core/` idea generalized across the
whole dev-tool lane. (2) **"API Reliability Suite" mega-bundle** — once the two
four-packs are live, a single 8-kit SKU (Webhook Verifier + API Robustness) at
a deeper anchor (e.g. $139 vs the $158 two-bundle / $232 all-singles total) is
the highest-AOV catalog reach at zero new build cost, and it composes cleanly
with move (1): the mega-bundle's `package.sh`/`MANIFEST` are the SAME zip-of-zips
assembly this bundle and the webhook bundle already prove, just over eight pins
instead of four. Pair it with the webhook card's #231 💡 (a
`scripts/derive_bundle_manifest.py` that globs the kits and emits each manifest)
so all three bundles re-derive their pins from disk and a shipped-but-unbundled
kit becomes red CI, not a reviewer's eyeball. Net: the two bundle cards (#231
manifest-derive, this one core-extract + mega-suite) and the shopify card (#227
core-extract) have now independently converged on "dedup the scaffold and
machine-derive the drift-prone tables" three times — the strongest possible
signal that the extraction is the next slice, before kit N+9 makes it a
nine-copy refactor.

## previous-session review

previous-session review: `.sessions/2026-07-18-jwt-auth-test-kit.md` (PR #238,
the R3 slice of ORDER 016 — the JWT Auth Test Kit $29, fourth own-endpoint kit
and the highest-severity problem class in the family). A clean, honest build: it
shipped the correct-stub / naive-stub evidence pattern so the suite *proves* it
catches the bypasses (alg:none, RS256→HS256 algorithm-confusion, tampered/
wrong-key, expired, not-yet-valid, wrong aud/iss, malformed — each cited to RFC
7519/7515/8725), and — the part I most respect — it drew the scope line loudly
rather than overclaiming: HS256 + the attack classes are fully covered
stdlib-only, and real RS256/ES256 signature-math verify is stated OUT of the
shipped scope in both PROVENANCE and the listing's "what it does NOT do." Its
💡 already named this exact bundle (plus the `_api-hardening-core` extraction),
so this session is the direct execution of its top idea — and this card's own 💡
carries the extraction half forward as the next slice, closing the loop the JWT
card opened. The one nit: it's the fourth kit built from a copy-pasted scaffold
with no shared core yet, which is precisely the debt both cards' ideas now flag.

## Work log

- 2026-07-18T19:15Z — Branch `claude/api-robustness-bundle-2026-07-18` from
  origin/main (`2fb86bf`); collision check clean (no `control/claims/` bundle
  claim, no open PR covering it). Born-red card committed (first commit),
  pushed. Build begins.
- 2026-07-18T19:3xZ — Built `candidates/api-robustness-bundle/`: README +
  per-kit summaries, QUICKSTART, MANIFEST.json (4 pins + $29×4=$116 → $79
  pricing), PROVENANCE (discount math + pins + the ~$89→$79 reconciliation to
  webhook-bundle parity), reproducible `package.sh` (zip-of-zips) and
  `test_bundle.py` (8-test assembly/inventory check). Double-rebuild
  byte-identical: bundle sha256
  `6be74b6d78a77180a133fd09c31c452baaea77497cd8db63461b9ee43dfb560c` (160,844 B,
  10 entries); 8 assembly tests green; 125 component tests re-verified green
  (Idempotency 20 + Rate-Limit 27 + Pagination 31 + JWT 47). Wired the
  `api-robustness-bundle-tests` CI job. Landed the launch dir and the §7 vetting
  packet mirroring the Webhook Verifier hard-gate; regenerated OWNER-QUEUE (+0
  decisions, +1 HARD-GATED 8-click sequence naming the four blocking component
  rows — Idempotency D6 / JWT D7 / Pagination D13 / Rate-Limit D16 — no D-shift).
  CATALOG bundle row + positioning + cross-sell cluster added. PR #239 opened
  READY. Card flipped `complete` (this commit).
