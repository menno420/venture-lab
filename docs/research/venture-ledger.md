# venture-ledger — running status of built venture candidates

> **Status:** `living-ledger`
>
> Honest running record of what the venture-lab lane has actually **built** per
> candidate (vs the ranked evaluation in
> [`venture-eval-001.md`](venture-eval-001.md)). Source code + merged work win
> over this file. One entry per candidate, updated as artifacts ship.

## Candidate #1 — Membership-Site Boilerplate Kit

- **Status:** `v0.1 artifact shipped (mock-mode demonstrable; live payments owner-gated)`
- **Artifact:** [`candidates/membership-kit/`](../../candidates/membership-kit/)
- **Shipped (date -u):** Fri Jul 10 03:04:32 UTC 2026 (build session 1)

### What is REAL now (built, runs, tested)

- **Membership-grant core** — `server/app.py`: in-memory `MembershipStore` +
  `handle_purchase_event()` shared by both mock and real webhook paths.
- **Mock end-to-end flow** — `POST /mock-purchase` grants access with **zero
  accounts/keys**; `/members` serves the gated page to members and returns
  **402** to everyone else. Verified live with curl (402 → purchase → 200).
- **Test suite** — `server/test_membership.py`, 6 tests, all green with
  `python3 -m unittest` (grant, deny-unpaid, idempotent-duplicate, email
  normalization, non-purchase-ignored, empty-email-rejected). No network, no
  Stripe, deterministic.
- **Landing page** — `web/index.html` + `web/styles.css`, self-contained,
  styled from `design-tokens.json`, renders standalone. Hero + feature grid +
  $49 pricing CTA + footer.
- **Members stub** — `web/members.html`, the gated post-purchase view.
- **Marketplace copy** — `LISTING.md`, publish-ready for Gumroad/Lemon Squeezy.
- **Docs** — product `README.md` + `server/README.md` (run + wire-up).

### What is OWNER-GATED (documented, code-ready, NOT performed)

- **Live Stripe test-mode E2E** — `/create-checkout-session` + `/webhook` real
  paths exist behind `if STRIPE_SECRET_KEY:`; they need a Stripe account + test
  keys pasted into `server/.env`. No account created, no transaction run.
- **Discord invite delivery** — `_deliver_discord_invite()` returns the
  configured URL; the real Discord API call needs a bot token (owner).
- **Supabase-backed users** — the in-memory store is the v0.1 stand-in; the
  persistent store needs a Supabase project (owner).
- **Marketplace publish** — `LISTING.md` is ready; the publish click needs a
  marketplace account (owner).

### Token-cost line (honest)

Candidate #1 real spend so far: **eval ~9k tokens amortized** (from
`venture-eval-001.md`'s shared recon) **+ ≈ 1 build session** for this v0.1
artifact (files + tests + mock-flow verification + landing page + listing copy).
No precise build-token figure is claimed — the eval's "300–500k build est." was
a projection; the real number is "one focused build session," to be reconciled
once measured. Return-on-agent-labor stays a projection until the owner
publishes and the first sale lands.

### Next increment

1. Owner wires Stripe test keys → run the live test-mode E2E (item ⚑A below).
2. Owner publishes `LISTING.md` to Gumroad/Lemon Squeezy (item ⚑B below).
3. Swap the in-memory store for Supabase; deliver real Discord invites (⚑C).
4. Add refund/cancellation webhooks, email receipts, and multi-tier pricing.
5. Prep candidate #2 (agent-workflow template packs) as a companion listing on
   the same funnel.

---

## ⚑ needs-owner — six-field owner actions (candidate #1)

None of these have been performed. Each is queued for one owner action.

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
  `candidates/membership-kit/LISTING.md`.
- **HOW:** Paste the title, tagline, description, bullets, FAQ, and $49 price
  from `LISTING.md`; attach the kit zip; press Publish.
- **WHY:** Distribution is the whole thesis for candidate #1 — the listing is
  the first-ten-customers channel, and it cannot exist without an owned
  marketplace account (agents cannot create one).
- **UNBLOCKS:** A live, purchasable listing — the first-revenue path.
- **VERIFIED-WHEN:** The product has a public URL and a test purchase completes
  checkout.

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
