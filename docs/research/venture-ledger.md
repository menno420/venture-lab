# venture-ledger — running status of built venture candidates

> **Status:** `living-ledger`
>
> Honest running record of what the venture-lab lane has actually **built** per
> candidate (vs the ranked evaluation in
> [`venture-eval-001.md`](venture-eval-001.md)). Source code + merged work win
> over this file. One entry per candidate, updated as artifacts ship.

## Candidate #1 — Membership-Site Boilerplate Kit

- **Status:** `v0.2 artifact shipped + buyer zip packaged + distribution assets shipped (live payments/publish owner-gated)`
- **Artifact:** [`candidates/membership-kit/`](../../candidates/membership-kit/)
- **Shipped (date -u):** v0.1 Fri Jul 10 03:04:32 UTC 2026 (build session 1) ·
  v0.2 Fri Jul 10 2026 (landed under PR #7 — see attribution note below)

### What is REAL now (built, runs, tested)

- **Pluggable persistence (v0.2)** — `server/app.py` now defines a
  `MembershipStore` **ABC** with two concrete backends: `JsonFileStore`
  (default, atomic file-backed writes) and a `SupabaseStore` drop-in skeleton.
  Backend is chosen by config flip (`make_store`) with **no app rework** — the
  webhook/grant code is store-agnostic.
- **Persistence SURVIVES RESTART (verified)** — the JSON file store keeps
  members across a full process restart: a grant, drop-the-store, re-open the
  same file path → access still present. Covered by
  `test_access_survives_restart` + `test_grant_idempotent_across_restart`.
- **Membership-grant core** — `handle_purchase_event()` shared by both mock and
  real webhook paths, now writing through the pluggable store.
- **Mock end-to-end flow** — `POST /mock-purchase` grants access with **zero
  accounts/keys**; `/members` serves the gated page to members and returns
  **402** to everyone else. Verified live with curl (402 → purchase → 200).
- **Test suite** — `server/test_membership.py`, **13 tests**, all green with
  `python3 -m unittest -v`: the original 6 grant/deny/idempotent/normalize tests
  + 5 JSON-file persistence tests (restart-survival, fresh-path-empty,
  idempotent-across-restart, factory-default, atomic-no-temp-left) + 2 Supabase
  skeleton tests (interface-conformance, missing-keys-fail-fast). No network, no
  Stripe, deterministic.
- **Landing page** — `web/index.html` + `web/styles.css`, self-contained,
  styled from `design-tokens.json`, renders standalone. Hero + feature grid +
  $49 pricing CTA + footer.
- **Members stub** — `web/members.html`, the gated post-purchase view.
- **Marketplace copy** — `LISTING.md`, publish-ready for Gumroad/Lemon Squeezy.
- **Buyer bundle SHIPPED (packaging)** — `candidates/membership-kit/package.sh`
  assembles a clean, buyer-facing zip (top-level `QUICKSTART.md` + README +
  `server/` + `web/` + `design-tokens.json`; excludes seller `LISTING.md`,
  runtime `members.json`, and build cruft) into
  `candidates/membership-kit/dist/membership-kit-v0.2.zip`. Deterministic,
  idempotent, and **committed**, so the owner just downloads and uploads — the
  publish step (⚑B) no longer has an unbuilt dependency.
- **Distribution assets** — real captured
  [`docs/distribution/demo-transcript.md`](../distribution/demo-transcript.md)
  (the mock purchase→access loop, verbatim curl output), ready-to-paste
  [`docs/distribution/launch-posts.md`](../distribution/launch-posts.md) (Show
  HN / Reddit / Claude-Code-community, no fabricated metrics), and a
  [`candidates/BUNDLE-LISTING.md`](../../candidates/BUNDLE-LISTING.md) pairing
  this kit with candidate #2 at $59 (vs $68 apart).
- **Docs** — product `README.md` + `server/README.md` (run + wire-up).

### What is OWNER-GATED (documented, code-ready, NOT performed)

- **Live Stripe test-mode E2E** — `/create-checkout-session` + `/webhook` real
  paths exist behind `if STRIPE_SECRET_KEY:`; they need a Stripe account + test
  keys pasted into `server/.env`. No account created, no transaction run.
- **Discord invite delivery** — `_deliver_discord_invite()` returns the
  configured URL; the real Discord API call needs a bot token (owner).
- **Supabase-backed users** — the `SupabaseStore` skeleton conforms to the
  store contract and fails fast without keys; wiring its live query bodies +
  provisioning the project is owner-gated (⚑C). The `JsonFileStore` default
  already gives real cross-restart persistence with zero accounts.
- **Marketplace publish** — `LISTING.md` is ready; the publish click needs a
  marketplace account (owner).

### Token-cost line (honest)

Candidate #1 real spend so far: **eval ~9k tokens amortized** (from
`venture-eval-001.md`'s shared recon) **+ ≈ 1 build session** for the v0.1
artifact **+ ≈ part of a build session** for the v0.2 persistence increment
(store ABC + JSON file backend + Supabase skeleton + 7 new tests). No precise
build-token figure is claimed — the eval's "300–500k build est." was a
projection; the real number is "≈1.x focused build sessions," to be reconciled
once measured. Return-on-agent-labor stays a projection until the owner
publishes and the first sale lands.

**This session (packaging + distribution):** est. **≈ 40–70k tokens**
(candidate #1's share: `package.sh` + buyer `QUICKSTART.md` + the real demo
capture + launch posts + this ledger update). Rough, not metered — the durable
output is the committed `dist/*.zip` and the distribution assets, which turn the
remaining owner work into pure download-and-upload.

### Next increment

1. Owner wires Stripe test keys → run the live test-mode E2E (item ⚑A below).
2. Owner publishes `LISTING.md` to Gumroad/Lemon Squeezy (item ⚑B below).
3. Fill the `SupabaseStore` query bodies + provision the project; deliver real
   Discord invites (⚑C).
4. Add refund/cancellation webhooks, email receipts, and multi-tier pricing.

---

## Candidate #2 — Agent-Workflow Template Packs

- **Status:** `v0.1 publish-ready + buyer zip packaged (real drop-in pack + $19 PWYW listing; publish owner-gated)`
- **Artifact:** [`candidates/template-packs/`](../../candidates/template-packs/)
- **Shipped (date -u):** Fri Jul 10 2026 (build session, landed under PR #7)

### What is REAL now (built, runs)

- **Real drop-in pack** — `pack/` is an actual copy-in bundle: a project
  constitution (`CLAUDE.md.template`), advisory hooks (`hooks/` — agent-orient,
  post-edit-reminder, session-close-check scripts + `settings.template.json`), a
  session-card template (`session-card.template.md`), and a session-discipline
  playbook (`session-discipline.md`). Drop it into a repo and it works — not a
  slideware mock.
- **Marketplace copy** — `LISTING.md`, a **$19 pay-what-you-want** listing that
  **cross-sells the membership-kit** (candidate #1), turning the two candidates
  into a bundle funnel.
- **Buyer bundle SHIPPED (packaging)** — `candidates/template-packs/package.sh`
  assembles a clean buyer zip (top-level `QUICKSTART.md` + `README.md` +
  `INCLUDED.md` + the whole `pack/`; excludes seller `LISTING.md` and build
  tooling) into `candidates/template-packs/dist/template-packs-v0.1.zip`.
  Deterministic, idempotent, and **committed** — the publish step (⚑D) no longer
  has an unbuilt dependency.
- **Bundle listing** — [`candidates/BUNDLE-LISTING.md`](../../candidates/BUNDLE-LISTING.md)
  pairs this pack with the membership-kit at $59 (vs $68 apart), riding
  candidate #1's funnel.
- **Docs** — `README.md` (what/why/how to install), `INCLUDED.md` (manifest of
  every file in the pack).

### What is OWNER-GATED (documented, NOT performed)

- **Marketplace publish** — `LISTING.md` + `pack/` are ready; publishing the
  listing needs an owned marketplace account (⚑D below).

### Token-cost line (honest)

Candidate #2 real spend: **≈ 1 build session** (pack authoring + listing copy +
docs). Return-on-agent-labor pending publish + first sale (owner-gated).

**This session (packaging + distribution):** est. **≈ 15–25k tokens**
(candidate #2's share: `package.sh` + buyer `QUICKSTART.md` + the shared
`BUNDLE-LISTING.md` + this ledger update). Rough, not metered; the durable
output is the committed `dist/template-packs-v0.1.zip` and the bundle listing.

### Next increment

1. Owner publishes `LISTING.md` to Gumroad/Lemon Squeezy (item ⚑D below).
2. Expand the pack (more hooks, more templates) once the first listing validates
   demand.

---

## ⚑ needs-owner — six-field owner actions

None of these have been performed. Each is queued for one owner action.
(⚑A/⚑B/⚑C are candidate #1; ⚑D is candidate #2.)

### ⚑A — Create a free Stripe account + paste TEST keys

- **WHAT:** Create a free Stripe account and paste the **test-mode** secret +
  webhook signing secret into `candidates/membership-kit/server/.env`.
- **WHERE:** Stripe dashboard → Developers → API keys (`sk_test_…`) and
  Developers → Webhooks → signing secret; local file `server/.env` (copied from
  `server/.env.example`).
- **HOW:** Sign up at stripe.com (free), stay in test mode, copy `sk_test_…`
  into `STRIPE_SECRET_KEY` and `whsec_…` into `STRIPE_WEBHOOK_SECRET`;
  `pip install stripe`; `stripe listen --forward-to localhost:8000/webhook`.
- **WHY:** The real Stripe `/create-checkout-session` + `/webhook` paths are
  built but env-gated; without keys they cannot run a live (even test-mode)
  transaction, so the payment leg stays mock-only.
- **UNBLOCKS:** Live test-mode purchase → webhook → membership-grant E2E, the
  last unproven leg of the paid flow.
- **VERIFIED-WHEN:** `python3 app.py` prints `mode=stripe`, and
  `stripe trigger checkout.session.completed` grants a membership visible at
  `/members?email=…` returning 200.

### ⚑B — Create a marketplace account + publish the listing (one click)

- **WHAT:** Create a Gumroad **or** Lemon Squeezy account and publish the
  `LISTING.md` copy as a $49 product.
- **WHERE:** gumroad.com or lemonsqueezy.com → new product; source copy in
  `candidates/membership-kit/LISTING.md`; the **buyer file to upload is the
  committed** `candidates/membership-kit/dist/membership-kit-v0.2.zip`.
- **HOW:** Paste the title, tagline, description, bullets, FAQ, and $49 price
  from `LISTING.md`; upload `candidates/membership-kit/dist/membership-kit-v0.2.zip`
  as the product file; press Publish. (Re-build the zip anytime with
  `sh candidates/membership-kit/package.sh`.) Optionally paste the copy from
  `docs/distribution/launch-posts.md` into the channels afterward.
- **WHY:** Distribution is the whole thesis for candidate #1 — the listing is
  the first-ten-customers channel, and it cannot exist without an owned
  marketplace account (agents cannot create one). The buyer zip now exists and
  is committed, so this is pure download-and-upload.
- **UNBLOCKS:** A live, purchasable listing — the first-revenue path.
- **VERIFIED-WHEN:** The product has a public URL, the uploaded
  `membership-kit-v0.2.zip` downloads, and a test purchase completes checkout.

### ⚑C — (Optional) Supabase + Discord accounts for the full production stack

- **WHAT:** Create a Supabase project (persistent users/auth) and a Discord
  server + bot token (auto-mint invites on purchase).
- **WHERE:** supabase.com → new project → Settings → API (`SUPABASE_URL`,
  `SUPABASE_KEY`); Discord → Server Settings → Invites / Developer Portal → bot
  token → `DISCORD_INVITE_URL` in `server/.env`.
- **HOW:** Create the free Supabase project and paste its URL + key; create the
  Discord server, generate an invite (or bot token), paste `DISCORD_INVITE_URL`.
- **WHY:** v0.1 uses an in-memory store and a static invite URL; production
  needs a real DB and real invite delivery — both require owner-owned accounts.
- **UNBLOCKS:** Persistent membership across restarts + real invite-on-purchase.
- **VERIFIED-WHEN:** Members survive a server restart (Supabase) and a purchase
  delivers a working Discord invite.

### ⚑D — Publish the template-packs listing (candidate #2)

- **WHAT:** Publish `candidates/template-packs/LISTING.md` as a live product.
- **WHERE:** Gumroad **or** Lemon Squeezy → new product; source copy in
  `candidates/template-packs/LISTING.md`; the **buyer file to upload is the
  committed** `candidates/template-packs/dist/template-packs-v0.1.zip`.
- **HOW:** Create/sign in to the seller account, paste the listing copy, set
  pay-what-you-want with a **$19 suggested** price, upload
  `candidates/template-packs/dist/template-packs-v0.1.zip` as the product file,
  press Publish. (Re-build anytime with `sh candidates/template-packs/package.sh`.)
- **WHY:** An unlisted pack earns nothing — publishing is the whole
  first-revenue path for candidate #2, and it cross-sells the membership-kit.
  The buyer zip now exists and is committed, so this is pure download-and-upload.
- **UNBLOCKS:** Candidate #2's first revenue + the membership-kit bundle
  cross-sell.
- **VERIFIED-WHEN:** The live listing URL resolves and the uploaded
  `template-packs-v0.1.zip` downloads.
