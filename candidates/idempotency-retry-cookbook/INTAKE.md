# The Idempotency & Retry Cookbook — intake

> *Retry API calls without double-charging, duplicating side effects, or turning a
> blip into an outage: idempotency keys, backoff + jitter, retry budgets, circuit
> breakers, Retry-After, and consumer dedup — taught, cited, and shipped with
> small self-tested runnable recipes.*

## What it is
A ($19) guide-shaped cookbook for developers who call APIs that mutate state
(charges, orders, messages) and retry on failure. Eight chapters teach the
safe-retry pattern stack; four stdlib recipes (`backoff.py`,
`idempotency_store.py`, `retry.py` + a 26-test `test_recipes.py` self-test) make
each pattern runnable and verifiable. Every chapter carries a Sources footer
citing the exact RFC / IETF draft / engineering source (RFC 9110, RFC 6585, the
IETF Idempotency-Key + RateLimit drafts, the AWS backoff-and-jitter blog, Google
SRE, gRPC retry throttling, Nygard's Circuit Breaker, Stripe's idempotency docs).
Evidence class: **hybrid** — runnable-and-self-tested recipes (26 tests, offline +
CI) + verified-by-citation prose.

**Product or funnel? PRODUCT.** Standalone $19 cookbook for a broad developer
audience (anyone integrating a paid/stateful API). No funnel dependency.

**Distinct from the Idempotency Key Test Kit ($29) and Rate-Limit Test Kit
($29).** Those TEST an endpoint you own over HTTP; this TEACHES the patterns and
ships reference recipes. Same teach-vs-test relationship the Merge-Wall /
Auto-Merge Enabler cookbooks have to their kits. Natural cross-sell: a client that
retries on 429 is exactly the client that needs idempotent writes, so the cookbook
sells the two kits and the kits' buyers want the cookbook.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3 | Broad, high-intent dev audience (bigger TAM than the agent-fleet cookbooks — everyone integrating a paid API hits this), but the same owner-gated community + content funnel as the rest of the catalog; does not diversify channel risk. |
| Agent-buildability | 20% | 5 | Fully from public specs + committed companion-kit material; the recipes are stdlib and self-tested in-session. |
| Owner-click cost | 15% | 4 | One publish click. |
| Speed to first dollar | 15% | 4 | Guide + tested recipes authored in one session; no new runtime infra. |
| WTP / moat | 15% | 3 | Real, recurring pain with a wide audience, but the material is assembled from free public sources — the moat is the *curation + the tested recipes + the honest citation footers*, not secret knowledge. |
| **Weighted total** | | **3.75** | 0.35·D + 0.20·AB + 0.15·OC + 0.15·Sp + 0.15·WTP |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 30 days, ≥1 sale OR ≥30 reads from the developer
  audience. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) in-repo
  README badge + cross-links from the two companion kits — $0; (2) r/programming ·
  r/webdev · r/ExperiencedDevs · Hacker News (a "safe retries" explainer) ⚑; (3)
  Dev.to / a blog article seeding the guide ⚑; (4) Gumroad Discover ⚑. NOTE: same
  concentrated community funnel as the rest of the catalog — not diversifying.
- **Max agent-effort budget (at intake):** ~90k tokens to v0.1. CI/polling
  overhead ≤12k — do NOT sleep-poll CI; PR events wake the session. Over budget
  without the signal = ledgered negative.
- **Conservative revenue estimate:** $19 one-time. Conservative first-90-day: 0–4
  sales ($0–$76). Zero distribution = $0.
- **Payback-time estimate:** unverified until first sale; owner-gated distribution.
- **Token-cost line:** build est. 70–90k. Actuals: not measured until built.

## Why this might fail
The content is assembled from free, public, well-known sources — a motivated
developer can read the AWS blog, the SRE book, and the RFCs themselves. The bet is
that the *curation* (one coherent pattern stack), the *tested runnable recipes*,
and the *auditable citation footers* are worth $19 over the scattered free
originals — the same bet the other cookbooks make. It also shares the catalog's
one concentrated community/content channel, so distribution — not build — is the
binding constraint, and absent it the honest expectation is ~$0.
