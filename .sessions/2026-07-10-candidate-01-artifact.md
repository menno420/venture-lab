# Session — candidate #1 membership-kit v0.1 artifact

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8[1m] · high · candidate-01-artifact
- **session:** venture-lab session 1 — build candidate #1's smallest real artifact
- **started (date -u):** Fri Jul 10 03:04:32 UTC 2026
- **completed (date -u):** Fri Jul 10 03:09:20 UTC 2026
- Delivered: `candidates/membership-kit/` v0.1 — a mock-demonstrable
  membership-site starter (landing page + gated members flow + Stripe-wired
  backend in mock + real modes + passing test suite) plus publish-ready
  marketplace listing copy. All live payment/account/publish steps queued as
  ⚑ owner actions; none performed.

## Purpose

Advance candidate #1 (recommended flagship from ORDER 001) from a shortlist
line to its smallest **real, runnable** artifact — the product the fleet sells.
Stop at every owner-click boundary (no accounts, no spend, no publish, no live
transactions).

## ⟲ Previous-session review

⟲ previous-session review: PR #4 adopted substrate-kit v1.6.0 + wired the
substrate-gate CI workflow, making `check --strict` an enforceable pre-push
floor and closing the two repo gaps flagged in session-001. This session is the
first to build *product* under that gate: the kit ships with a COMPLETE session
card + green `check --strict`, exercising exactly the CI gate PR #4 installed.

## 💡 Session idea

💡 The kit's real moat isn't the code — it's that the payment→access loop is
**demonstrable with zero accounts**. Mock mode routes a fake purchase through
the *same* `handle_purchase_event()` the real Stripe webhook uses, so the demo
proves production logic, not a throwaway path. That "runs before you sign up for
anything" property is both the sales hook (LISTING.md) and what lets an agent
build/test the whole flow with no owner in the loop.

## Log

- Synced to `origin/main` @ 9f028ee; branched `venture-lab/session-1-candidate-01`.
- Built `candidates/membership-kit/`: README, LISTING, design-tokens.json,
  web/{index.html,styles.css,members.html}, server/{app.py,.env.example,
  test_membership.py,README.md}.
- Proved it runs: `python3 -m unittest test_membership -v` → 6/6 OK; live curl
  mock flow → `/members` 402 (unpaid) → `/mock-purchase` grant → `/members` 200.
- Ledger: `docs/research/venture-ledger.md` (living-ledger badge) with the
  honest REAL-vs-owner-gated split, token-cost line (eval ~9k + ≈1 build
  session), next increment, and three six-field ⚑ owner-action items
  (Stripe test keys / marketplace publish / Supabase+Discord).
- Linked the ledger from read-path doc `docs/current-state.md` so it is
  reachable (orphan-free) under the gate.
- Drove `python3 bootstrap.py check --strict` to exit 0.

## Deliverable summary

A v0.1 membership-site boilerplate kit: mock-demonstrable end-to-end, tested,
with publish-ready listing copy and a rendered landing page. Nothing
owner-gated was performed — Stripe/marketplace/Supabase/Discord steps are
queued as ⚑ owner actions in the ledger.
