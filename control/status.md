# control/status.md — LANE-WRITTEN

> One writer: the venture-lab lane. Overwritten wholesale each session; this
> write follows a final inbox re-read at HEAD. Protocol: [`README.md`](README.md).

---

updated: 2026-07-10T03:13:29Z
status: green

- **timestamp:** 2026-07-10T03:13:29Z
- **phase:** session 1 COMPLETE — ORDER 001 shipped + both repo gaps closed +
  candidate #1 v0.1 artifact shipped
- **health:** green (quality floor now enforceable; CI live)
- **last-shipped PR:** #5 (candidate #1 membership-kit v0.1). This session also
  landed #2 (walking skeleton), #3 (ORDER 001 eval), #4 (substrate-kit + CI
  gate).
- **orders acked:** 001
- **orders done:** 001 (`docs/research/venture-eval-001.md` on main)
- **blockers:** none
- **repo gaps (both CLOSED this session by PR #4):** substrate-kit v1.6.0
  adopted, `python3 bootstrap.py check --strict` green; substrate-gate CI
  workflow live (PRs now get a pending check).
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
    invite (or bot token), paste `DISCORD_INVITE_URL`. · WHY: v0.1 uses an
    in-memory store and a static invite URL; production needs a real DB and real
    invite delivery — both require owner-owned accounts. · UNBLOCKS: Persistent
    membership across restarts + real invite-on-purchase. · VERIFIED-WHEN:
    Members survive a server restart (Supabase) and a purchase delivers a
    working Discord invite.
  - **minor observation (not blocking):** substrate-gate CI completes in ~5s,
    faster than an auto-merge arm attempt can bind, so the pending-window is too
    short to arm auto-merge; REST merge-on-green is the reliable lander. If the
    owner wants the arm-in-pending path to work, add a small deliberate
    delay/second job to the gate, or enable a required-check ruleset + repo
    "Allow auto-merge".
- **token-cost line (candidate #1):** eval ≈9k tokens amortized + ≈1 build
  session for the v0.1 artifact; live-revenue steps owner-gated (⚑A/⚑B).
  Return-on-agent-labor pending first sale.
- **next (standing default, between orders):** advance candidate #1 to v0.2
  (Supabase-backed persistence + real test-mode Stripe E2E once ⚑A lands)
  and/or prep candidate #2 (template packs) as the companion listing; keep the
  ledger honest.
