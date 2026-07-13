**STATUS: CLICKED — LIVE (2026-07-12). Do NOT re-queue this click.**

> **Status:** `owner-guidance`

**This action was executed by the owner on 2026-07-12** — the $29 listing is
live at <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit> (HTTP 200
verified 2026-07-12T16:25:16Z, independently re-verified 16:28:47Z; owner test
purchase verified end-to-end 18:09:34Z). Durable record:
[`LAUNCH-LOG.md`](LAUNCH-LOG.md). The launch is in MEASUREMENT mode
(kill-clock checkpoints 2026-07-19 / 2026-07-26). This file stays as the
historical click-script. There is deliberately NO
`docs/publishing/vetting/` §7 packet for this product: the derive grammar
(`scripts/derive_owner_queue.py`) turns every `⚑ **Owner:**` checkbox into a
queued click and has no already-live/no-click disposition, so a packet here
would put a DUPLICATE publish click in front of the owner.

- **ARTIFACT (2026-07-13 catalog-parity verification):** the shipped bundle is
  `candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`
  @ sha256 `d3ac5f88620976c4dee15f70801eba5986faa47f4898a1a3bda4907336eeb0d8`
  (19,872 bytes, 10 files; byte-reproducible via `package.sh`, proven by
  unconditional double rebuild 2026-07-13T01:36:52Z — committed zip and both
  rebuilds identical). Matches the 2026-07-11 non-author verification sha
  (`d3ac5f88…eeb0d8`) and the 19.4 KB size observed on the live download page.
  If the source ever changes: rebuild, re-pin this line, and treat the live
  listing as STALE until the owner re-uploads.

This publish click was **earned**, not pre-queued. Both gate conditions now
hold; evidence below.

## Evidence (gates satisfied 2026-07-11)

1. **Real-path suite green IN CI on the built head SHA.** The
   `stripe-webhook-test-kit-tests` job ran the 14-test real-path HTTP suite
   green on PR head `b5b99cd`
   ([run 29137071195, job 86503253681](https://github.com/menno420/venture-lab/actions/runs/29137071195/job/86503253681)
   — "Ran 14 tests ... OK") and again on main at `fc7f39c`
   ([run 29137129185](https://github.com/menno420/venture-lab/actions/runs/29137129185)).
2. **Coordinator review via NON-AUTHOR adversarial verification (2026-07-11,
   independent worker):** suite green from the extracted zip ("Ran 14 tests in
   3.033s / OK"); forge-mode correctly fails an insecure handler; fixture
   shapes spot-verified against stripe-go @ master; success-URL lint
   confirmed; no secret values in repo or bundle; zip byte-reproducible
   (sha256 `d3ac5f88…eeb0d8`).

This satisfies the VERIFIED-WHEN's CI leg and playbook R23 (non-author
verification). The remaining VERIFIED-WHEN leg — the live listing URL
returning HTTP 200 — is the owner's click itself. Do not auto-publish or arm
auto-merge; the owner performs the click.

## Owner-action row (six-field grammar)

- **WHAT:** publish Stripe Webhook Test Kit v0.1 at $29 on a digital marketplace.
- **WHERE:** Gumroad or Lemon Squeezy (Discover).
- **HOW:** upload `candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`;
  paste the listing copy from `docs/launch/stripe-webhook-test-kit/LISTING.md`;
  set price $29.
- **WHY:** revenue-lane candidate #1 (eval-001, 2026-07-11); packages the lane's
  paid-for real-Stripe-path lessons into a sellable dev tool.
- **UNBLOCKS:** the first-ten-customers funnel (free gotcha article → free gist →
  StackOverflow answer → this listing → r/stripe).
- **VERIFIED-WHEN:** the live listing URL returns HTTP 200 AND the real-path HTTP
  test is green in CI on the built head SHA.

No secret values are involved in this action — the webhook signing secret is read
from an environment variable at test time and never stored in the repo or the
bundle. The owner performs the click.
