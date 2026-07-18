# Webhook Verifier Bundle ($79) — owner bundle-creation click-script

> **Status:** `reference`
>
> **HARD-GATED (2026-07-18):** a Gumroad bundle is assembled FROM existing live
> products — it cannot be created while its component kits are unpublished. Of
> the four components only the **Stripe Webhook Test Kit** ($29) is LIVE; the
> **GitHub** ($29, OWNER-QUEUE **D5**), **Slack** ($29, **D14**), and
> **Shopify** ($29, **D13**) kits are queued publish clicks in
> [`OWNER-QUEUE.md`](../../publishing/OWNER-QUEUE.md). Those three publish clicks
> must be executed FIRST. Nothing below the blocking rows in the
> [§7 packet](../../publishing/vetting/webhook-verifier-bundle.md) proceeds until
> all four component products are live. This is a click-script for the owner,
> not a request to any agent; no agent performs publish/spend/account actions.
>
> This mirrors the existing **Ship-It Bundle** hard-gate precedent
> ([`../bundle-starter/owner-actions.md`](../bundle-starter/owner-actions.md)).

## Honesty section

- The bundle ships **no new product code** — it assembles four already-built,
  already-tested kits (67 component tests green: Stripe 14 + GitHub 18 + Slack
  18 + Shopify 17) plus a README / QUICKSTART / MANIFEST / PROVENANCE. The
  bundle's own test is an **assembly/inventory check**, not a fifth product.
- Only the **Stripe** kit is live today; the other three are queued owner
  clicks. Until they are published, a Gumroad bundle referencing them cannot be
  created by anyone, owner included — this is why the click-script is gated.
- The $116 separate-purchase total is the genuine sum of four $29 kits, not a
  manufactured anchor. **Never price at $116** (zero discount voids the bundle).
- The seat performed NONE of the steps below — every step is an owner click.

### ⚑ — Create the "Webhook Verifier Bundle" at $79 · HARD-GATED on GitHub (D5) + Slack (D14) + Shopify (D13)

- **WHAT:** Create a Gumroad **bundle** priced **$79** (one-time, fixed)
  combining the four live component kits — Stripe / GitHub / Slack / Shopify
  Webhook Test Kits ($29 each) — using the copy in
  [`listing-copy.md`](listing-copy.md). On Gumroad a bundle references the
  component products' existing uploads; if instead you upload a single file, use
  the reproducible bundle zip
  `candidates/webhook-verifier-bundle/dist/webhook-verifier-bundle-v0.1.zip`
  (sha256 `28f61d8a33309310640375581ff7a6d2f1320bc03bdecbbc1c08c83d5aaf26c8`,
  121,689 B) which contains the four component zips verbatim (each pinned in
  [`MANIFEST.json`](../../../candidates/webhook-verifier-bundle/MANIFEST.json)).
- **WHERE:** gumroad.com → *Products* → *New product* → *Bundle*, signed into
  the same account that published the four component kits.
- **HOW:** 1) Execute the GitHub (D5), Slack (D14), and Shopify (D13) publish
  clicks first — their own click-scripts; blocking. (Stripe is already live.)
  2) Sign in to the same Gumroad account. 3) New product → **Bundle**.
  4) Name = "Webhook Verifier Bundle — Stripe + GitHub + Slack + Shopify Test
  Kits". 5) Select the four live kits as the bundle contents (or upload the
  single reproducible bundle zip). 6) Price = **$79**, one-time, fixed.
  7) Paste Title / Short + Long / Bullets / FAQ from
  [`listing-copy.md`](listing-copy.md). 8) Publish. 9) Copy the public
  bundle URL.
- **WHY:** A higher-AOV price point over four kits at zero new build cost: $79
  removes three checkout decisions for a buyer wiring up more than one provider,
  an honest $37 (~32%) under the $116 separate total
  ([`PROVENANCE.md`](../../../candidates/webhook-verifier-bundle/PROVENANCE.md)
  § Pricing rationale). Conservative expectation: 0–2 sales/month absent
  distribution; the bundle adds a price point, not a new audience.
- **UNBLOCKS:** the bundle revenue path; a cross-sell landing spot the four kit
  intakes already name as first-ten channel 2.
- **VERIFIED-WHEN:** the public URL loads a purchasable $79 bundle page listing
  all four kits, and the storefront's preview/test purchase delivers the four
  kit zips (spot-check the downloads against the four sha256 pins in
  `MANIFEST.json`). HARD-GATE stands until then: no bundle click is actionable
  while any of the GitHub / Slack / Shopify publish clicks is unexecuted.

## PROVENANCE-FOOTER

Sources this click-script binds to (file@sha at authoring, base `main@ae36afb`):

- `candidates/webhook-verifier-bundle/MANIFEST.json` — the four component pins +
  pricing ($29 ×4 = $116 → $79, $37 off).
- `candidates/webhook-verifier-bundle/PROVENANCE.md` — pricing math + artifact
  pins.
- `docs/publishing/OWNER-QUEUE.md` — GitHub D5 / Slack D14 / Shopify D13 publish
  decisions (Stripe live, DONE 2026-07-12).
- `docs/launch/bundle-starter/owner-actions.md` — the Ship-It Bundle hard-gate
  precedent this mirrors.
