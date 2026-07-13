# Checkout Revamp

> Gate file written by the payments agent, session 2026-07-10. The
> revamp branch is built and tested; everything below is owner-only
> (live payment settings + a real spend).

Context for the human: the new checkout flow is merged behind a flag.
Turning it on requires touching the LIVE payment provider dashboard and
buying one real test order — both outside what agents may ever do.

## ⚑ OWNER-GATE — live checkout actions

**OWNER-ACTION — Enable the revamped checkout**
1. **Dashboard sign-in:** owner signs into the payment provider
   dashboard (agents hold no credentials for it — by design).
2. **⚑ Rollout scope:** **10% traffic canary** (default — the flag
   supports percentage rollout and the error budget covers it) or
   straight to 100% — owner's call.
3. **Webhook endpoint:** flip the endpoint to `/v2/webhook` in the
   dashboard; the old route stays live until the canary clears.
4. **Real test purchase:** one live $1 order to prove the full path
   (this is a real spend — owner-only, blocking everything below).

- [ ] ⚑ **Owner:** rollout scope set (**10% traffic canary** (default)).
- [ ] ⚑ **Owner:** webhook endpoint flipped to `/v2/webhook` in the
      live dashboard.
- [ ] ⚑ **Owner:** the $1 live test purchase — blocking: no expansion
      past the canary until this order shows paid AND delivered.
- [ ] Agent (post-click, no money moved): record order id + timestamp
      in `docs/launch-log.md`, then flip these rows DONE and re-derive.
