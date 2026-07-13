# Kill-Rule Intake Kit — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-13, ORDER 008 night run, PRODUCT #7). No freeze applies: this
is a zero-runtime Markdown kit with no Stripe/payment-path dependency, so the
ORDER 003 gate (which froze ⚑B/⚑D and was lifted 2026-07-11 by PR #22) never
attached to it. Honest caveat: a live purchase of ANY catalog product besides
SWTK remains unverified — QUEUED means the owner may click, not that this
product's delivery is live-proven. This is a click-script for the owner, not a
request to any agent; no agent performs publish/spend/account actions.

### ⚑ — Publish the Kill-Rule Intake Kit at $15 (one-time)
- **WHAT:** Create a $15 one-time digital product on your own no-code
  storefront, selling `candidates/kill-rule-intake-kit/dist/kill-rule-intake-kit-v0.1.zip`,
  using `docs/launch/kill-rule-intake-kit/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $15), or
  lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "Kill-Rule
  Intake Kit". 4) Price = $15 one-time. 5) Upload the dist zip. 6) Paste the
  listing copy (Title / Short / Long / Bullets / FAQ). 7) Publish. 8) Copy the
  public product URL.
- **WHY:** Bottom-of-catalog price rung packaging the lane's intake
  methodology for indie builders (intake: `candidates/kill-rule-intake-kit/INTAKE.md`,
  scored 3.38 weighted). Conservative expectation: 0–3 sales in 90 days,
  $0–$45; zero distribution = $0 (Q-0259.4 framing — the kit's own WTP axis
  scored 2/5 and the listing says so).
- **UNBLOCKS:** First intake-kit sale; a natural cross-link from the Agent
  Fleet Field Manual (its chapter 8 teaches this discipline; the kit is the
  fillable version); a future methodology-tier bundle candidate.
- **VERIFIED-WHEN:** The public URL loads a purchasable $15 page and a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT
  line below.
- **ARTIFACT (verified 2026-07-13):** upload exactly
  `candidates/kill-rule-intake-kit/dist/kill-rule-intake-kit-v0.1.zip` @
  sha256 `53a840fd6b4f0860accecff8d2bbc16abeab06e1d2bb38e03251ca8993a770e5`
  (15,875 bytes; byte-reproducible via `package.sh` — double rebuild produced
  the identical sha; the committed dist IS that build). The kit ships no test
  suite (plain Markdown, zero runtime — the listing's honesty FAQ says so);
  verification ran from the extracted bundle instead: all 9 files non-empty
  valid UTF-8 with H1 headings and balanced code fences, the two worked
  examples' weighted-total arithmetic recomputed and matches the shipped
  numbers (3.55 / 3.10), rubric weights sum to 1.00, and a secret-pattern
  scan found zero hits — no `.DS_Store`, no `__pycache__`, no junk entries in
  the archive listing.

## Price precedent chain

$15 sits on the catalog's existing rungs, below the closest comparable:
Agent-Workflow Template Pack $19 PWYW (click-queued, PR #108) — a
drop-in scaffold, larger surface; SWTK $29 (live, PR #86); Agent Fleet
Field Manual $39 (click-queued, PR #110); Membership Kit $49 (click-queued,
PR #106). A pure-decision template kit is the smallest artifact in the
catalog and prices under all of them; $15 was set at intake
(`candidates/kill-rule-intake-kit/INTAKE.md`) and is recorded identically in
the listing copy, the §7 packet, and this script.
