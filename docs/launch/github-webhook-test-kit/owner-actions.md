# GitHub Webhook Test Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-13, products lane — BUILD #1 of the 2026-07-13 ideation
batch, `docs/products/ideas-2026-07-13.md` §1, scored 3.60). No freeze
applies: the kit has no Stripe/payment-path dependency of its own, so the
ORDER 003 gate (lifted 2026-07-11 by PR #22) never attached to it. Honest
caveat: a live purchase of ANY catalog product besides SWTK remains
unverified — QUEUED means the owner may click, not that this product's
delivery is live-proven. This is a click-script for the owner, not a
request to any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "GitHub Webhook Test Kit" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code
  storefront, selling
  `candidates/github-webhook-test-kit/dist/github-webhook-test-kit-v0.1.zip`,
  using `docs/launch/github-webhook-test-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $29) —
  same account as the live SWTK listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "GitHub
  Webhook Test Kit". 4) Price = $29 one-time. 5) Upload the dist zip.
  6) Paste the listing copy (Title / Short / Long / Bullets / FAQ; set the
  refund/license lines the copy marks owner-to-set). 7) Publish. 8) Copy
  the public product URL. Optional same-visit cross-sell: add one line to
  the live SWTK listing pointing at this kit (same buyer, sibling product —
  first-ten path channel 2).
- **WHY:** The direct sibling of the catalog's one LIVE product, built on
  its proven template: "verify X-Hub-Signature-256" is a real, searched
  pain, and the kit ships the checks GitHub will never send you (forged /
  unsigned / SHA-1-downgrade / form-encoded / replayed deliveries) plus
  GitHub's own published HMAC test vector as an offline proof. Ideation
  scored 3.60 weighted (BUILD #1, `docs/products/ideas-2026-07-13.md` §1).
  Conservative expectation: 0–5 sales in 90 days, $0–$145; zero
  distribution = $0 (the intake's own line — SWTK has 0 organic sales as
  of 2026-07-13).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to gotcha article ⚑ →
  SWTK cross-link ⚑ → Gumroad Discover ⚑) and the catalog's second
  dev-tool rung at $29.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT
  line below AND the real-path suite is green in CI on the built head SHA
  (the `github-webhook-test-kit-tests` job in
  `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-13):** upload exactly
  `candidates/github-webhook-test-kit/dist/github-webhook-test-kit-v0.1.zip`
  @ sha256
  `e17b08bac25b047942281c00eb0047ae592d6bda790284aade7b6cf58dcbf6a9`
  (36,214 bytes, 13 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild 2026-07-13T09:47:54Z produced the identical
  sha; the committed dist IS that build). Executed verification from the
  extracted bundle in a clean dir (2026-07-13T09:48:06Z): the 18-test
  real-path HTTP suite green from the extracted copy (`Ran 18 tests in
  4.547s / OK`); `node gwtk.js vector` PASS against GitHub's published
  constant; real-secret-shape scan **0 hits** (the only secret-like
  strings are GitHub's own PUBLIC documentation test-vector values and
  fake test secrets, both labeled as such in the files); inventory 13/13
  files vs the listing's "What's inside"; no `.DS_Store`, no
  `__pycache__`, no junk entries in the archive listing. If the source
  ever changes: rebuild, re-pin this line, and treat any uploaded copy as
  STALE until re-uploaded.

## Price precedent chain

$29 one-time — set at ideation (`docs/products/ideas-2026-07-13.md` §1:
"GitHub Webhook Test Kit (GWTK) — $29") and recorded identically in
`INTAKE.md`, the listing copy, the §7 packet, and this script. Precedent
rung: the Stripe Webhook Test Kit sells LIVE at exactly $29 (PR #86;
`price_cents 2900` verified on the live page) and this kit is the same
product shape for the sibling webhook ecosystem — same stdlib-only
harness + vendored-fixture + hostile-mode structure, same buyer. Chain:
Kill-Rule Intake Kit $15 = False-Green Test Trap $15 < Merge-Wall
Cookbook $19 = template-packs $19 PWYW < **$29 this kit** = SWTK $29
(live) < Field Manual $39 (PR #110) < Membership Kit $49 (PR #106).
