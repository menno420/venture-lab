# Title Vetting — The Auto-Merge Enabler Cookbook

> **Status:** `plan`
>
> PRODUCT packet in the vetting directory, so the publish click rides the
> derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Queued under ORDER 016 (2026-07-17
> overnight run). No freeze applies — a guide + workflow-YAML cookbook with
> no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze, lifted
> 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** The Auto-Merge Enabler Cookbook · **Category:** digital product /
infrastructure recipe cookbook · **Date vetted:** 2026-07-17

Product: [`candidates/auto-merge-enabler-cookbook/`](../../../candidates/auto-merge-enabler-cookbook/README.md)
(v0.1; buyer bundle `dist/auto-merge-enabler-cookbook-v0.1.zip`; launch
assets in
[`docs/launch/auto-merge-enabler-cookbook/`](../../launch/auto-merge-enabler-cookbook/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/auto-merge-enabler-cookbook/INTAKE.md),
scored 3.75).

## 1. Built (verified this session, 2026-07-17)

- [x] Guide assembled ONLY from committed repo material, every chapter with
      a Sources footer citing file@sha: ch.1 merge-on-green model ←
      `docs/current-state.md` @ `4e0a37c` + the five 2026-07-17
      `github-actions[bot]` merge events (PR #219 `389ab6e` … #223
      `f0511ae`); ch.2 enabler annotated ←
      `.github/workflows/auto-merge-enabler.yml` @ `aa04700` (every guard
      quoted verbatim); ch.3 required-checks gating ← same enabler +
      `.github/workflows/substrate-gate.yml` @ `aa04700`; ch.4 born-red HOLD
      ← `substrate-gate.yml` @ `aa04700`; ch.5 opt-out ← the enabler's label
      carve-out @ `aa04700` + PR #218 (`do-not-automerge` → `merged_by
      menno420`); ch.6 classifier caveat ← `docs/current-state.md` @
      `4e0a37c`; ch.7 troubleshooting ← the enabler + `main-verify.yml` @
      `f8ccc60`; ch.8 recipes + honesty ledger.
- **Evidence class: verified-by-production.** The subject IS this repo's own
  live merge infrastructure, so the primary evidence is real merge events +
  byte-identical production workflow files — stronger than a synthetic HTTP
  test, which is why this packet does not carry the webhook-kit HTTP test
  row. The two shipped recipes (`auto-merge-enabler.yml`,
  `substrate-gate.yml`) are `cmp`-verified byte-identical to the live
  workflows at `aa04700`; the third (`auto-merge-enabler-minimal.yml`) is a
  readability distillation, labeled parse-verified-only in its header, the
  listing FAQ, and guide ch.8. Nothing is asserted as production-run that
  isn't.
- [x] **Honest size verdict:** ~4,300 words (~10 pages) of guide across 8
      chapters + 3 commented YAML files (~450 lines, two of them the exact
      production workflows) + ~1,300 words README/QUICKSTART/PROVENANCE. The
      committed material fully supports every chapter; the one path this
      repo does NOT run (a runnable REST merge-on-green fallback) is
      explicitly NOT shipped and pointed at the Merge-Wall Cookbook instead.
- [x] All 3 recipe YAMLs **executed through `yaml.safe_load`** from the
      extracted bundle in a clean dir (each parses to a dict with
      `name`/`on`/`jobs`), plus the shipped stdlib structural check — 3/3
      pass both.
- [x] Buyer bundle built via allow-list `package.sh` (merge-wall-cookbook /
      false-green-test-trap pattern: fixed mtimes, sorted entries, `zip -X`),
      **byte-reproducible** — double rebuild, identical sha256, committed
      dist IS that build.
- [x] **sha256 `3deceb46b587f8d24899c63cba7ce58d0a41aae564b2dfeabe5b80135bfdd703`**
      (36,456 bytes, 15 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Inventory + honest-null check (executed substitute for a runtime test
      row, since a zero-runtime content product has no HTTP surface):
      inventory 15/15 vs INCLUDED.md; all 12 markdown files valid UTF-8
      non-empty, H1-headed with balanced fences; both shipped verification
      commands executed from the extracted bundle (3/3 recipes pass both).
      Honest remainder: the workflows were not re-run on a fresh GitHub
      runner in this slice — the evidence is that the two production recipes
      ARE the live workflows (`cmp`-identical at `aa04700`) + the five
      #219–#223 merge events; the minimal variant has no production evidence
      and is labeled so everywhere it appears.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + INCLUDED + PROVENANCE at top level, guide/ 8
      chapters, recipes/ 3 YAMLs (matches INCLUDED.md manifest 15/15).
      **Secret scan, allowlist-aware:** real-secret-shape scan (ghp_/ gho_/
      github_pat_/ sk_live_/ whsec_/ AKIA/ xox/ AIza) **0 hits**; the 12
      `secrets.GITHUB_TOKEN`/`secrets.ROUTINE_PAT` occurrences are `${{ … }}`
      template-variable references — GitHub Actions syntax naming which
      secret to READ at runtime, containing no secret value — documented as
      the allowlisted remainder rather than scanned around. No junk entries
      in the archive.

## 2. Collision scan

- [x] No in-catalog title collision. **Disclosed overlap with the Agent
      Merge-Wall Cookbook ($19):** same agent-builder audience, adjacent
      subject. The honest boundary, stated in both listings: the Merge-Wall
      Cookbook is conflict AVOIDANCE (the walls a self-merging fleet hits +
      fallbacks, including a runnable REST merge-on-green recipe); THIS
      cookbook is the merge-on-green ENABLE mechanism — the enabler workflow
      itself, annotated guard by guard, with the born-red HOLD. They
      cross-sell; neither claims the other's scope. Same concentrated
      community channel as merge-wall / field-manual / template-packs (the
      intake's own channel-risk note, disclosed).

## 3. Market / price

- [x] Price **$19 one-time** — set at intake
      ([`INTAKE.md`](../../../candidates/auto-merge-enabler-cookbook/INTAKE.md):
      "Conservative revenue estimate: $19 one-time") and recorded
      identically in the listing copy, the click-script, and here.
      Precedent: the **Agent Merge-Wall Cookbook's $19 rung**
      ([merge-wall-cookbook.md](merge-wall-cookbook.md)) — a runnable,
      production-cited GitHub Actions cookbook for the same audience and this
      product's nearest sibling. Chain: $15 (kill-rule kit, false-green) <
      **$19** = merge-wall-cookbook $19 = template-packs $19 PWYW < SWTK $29
      live < field-manual $39 < membership-kit $49. Conservative expectation
      0–3 sales / $0–$57 first-90-day, $0 absent distribution (the intake's
      own line; validation signal ≥1 sale OR ≥30 reads in 30 days, else
      ledgered negative). Fixed $19 (not PWYW — the ⚑D template-packs
      listing is the catalog's designated PWYW instrument).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      QUICKSTART + INCLUDED + PROVENANCE + `guide/` + `recipes/`;
      deliberately excludes LISTING.md, the lane-internal INTAKE.md, dist/,
      package.sh). No cover image ships — owner adds one or uses the
      storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/auto-merge-enabler-cookbook/listing-copy.md)
      at catalog parity (Title / short ≤200 chars / long / bullets / FAQ +
      the "what it does NOT do" honesty section + PROVENANCE-FOOTER) and
      checked claim-by-claim against the extracted bundle: "~10 pages" =
      measured from the extracted guide/; "three GitHub Actions files, two
      verbatim production workflows" = `cmp`-verified; the five
      #219–#223 `github-actions[bot]` citations and the #218 opt-out
      counter-example match the API reads captured this session; the FAQ
      states what was NOT machine-verified (prose by citation + real merge
      events; minimal variant parse-verified only; no REST fallback shipped)
      and tells already-disciplined buyers to buy nothing.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none**
of it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/auto-merge-enabler-cookbook/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "The Auto-Merge Enabler Cookbook" at $19 one-time**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — the click-script's HOW is
   written against it; same account as the live SWTK listing) or Lemon
   Squeezy — owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "The Auto-Merge
   Enabler Cookbook"; upload
   `candidates/auto-merge-enabler-cookbook/dist/auto-merge-enabler-cookbook-v0.1.zip`
   and verify the upload matches sha256 `3deceb46…5bfdd703` (full hash in §1
   and the click-script ARTIFACT line — never upload a stale local copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ + the
   "what it does NOT do" honesty section from
   [`listing-copy.md`](../../launch/auto-merge-enabler-cookbook/listing-copy.md).
5. **Price:** set **$19 one-time** (fixed — set at intake; merge-wall
   $19 precedent rung).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$19 one-time** (default per intake + precedent
      chain)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main`
      — verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      arm the intake's 30-day kill clock as a `KILL-CHECK:` line here, and
      cross-link the cookbook from the Agent Merge-Wall Cookbook / Field
      Manual surfaces (same agent-builder audience).

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above);
the product parks at §7 (owner clicks) by design. Honest caveats: the guide
is ~10 pages of prose + recipes, sized to what the committed material
supports; the prose is verified by citation + real merge events, the two
production recipes by byte-identity to the live workflows, and only the
minimal variant is parse-verified-only (labeled so in its header, the FAQ,
and ch.8); no REST merge-on-green fallback is shipped (this repo lands via
the native arm); platform workarounds rot (re-verify against current GitHub
docs); the buyer TAM is narrow on a concentrated channel shared with the
Merge-Wall Cookbook (intake distribution 3/5) — expect ~$0 absent
distribution; and a live purchase remains unverified until the owner's own
test purchase.
