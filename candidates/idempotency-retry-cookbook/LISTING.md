# Listing pointer (seller-side, NOT in the buyer bundle)

The storefront listing copy for this product lives at
[`docs/launch/idempotency-retry-cookbook/listing-copy.md`](../../docs/launch/idempotency-retry-cookbook/listing-copy.md);
the owner publish click-script at
[`docs/launch/idempotency-retry-cookbook/owner-actions.md`](../../docs/launch/idempotency-retry-cookbook/owner-actions.md);
the queue-parseable §7 packet at
[`docs/publishing/vetting/idempotency-retry-cookbook.md`](../../docs/publishing/vetting/idempotency-retry-cookbook.md).

Price: **$19 one-time** (precedent: the Merge-Wall Cookbook and the Auto-Merge
Enabler Cookbook both at the $19 guide rung — a cited-throughout,
runnable-recipe-shipping cookbook for a developer audience). `package.sh` excludes
this file, `INTAKE.md`, `dist/`, and itself from the buyer bundle.

Distinct from the **Idempotency Key Test Kit ($29)** and the **Rate-Limit Test
Kit ($29)**: those TEST an endpoint you own over real HTTP (PASS/FAIL on the
exactly-once / throttling contracts); THIS cookbook TEACHES the safe-retry
patterns (idempotency keys, backoff+jitter, retry budgets, circuit breakers,
`Retry-After`, consumer dedup) and ships small runnable reference recipes. Same
relationship the Merge-Wall / Auto-Merge Enabler cookbooks have to their kits —
natural cross-sell, non-overlapping scope.
