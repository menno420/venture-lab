# Owner-Click Queue Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-13, products lane — BUILD #2 of the 2026-07-13 ideation
batch, `docs/products/ideas-2026-07-13.md` §2, scored 3.60). No freeze
applies: the kit has no payment-path dependency of its own, so the ORDER
003 gate (lifted 2026-07-11 by PR #22) never attached to it. Honest
caveat: a live purchase of ANY catalog product besides SWTK remains
unverified — QUEUED means the owner may click, not that this product's
delivery is live-proven. This is a click-script for the owner, not a
request to any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "Owner-Click Queue Kit" at $19 (one-time)
- **WHAT:** Create a $19 one-time digital product on your own no-code
  storefront, selling
  `candidates/owner-click-queue-kit/dist/owner-click-queue-kit-v0.1.zip`,
  using `docs/launch/owner-click-queue-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $19)
  — same account as the live SWTK listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name =
  "Owner-Click Queue Kit". 4) Price = $19 one-time. 5) Upload the dist
  zip. 6) Paste the listing copy (Title / Short / Long / Bullets / FAQ;
  set the refund/license lines the copy marks owner-to-set). 7) Publish.
  8) Copy the public product URL. Optional same-visit cross-sell: one
  line each on the field-manual ($39, its ch.4 teaches this pattern in
  prose) and kill-rule-kit ($15) listings pointing here (the disclosed
  cross-sell precedent — first-ten path channel 2).
- **WHY:** "How do I let my agent run without letting it spend" is a
  live, growing pain with almost no packaged alternatives; the kit is
  the generalized distillation of the owner-queue system THIS repo runs
  in production (`scripts/derive_owner_queue.py` →
  `docs/publishing/OWNER-QUEUE.md` — this very click rides it), with
  the production gotchas as the moat. Ideation scored 3.60 weighted
  (BUILD #2, `docs/products/ideas-2026-07-13.md` §2). Conservative
  expectation: 0–5 sales in 90 days, $0–$95; zero distribution = $0
  (the intake's own line — SWTK has 0 organic sales as of 2026-07-13).
- **UNBLOCKS:** The first-ten-customers funnel (dev.to "my agent never
  spends money" article ⚑ → field-manual + kill-rule-kit cross-links ⚑
  → Gumroad Discover ⚑) and the catalog's agent-ops rung at $19.
- **VERIFIED-WHEN:** The public URL loads a purchasable $19 page AND a
  preview/test purchase delivers the zip whose sha256 matches the
  ARTIFACT line below AND the kit suite is green in CI on the built
  head SHA (the `owner-click-queue-kit-tests` job in
  `.github/workflows/kit-tests.yml`).
- **ARTIFACT (verified 2026-07-13):** upload exactly
  `candidates/owner-click-queue-kit/dist/owner-click-queue-kit-v0.1.zip`
  @ sha256
  `f81f1b4eb39194ef96551b24bb20ffbd6f15aac07543fba2f894c670734564e7`
  (28,712 bytes, 12 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild 2026-07-13T10:18:35Z produced the
  identical sha; the committed dist IS that build). Executed
  verification from the extracted bundle in a clean dir
  (2026-07-13T10:18:50Z): the 38-test suite green from the extracted
  copy (`Ran 38 tests in 0.023s / OK`); the shipped agent-fleet example
  derived from the extracted copy byte-identical to its committed
  EXPECTED output, and `lint` OK on it; real-secret-shape scan **0
  hits**; inventory 12/12 content files vs the listing's "What's
  inside"; no `.DS_Store`, no `__pycache__`, no junk entries in the
  archive listing. If the source ever changes: rebuild, re-pin this
  line, and treat any uploaded copy as STALE until re-uploaded.

## Price precedent chain

$19 one-time — set at ideation (`docs/products/ideas-2026-07-13.md` §2:
"Owner-Click Queue Kit — $19") and recorded identically in `INTAKE.md`,
the listing copy, the §7 packet, and this script. Precedent rung: the
Agent Merge-Wall Cookbook sells at exactly $19 (conventions + runnable
recipes distilled from this repo's production infrastructure — the same
product shape as this kit) and template-packs anchors $19 PWYW. The
ideation entry's own WTP note caps it below the $29 tool rung: it's
conventions-plus-one-script, DIY-able by a strong buyer in an afternoon,
so the price sits at the guide/conventions tier, not the
multi-fixture-harness tier. Chain: Kill-Rule Intake Kit $15 =
False-Green Test Trap $15 < **$19 this kit** = Merge-Wall Cookbook $19 =
template-packs $19 PWYW < SWTK $29 (live) = GWTK $29 < Field Manual $39
< Membership Kit $49.
