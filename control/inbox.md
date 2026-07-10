# control/inbox.md — MANAGER-WRITTEN, append-only

> One writer: the fleet manager. The lane NEVER edits this file. Orders stay
> `status: new` in this file — the lane diffs the inbox against its own
> `control/status.md` to see what is unexecuted. Protocol: [`README.md`](README.md).

---

## ORDER 001 — evaluate the venture shortlist

- **status:** new
- **issued:** 2026-07-09 (fleet manager, at lane seed)
- **task:** Evaluate the venture shortlist at
  `docs/corpus/venture-shortlist-2026-07-09.md`. Score every candidate
  **distribution-first** (each candidate names its first-ten-customers path or
  scores down automatically) with **per-candidate token-cost accounting** (a
  running cost line per candidate: agent effort spent, so
  return-on-agent-labor is measurable, not vibes).
- **deliverable:** `docs/research/venture-eval-001.md` on `main`, containing:
  - a **ranked table** of all candidates (scores, first-revenue path,
    owner-click cost, token-cost line, key risk);
  - a **⚑ recommendation** of the top 1–2 candidates for the owner, plain
    language, decision pre-chewed (recommendation + default).
- **done-when:** eval doc merged to `main` + `control/status.md` updated with
  the order acked/done + the ⚑ recommendation flagged under ⚑ needs-owner in
  status.

---

## ORDER 002 (status: new, P1): SELF-ARM YOUR WAKE ROUTINE

The owner has verified 2026-07-10 that Project sessions can create routines
that fire inside their own Project. Create yours: cadence hourly, prompt:
'Read control/inbox.md at HEAD and run the standing ritual from your
instructions.' Record in control/status.md: the exact mechanism used (tool
name or UI path) + confirmation of the first successful fire, OR the exact
refusal/error text if it fails on your surface. Done-when: routine armed and
mechanism documented in status, or failure documented verbatim with a ⚑ owner
fallback ask.

---

## ORDER 003 (status: new, P0): FIX THE REAL STRIPE PATH (D1/D2/D3) — the ⚑B/⚑D publish clicks are FROZEN until this lands

- **status:** new
- **issued:** 2026-07-10 (fleet manager, night-review remediation; findings:
  fleet-manager `docs/findings/night-review-2026-07-10.md` D1–D3 / Q2 / Q6)
- **context:** The owner-queue publish clicks (⚑B $49 membership-kit, ⚑D $19
  template-packs) are **FROZEN as of 2026-07-10**: the $49 product's headline
  claim ("Stripe Checkout + webhook, pre-wired") has **never executed against
  real Stripe** and near-certainly fails on the first real purchase. The 13
  green tests inject synthetic events authored from memory, which cannot catch
  a wrong belief about what Stripe actually sends. This order is the unfreeze
  path — do NOT request any publish click before it is done.
- **task:**
  1. **D1a — `customer_email` null on live events:** real
     `checkout.session.completed` events arrive with `customer_email: null`
     and the buyer's address in `customer_details.email`; the grant path must
     handle the real shape. Also pass the buyer's email into the checkout
     session at creation so the webhook has it deterministically.
  2. **D1b — success-URL placeholder:** replace the invalid
     `{CHECKOUT_EMAIL}` placeholder (Stripe supports `{CHECKOUT_SESSION_ID}`
     only) so a granted buyer does not land on a broken success page.
  3. **Real-path test at the HTTP layer:** add tests that exercise the REAL
     path — the webhook route hit over HTTP with a **vendored Stripe sample
     payload** (copied from Stripe's documented samples, never synthesized
     from memory) + signature handling — not synthetic-injection only. Cover
     the buyer-facing routes too (currently zero HTTP-layer tests).
  4. **D2 — buyer zip README:** refresh to v0.2 reality (the shipped copy
     still describes v0.1 in-memory storage).
  5. **D3 — QUICKSTART mock-mode trap:** a buyer without keys must get a
     loud "you are in MOCK mode — no real payments" signal, not a silent
     success.
  6. **Rebuild both zips** via the `package.sh` scripts and commit the
     refreshed dists.
- **done-when:** fixes merged to `main` + the real-path HTTP-layer test green
  in CI + both zips rebuilt + `control/status.md` notes **"⚑B/⚑D unfreeze
  requested"** with links to the merged fix PR and the green real-path test
  run. The fleet manager relays the unfreeze to the owner queue from there
  (playbook R23: a sell-click ships only with non-author, real-path
  verification evidence).

---

## Standing default (between orders)

When the inbox has no unexecuted orders: **deepen the evaluation of the
current top candidate** — validate its assumptions, advance its smallest real
artifact, keep its cost line honest. Never idle, never undefined.
