# venture-lab — next-session / succession brief

> **Status:** `reference`
>
> Resume pointer on `main` for the first venture-lab session of a fresh Project.
> Boot clean from this — do NOT re-derive lane state from PR archaeology.
> Written 2026-07-11 (ORDER 004, gen-2 archive ender). Authoritative live state: `control/status.md`; unexecuted orders: `control/inbox.md` (diff against status).

## Boot ritual
1. Land on origin/main HEAD; `python3 bootstrap.py check --strict` must be exit 0 before any push.
2. Read `control/inbox.md` at HEAD — orders stay `status: new`; diff against `control/status.md` `done=` lines to find what is unexecuted. A `new` ORDER outranks plans.
3. You NEVER edit `control/inbox.md` (manager-written). You overwrite `control/status.md` wholesale as the deliberate LAST step, after a final inbox re-read at HEAD.

## What is LANDED (on main)
- **PR #9** (`95b755b`, merged 2026-07-10T05:11:50Z): sellable buyer zips + distribution assets. Buyer zips: `candidates/membership-kit/dist/membership-kit-v0.2.zip`, `candidates/template-packs/dist/template-packs-v0.1.zip`. Plus `candidates/BUNDLE-LISTING.md` ($59), `docs/distribution/launch-posts.md`, `docs/distribution/demo-transcript.md`. Repeatable `package.sh` per candidate.
- **Kit v1.7.1** on main (#13 `ce22315`, #14 `7558cb2`) — kit-maintenance, not venture-lane work.
- **ORDER 001 eval:** `docs/research/venture-eval-001.md` — candidate #1 (membership-kit) flagship, #2 (template-packs) companion.

## What is FROZEN ❄️ (do NOT publish)
- **⚑B ($49 membership-kit)** and **⚑D ($19 template-packs)** publish clicks are FROZEN until ORDER 003 (real-Stripe-path fix) is MERGED with the real-path HTTP-layer test GREEN in CI. Do not request either click before that.
- **THE D1 LESSON (binding forever):** never claim a payment path works without EXECUTING it. The $49 kit's "Stripe pre-wired" headline had 13 green tests that injected synthetic events authored from memory. But real `checkout.session.completed` events carry **`customer_email: null`** — the buyer address is in **`customer_details.email`**. And the success-URL used an invalid **`{CHECKOUT_EMAIL}`** placeholder; Stripe supports **`{CHECKOUT_SESSION_ID}`** only. Test payment code against VENDORED real Stripe sample payloads at the HTTP layer — never payloads synthesized from memory.

## What ORDER 003 (P0) requires before unfreeze
1. **D1a:** the grant path reads the buyer email from `customer_details.email` (not `customer_email`, which is null on live events); also pass the buyer email into the checkout session at creation so the webhook has it deterministically.
2. **D1b:** replace the `{CHECKOUT_EMAIL}` success-URL placeholder with `{CHECKOUT_SESSION_ID}` (the only one Stripe supports).
3. **Real-path HTTP-layer test:** hit the webhook route over HTTP with a VENDORED Stripe sample payload (copied from Stripe's documented samples, never memory) + signature handling; add buyer-route HTTP tests (currently zero).
4. **D2:** refresh the buyer-zip README to v0.2 reality (file-backed store, not v0.1 in-memory).
5. **D3:** a keyless buyer must get a loud "MOCK mode — no real payments" signal, not silent success.
6. **Rebuild both zips** via `package.sh`; commit the refreshed dists.
- **Done-when:** fixes merged to main + real-path HTTP test green in CI + both zips rebuilt + status notes "⚑B/⚑D unfreeze requested" with links to the merged fix PR + green real-path run. The manager relays the unfreeze to the owner queue (playbook R23: a sell-click ships only with non-author, real-path verification evidence).
- **Prereq for live E2E (not for the merge):** ⚑A — owner pastes Stripe test keys (env names `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`).

## Landing / merge wall (re-verified 2026-07-11 — STILL UP)
- Self-merge is classifier-walled without genuine-user auth (PR #9 got two verbatim denials; re-verified again 2026-07-11 on the ORDER-004 PR — BOTH the REST self-merge AND the auto-merge arm were denied; the arm denial cites "substrate-gate not required," so the owner-noted "make required + enable auto-merge" change is not yet effective). See `docs/PLATFORM-LIMITS.md` and `control/status.md` BLOCKER. REFUSAL BRANCH: the first denial per path is terminal — never retry/reword; leave the PR READY+green, record the refusal verbatim in status + PLATFORM-LIMITS, ⚑ the owner. Done-when degrades to "PR open, READY, green."
- **Owner action still needed:** either merge ORDER-004-style PRs by hand (⚑ HOT click) OR complete the systemic fix (make substrate-gate a required check, or add a `GITHUB_TOKEN` merge-on-green workflow) so agent PRs land unattended.

## Routines (ORDER 002, armed from the coordinator seat)
15-min `send_later` pacemaker chain + 2-hourly cron failsafe ("venture-lab failsafe wake", cron `0 */2 * * *`, trig_01X1dw1L1Udgt8atzzNWEJic). Verbatim create-args in `control/status.md` ORDER-002 section.

## Standing default (between orders)
Deepen the current top candidate — validate its assumptions, advance its smallest real artifact, keep its token-cost line honest. Never idle undefined.
