---
state: captured
origin: agent
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Next-wave product roadmap — 2026-07-18

> **Status:** `ideas` — a ranked pipeline of the next ~10 SKU/product candidates,
> scored by estimated value · buildability · owner-gates, with a suggested
> scaffold to copy for each. This is a **planning doc**: nothing here is built,
> priced-live, or published; every publish remains an owner click queued in
> `docs/publishing/OWNER-QUEUE.md`. No §7 vetting packet and no OWNER-QUEUE regen
> accompany this file — a roadmap adds no publish surface.

## Why this list means the backlog is NOT dry

The overnight menu (`docs/ideas/2026-07-17-overnight-menu.md`) declared the
agent-executable backlog "DRY at PR #215" and switched to planning mode. Since
then the lane has SHIPPED, one PR each, five of that menu's own product items to
owner-click-ready (Slack, Shopify, Auto-Merge-Enabler cookbook, the four-kit
Webhook Verifier Bundle) plus a genuinely new sellable (the Idempotency Key Test
Kit, PR #233). That is the pattern: "dry" was never true — it meant "the easy
copies are done." This roadmap re-stocks the shelf so no future session re-derives
a false "backlog dry" line from an empty grep. It carries a standing supply of
work that is **agent-completable end-to-end to owner-click-ready without any
owner gate** (the API-robustness kits at the top), followed by high-value work
that an agent can build but that stalls at a named owner gate (bundles awaiting
component publishes; NL/DE editions awaiting the native-speaker proofread). A
session picks the top un-retired, un-gated row and builds it. The list is
deliberately longer than one session can clear.

## Already BUILT — retired from the roadmap (do NOT propose rebuilding)

These carried over from the overnight menu or the webhook family and are now in
the tree at owner-click-ready or better; they are **retired** so they never
re-surface as "candidates":

| Menu item | What it became | Where | Status |
|---|---|---|---|
| P-1 Slack Webhook Test Kit | Built | `candidates/slack-webhook-test-kit/` | READY · D15 |
| P-2 Shopify Webhook Test Kit | Built | `candidates/shopify-webhook-test-kit/` | READY · D14 |
| P-3 Webhook Test Kit Trio ($59, 3-pack) | Superseded by the **4-pack** | `candidates/webhook-verifier-bundle/` ($79) | HARD-GATED on D5/D14/D15 publishes |
| P-4 Auto-Merge Enabler Cookbook | Built | `candidates/auto-merge-enabler-cookbook/` | READY · D3 |
| (new, not on the menu) Idempotency Key Test Kit | Built | `candidates/idempotency-key-test-kit/` | READY · D6 (PR #233) |
| P-9 Audiobook / narration-ready edition spec | Built (Paper Orange + Night Kiln lead titles) | `.../the-paper-orange/versions/audio`, `.../the-night-kiln/versions/audio` | in tree |
| P-10 Night Kiln omnibus — **EN** | Built (EN only) | `.../the-night-kiln/versions/omnibus-en` | in tree — **NL omnibus still open** (see R9) |

Everything else on the overnight menu (P-5…P-8, P-11, P-12, the PUB / REV / OPS
lanes) is still open; the product-lane survivors are folded into the ranks below.

## Ranked roadmap

Rank optimizes for **reaching owner-click-ready without an owner gate first**
(so the lane keeps converting build-hours into shippable inventory with no human
in the loop), **then high-value work that stalls at a named owner gate**.
Buildability legend — evidence class: *real-path test* (fires real-shape traffic
at a reference implementation, correct+broken pair proves the check bites) ·
*honest-null* (a guide/spec whose claims are cited, no runtime) ·
*verified-by-production* (distils workflow/state this repo actually runs). Size:
S / M / L (diff surface, not time). Gate legend: *fully agent-completable* =
reaches owner-click-ready with only the always-present publish click outstanding;
*builds-but-owner-gate* = an agent builds the whole artifact but it cannot go
live until a named owner-only step clears.

| # | Candidate | Cat. | Value | Buildability (evidence · size) | Owner gate beyond publish | Scaffold to copy |
|---|---|---|---|---|---|---|
| R1 | Rate-Limit / Retry-After Test Kit — $29 | dev tool | **High** | real-path test · M | none — fully agent-completable | `idempotency-key-test-kit/` |
| R2 | Pagination / Cursor Test Kit — $29 | dev tool | Med | real-path test · M | none — fully agent-completable | `idempotency-key-test-kit/` |
| R3 | JWT / Bearer-Auth Verification Test Kit — $29 | dev tool | **High** | real-path test · M | none — fully agent-completable | `slack-webhook-test-kit/` (sig family) |
| R4 | The Idempotency & Retry Cookbook — $19 | guide | Med | honest-null / verified-by-prod · S–M | none — fully agent-completable | `false-green-test-trap/`, `merge-wall-cookbook/` |
| R5 | `_api-hardening-core/` + `provenance_lint.py` (kit-family enabler) | tooling | Med (leverage) | real-path test + unit · M | none — fully agent-completable | existing `scripts/*` + kit test scaffold |
| R6 | Pricing-experiment spec (PWYW floor + Founder's Everything anchor) | writing/spec | Med | honest-null · S | price edit is an owner click | `docs/ideas/*`, existing packets |
| R7 | API Robustness Bundle — $49 (idempotency + R1) | bundle | Med | honest-null · S | HARD-GATED: needs D6 + R1 published live | `webhook-verifier-bundle/` |
| R8 | Trilingual board-book "First Library" bundle — manifest | bundle/spec | Med | honest-null · M | POD/print + publish owner-gated | `candidates/BUNDLE-LISTING.md` |
| R9 | The Night Kiln — **NL** omnibus (De Nachtoven box set) | writing | Med | honest-null (recombination) · S–M | native-speaker proofread (softened — components already passed) | `.../the-night-kiln/versions/omnibus-en` |
| R10 | The Salt Bell — NL edition (*De zoute klok*) | writing | **High** (NL fit) | honest-null · L | native-speaker proofread (owner-only) | existing `versions/nl` editions |

---

## Candidate detail

### R1. Rate-Limit / Retry-After Test Kit — $29 · dev tool
- **Concept:** a stdlib-only local harness that proves your API's rate-limit
  contract on both edges — does your *server* emit correct `429` + `Retry-After`
  + `RateLimit-*` headers (IETF `RateLimit` header draft), and does your *client*
  honour `429`/`Retry-After` with exponential backoff + jitter rather than
  hammering. Correct + deliberately-naive reference pair so the suite provably
  catches a client that ignores `Retry-After`.
- **Value — High:** the exact same dev buyer as the idempotency kit; a client
  that retries on 429 is *definitionally* the client that needs idempotency, so
  the cross-sell is native. This was already flagged as the obvious next SKU in
  the Idempotency Key Test Kit session card's 💡.
- **Buildability:** real-path test; M. Fully agent-completable to owner-click-ready
  — the whole kit (harness, correct/naive stubs, real-path suite, docs-derived
  fixtures + PROVENANCE, byte-reproducible `package.sh`, §7 packet, CI job)
  mirrors the idempotency kit's proven shape end-to-end. No live account or key.
- **Gate:** none beyond the always-present publish click.
- **Scaffold:** `candidates/idempotency-key-test-kit/` — nearly file-for-file
  (dedup semantics swap for backoff/header semantics).

### R2. Pagination / Cursor Test Kit — $29 · dev tool
- **Concept:** proves a list endpoint paginates safely — a cursor stays stable
  across inserts/deletes (no rows silently skipped or double-returned mid-scan),
  the cursor is opaque and tamper-rejecting, page-size limits are enforced, and
  the terminal page signals "done" correctly. Correct + naive (offset-based,
  drifts under concurrent insert) reference pair.
- **Value — Med:** narrower failure class than rate-limiting but a real, silent
  data-loss bug; broadens the dev-tool family without cannibalising it.
- **Buildability:** real-path test; M. Fully agent-completable — same kit shape,
  a state-mutation-during-scan test rig instead of a signature or dedup rig.
- **Gate:** none beyond publish.
- **Scaffold:** `candidates/idempotency-key-test-kit/` (stateful multi-request
  harness is the closest existing pattern).

### R3. JWT / Bearer-Auth Verification Test Kit — $29 · dev tool
- **Concept:** fires real-shape JWTs at your protected endpoint and proves it
  *rejects* the dangerous ones — expired (`exp`), not-yet-valid (`nbf`),
  `alg: none`, algorithm-confusion (HS256 signed with the RS256 public key),
  wrong `aud`/`iss`, tampered payload — and accepts only a valid token. Correct
  + naive (verifies signature but ignores `exp`/`aud`) reference pair.
- **Value — High:** auth bugs are the highest-severity class in this family and
  the audience (anyone building a token-protected API) is the largest; sits
  naturally beside the four signature-verification webhook kits.
- **Buildability:** real-path test; M. Fully agent-completable — JWT signing is
  stdlib-doable (`hmac`/`hashlib` for HS256; RS256 needs a vendored key, still no
  third-party account). Honest caveat: pin the claim set to RFC 7519 + document
  which library behaviours are modelled vs asserted.
- **Gate:** none beyond publish.
- **Scaffold:** `candidates/slack-webhook-test-kit/` (the signature-verification
  branch of the family — HMAC basestring + reject-cases structure).

### R4. The Idempotency & Retry Cookbook — $19 · guide
- **Concept:** the operating-lesson guide under the R1/idempotency kits: why a
  network timeout is an *unknown* not a failure, at-least-once delivery, the
  dedup-key + stored-response pattern, backoff + jitter, and how the same failure
  hides behind a green unit suite. Cites the kits' own fixtures and the false-green
  incident.
- **Value — Med:** a $15–19 content SKU that anchors the outbound-robustness
  cluster the way *The False-Green Test Trap* anchors the inbound webhook cluster;
  cheap cross-sell into R1 + the idempotency kit.
- **Buildability:** honest-null / verified-by-production; S–M. Fully
  agent-completable — prose + a small offline helper, cited to committed fixtures
  and public docs.
- **Gate:** none beyond publish.
- **Scaffold:** `candidates/false-green-test-trap/` (guide + tiny tool shape) or
  `candidates/merge-wall-cookbook/` (cookbook prose grammar).

### R5. `_api-hardening-core/` + `provenance_lint.py` — kit-family enabler · tooling
- **Concept:** extract the ~70%-shared kit scaffold (byte-reproducible allow-list
  `package.sh`, the reference-stub HTTP test rig, the `is_2xx`/verdict pair, the
  `post`/`get`/`build_request` shape, the side-effect-counter demo pattern, the
  PROVENANCE discipline) into a `candidates/_api-hardening-core/` the kits inherit,
  plus a `provenance_lint.py` that FAILS a kit whose fixture lacks a pinned
  sha256 or a cited source. Makes kit N+1 a scheme-and-fixtures diff, not a
  re-implementation, and machine-enforces the honesty bar.
- **Value — Med (leverage, not direct revenue):** every future kit (R1/R2/R3)
  gets cheaper and more consistent; this is the enabler both the Shopify and
  bundle cards independently flagged. Not itself a SKU — an infrastructure slice.
- **Buildability:** real-path test + unit tests; M. Fully agent-completable.
- **Gate:** none (no publish surface at all — pure repo tooling).
- **Scaffold:** existing `scripts/*.py` + `test_*.py` pairs; the kits' current
  `package.sh`/`test_http_realpath.py`.
- **Sequencing note:** highest leverage if built *before* R1–R3 so they inherit
  the core; still worthwhile after, as a de-duplication refactor.

### R6. Pricing-experiment spec — PWYW floor + "Founder's Everything" anchor · writing/spec
- **Concept:** the P-12 experiment written as a spec: (a) launch the AI Novella
  Production Kit as pay-what-you-want with a $19 floor (mirrors the proven
  template-packs PWYW on-ramp) to buy first-sale signal on the writing channel;
  (b) a time-boxed tiered "Founder's Everything" bundle stacking the publish-READY
  dev/agent SKUs at a launch discount vs the à-la-carte sum, to test whether a
  catalog-wide anchor converts where singles have not (0 organic sales to date).
- **Value — Med:** first deliberate pricing signal; every single listing gains an
  upsell anchor once components are live.
- **Buildability:** honest-null; S. Fully agent-completable as a spec (respect the
  sim-lab pricing bands V037–V041).
- **Gate:** every price change / new bundle SKU is an owner click (the build is
  the spec, not the price edit).
- **Scaffold:** `docs/ideas/*` spec convention + existing packet pricing blocks.

### R7. API Robustness Bundle — $49 · bundle
- **Concept:** Idempotency Key Test Kit + Rate-Limit/Retry-After Kit (R1) as one
  "make your outbound API calls safe under retries" pack, the same higher-AOV move
  the Webhook Verifier Bundle makes for the signature four-pack.
- **Value — Med:** raises average order value on the outbound-robustness cluster;
  native cross-sell (retry ⇒ idempotency).
- **Buildability:** honest-null; S (a listing + manifest, like the webhook bundle).
- **Gate:** **HARD-GATED** — a storefront bundle references its components as
  *live* listings, so it cannot be created until both D6 (idempotency) and R1 are
  published. Agent can build the listing/manifest now; it stalls at the two
  component publish clicks.
- **Scaffold:** `candidates/webhook-verifier-bundle/`.

### R8. Trilingual board-book "First Library" bundle — manifest · bundle/spec
- **Concept:** bundle the 27 existing board-book texts (7 title-lines × EN/NL/DE
  + Comet Biscuit ×3) as a trilingual "first library" box for bilingual/trilingual
  NL/BE/DE households — a listing + edition-manifest over content that already
  exists, not new writing.
- **Value — Med:** first bundle in the children's line; names a first-ten path
  (trilingual-parenting communities) distinct from every dev/agent channel.
- **Buildability:** honest-null; M. Agent-completable as a digital manifest/spec.
- **Gate:** any physical POD/print step is hard owner-gated (as with photo-packs);
  digital side + publish is the usual owner click.
- **Scaffold:** `candidates/BUNDLE-LISTING.md` + `webhook-verifier-bundle/`
  (bundle grammar).

### R9. The Night Kiln — NL omnibus (De Nachtoven box set) · writing
- **Concept:** the EN omnibus is built (`versions/omnibus-en`); assemble the NL
  omnibus from the three already-complete, already-verified NL manuscripts
  (De Nachtoven / De Morgendeur / De Oogstslag) — unified front matter, single
  TOC, inter-book continuity note — sold at a modest premium over a single book.
- **Value — Med:** higher-AOV listing off the completed NL trilogy; pure
  recombination, EN omnibus is the working template.
- **Buildability:** honest-null (recombination); S–M. Agent builds the derived
  edition file.
- **Gate:** native-speaker proofread — but **softened**: the component manuscripts
  already carry their PRE-QA/proofread state, so the omnibus adds only
  front/back-matter to clear, not a fresh full-length pass.
- **Scaffold:** `candidates/adult-novels/the-night-kiln/versions/omnibus-en`.

### R10. The Salt Bell — NL edition (*De zoute klok*) · writing
- **Concept:** full Dutch edition of The Salt Bell (Zeeland, 1953 Watersnoodramp),
  currently EN-only; the NL title is pre-named in the concept doc and the subject
  is core Dutch national memory — the single highest NL-market-fit title in the
  catalog.
- **Value — High (for the NL funnel):** the most commercially obvious NL gap;
  pairs with the EN packet (PR #211) for a bilingual listing and joins the 13
  live NL editions.
- **Buildability:** honest-null; L (a real full-length translation/adaptation).
  Agent builds the manuscript to draft.
- **Gate:** **builds-but-owner-gate** — the owner-only native-speaker proofread
  pass is the binding lever (19 OWNER-QUEUE rows are hard-gated on it); an AI
  cannot clear it, only tool it (see PUB-7). Ranked last of the ten because its
  gate is the hardest and slowest, despite high value.
- **Scaffold:** the existing `versions/nl` editions across the adult line.

## Below the top ten — a standing gated cluster (not dry either)

The remaining overnight-menu NL/DE edition swings are real but all stall at the
same owner-only native-speaker proofread gate, so they sit below the un-gated
work: **P-6** The Wire Garden NL (*Een novelle van de Dodendraad*), **P-7** a YA
first-NL pilot, **P-8** The Paper Orange DE edition (the biggest reach, most
sensitive subject). Build order among them should follow whichever the owner
proofread-commits first. The publishing/ops enablers (PUB-1…PUB-9, OPS-1…OPS-9)
that TOOL that gate — spellcheck-in-CI, `categorize.py`, the structured proofread
packet (PUB-7), length-band checker — are the highest-leverage way an agent can
move the gated cluster without owning the gate.

## Provenance

Derived from the repo, not invented — no fabricated metrics. Sources as of
`main@c1bf40a`:

- Built-vs-open status, prices, decision numbers (D3/D5/D6/D14/D15) —
  `docs/publishing/OWNER-QUEUE.md@c1bf40a` and `docs/launch/CATALOG.md@c1bf40a`
  (the authoritative generated queue + the storefront catalog).
- Raw candidate pool (P-/PUB-/REV-/OPS- items, effort, gates) —
  `docs/ideas/2026-07-17-overnight-menu.md@2348575`.
- Catalog scope, LIVE-SKU + kill clock, the native-speaker proofread gate as the
  binding lever — `docs/current-state.md@df75b72`.
- The R1/R5 "next SKU + core-extraction" framing — the Session idea in
  `.sessions/2026-07-18-idempotency-key-test-kit.md`.
- Built-artifact confirmations (audio specs, EN omnibus, absence of NL omnibus) —
  the `candidates/adult-novels/*/versions/` tree at `main@c1bf40a`.
