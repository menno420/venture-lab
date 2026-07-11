# Session — membership-kit /webhook fail-closed hotfix (owner-directed cross-repo)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 · high · membership-kit-stripe-failclosed-hotfix
- **session:** owner-directed hotfix dispatched from the superbot hub fleet-review
  session (superbot PR #1998). Not a routine wake — a live, owner-authorized
  cross-repo fix of a verified real-money publish-blocker found in that review.
- **stamp (date -u):** 2026-07-11T18:15:18Z

## What this fixes

A verified **fail-open** in `candidates/membership-kit/server/app.py`: the
`/webhook` handler verified the Stripe signature only when
`STRIPE_WEBHOOK_SECRET` was set. On a **partial config** — `STRIPE_SECRET_KEY`
set (real checkout live) but `STRIPE_WEBHOOK_SECRET` unset — the `else` branch
treated the request as *mock* and granted membership from **unsigned JSON**, and
because `_is_mock()` is False in that state the loud MOCK banner never fired
(silent fail-open). Any buyer who forgot the webhook secret would let anyone POST
an unsigned `checkout.session.completed` and mint free paid memberships.

Confirmed by an independent source-verified review (Codex PR #38 + the superbot
fleet review 2026-07-11, both against source) — this hotfix is the remediation
that PR only documented.

## Change

- **Fail CLOSED on partial config.** The `/webhook` no-secret path now splits:
  full mock (no keys at all) keeps the loud-warning grant (legitimate local/test
  path, unchanged); a partial/misconfigured deploy (real key set, webhook secret
  missing) returns **HTTP 400** and never grants. The signed path (both keys) is
  untouched and remains correct (timing-safe compare, 300s tolerance, raw-body-first).
- **Regression test** `test_webhook_partial_config_fails_closed`: sets
  `STRIPE_SECRET_KEY`, leaves `STRIPE_WEBHOOK_SECRET` unset, POSTs unsigned →
  asserts 400 + not granted. Full suite green (9 HTTP + 15 unit = 24 tests).
- **LISTING.md truth-fix:** the Discord "invite-on-purchase" copy now states it
  returns the configured invite URL (live Discord API send is a documented next
  step, matching `_deliver_discord_invite`); version corrected v0.1 → v0.2.

No owner action performed; no secrets touched; store/heartbeat untouched.

## 💡 Session idea

💡 The bug survived a 35/35-green suite + a 9/9 adversarial pass because a test
(`test_mock_mode_loud_warning`) *codified the fail-open as intended mock
behavior* — the assertion asserted the wrong thing for the money-live state.
Worth a kit-level lint for adopters that sell: "a handler that grants on an
unsigned request must be gated on a full-mock predicate, never on a single
missing-secret branch." An honest-coverage gap, not a false-green checker — but a
generative pattern the substrate-kit revenue-adopters could all trip.

## ⟲ Previous-session review

The v0.2 persistence session (candidate-01-v02) did clean seam work, but the
"signature path solid / ORDER 003 DONE" framing it and the lane inherited focused
on the *signed* path being correct and never audited the *unsigned* branch's
mode-gating — which is where the real-money hole was. Lesson carried into the
kit-idea above: for a sellable payment handler, the review target is "what does
the UNSIGNED path do in every key-config permutation," not just "is the signature
verifier correct."

## Run report

- **Did:** fixed the /webhook partial-config fail-open + regression test + 2
  LISTING overclaims · **Outcome:** shipped (24 tests green)
- **Run type:** `owner-directed cross-repo hotfix` (from superbot hub session)
- **⚑ Owner action:** none blocking; run a live Stripe test-key E2E before publish
  (⚑A) as already queued. The fail-open path is now closed regardless.
