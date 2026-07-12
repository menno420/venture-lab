# LAUNCH LOG — Stripe Webhook Test Kit ($29)

> **Status:** `historical`

**Launch date:** 2026-07-12. The $29 Stripe Webhook Test Kit went live on
Gumroad today — the flagship revenue candidate's first external listing. This
log is the durable, on-`main` record of the ⚑E launch: the verified facts, an
independent URL re-verification, evidence links, and the kill rule with concrete
dates.

---

## Verified facts (coordinator-attested)

- **Public listing:** <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>
- **Price:** **$29 USD** (`price_cents 2900`, `currency_code usd`).
- **Published state:** `is_published: true`, `is_compliance_blocked: false`; no
  review/draft flags. Product permalink `rigjeg`, native type `digital`.
- **Store / seller:** **Fleetwork Labs** / `mennomagic01.gumroad.com`, seller
  **Menno van Hattum** (Gumroad seller id `1473031465158`).
- **Owner-published:** the owner published the listing **personally** (owner
  click, per the money protocol). No agent published, spent, or created an
  account — agents plan and queue; the owner performs every click.
- **Coordinator verification:** HTTP 200 at **2026-07-12T16:25:16Z** — published,
  $29 USD, `is_published true`, `is_compliance_blocked false`, no review/draft
  flags.

---

## Independent URL re-verification (this launch-log slice)

Re-verified by this worker directly, independent of the coordinator's check:

- **Command:** `curl -sS -w "\nHTTP %{http_code}\n" "https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit"`
- **Fetch timestamp (`date -u`):** **2026-07-12T16:28:47Z**
- **HTTP status:** **200**
- **Price visible:** yes — `product:price:amount = 29.0`, `product:price:currency = USD`,
  and in the embedded product JSON `price_cents: 2900`, `currency_code: "usd"`.
- **Published state:** `is_published: true`, `is_compliance_blocked: false`,
  `gr:page:type = product`, `gr:environment = production`.
- **Store / seller confirmed in-page:** seller `Menno van Hattum`, subdomain
  `mennomagic01.gumroad.com`, product name "Stripe Webhook Test Kit — catch the
  gotchas before you ship", size 19.4 KB.
- **Result:** the live listing is a purchasable $29 published product page. The
  fetch was NOT proxy-blocked; the full product HTML/JSON rendered.

---

## Evidence links

- **Listing (live):** <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>
- **⚑A live verification — PR #74:** <https://github.com/menno420/venture-lab/pull/74>
  (merged ~2026-07-12T15:09Z): HTTP 200 against a real Stripe-issued webhook
  signing secret; forged event rejected HTTP 400; stale-timestamp event rejected
  HTTP 400; real-path suite `python3 -m unittest test_http_realpath -v` →
  14/14 green (exit 0). Card: `.sessions/2026-07-12-swtk-live-verification.md`.
- **Runbook:** [`docs/launch/OWNER-LAUNCH-HOUR.md`](../OWNER-LAUNCH-HOUR.md) — the
  atomic ~1-hour owner runbook consolidating ⚑A (Stripe keys) + ⚑E (publish the
  $29 kit) + first-sale verification (landed via PR #57).
- **Publish owner-action:** [`publish-owner-action.md`](publish-owner-action.md)
- **Listing copy:** [`LISTING.md`](LISTING.md)

---

## Kill rule (concrete dates)

- **T (listing-live)** = **2026-07-12T16:25Z** (first verification).
- **T+7 (checkpoint)** = **2026-07-19** — coordinator mid-window review.
- **T+14 (deadline)** = **2026-07-26** — **signal = ≥1 organic sale OR ≥1
  qualified inbound within 14 days of the listing going live.** No signal by
  T+14 → ledger ⚑E a **NEGATIVE** and **pause / delist** the product.
- **Effort cap:** cap further agent launch-support effort on this candidate at
  **~50k tokens** per the runbook. Exceeding that budget without a signal is a
  ledgered negative.

---

## Measurement plan

- **Source of truth:** Gumroad's own analytics — the owner-readable dashboard
  reports views and sales per product. The Routines/agent surfaces do NOT see
  sales; only the owner's Gumroad dashboard is authoritative for the
  organic-sale / qualified-inbound signal.
- **Cadence:** the coordinator checks the signal at **T+7 (2026-07-19)** and
  **T+14 (2026-07-26)**. A qualified inbound (a real prospect email/DM referencing
  the kit) also counts toward the kill-rule signal.
- **Effort discipline:** launch-support agent effort is capped at ~50k tokens
  (runbook). BASE CASE is **0 sales** until a distribution channel is wired (the
  free gotcha article → gist → StackOverflow answer → listing → r/stripe funnel
  is still owner-gated), so payback is INDEFINITE absent traffic. Revenue is
  neither projected nor promised.

---

*This log records the ⚑E launch event only. The owner still performs any first
test purchase and the free-gotcha-article publish (funnel top); those clicks stay
open and benefit the T→T+14 validation clock.*
