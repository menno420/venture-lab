# ⚑ Owner queue — every decision and click, in one list

> GENERATED FILE — regenerate with `ocq.py derive`; edit the
> gate files, never this file. A stale copy of this file is a
> bug in the workflow, never in the gate files.

The agents performed NONE of the actions below — every item is an owner click or an owner choice, queued and pre-chewed. Decisions come first (each with a bolded default so “agree” is a one-word reply); the pure click-run sequences follow.

## 1. Decisions — pick the default or override

### D1 — Checkout Revamp — Rollout scope

- **WHAT:** ⚑ Rollout scope: 10% traffic canary (default — the flag supports percentage rollout and the error budget covers it) or straight to 100% — owner's call.
- **WHERE:** `gates/checkout-revamp.md` @ OWNER-GATE step 2
- **DEFAULT:** **10% traffic canary**
- **UNBLOCKS:** the entire remaining “Checkout Revamp” click-run — hard gate, nothing below it proceeds

## 2. Click-run — mechanical owner clicks, paste-ready

### Status Page — `gates/status-page.md` @ OWNER-GATE checklist

- [ ] **WHAT:** CNAME status → pages.example-host.net added at the registrar (TTL 300). · **UNBLOCKS:** the next click in this sequence
- [ ] **WHAT:** confirm https://status.example.com loads the committed page (VERIFIED-WHEN: the page shows build id 7f3a2). · **UNBLOCKS:** the next click in this sequence

### Checkout Revamp — `gates/checkout-revamp.md` @ OWNER-GATE checklist — **HARD-GATED** (a D-item above blocks this sequence)

- [ ] **WHAT:** rollout scope set (10% traffic canary (default)). · **DEFAULT:** **10% traffic canary** (executes its D-item above) · **UNBLOCKS:** the next click in this sequence
- [ ] **WHAT:** webhook endpoint flipped to /v2/webhook in the live dashboard. · **UNBLOCKS:** the next click in this sequence
- [ ] **WHAT:** the $1 live test purchase — blocking: no expansion past the canary until this order shows paid AND delivered. · **UNBLOCKS:** the next click in this sequence

## 3. Manual review — gate files the parser could not read reliably

*(none — every input parsed clean)*

## 4. Live / completed — already executed, read-only

Derived from checked `- [x] ⚑ **Owner:** … — DONE <date>` rows: owner actions ALREADY executed. Nothing here is queued, and nothing here counts toward the pending totals above.

### Newsletter Launch — `gates/newsletter-launch.md` @ OWNER-GATE checklist

- [x] newsletter created + welcome sequence pasted · **DONE:** 2026-07-08
- [x] signup form embedded on the site + test signup delivered · **DONE:** 2026-07-08
- ⏲ **Next checkpoint:** 2026-07-15 — T+7 funnel checkpoint (any organic signups?)
- ⏲ then: 2026-08-07 — T+30 kill-rule deadline (≥25 subscribers, else archive the sequence and stop linking it)
