# Multi-Agent Control-Plane Pack — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-13, products lane — BUILD #3 of the 2026-07-13 ideation
batch, `docs/products/ideas-2026-07-13.md` §3, scored 3.525, tight
budget). No freeze applies: a zero-runtime document pack with no
payment-path dependency of its own, so the ORDER 003 gate (lifted
2026-07-11 by PR #22) never attached to it. Honest caveat: a live
purchase of ANY catalog product besides SWTK remains unverified —
QUEUED means the owner may click, not that this product's delivery is
live-proven. This is a click-script for the owner, not a request to any
agent; no agent performs publish/spend/account actions.

### ⚑ — Publish "Multi-Agent Control-Plane Pack" at $29 (one-time)
- **WHAT:** Create a $29 one-time digital product on your own no-code
  storefront, selling
  `candidates/multi-agent-control-plane-pack/dist/multi-agent-control-plane-pack-v0.1.zip`,
  using `docs/launch/multi-agent-control-plane-pack/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price
  $29) — same account as the live SWTK listing
  (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>) — or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name =
  "Multi-Agent Control-Plane Pack". 4) Price = $29 one-time. 5) Upload
  the dist zip. 6) Paste the listing copy (Title / Short / Long /
  Bullets / FAQ; set the refund/license lines the copy marks
  owner-to-set). 7) Publish. 8) Copy the public product URL. Optional
  same-visit cross-sell: one line each on the template-packs ($19 PWYW,
  the single-repo layer below this pack) and field-manual ($39, its
  ch.6/7 teach this layer in prose) listings pointing here (the
  disclosed cross-sell precedent — first-ten path channel 1).
- **WHY:** Developers coordinating 2+ concurrent agent sessions on one
  codebase hit duplicated work, clobbered status files, and lost
  orders, and have almost no packaged alternatives (the ideation
  entry's moat note); the pack is the distillation of the control
  plane THIS repo runs in production (150+ PRs coordinated through
  these exact files). Ideation scored 3.525 weighted (BUILD #3, tight
  budget, `docs/products/ideas-2026-07-13.md` §3). Conservative
  expectation: 0–5 sales in 90 days, $0–$145; zero distribution = $0
  (the intake's own line — SWTK has 0 organic sales as of 2026-07-13,
  and this audience is the smallest of the three BUILDs).
- **UNBLOCKS:** The first-ten-customers funnel (template-packs +
  field-manual cross-links ⚑ → dev.to "two agents, one repo" war-story
  article ⚑ → Gumroad Discover ⚑) and the catalog's multi-agent rung
  at $29.
- **VERIFIED-WHEN:** The public URL loads a purchasable $29 page AND a
  preview/test purchase delivers the zip whose sha256 matches the
  ARTIFACT line below.
- **ARTIFACT (verified 2026-07-13):** upload exactly
  `candidates/multi-agent-control-plane-pack/dist/multi-agent-control-plane-pack-v0.1.zip`
  @ sha256
  `39fc864880c1fa6d21f1a6974543c4df95df6e89cd8b6ae4656f9dd8311b0a9e`
  (21,989 bytes, 17 content files; byte-reproducible via `package.sh` —
  unconditional double rebuild 2026-07-13T14:22:25Z produced the
  identical sha; the committed dist IS that build). Executed
  honest-null substitute from the extracted bundle in a clean dir
  (2026-07-13T14:22:25Z, zero-runtime product — no test suite exists or
  is warranted): inventory 17/17 content files vs the listing's "What's
  inside"; every file UTF-8-decoded; markdown pass OK (H1-first,
  balanced fences, no fill-slot tokens; `templates/claim-file.md`
  exempt from H1 — a one-bullet fragment by design);
  secret/session-id/trigger-id scan **0 hits**; no `.DS_Store`, no
  `__pycache__`, no junk entries in the archive listing. If the source
  ever changes: rebuild, re-pin this line, and treat any uploaded copy
  as STALE until re-uploaded.

## Price precedent chain

$29 one-time — set at ideation (`docs/products/ideas-2026-07-13.md` §3:
"Multi-Agent Control-Plane Pack — $29") and recorded identically in
`INTAKE.md`, the listing copy, the §7 packet, and this script.
Precedent rung: SWTK sells live at exactly $29 and GWTK is queued at
$29; this pack sits at that rung rather than the $19
conventions-distillation rung (merge-wall cookbook, OCQK,
template-packs) because it is a complete multi-surface system (5
coordination surfaces + 7 installable templates + the folded claims-kit
chapter that ideation priced at $15 standalone) rather than one
convention plus one script — while the $39 field-manual rung stays
above it (broad fleet operations in prose vs this pack's one layer).
Chain: Kill-Rule Intake Kit $15 = False-Green $15 < OCQK $19 =
Merge-Wall $19 = template-packs $19 PWYW < **$29 this pack** = SWTK $29
(live) = GWTK $29 < Field Manual $39 < Membership Kit $49.
