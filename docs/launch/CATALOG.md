# Storefront Catalog — positioning & comparison

> **Status:** `reference`
>
> A single storefront-facing view of the sellable software, guides, writing
> kits, and bundles: one comparison table, a positioning block per SKU (who it's
> for, the problem, the buy-vs-DIY angle, and cross-sell), the bundle discount
> math, and an **advisory** recommended publish order. This is a launch **asset**
> that complements the per-SKU listing copy — it does not replace it. Prices,
> publish status, and queue decision numbers are pulled from
> [`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md) and
> [`../current-state.md`](../current-state.md); the positioning is derived from
> each SKU's own listing copy. **Nothing here is published, priced-live, or
> spent by the seat — every publish is an owner click, queued in OWNER-QUEUE.**

## What's in the catalog

Eighteen self-hosted, stdlib-first products across four lanes, plus two bundles:

- **Developer tools** — webhook signature-verifier test kits (Stripe, GitHub,
  Slack, Shopify), the idempotency / safe-retry test kit, the rate-limit /
  throttling test kit, the pagination / result-set-integrity test kit, the JWT
  auth / verifier-security test kit, and the membership-site starter. You run them
  locally, no vendor account required.
- **Agent-ops tools & templates** — the session-discipline template pack, the
  owner-click queue control surface, and the multi-agent control plane.
- **Guides & cookbooks** — the field manual and the four operating-lesson guides
  (false-green testing, the two merge-wall/auto-merge landing paths, kill-rule
  intake), each cited to real commits.
- **Writing kits** — the AI novella production method.
- **Bundles** — Ship-It (product + process) and the Webhook Verifier four-pack.

Out of scope here (separate lanes, each hard-gated on owner-only work): the
Photo Packs and the KDP book catalog — see
[`../current-state.md`](../current-state.md).

## Comparison table

| Product | Price | Category | Publish status | Queue decision |
|---|---|---|---|---|
| Stripe Webhook Test Kit | $29 one-time | Dev tool · webhook verifier | **LIVE** (Gumroad, since 2026-07-12) | — (live; no pending decision) |
| GitHub Webhook Test Kit | $29 one-time | Dev tool · webhook verifier | READY | D5 |
| Slack Webhook Test Kit | $29 one-time | Dev tool · webhook verifier | READY | D18 |
| Shopify Webhook Test Kit | $29 one-time | Dev tool · webhook verifier | READY | D17 |
| Idempotency Key Test Kit | $29 one-time | Dev tool · idempotency / safe-retry | READY | D6 |
| Rate-Limit Test Kit | $29 one-time | Dev tool · rate-limit / throttling | READY | D16 |
| Pagination Test Kit | $29 one-time | Dev tool · pagination / result-set integrity | READY | D13 |
| JWT Auth Test Kit | $29 one-time | Dev tool · JWT auth / verifier security | READY | D7 |
| Membership-Site Boilerplate Kit | $49 one-time | Dev tool · starter | READY | D9 |
| Agent-Workflow Template Pack | $19 pay-what-you-want | Agent-ops · templates | READY | D19 |
| Owner-Click Queue Kit | $19 one-time | Agent-ops · tool | READY | D12 |
| Multi-Agent Control-Plane Pack | $29 one-time | Agent-ops · tool | READY | D11 |
| Agent Fleet Field Manual | $39 one-time | Guide | READY | D1 |
| The False-Green Test Trap | $15 one-time | Guide + tool | READY | D4 |
| The Agent Merge-Wall Cookbook | $19 one-time | Guide | READY | D10 |
| The Auto-Merge Enabler Cookbook | $19 one-time | Guide | READY | D3 |
| Kill-Rule Intake Kit | $15 one-time | Guide + templates | READY | D8 |
| AI Novella Production Kit | $29 one-time | Writing kit | READY | D2 |
| Ship-It Bundle | $59 one-time | Bundle | **HARD-GATED** on D9 + D19 publishes | — (derives no decision) |
| Webhook Verifier Bundle | $79 one-time | Bundle | **HARD-GATED** on D5 + D18 + D17 publishes (Stripe already LIVE) | — (derives no decision) |

Status legend: **LIVE** = published and buyable now · **READY** = built, priced,
listing drafted, verified — one owner publish click from live · **HARD-GATED** =
a bundle that references its component products as live listings, so it cannot be
created until those components are published.

> Note on sourcing: [`../current-state.md`](../current-state.md) was last
> restamped 2026-07-17 and names "10 publish-READY SKUs"; the Slack, Shopify,
> Auto-Merge Enabler, Idempotency Key Test Kit, Rate-Limit Test Kit, Pagination
> Test Kit, and JWT Auth Test Kit packets landed after that stamp, so the counts
> and decision numbers in this catalog follow the regenerated
> [`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md), which is the
> authoritative queue. The JWT Auth Test Kit was added 2026-07-18 as a new
> decision **D7** (its packet `jwt-auth-test-kit.md` sorts by filename between
> `idempotency-key-test-kit` and `kill-rule-intake-kit`), which shifted every
> alphabetically-later decision up by one: Kill-Rule D7→D8, Membership D8→D9,
> Merge-Wall D9→D10, Multi-Agent D10→D11, Owner-Click Queue D11→D12, Pagination
> D12→D13, Photo Packs D13/D14→D14/D15, Rate-Limit D15→D16, Shopify D16→D17, Slack
> D17→D18, Template Pack D18→D19, and the book/keyword decisions D19–D25→D20–D26.
> The numbers below reflect the post-insert queue. (The Pagination Test Kit — added
> earlier the same day at what was then D12 — is now D13, and the Rate-Limit Test
> Kit is now D16.)

---

## Positioning by product

### Developer tools — webhook verifier kits

The four webhook kits share one shape: they sign **real-shape** provider payloads
with that provider's actual HMAC scheme and fire them over HTTP at your local
endpoint — true-pass plus the tamper / wrong-secret / replay-or-malformed
rejection cases — with **no vendor account, no app install, no tunnel, stdlib
only.** The buy-vs-DIY angle is the same across all four and it is strong: the
DIY path is to read the vendor's signature docs and hand-author fixtures from
memory, which is the exact path that produces a green suite that still drops the
first real delivery (see *The False-Green Test Trap*). Each kit ships the correct
scheme and the failing cases already written.

**Stripe Webhook Test Kit — $29 · LIVE**
([listing](stripe-webhook-test-kit/LISTING.md) ·
[packet](../publishing/vetting/stripe-webhook-test-kit.md))
- **Who it's for:** developers wiring Stripe Checkout webhooks into a backend.
- **The problem:** on a real `checkout.session.completed`, top-level
  `customer_email` is `null` (the address is in `customer_details.email`), forged
  events are accepted if you skip verification, and `success_url` only expands
  `{CHECKOUT_SESSION_ID}` — each silently drops or leaks a sale.
- **Buy vs DIY:** vs. hand-writing a payload from memory that says `customer_email`
  is populated — the exact fixture bug that would have dropped this lab's own
  first sale. The kit vendors the real shape and lints the `success_url` trap.
- **Cross-sell:** Webhook Verifier Bundle · The False-Green Test Trap.

**GitHub Webhook Test Kit — $29 · READY (D5)**
([listing](github-webhook-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/github-webhook-test-kit.md))
- **Who it's for:** developers building a GitHub App / webhook receiver.
- **The problem:** the `ping` your handler 500s on, the signature that "never
  validates" because the delivery is form-encoded, the forged POST your endpoint
  silently accepts, the legacy SHA-1 header, replays.
- **Buy vs DIY:** vs. standing up a real GitHub App + tunnel just to exercise six
  gotchas. The kit fires them locally with the exact `X-Hub-Signature-256` scheme
  and full header set.
- **Cross-sell:** Webhook Verifier Bundle · The False-Green Test Trap.

**Slack Webhook Test Kit — $29 · READY (D18)**
([listing](slack-webhook-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/slack-webhook-test-kit.md))
- **Who it's for:** developers building a Slack app / Events API endpoint.
- **The problem:** the `url_verification` challenge you never answer (so Slack
  silently delivers nothing), the form-encoded signature that "never validates,"
  and the replayed request you re-process because you checked the signature but
  never the clock.
- **Buy vs DIY:** vs. a real Slack app + workspace + tunnel to reproduce the
  challenge and the 5-minute replay window. The kit signs the real
  `v0:{timestamp}:{body}` basestring locally.
- **Cross-sell:** Webhook Verifier Bundle · The False-Green Test Trap.

**Shopify Webhook Test Kit — $29 · READY (D17)**
([listing](shopify-webhook-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/shopify-webhook-test-kit.md))
- **Who it's for:** developers building a Shopify app / webhook receiver.
- **The problem:** the signature that "never validates" because you hashed a
  re-serialised copy instead of the raw body, the hex digest you computed when
  Shopify sends **base64**, the 500 on a garbage signature header, the retry you
  process twice.
- **Buy vs DIY:** vs. a dev store + app install to learn base64-not-hex the hard
  way. The kit ships the real `X-Shopify-Hmac-Sha256` base64 scheme plus topic
  routing.
- **Cross-sell:** Webhook Verifier Bundle · The False-Green Test Trap.

### Developer tools — idempotency / safe-retry

The outbound companion to the inbound webhook kits: where those verify a
provider's signature on requests coming *in*, this kit verifies the safe-retry
contract of the writes your service sends *out*. Same kit shape (stdlib harness +
docs-derived fixtures + a correct/broken reference pair + byte-reproducible
bundle), different problem class — dedup, not signatures.

**Idempotency Key Test Kit — $29 · READY (D6)**
([listing](idempotency-key-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/idempotency-key-test-kit.md))
- **Who it's for:** developers building a `POST` endpoint (charges, orders,
  transfers) that clients retry — anyone who must guarantee a retried request
  can't run twice.
- **The problem:** a network timeout isn't a failure, it's an *unknown* — the
  client retries, and without idempotency the customer is charged twice. The bug
  is invisible in a green unit-test suite, which never fires two concurrent
  same-key requests.
- **Buy vs DIY:** vs. reading Stripe's idempotency docs and hoping your endpoint
  matches. The kit points at your endpoint and proves five properties (replay =
  exactly once, same-key/different-body → 409/422, per-key scoping, concurrent
  in-flight lock, missing-key policy) — including the concurrency case a
  from-memory test skips — and ships a correct/naive reference pair that proves
  the checks catch a broken implementation.
- **Cross-sell:** any webhook kit (the inbound half of the same integration) ·
  The False-Green Test Trap · Membership-Site Boilerplate Kit.

### Developer tools — rate-limit / throttling

The server-emitting-429 half of API robustness — the pair to the idempotency
kit's safe-retry half. Same kit shape (stdlib harness + docs-derived templates +
a correct/broken reference pair + byte-reproducible bundle), a third problem
class: throttling correctness, not signatures and not dedup.

**Rate-Limit Test Kit — $29 · READY (D16)**
([listing](rate-limit-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/rate-limit-test-kit.md))
- **Who it's for:** developers who hand-rolled a rate limiter (or middleware) on
  a `POST`/`GET` endpoint and need to prove it throttles correctly.
- **The problem:** the `count <= limit + 1` off-by-one that lets your "100/hour"
  pass 101; the 429 that ships with no `Retry-After` so clients hammer or give up;
  the `X-RateLimit-Remaining` stuck at the limit and the `Reset` timestamp already
  in the past; the window that quietly never reopens. None show up in a green
  unit-test suite, which never crosses the boundary or waits out a window.
- **Buy vs DIY:** vs. reading RFC 6585 / the RateLimit draft and hoping your
  limiter matches. The kit points at your endpoint and proves six properties
  (2xx under the limit, 429 at limit+1, a valid Retry-After, consistent
  RateLimit-* headers, the window resets, and the advertised Retry-After is
  honoured) — including the boundary and reset a from-memory test skips — and
  ships a correct/naive reference pair that proves the checks catch a broken
  limiter. Honest: the RateLimit-* header spec is an IETF draft (not an RFC), and
  those headers are optional; the 429 + Retry-After half rests on stable RFCs.
- **Cross-sell:** Idempotency Key Test Kit (the safe-retry half of API
  robustness) · Pagination Test Kit (the result-set-integrity half) · any webhook
  kit · The False-Green Test Trap.

### Developer tools — pagination / result-set integrity

The result-set-integrity rung of API robustness — the pair to the idempotency
kit's safe-retry half and the rate-limit kit's throttling half. Same kit shape
(stdlib harness + docs-derived templates + a correct/broken reference pair +
byte-reproducible bundle), a fourth problem class: pagination correctness, not
signatures, not dedup, and not throttling.

**Pagination Test Kit — $29 · READY (D13)**
([listing](pagination-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/pagination-test-kit.md))
- **Who it's for:** developers who hand-rolled pagination (or an offset-based
  endpoint) over a list/collection and need to prove it doesn't drop or repeat
  rows.
- **The problem:** `LIMIT n OFFSET k` looks fine in every test until a row is
  inserted/deleted between page fetches and the offset window shifts — silently
  **skipping** or **duplicating** rows in every export, sync, and "load more"
  scroll; the cursor a client can forge; the garbage cursor coerced to page 1
  instead of a 400; the unbounded `?limit=100000`. None show up in a green
  unit-test suite, which never mutates the dataset mid-traversal.
- **Buy vs DIY:** vs. reading a keyset-pagination blog post and hoping your
  endpoint matches. The kit points at your endpoint and proves six properties
  (no overlap/gap, stable under mid-traversal mutation, a consistent order, a
  clamped page size, a terminal signal, a rejected forged cursor) — including the
  mutation and forged-cursor cases a from-memory test skips — and ships a
  correct/naive reference pair that proves the checks catch a broken offset pager.
  Honest: there is no single RFC for cursor pagination; the model is the
  keyset/cursor pattern (Stripe/Slack/GitHub cursor docs + the keyset-vs-offset
  literature), and the stability check SKIPs on a read-only endpoint (run it
  against a seeded, mutable test dataset).
- **Cross-sell:** Idempotency Key Test Kit (safe-retry) · Rate-Limit Test Kit
  (throttling) · JWT Auth Test Kit (auth) · any webhook kit · The False-Green Test
  Trap.

### Developer tools — JWT auth / verifier security

The highest-severity rung of API robustness — where the idempotency, rate-limit,
and pagination kits catch correctness bugs, a failure here is a **security
incident** (auth bypass). Same kit shape (stdlib harness + docs-derived fixtures +
a correct/broken reference pair + byte-reproducible bundle), a fifth problem class:
JWT verifier security, not signatures, dedup, throttling, or pagination.

**JWT Auth Test Kit — $29 · READY (D7)**
([listing](jwt-auth-test-kit/listing-copy.md) ·
[packet](../publishing/vetting/jwt-auth-test-kit.md))
- **Who it's for:** developers who hand-rolled JWT verification (or wired a JWT
  library with defaults) on a protected endpoint and need to prove it can't be
  bypassed.
- **The problem:** the verifier reads the algorithm from the token and honours
  `alg:none`, so anyone mints an admin token; it HMACs an HS256 token against an
  identity provider's **public** key (RS256→HS256 algorithm-confusion — and the
  public key is public); it never checks `exp`, so a leaked token is valid forever;
  it never checks `aud`/`iss`, so a token minted for another service is accepted.
  None show up in a green unit-test suite, which only ever fires a valid token.
- **Buy vs DIY:** vs. reading RFC 8725 and hoping your configuration matches. The
  kit points at your endpoint and proves nine properties (accepts a valid token;
  rejects alg:none, a bad signature, algorithm-confusion, expired, not-yet-valid,
  wrong/missing `aud`, wrong/missing `iss`, and malformed) — including the
  `alg:none` and algorithm-confusion tokens a from-memory test skips — and ships a
  correct/naive reference pair that proves the checks catch a bypassable verifier.
  Honest: stdlib-only (HS256 + every attack class), and it does NOT do real
  RS256/ES256 signature-math verification — that's out of scope, stated plainly so
  nothing is overclaimed; the `aud`/`iss` properties SKIP if you configure no
  expected value.
- **Cross-sell:** Idempotency Key Test Kit (safe-retry) · Rate-Limit Test Kit
  (throttling) · Pagination Test Kit (result-set integrity) · any webhook kit · The
  False-Green Test Trap.

### Developer tools — starter

**Membership-Site Boilerplate Kit — $49 · READY (D9)**
([listing](membership-kit/listing-copy.md) ·
[packet](../publishing/vetting/membership-kit.md))
- **Who it's for:** indie builders / solo founders standing up a paid-membership
  site who want the loop wired, not a framework to learn.
- **The problem:** the checkout → webhook → grant → gated-access loop is fiddly
  to wire correctly, and the failure modes (reading the wrong email field, a
  misconfigured deploy minting free memberships, double-grant on retry) don't
  show up until real money moves.
- **Buy vs DIY:** vs. wiring it yourself and hitting the same Stripe gotchas in
  production. The kit ships the loop pre-wired, a loud MOCK-MODE that runs with
  **zero accounts**, HMAC verification that **fails closed** on a missing webhook
  secret, idempotent grants, and 36 tests against real-shape payloads. Honest
  v0.2: you still run the first live-Stripe purchase yourself.
- **Cross-sell:** Ship-It Bundle (+ Template Pack) · Stripe Webhook Test Kit (its
  webhook path is a Stripe path).

### Agent-ops tools & templates

**Agent-Workflow Template Pack — $19 PWYW · READY (D19)**
([listing](template-packs/listing-copy.md) ·
[packet](../publishing/vetting/template-packs.md))
- **Who it's for:** teams / solo devs running Claude Code or other agent sessions.
- **The problem:** every session logs, claims, and defines "done" differently, so
  parallel agents collide and quality drifts.
- **Buy vs DIY:** vs. reinventing session conventions per team. Drop-in Markdown +
  shell (constitution, session-log card, one-page playbook, three advisory
  fail-open hooks) you customize in place. Honestly conventions, not a policy
  engine.
- **Cross-sell:** Ship-It Bundle · Multi-Agent Control-Plane Pack · Owner-Click
  Queue Kit.

**Owner-Click Queue Kit — $19 · READY (D12)**
([listing](owner-click-queue-kit/listing-copy.md) ·
[packet](../publishing/vetting/owner-click-queue-kit.md))
- **Who it's for:** operators running autonomous coding agents who must keep
  spend / publish / account-creation human-gated.
- **The problem:** you have the "agent never spends" rule, but the actions only
  you can take pile up in chat scrollback, get asked twice, or quietly never
  happen.
- **Buy vs DIY:** vs. tracking owner-only actions by hand. A parseable
  **OWNER-GATE** grammar + one stdlib command that compiles every gate in your
  repo into a single prioritized queue — decisions-with-defaults first,
  click-runs second. (This repo's own OWNER-QUEUE is built with it.)
- **Cross-sell:** Multi-Agent Control-Plane Pack · Agent-Workflow Template Pack.

**Multi-Agent Control-Plane Pack — $29 · READY (D11)**
([listing](multi-agent-control-plane-pack/listing-copy.md) ·
[packet](../publishing/vetting/multi-agent-control-plane-pack.md))
- **Who it's for:** operators running 2+ concurrent agent sessions on one repo.
- **The problem:** the moment there's a second session, both pick up the same
  task, both append to the same status file (conflict), and one session's
  instructions vanish with its window.
- **Buy vs DIY:** vs. discovering the one-writer/merge-conflict failure class the
  hard way. Ships the coordination layer — one-writer inbox/status/outbox files,
  a one-file-per-claim ledger, born-red cards — with the production WHY behind
  each rule (150+ merged PRs coordinated through exactly these files).
- **Cross-sell:** Owner-Click Queue Kit · Agent-Workflow Template Pack · the
  merge-wall guides.

### Guides & cookbooks

**Agent Fleet Field Manual — $39 · READY (D1)**
([listing](agent-fleet-field-manual/LISTING.md) ·
[packet](../publishing/vetting/agent-fleet-field-manual.md))
- **Who it's for:** indie operators, platform engineers wiring agents into CI,
  and founders running an agent lane to produce sellable artifacts.
- **The problem:** agents overstate — they synthesize a payload from memory and
  call it a test, mark work done before it is, report "green" when the check
  never ran the code.
- **Buy vs DIY:** vs. learning each discipline by getting burned. Eleven chapters
  of mechanical disciplines (the D1 payment lesson, born-red work tracking, the
  six-field money protocol, merge-wall refusal, honest negative ledgering), every
  claim cited to a real commit/PR — two chapters free.
- **Cross-sell:** the whole agent-ops lane; strongest with Multi-Agent
  Control-Plane Pack and the merge-wall guides.

**The False-Green Test Trap — $15 · READY (D4)**
([listing](false-green-test-trap/listing-copy.md) ·
[packet](../publishing/vetting/false-green-test-trap.md))
- **Who it's for:** any developer who ships webhook/integration code and has
  watched green tests lie.
- **The problem:** a suite passes and the first real sale still fails, because
  memory-authored fixtures encode wrong beliefs (the real event carried
  `customer_email: null`; every test said otherwise).
- **Buy vs DIY:** vs. trusting green. A documented-incident guide (~8 pages) plus
  `vendor_fixture.py` — an offline stdlib tool that vendors real payloads, keeps
  the nulls, and writes a PROVENANCE stub. This is the *why* under every webhook
  kit above.
- **Cross-sell:** any webhook kit · Webhook Verifier Bundle · Agent Fleet Field
  Manual.

**The Agent Merge-Wall Cookbook — $19 · READY (D10)**
([listing](merge-wall-cookbook/listing-copy.md) ·
[packet](../publishing/vetting/merge-wall-cookbook.md))
- **Who it's for:** operators whose agent fleets open their own PRs and can't land
  them.
- **The problem:** the green PR that self-merge denies, auto-merge won't arm, and
  a human has to click at 3am.
- **Buy vs DIY:** vs. hitting each wall yourself and reconstructing the fix. Four
  runnable GitHub Actions recipes + the verbatim denial texts, from a repo whose
  fleet landed 13 agent PRs green in one night. Breadth pick (four recipes).
- **Cross-sell:** The Auto-Merge Enabler Cookbook (the depth companion) · Agent
  Fleet Field Manual.

**The Auto-Merge Enabler Cookbook — $19 · READY (D3)**
([listing](auto-merge-enabler-cookbook/listing-copy.md) ·
[packet](../publishing/vetting/auto-merge-enabler-cookbook.md))
- **Who it's for:** the same operators who want the single production workflow,
  annotated.
- **The problem:** the agent can't merge or even arm auto-merge from its own seat
  (policy denies it) — so how does a green PR land itself, safely?
- **Buy vs DIY:** vs. trial-and-error against the policy layer. The exact
  merge-on-green enabler this repo runs, annotated guard by guard, with the
  born-red HOLD that keeps it safe and **five citable `github-actions[bot]`
  merges** you can verify from the public API. Depth pick (one workflow, deep).
- **Cross-sell:** The Agent Merge-Wall Cookbook (breadth companion) · Multi-Agent
  Control-Plane Pack.

**Kill-Rule Intake Kit — $15 · READY (D8)**
([listing](kill-rule-intake-kit/listing-copy.md) ·
[packet](../publishing/vetting/kill-rule-intake-kit.md))
- **Who it's for:** indie builders / solo founders with an idea backlog and no
  intake discipline.
- **The problem:** side projects don't fail at launch, they fail at intake —
  because there never was one.
- **Buy vs DIY:** vs. building weak ideas to launch before finding there was no
  distribution path. A fillable intake with binding kill-rule fields + a
  distribution-first scoring rubric (distribution = 35%) + two brutally honest
  worked examples.
- **Cross-sell:** Agent Fleet Field Manual · Owner-Click Queue Kit.

### Writing kits

**AI Novella Production Kit — $29 · READY (D2)**
([listing](ai-novella-production-kit/listing-copy.md) ·
[packet](../publishing/vetting/ai-novella-production-kit.md))
- **Who it's for:** AI-assisted fiction writers who keep starting novels and never
  finishing.
- **The problem:** AI is great at starting; the graveyard is the middle — drift,
  then a new project. The gap is production structure, not prose.
- **Buy vs DIY:** vs. the 2,000-words-then-drift loop. The method behind 16
  finished manuscripts: declared length bands, series-bible CANON files, a
  promise manifest, dead-session recovery, and the gate between "written" and
  "publishable." Every word count an honest `wc -w` cited to a PR.
- **Cross-sell:** standalone (a distinct writing audience); a natural first pick
  for the broader book-catalog buyer.

---

## Bundles & cross-sell map

Two bundles roll singles into a discounted anchor. Both are **hard-gated**: a
storefront bundle references its component products as *existing live listings*,
so it cannot be created until those components are published.

**Ship-It Bundle — $59** ([listing](bundle-starter/listing-copy.md) ·
[packet](../publishing/vetting/bundle-starter.md))
- **Rolls up:** Membership-Site Boilerplate Kit ($49) + Agent-Workflow Template
  Pack ($19).
- **Discount math:** $68 separately → **$59** = **$9 off (~13%)**.
- **Angle:** the tested product layer plus the agent discipline that built it —
  product + process in one purchase.
- **Gate:** the Membership (D9) and Template Pack (D19) publish clicks.

**Webhook Verifier Bundle — $79** ([listing](webhook-verifier-bundle/listing-copy.md) ·
[packet](../publishing/vetting/webhook-verifier-bundle.md))
- **Rolls up:** Stripe + GitHub + Slack + Shopify Webhook Test Kits ($29 each).
- **Discount math:** $116 separately → **$79** = **$37 off (~32%)**.
- **Angle:** all four verifier kits for the developer wiring more than one
  provider — one download, three fewer checkouts.
- **Gate:** the GitHub (D5), Slack (D18), and Shopify (D17) publish clicks
  (Stripe is already LIVE).

**Cross-sell clusters (for storefront "you may also like"):**
- **Webhook cluster:** any webhook kit → the other three → Webhook Verifier
  Bundle → The False-Green Test Trap (the discipline behind them).
- **Membership cluster:** Membership Kit → Stripe Webhook Test Kit → Ship-It
  Bundle (+ Template Pack).
- **Agent-ops cluster:** Template Pack ↔ Owner-Click Queue Kit ↔ Multi-Agent
  Control-Plane Pack ↔ Agent Fleet Field Manual ↔ Merge-Wall / Auto-Merge Enabler
  cookbooks — all reinforce each other; the two merge cookbooks are
  breadth/depth siblings.

---

## Recommended publish order (advisory only)

> This is a suggestion to make the owner's publish clicks convert faster — it is
> **not** an instruction and the seat performs **no** publish. Every item below
> is an owner click queued in [`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md).
> Sequencing rationale: ride the one existing LIVE listing's account/precedent,
> lead with the highest-intent developer buyers, and unlock the bundles early.

1. **The three remaining webhook kits — GitHub (D5), Slack (D18), Shopify (D17).**
   Same Gumroad account and flow as the live Stripe kit, same buyer, lowest
   friction, and they unlock the Webhook Verifier Bundle. Highest leverage per
   click.
2. **Webhook Verifier Bundle** — once step 1 is done, one extra click turns four
   singles into a $79 anchor.
3. **Idempotency Key Test Kit (D6) + Rate-Limit Test Kit (D16) + Pagination Test Kit (D13) + JWT Auth Test Kit (D7)** —
   the same dev-tool buyer and Gumroad account as the webhook kits (four rungs of
   API robustness: safe retries + correct throttling + correct pagination + a secure
   JWT verifier — the last the highest-severity, an auth-bypass tier), so publish all
   four in the same visit; none gates the Webhook Verifier Bundle (that's the four
   signature kits), they're just the next high-intent dev-tool clicks.
4. **Membership-Site Boilerplate Kit (D9) + Agent-Workflow Template Pack (D19)** —
   the highest-price single plus its natural pair; unlocks the Ship-It Bundle.
5. **Ship-It Bundle** — once step 4 is done.
6. **The agent-ops guides & tools** — Agent Fleet Field Manual (D1), The Agent
   Merge-Wall Cookbook (D10), The Auto-Merge Enabler Cookbook (D3), Owner-Click
   Queue Kit (D12), Multi-Agent Control-Plane Pack (D11), Kill-Rule Intake Kit
   (D8), The False-Green Test Trap (D4). Lower-friction content SKUs; publish as
   time allows.
7. **AI Novella Production Kit (D2)** — a distinct writing audience; publish under
   the writing-category note flagged in D2.

**Live-listing caveat:** the Stripe Webhook Test Kit is under a measurement kill
clock — T+7 funnel checkpoint **2026-07-19**, T+14 kill rule **2026-07-26** (≥1
organic sale OR ≥1 qualified inbound, else pause/delist). Distribution, not
catalog size, is the binding constraint; see
[`../current-state.md`](../current-state.md) and
[`stripe-webhook-test-kit/LAUNCH-LOG.md`](stripe-webhook-test-kit/LAUNCH-LOG.md).

---

## Provenance

Derived, not invented — no fabricated metrics or testimonials. Sources as of
`main@aee9a08`:

- Prices, publish status, queue decision numbers (D1–D26) —
  `docs/publishing/OWNER-QUEUE.md` (generated queue; decision numbers reflect the
  2026-07-18 JWT Auth Test Kit insert at D7, which shifted the later product
  decisions up by one — see the sourcing note under the comparison table).
- LIVE-SKU fact + kill clock + lane scope —
  `docs/current-state.md@df75b72` (2026-07-17 restamp; its "10 READY" list
  predates the Slack/Shopify/Auto-Merge-Enabler packets, so status here follows
  OWNER-QUEUE).
- Per-SKU positioning (buyer · value · DIY angle) — each product's listing copy
  under `docs/launch/<sku>/@aee9a08`.
- Bundle discount math — `docs/launch/bundle-starter/listing-copy.md@aa04700`
  and `docs/launch/webhook-verifier-bundle/listing-copy.md@aee9a08`.
