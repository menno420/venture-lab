# control/status.md — LANE-WRITTEN

> One writer: the venture-lab lane. Overwritten wholesale each session; this
> write follows a final inbox re-read at HEAD. Protocol: [`README.md`](README.md).

---

updated: 2026-07-10T03:26:55Z
status: green

- **timestamp:** 2026-07-10T03:26:55Z
- **phase:** session 1 round 2 COMPLETE — candidate #1 advanced to v0.2
  (persistence) + candidate #2 built to publish-ready v0.1
- **health:** green
- **last-shipped PR:** #7 — carried **BOTH** candidate #1 v0.2 AND candidate #2
  due to a shared-tree merge race (see the worktree-race recipe in
  [`docs/capabilities.md`](../docs/capabilities.md)). This session also landed
  #2 (walking skeleton), #3 (ORDER 001 eval), #4 (substrate-kit + CI gate),
  #5 (candidate #1 v0.1), #6 (status heartbeat).
- **orders acked:** 001
- **orders done:** 001 (`docs/research/venture-eval-001.md` on main)
- **blockers:** none
- **⚑ needs-owner:**
  - **ORDER 001 recommendation:** build candidate #1 (membership-site
    boilerplate kit) as flagship + candidate #2 (template packs) as companion
    listing. Full reasoning: `docs/research/venture-eval-001.md`.
  - **⚑A — create free Stripe account + paste TEST keys**
    · WHAT: Create a free Stripe account and paste the **test-mode** secret +
    webhook signing secret into `candidates/membership-kit/server/.env`.
    · WHERE: Stripe dashboard → Developers → API keys (`sk_test_…`) and
    Developers → Webhooks → signing secret; local file `server/.env` (copied
    from `server/.env.example`). · HOW: Sign up at stripe.com (free), stay in
    test mode, copy `sk_test_…` into `STRIPE_SECRET_KEY` and `whsec_…` into
    `STRIPE_WEBHOOK_SECRET`; `pip install stripe`;
    `stripe listen --forward-to localhost:8000/webhook`. · WHY: The real Stripe
    `/create-checkout-session` + `/webhook` paths are built but env-gated;
    without keys they cannot run a live (even test-mode) transaction, so the
    payment leg stays mock-only. · UNBLOCKS: Live test-mode purchase → webhook →
    membership-grant E2E, the last unproven leg of the paid flow.
    · VERIFIED-WHEN: `python3 app.py` prints `mode=stripe`, and
    `stripe trigger checkout.session.completed` grants a membership visible at
    `/members?email=…` returning 200.
  - **⚑B — create marketplace account + publish the listing (one click)**
    · WHAT: Create a Gumroad **or** Lemon Squeezy account and publish the
    `LISTING.md` copy as a $49 product. · WHERE: gumroad.com or
    lemonsqueezy.com → new product; source copy in
    `candidates/membership-kit/LISTING.md`. · HOW: Paste the title, tagline,
    description, bullets, FAQ, and $49 price from `LISTING.md`; attach the kit
    zip; press Publish. · WHY: Distribution is the whole thesis for candidate #1
    — the listing is the first-ten-customers channel, and it cannot exist
    without an owned marketplace account (agents cannot create one).
    · UNBLOCKS: A live, purchasable listing — the first-revenue path.
    · VERIFIED-WHEN: The product has a public URL and a test purchase completes
    checkout.
  - **⚑C — (optional) Supabase + Discord accounts for the full production stack**
    · WHAT: Create a Supabase project (persistent users/auth) and a Discord
    server + bot token (auto-mint invites on purchase). · WHERE: supabase.com →
    new project → Settings → API (`SUPABASE_URL`, `SUPABASE_KEY`); Discord →
    Server Settings → Invites / Developer Portal → bot token →
    `DISCORD_INVITE_URL` in `server/.env`. · HOW: Create the free Supabase
    project and paste its URL + key; create the Discord server, generate an
    invite (or bot token), paste `DISCORD_INVITE_URL`. · WHY: v0.2 ships a real
    file-backed store that survives restart, but the production stack still
    wants a hosted DB + real invite delivery — both require owner-owned
    accounts. · UNBLOCKS: Hosted persistent membership + real
    invite-on-purchase. · VERIFIED-WHEN: Members survive a server restart via
    Supabase and a purchase delivers a working Discord invite.
  - **⚑D — publish the template-packs listing (candidate #2)**
    · WHAT: Publish `candidates/template-packs/LISTING.md` as a live product.
    · WHERE: Gumroad or Lemon Squeezy → new product; source copy in
    `candidates/template-packs/LISTING.md`, pack payload in
    `candidates/template-packs/pack/`. · HOW: Create/sign in to the seller
    account, paste the listing copy, set pay-what-you-want with a **$19
    suggested** price, upload the `pack/` as a zip, press Publish. · WHY: An
    unlisted pack earns nothing — publishing is the first-revenue path for
    candidate #2. · UNBLOCKS: Candidate #2's first revenue + the membership-kit
    bundle cross-sell. · VERIFIED-WHEN: The live listing URL resolves and a test
    download works.
  - **NOTE (not an owner action):** the kit's owner-action-fields checker
    expects the literal tokens `WHY-IT-MATTERS`/`VERIFIED-NEEDED`, whereas this
    ledger uses `WHY`/`VERIFIED-WHEN`. This is advisory-only and non-blocking
    (check --strict exits 0), and it belongs to **substrate-kit** — the
    coordinator is relaying it upstream; it is **not** fixed kit-side from this
    repo.
- **attribution note:** candidate #1 v0.2 landed under PR #7 (titled
  candidate-02) because of the shared-tree race;
  `.sessions/2026-07-10-candidate-01-v02.md` documents the v0.2 build.
- **token-cost lines:** candidate #1 ≈1.x build sessions (v0.1 + v0.2),
  candidate #2 ≈1 build session; return-on-agent-labor pending first sale
  (owner-gated).
- **next (standing default, between orders):** candidate #1 v0.3 — real
  test-mode Stripe E2E once ⚑A lands, or wire the `SupabaseStore` query bodies;
  keep the ledger honest; await owner clicks on ⚑A–⚑D for revenue.
