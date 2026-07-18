# API Robustness Bundle ($79) — owner bundle-creation click-script

> **Status:** `reference`
>
> **HARD-GATED (2026-07-18):** a Gumroad bundle is assembled FROM existing live
> products — it cannot be created while its component kits are unpublished. None
> of the four components is LIVE: the **Idempotency Key** ($29, OWNER-QUEUE
> **D6**), **JWT Auth** ($29, **D7**), **Pagination** ($29, **D13**), and
> **Rate-Limit** ($29, **D16**) kits are queued publish clicks in
> [`OWNER-QUEUE.md`](../../publishing/OWNER-QUEUE.md). All four publish clicks
> must be executed FIRST. Nothing below the blocking rows in the
> [§7 packet](../../publishing/vetting/api-robustness-bundle.md) proceeds until
> all four component products are live. This is a click-script for the owner,
> not a request to any agent; no agent performs publish/spend/account actions.
>
> This mirrors the existing **Webhook Verifier Bundle** hard-gate precedent
> ([`../webhook-verifier-bundle/owner-actions.md`](../webhook-verifier-bundle/owner-actions.md)).

## Honesty section

- The bundle ships **no new product code** — it assembles four already-built,
  already-tested kits plus a README / QUICKSTART / MANIFEST / PROVENANCE. The
  bundle's own test is an **assembly/inventory check**, not a fifth product.
- **None** of the four kits is live today — all four are queued owner clicks.
  Until they are published, a Gumroad bundle referencing them cannot be created
  by anyone, owner included — this is why the click-script is gated.
- The $116 separate-purchase total is the genuine sum of four $29 kits, not a
  manufactured anchor. **Never price at $116** (zero discount voids the bundle).
- Priced at **$79** to match the Webhook Verifier Bundle (also four $29 kits)
  exactly — two four-kit SKUs at one price, not two ad-hoc anchors.
- The seat performed NONE of the steps below — every step is an owner click.

### ⚑ — Create the "API Robustness Bundle" at $79 · HARD-GATED on Idempotency (D6) + JWT (D7) + Pagination (D13) + Rate-Limit (D16)

- **WHAT:** Create a Gumroad **bundle** priced **$79** (one-time, fixed)
  combining the four live component kits — Idempotency Key / Rate-Limit /
  Pagination / JWT Auth Test Kits ($29 each) — using the copy in
  [`listing-copy.md`](listing-copy.md). On Gumroad a bundle references the
  component products' existing uploads; if instead you upload a single file, use
  the reproducible bundle zip
  `candidates/api-robustness-bundle/dist/api-robustness-bundle-v0.1.zip`
  (sha256 `6be74b6d78a77180a133fd09c31c452baaea77497cd8db63461b9ee43dfb560c`,
  160,844 B) which contains the four component zips verbatim (each pinned in
  [`MANIFEST.json`](../../../candidates/api-robustness-bundle/MANIFEST.json)).
- **WHERE:** gumroad.com → *Products* → *New product* → *Bundle*, signed into
  the same account that published the four component kits.
- **HOW:** 1) Execute the Idempotency (D6), JWT Auth (D7), Pagination (D13), and
  Rate-Limit (D16) publish clicks first — their own click-scripts; all four
  blocking. 2) Sign in to the same Gumroad account. 3) New product → **Bundle**.
  4) Name = "API Robustness Bundle — Idempotency + Rate-Limit + Pagination + JWT
  Auth Test Kits". 5) Select the four live kits as the bundle contents (or
  upload the single reproducible bundle zip). 6) Price = **$79**, one-time,
  fixed. 7) Paste Title / Short + Long / Bullets / FAQ from
  [`listing-copy.md`](listing-copy.md). 8) Publish. 9) Copy the public
  bundle URL.
- **WHY:** A higher-AOV price point over four kits at zero new build cost: $79
  removes three checkout decisions for a buyer hardening more than one property
  of an API, an honest $37 (~32%) under the $116 separate total
  ([`PROVENANCE.md`](../../../candidates/api-robustness-bundle/PROVENANCE.md)
  § Pricing rationale). Conservative expectation: 0–2 sales/month absent
  distribution; the bundle adds a price point, not a new audience.
- **UNBLOCKS:** the bundle revenue path; the own-endpoint cross-sell landing
  spot the four kit intakes already name.
- **VERIFIED-WHEN:** the public URL loads a purchasable $79 bundle page listing
  all four kits, and the storefront's preview/test purchase delivers the four
  kit zips (spot-check the downloads against the four sha256 pins in
  `MANIFEST.json`). HARD-GATE stands until then: no bundle click is actionable
  while any of the four component publish clicks is unexecuted.

## PROVENANCE-FOOTER

Sources this click-script binds to (file@sha at authoring, base `main@2fb86bf`):

- `candidates/api-robustness-bundle/MANIFEST.json` — the four component pins +
  pricing ($29 ×4 = $116 → $79, $37 off).
- `candidates/api-robustness-bundle/PROVENANCE.md` — pricing math + artifact
  pins.
- `docs/publishing/OWNER-QUEUE.md` — Idempotency D6 / JWT D7 / Pagination D13 /
  Rate-Limit D16 publish decisions (none live).
- `docs/launch/webhook-verifier-bundle/owner-actions.md` — the Webhook Verifier
  Bundle hard-gate precedent this mirrors.
