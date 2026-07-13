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

## Funnel top LIVE — free gotcha article published (2026-07-12)

The free gotcha article — the funnel top that feeds the $29 listing — is now
**live on dev.to**. The owner published it personally (owner click).

- **Article URL (live):**
  <https://dev.to/menno420/your-stripe-webhook-says-customeremail-is-null-heres-why-and-the-fix-1bgp>
- **Published:** **2026-07-12T17:18:47Z** by **menno420** (owner click, per the
  money protocol — no agent published, spent, or created an account).
- **Independent re-verification (this slice):** `curl -s -o /dev/null -w "HTTP
  %{http_code}"` → **HTTP 200 at 2026-07-12T17:24:10Z** (`date -u` fetch
  timestamp). Not proxy-blocked; the full article HTML rendered.
- **Product link present:** yes — `gumroad.com/l/stripe-webhook-test-kit`
  appears **2×** in the rendered article HTML (the article links through to the
  paid listing, so the funnel is wired end-to-end).
- **Tag state — CORRECTED (tags ARE live).** The 17:24:10Z fetch above
  observed zero `/t/<tag>` links and this log earlier recorded that as "ZERO
  tags." That fetch **raced the owner's edit**: the article's **four tags —
  `stripe`, `debugging`, `webhooks`, `payments` — went live at
  2026-07-12T17:24:24Z** (14 seconds after the racing fetch), verified via the
  dev.to API. The tags ARE present on the live article; the earlier zero-tags
  reading was a transient of the edit race, not the settled state. dev.to
  feed/tag-page discovery therefore applies as intended — no owner follow-up is
  needed on tagging.

---

## Funnel measurement — article → listing → sales

- **Funnel:** **dev.to article views → Gumroad listing visits → sales.**
- **Sources of truth:** dev.to's public **reactions / comments** (the only
  agent-visible article-engagement signal — the private view counter is
  owner-dashboard-only) + **Gumroad analytics** (owner-readable views/sales per
  product; the authoritative organic-sale / qualified-inbound signal — agent
  surfaces do NOT see sales).
- **Checkpoints (already armed by the coordinator, aligned to the kill clock):**
  **2026-07-19** (T+7 mid-window review) and **2026-07-26** (T+14 deadline —
  ≥1 organic sale OR ≥1 qualified inbound, else ledger ⚑E NEGATIVE +
  pause/delist).
- **Owner test purchase — VERIFIED 2026-07-12 (see the entry below).** The
  first end-to-end buyer-path test purchase is now complete; this row is
  **CLOSED.**

---

## Owner test purchase — VERIFIED end to end (2026-07-12)

The last open leg of the launch hour is closed: the owner personally completed
a **discounted test purchase** of the $29 Stripe Webhook Test Kit on Gumroad
(owner click, per the money protocol — no agent purchased or spent).

- **Timestamp (`date -u`):** **Sun Jul 12 18:09:34 UTC 2026**
- **What was verified:** the owner completed a discounted test purchase of the
  $29 Stripe Webhook Test Kit on Gumroad. The **success banner** was shown
  ("Your purchase was successful! We sent a receipt to the owner's email"). The
  **download page served the `stripe-webhook-test-kit-v0.1` ZIP** with a working
  **Download** button. The delivery pipeline — **checkout → receipt → download**
  — is verified **end to end**.
- **ZIP size observed:** **19.4 KB** (matches the listing's stated product size
  and the durable record above).
- **Owner privacy:** the receipt went to the owner's email; the address is
  deliberately **not recorded here**.

**Launch hour — COMPLETE end to end.** All four legs are now done and recorded
on `main`: **⚑A PR #74** (kit verified against a real Stripe signing secret) ·
**⚑E PR #84** (the $29 Gumroad listing LIVE) · **article PR #85** (free gotcha
article LIVE on dev.to, funnel top) · **test purchase (this entry)**. With the
buyer path verified, the launch now moves into **MEASUREMENT mode**: the
coordinator watches Gumroad analytics + dev.to public engagement against the
kill clock at the two armed checkpoints — **2026-07-19 (T+7)** and **2026-07-26
(T+14)**, both armed coordinator-side.

---

## Catalog-parity verification — 2026-07-13 night run (ORDER 008 PRODUCT #4)

SWTK predates the packet-era pipeline (`docs/products/TEMPLATE.md`, PRs
#106/#108/#110); this entry brings it to catalog parity WITHOUT queueing a
duplicate click. All items executed 2026-07-13 ~01:36–01:38Z on branch
`claude/night-swtk-packet`:

- **Dist freshness (TEMPLATE.md stage-6 double rebuild):** committed
  `dist/stripe-webhook-test-kit-v0.1.zip` sha256
  `d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8`
  (19,872 B); `package.sh` run twice → both rebuilds byte-identical to the
  committed zip (same sha, 3× identical, 01:36:52Z). Matches the 2026-07-11
  non-author verification sha and the 19.4 KB size observed at the live
  download.
- **Test suite:** `python3 -m unittest test_http_realpath -v` from source →
  `Ran 14 tests in 3.028s / OK` (01:37:03Z); re-run from the zip extracted
  into a clean dir → `Ran 14 tests in 3.033s / OK` (01:37:19Z).
- **Bundle inspection:** 10/10 expected files (README, GOTCHAS, swtk.py,
  swtk.js, stub_handler.py, test suite, 3 fixtures + PROVENANCE), zero junk
  entries, zero empty files; secret-pattern scan (sk_live/sk_test/whsec_/keys)
  zero hits; every README-invoked command's file ships in the bundle, and
  buyer-side `python3 swtk.py list` + `node swtk.js list` both executed clean
  from the extracted copy (no pip/npm install — stdlib claim TRUE).
- **Listing parity:** all four gotcha claims map to named executed tests
  (null email → `test_checkout_fixture_has_null_top_level_email` /
  `test_resolve_email_prefers_customer_details`; forged →
  `test_forged_signature_rejected_by_correct_handler`; stale timestamp →
  `test_stale_timestamp_rejected`; success_url lint → `test_lint_*`); price
  $29 identical in `LISTING.md`, `publish-owner-action.md`, and the live page
  (`price_cents 2900`).
- **ARTIFACT sha line** pinned in
  [`publish-owner-action.md`](publish-owner-action.md), whose stale
  "QUEUED (2026-07-11)" header is flipped to **CLICKED — LIVE (2026-07-12)**.
- **No §7 packet, deliberately:** `scripts/derive_owner_queue.py`'s grammar
  parses §7 blocks into owner DECISIONS and click-run checkboxes only — every
  `⚑ **Owner:**` checkbox becomes a queued click, and a §7 with neither lands
  in the generated file's "Manual review" noise. There is no
  already-live/RECORD disposition, so a packet would either queue a DUPLICATE
  publish click for a live product or degrade the queue's "all inputs clean"
  hygiene. The already-live record lives here and in the flipped click-script
  instead.

---

*This log records the ⚑E launch event, the free gotcha-article publish (funnel
top, LIVE 2026-07-12), and the owner's end-to-end **test purchase** (VERIFIED
2026-07-12). The launch hour is **COMPLETE** — all four legs done — and the
launch is now in **MEASUREMENT mode** (checkpoints 2026-07-19 / 2026-07-26
armed coordinator-side).*
