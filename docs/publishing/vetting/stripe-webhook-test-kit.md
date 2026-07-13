# Title Vetting — Stripe Webhook Test Kit

> **Status:** `historical`
>
> First LIVE-product packet in the vetting directory — every §7 row uses the
> checked `- [x] ⚑ **Owner:** … — DONE <date>` disposition, so
> `scripts/derive_owner_queue.py` renders this product in the read-only
> "Live / completed" section of [`../OWNER-QUEUE.md`](../OWNER-QUEUE.md) and
> queues **ZERO** new clicks. Before this disposition existed the product was
> deliberately packet-less (see the rationale that used to live in the
> click-script) and the derived queue silently under-reported the catalog:
> the owner saw every queued click-run but not the one product actually
> earning. **Do NOT flip any row here back to `- [ ]` — the product is LIVE;
> re-queueing its publish click is the documented anti-pattern.**

**Title:** Stripe Webhook Test Kit · **Category:** digital product / dev tool ·
**Date live:** 2026-07-12 · **Date recorded here:** 2026-07-13

Product: [`candidates/stripe-webhook-test-kit/`](../../../candidates/stripe-webhook-test-kit/README.md)
(v0.1; buyer bundle `dist/stripe-webhook-test-kit-v0.1.zip`; launch assets in
[`docs/launch/stripe-webhook-test-kit/`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md)).

## 1. Built + verified (facts from the durable records)

- [x] **LIVE listing:** <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>
      — HTTP 200 verified 2026-07-12T16:25:16Z, independently re-verified
      16:28:47Z; owner test purchase verified end-to-end 18:09:34Z
      ([`LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md)).
- [x] **Price:** **$29 USD** (`price_cents 2900`, `currency_code usd`) —
      identical across `LISTING.md`, the click-script, and the live page.
- [x] **Artifact:** `dist/stripe-webhook-test-kit-v0.1.zip` @ sha256
      `d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8`
      (19,872 bytes, 10 files); byte-reproducible via `package.sh`, proven by
      unconditional double rebuild 2026-07-13T01:36:52Z (catalog-parity pass,
      PR #112); matches the 2026-07-11 non-author verification sha.
- [x] **Tests:** 14-test real-path HTTP suite green from source AND from the
      extracted zip (2026-07-13 parity pass: `Ran 14 tests … OK` both runs).
- [x] **Click-script:** [`publish-owner-action.md`](../../launch/stripe-webhook-test-kit/publish-owner-action.md)
      flipped **CLICKED — LIVE (2026-07-12)**; launch in MEASUREMENT mode,
      kill-clock checkpoints 2026-07-19 (T+7) / 2026-07-26 (T+14).

## 7. ⚑ OWNER-GATE — ALL EXECUTED (product live; nothing to click)

Every owner action below was performed **by the owner personally** on
2026-07-12 (no agent published, spent, or created an account). The rows are
checked + DONE-marked so the derive script records them read-only instead of
queueing duplicates. Post-click seat work (durable LAUNCH-LOG, ARTIFACT sha
pin, catalog parity) landed via PRs #74 / #112.

- [x] ⚑ **Owner:** Gumroad listing published at $29 (`price_cents 2900`) at
      <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>, HTTP 200
      verified twice — DONE 2026-07-12
- [x] ⚑ **Owner:** zip uploaded matching sha256 `d3ac5f88…eeb0d8` (19,872 B,
      19.4 KB shown on the live download page) — DONE 2026-07-12
- [x] ⚑ **Owner:** end-to-end test purchase verified (owner buy, delivery
      confirmed 18:09:34Z) — DONE 2026-07-12

---

**Verdict: LIVE — measurement mode.** The queue entry above is a record, not
a queue: signal bar is ≥1 organic sale OR ≥1 qualified inbound by 2026-07-26,
else ledger a NEGATIVE and pause/delist per the LAUNCH-LOG kill rule.
