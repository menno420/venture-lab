# Membership-Site Boilerplate Kit — Marketplace Listing

> Ready-to-publish copy for Gumroad / Lemon Squeezy. One publish click by the
> owner ships it. Nothing here has been published — see the ⚑ owner-action
> item in `docs/research/venture-ledger.md`.

---

**Title:** Membership-Site Boilerplate Kit — Auth, Payments & Gated Content, Wired

**Tagline:** Launch a paid membership site this weekend — the purchase→access flow is already built, tested, and runs with zero accounts.

## Description (≈120 words)

Stop re-wiring Stripe webhooks, gated routes, and invite-on-purchase from
scratch. This kit hands you the whole membership loop — checkout, webhook,
membership grant, gated content, and a Discord invite on purchase — already
connected and covered by tests. It ships in **mock mode**, so you clone it and
watch a purchase unlock the members area in one command, before you sign up for
Stripe, Supabase, or Discord. When you're ready, paste your test keys and the
same code goes live. Stdlib-only backend (no dependency hell), a styled landing
page driven by editable brand tokens, and a gated members stub. Built to be
readable, forkable, and extended by you — or by your coding agent. Skip the
boilerplate; ship the product.

## Feature bullets

- **Runs with zero accounts** — mock mode demonstrates the full purchase→access flow before you sign up for anything.
- **Stripe Checkout + webhook, pre-wired** — `/create-checkout-session` and a signature-ready `/webhook` handler that grants membership.
- **Invite-on-purchase** — Discord invite hook fires the moment a payment lands.
- **Gated content that actually gates** — a membership store with a tested access check; unpaid users get a clean 402.
- **Tested membership logic** — grant, deny, and idempotent-duplicate cases proven by a `unittest` suite that needs no network.
- **Stdlib-only backend** — `python3 app.py`, no pip install, no build step.
- **Brand tokens as data** — colors, fonts, and spacing in one JSON file the landing page consumes; rebrand by editing values.
- **Agent-buildable & documented** — clear READMEs and env markers so a coding agent (or you) can extend it in minutes.

## Who it's for

Indie hackers, solo founders, and coding-agent operators who want to sell
access — a paid community, a course, a members-only tool — without spending the
first week gluing Stripe to a gated route. If you'd rather extend a tested
starter than debug a webhook signature at midnight, this is for you.

## Launch price

**$49** (one-time, lifetime updates to the v0.x line).

## FAQ

**Q: Do I need a Stripe account to try it?**
No. Mock mode runs the entire purchase→access flow with zero accounts. Add your
test keys only when you're ready to charge real cards.

**Q: What's the stack?**
Stdlib Python backend (http.server), Stripe for payments, Supabase for
auth/DB, Discord for invites, and a static landing page styled from a JSON
token file. Integrations are env-gated so nothing breaks before you wire keys.

**Q: Is this production-ready?**
It's an honest **v0.1** — the membership-grant flow is real and tested; the
in-memory store, live-Stripe E2E, and Discord delivery are documented next
steps. You're buying a wired, readable head start, not a black box.

**Q: Can my coding agent build on it?**
Yes — that's the point. Clean structure, explicit env markers, and READMEs
written so an agent can extend the flow without reverse-engineering it.

## Why this over a free OSS starter

Free starters are common; **documented, tested, agent-buildable** ones are not.
Most free membership repos are undocumented, untested, and assume you already
have every account wired — you find out what's broken only after you've signed
up for four services. This kit inverts that: it **runs and proves itself in one
command with zero accounts**, ships a test suite that pins the grant/deny/
idempotency behavior, and is written to be extended by a human *or* a coding
agent. You're paying $49 to skip a weekend of webhook archaeology.
