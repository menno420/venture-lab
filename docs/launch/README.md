# Launch & distribution assets

> **Status:** `reference`

Zero-owner-click launch material for the sellable candidates. Everything here is committed in-repo; nothing is published externally. Publish steps are owner-only click-scripts; each script carries its own freeze state (the ⚑B/⚑D ORDER 003 freeze was lifted by PR #22, 2026-07-11, after the real-path gate landed via PR #16).

**Storefront-wide view:** [CATALOG.md](CATALOG.md) — the cross-SKU positioning & comparison catalog (comparison table, per-SKU buy-vs-DIY angle, bundle discount math, and an advisory recommended publish order). Complements the per-SKU listing copy below; prices/status derive from [OWNER-QUEUE.md](../publishing/OWNER-QUEUE.md).

## Membership-Site Boilerplate Kit — $49
- [One-pager](membership-kit/one-pager.md)
- [Listing copy](membership-kit/listing-copy.md)
- [Owner publish click-script (UNFROZEN 2026-07-11)](membership-kit/owner-actions.md)
- [README buy-section snippet](membership-kit/readme-buy-snippet.md)
- [Queue-parseable §7 packet → derived owner queue](../publishing/vetting/membership-kit.md)
- [Repeatable product path template](../products/TEMPLATE.md)

## Agent-Workflow Template Pack — $19 pay-what-you-want
- [One-pager](template-packs/one-pager.md)
- [Listing copy](template-packs/listing-copy.md)
- [Owner publish click-script (UNFROZEN 2026-07-11)](template-packs/owner-actions.md)
- [README buy-section snippet](template-packs/readme-buy-snippet.md)
- [Queue-parseable §7 packet → derived owner queue](../publishing/vetting/template-packs.md)

## Ship-It Bundle — $59 (HARD-GATED on ⚑B + ⚑D)
- [Listing copy (refreshed from `candidates/BUNDLE-LISTING.md`, catalog parity)](bundle-starter/listing-copy.md)
- [Owner bundle-creation click-script (HARD-GATED 2026-07-13)](bundle-starter/owner-actions.md)
- [Queue-parseable §7 packet → derived owner queue](../publishing/vetting/bundle-starter.md)

## Kill-Rule Intake Kit — $15
- [Listing copy](kill-rule-intake-kit/listing-copy.md)
- [Owner publish click-script (QUEUED 2026-07-13, no freeze applies)](kill-rule-intake-kit/owner-actions.md)
- [Queue-parseable §7 packet → derived owner queue](../publishing/vetting/kill-rule-intake-kit.md)

## The False-Green Test Trap — $15
- [Listing copy](false-green-test-trap/listing-copy.md)
- [Owner publish click-script (QUEUED 2026-07-13, no freeze applies)](false-green-test-trap/owner-actions.md)
- [Queue-parseable §7 packet → derived owner queue](../publishing/vetting/false-green-test-trap.md)

## The Agent Merge-Wall Cookbook — $19
- [Listing copy](merge-wall-cookbook/listing-copy.md)
- [Owner publish click-script (QUEUED 2026-07-13, no freeze applies)](merge-wall-cookbook/owner-actions.md)
- [Queue-parseable §7 packet → derived owner queue](../publishing/vetting/merge-wall-cookbook.md)

## Stripe Webhook Test Kit — $29
- [**OWNER LAUNCH HOUR** — atomic ~1h runbook (⚑A + ⚑E + first-sale verification)](OWNER-LAUNCH-HOUR.md)
- [One-pager](stripe-webhook-test-kit/one-pager.md)
- [Listing copy](stripe-webhook-test-kit/LISTING.md)
- [Publish owner-action (NOT-QUEUED)](stripe-webhook-test-kit/publish-owner-action.md)
- [Free gotcha article draft](stripe-webhook-test-kit/gotcha-article.md)

## Agent Fleet Field Manual ($39)
- [One-pager](agent-fleet-field-manual/one-pager.md)
- [Listing copy](agent-fleet-field-manual/LISTING.md)
- [Publish owner-action (NOT-QUEUED)](agent-fleet-field-manual/publish-owner-action.md)
- [Free chapter 1 — The D1 Lesson](agent-fleet-field-manual/chapter-01-the-d1-lesson.md)
- [Free chapter 2 — The 13 Green Tests Trap](agent-fleet-field-manual/chapter-02-the-13-green-tests-trap.md)

$39 one-time. Conservative first-90-day: 0–4 sales ($0–$156). Zero distribution = $0. Same saturated community funnel as membership-kit/template-packs — does not diversify channel risk.

## Cross-product
- [Funnel diagnostic — the one live listing (Stripe Webhook Test Kit, $29)](funnel-diagnostic.md) — DIST-3 / REV-2: an honest, repo-grounded read of *why the one LIVE listing has zero organic sales* ahead of the T+7 (2026-07-19) checkpoint and T+14 (2026-07-26) kill rule — separates traffic vs listing-copy vs price, names the cheapest owner-executed test of each, and states "not measured (owner-dashboard-only)" wherever the funnel is dark rather than inventing a number. Pairs with the MISC-3 kill-clock decision packet
- [Kill-clock decision packet — the one live listing (Stripe Webhook Test Kit, $29)](kill-clock-decision-packet.md) — MISC-3: a pre-written **keep / iterate / delist** decision packet for the **T+14 kill-clock call (2026-07-26)**, so the owner's decision is a two-minute read, not a cold re-derivation — the kill rule quoted verbatim from `LAUNCH-LOG.md`, the exact evidence to check (pointing at the funnel diagnostic's traffic/copy/price hypotheses), each option with its concrete consequences, and an owner-only action checklist. Consumes the DIST-3 funnel diagnostic; the decision is owner-only, never auto-executed
- [Cluster lead-magnet distribution playbook](DISTRIBUTION-PLAYBOOK.md) — the reusable recipe (teaching article → channel drafts → CATALOG funnel-top registration → owner paste-and-post) distilled from PR #243 and PR #246, so the next cluster magnet is fill-in-the-blank
- [Membership/boilerplate cluster lead magnet](membership-lead-magnet.md) — free top-of-funnel teaching article ("The seven things every paid-membership site gets wrong about Stripe webhooks and access control"), funnelling soft-and-honest to the Ship-It Bundle → Membership Kit + Stripe Webhook Test Kit → The False-Green Test Trap; channel drafts live in `distribution-drafts.md`
- [AI-Novella / writing-tools cluster lead magnet](ai-novella-lead-magnet.md) — free top-of-funnel teaching article ("How to run an AI-assisted novella production line without shipping slop"), teaching the honest craft-and-QA discipline (length bands, structure passes, the anti-slop repair loop, the promise manifest, CANON continuity, dead-session recovery, the publish gate) and funnelling soft-and-honest to the AI Novella Production Kit
- [Pre-EAP-read-only publish sprint plan](pre-eap-sprint-plan.md) — DIST-9: a one-page wind-down plan for the ~2 days of write access before the **2026-07-21 read-only cutover**, splitting **AGENT-LANDS-THESE** (repo work that needs the write seat, in priority order) from **OWNER-CLICKS-THESE** (publish clicks that survive the cutover — the webhook trio GitHub D6 / Slack D20 / Shopify D19 → Webhook Verifier Bundle unlock — batched into one pre-cutover session). Honest about what read-only means for autonomy (no repo landing; owner clicks still work) and about the real freeze/gate state (⚑B/⚑D unfrozen 2026-07-11; proofread/length-band/R5 owner-only); grounded in #254 and the live OWNER-QUEUE
- [Distribution drafts](distribution-drafts.md)
- [Distribution channels shortlist](distribution-channels.md)

Revenue numbers here are deliberately conservative (Q-0259.4: expect bad results, never overstate). Absent active distribution, assume low single-digit sales per month or $0.
