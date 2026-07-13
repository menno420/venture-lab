# Title Vetting — The Agent Merge-Wall Cookbook

> **Status:** `plan`
>
> Ninth PRODUCT packet in the vetting directory, so the publish click
> rides the derived owner queue (`../OWNER-QUEUE.md` via
> `scripts/derive_owner_queue.py`). Queued under ORDER 008 (2026-07-13
> night run, PRODUCT #9). No freeze applies — a guide + workflow-YAML
> cookbook with no payment-path dependency (the ORDER 003 ⚑B/⚑D freeze,
> lifted 2026-07-11 by PR #22, never attached to it). Every step marked
> **⚑ OWNER-GATE** is an owner click, never automated.

**Title:** The Agent Merge-Wall Cookbook · **Category:** digital product /
infrastructure recipe cookbook · **Date vetted:** 2026-07-13

Product: [`candidates/merge-wall-cookbook/`](../../../candidates/merge-wall-cookbook/README.md)
(v0.1; buyer bundle `dist/merge-wall-cookbook-v0.1.zip`; launch assets in
[`docs/launch/merge-wall-cookbook/`](../../launch/merge-wall-cookbook/owner-actions.md);
intake [`INTAKE.md`](../../../candidates/merge-wall-cookbook/INTAKE.md),
scored 3.55).

## 1. Built (verified this session, 2026-07-13)

- [x] Guide assembled ONLY from committed repo material, every chapter
      with a Sources footer citing file@sha: ch.1 walls verbatim ←
      `docs/PLATFORM-LIMITS.md` @ `2044dc6` (PR #9 / #15 / #55 denial
      texts); ch.2 zero-required-checks trap ← same ledger @ `2044dc6` +
      the enabler's refuse-to-arm guard @ `305646f`; ch.3 enabler
      walkthrough ← `.github/workflows/auto-merge-enabler.yml` @
      `305646f` + API-verified merge events (PR #104 merged
      2026-07-13T00:56:20Z, PR #128 merged 2026-07-13T02:46:46Z, both
      merged_by github-actions[bot]); ch.4 born-red HOLD ← `bootstrap.py`
      @ `6c46941` (`BORN_RED_HOLD_MESSAGE`, `IN_PROGRESS_TOKENS`,
      `check_added_card`) + `.github/workflows/substrate-gate.yml` @
      `4776045`; ch.5 fast lane ← `substrate-gate.yml` @ `4776045`; ch.6
      advisory pattern ← `.github/workflows/kit-tests.yml` @ `838b46e`;
      ch.7 REST fallback ← `PLATFORM-LIMITS.md` @ `2044dc6` + the
      enabler's own fallback message @ `305646f`.
- [x] **The sweep's honesty gap, closed rather than dodged:** the sweep
      verdict said the intake's "CI-verified YAML" claim couldn't be
      fully executed in-slice. Resolution: the primary recipe is adapted
      from this repo's own LIVE enabler — production-evidenced by real
      merge events, stronger than a lint run — while Recipe 2
      (`merge-on-green.yml`) is explicitly labeled parse-verified-only in
      its header, the listing FAQ, and guide ch.7's per-recipe honesty
      ledger. Nothing is asserted as CI-verified that wasn't.
- [x] **Honest size verdict:** ~3,500 words (~8 pages) of guide across 7
      chapters + 4 commented YAML recipes (~330 lines) + ~950 words
      README/QUICKSTART. The committed material fully supports the walls,
      enabler, born-red, fast-lane, and advisory chapters; the REST
      fallback chapter is honestly thinner (doctrine, not production) and
      says so.
- [x] All 4 recipe YAMLs **executed through `yaml.safe_load`** (PyYAML
      6.0.1, 2026-07-13 03:19Z): each parses to a dict with `name` +
      `jobs` (enable-auto-merge / merge / required-gate / drift-advisory).
      Repeated from the extracted bundle in a clean dir via the
      QUICKSTART's own shipped commands (PyYAML pass + stdlib structural
      pass): identical result.
- [x] Buyer bundle built via allow-list `package.sh` (false-green-test-trap
      pattern: fixed mtimes, sorted entries, `zip -X`),
      **byte-reproducible** — double rebuild, identical sha256, committed
      dist IS that build.
- [x] **sha256 `8d12a4371850689ed7f1be5b7f13fa0017db98bfa163bc6570edca1306a3c2b0`**
      (25,629 bytes, 14 content files) — also pinned in the click-script's
      ARTIFACT line.
- [x] Test row (honest-null clause, executed substitute): the recipes'
      only executable surface outside a GitHub runner is parse/structure —
      both shipped verification commands executed from the extracted
      bundle (4/4 recipes pass both); inventory 14/14 vs INCLUDED.md;
      all files valid UTF-8 non-empty; all 10 markdown files H1-headed
      with balanced fences. Honest remainder: no recipe was executed on a
      GitHub runner in this slice — the enabler pattern's evidence is the
      LIVE production workflow it was adapted from (file @ `305646f` +
      the #104/#128 merge events); Recipe 2 has no production evidence
      and is labeled so everywhere it appears.
- [x] Checkout/format verified from the artifact itself: clean-dir unzip —
      README + QUICKSTART + INCLUDED at top level, guide/ 7 chapters,
      recipes/ 4 YAMLs (matches INCLUDED.md manifest 14/14).
      **Secret scan, allowlist-aware:** real-secret-shape scan (ghp_/
      gho_/github_pat_/sk_live_/sk_test_/whsec_/AKIA/private-key/xox/
      AIza) **0 hits**; the 9 `secrets.GITHUB_TOKEN`/`secrets.MERGE_PAT`
      occurrences are `${{ … }}` template-variable references — GitHub
      Actions syntax naming which secret to READ at runtime, containing
      no secret value — documented as the allowlisted remainder rather
      than scanned around. No junk entries in the archive.

## 2. Collision scan

- [x] "Merge-wall" is the lane's own coinage — no in-catalog title
      collision. In-catalog overlap disclosed: the Agent Fleet Field
      Manual ($39) covers fleet operations broadly and mentions landing
      discipline; this cookbook is the deep, runnable-YAML treatment of
      the merge path specifically — the listing does not claim the
      manual's scope. Same buyer audience as field-manual/template-packs
      (the intake's own concentrated-channel-risk note, disclosed).

## 3. Market / price

- [x] Price **$19 one-time** — set at intake
      ([`INTAKE.md`](../../../candidates/merge-wall-cookbook/INTAKE.md):
      "Conservative revenue estimate: $19 one-time") and recorded
      identically in the listing copy, the click-script, and here.
      Precedent: the Agent-Workflow Template Pack's $19 rung (PWYW,
      PR #108) — runnable-artifact packs for the same builder audience.
      Chain: $15 (kill-rule kit, false-green) < **$19** = template-packs
      $19 PWYW < SWTK $29 live (PR #86) < field-manual $39 (PR #110) <
      membership-kit $49 (PR #106). Conservative expectation stays 0–3
      sales / $0–$57 first-90-day, $0 absent distribution (the intake's
      own line; validation signal ≥1 sale OR ≥30 reads in 30 days, else
      ledgered negative).

## 4–5. Packaging

- [x] Buyer bundle is the allow-listed `package.sh` output (README +
      QUICKSTART + INCLUDED + `guide/` + `recipes/`; deliberately
      excludes LISTING.md, the lane-internal INTAKE.md, dist/,
      package.sh). No cover image ships — owner adds one or uses the
      storefront default.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/merge-wall-cookbook/listing-copy.md)
      at catalog parity (Title / short ≤200 chars (193) / long / bullets /
      FAQ) and checked claim-by-claim against the extracted bundle:
      "~3,500 words, ~8 pages" = measured 3,531 from the extracted
      guide/; "four runnable recipes" = 4 (parse-executed); "13 agent PRs
      in a single night" + the #104/#128 merged_by github-actions[bot]
      citations match the API reads captured this session; the FAQ states
      what was NOT machine-verified (prose by citation; Recipe 2 never
      production-run) and tells already-disciplined buyers to buy
      nothing.

## 7. ⚑ OWNER-GATE — publish clicks (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none**
of it. It is the queue-parseable form of the click-script in
[`owner-actions.md`](../../launch/merge-wall-cookbook/owner-actions.md) —
the HOW detail lives there; no freeze applies (no payment-path gate).

**OWNER-ACTION — Publish "The Agent Merge-Wall Cookbook" at $19 one-time**
1. **Storefront account:** owner signs into (or creates) the storefront;
   complete its payout setup first or revenue holds.
2. **⚑ Storefront pick:** **Gumroad** (default — the click-script's HOW is
   written against it; same account as the SWTK live listing) or Lemon
   Squeezy — owner's call; either works with the same zip + copy.
3. **Product:** New product → Digital product; Name = "The Agent
   Merge-Wall Cookbook"; upload
   `candidates/merge-wall-cookbook/dist/merge-wall-cookbook-v0.1.zip`
   and verify the upload matches sha256 `8d12a437…06a3c2b0` (full hash in
   §1 and the click-script ARTIFACT line — never upload a stale local
   copy).
4. **Copy:** paste Title / Short + Long description / Bullets / FAQ from
   [`listing-copy.md`](../../launch/merge-wall-cookbook/listing-copy.md).
5. **Price:** set **$19 one-time** (fixed — set at intake; template-packs
   $19 rung).
6. **Publish + record:** publish, copy the public product URL, storefront
   preview/test purchase to confirm the zip delivers.

- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Lemon Squeezy.
- [ ] ⚑ **Owner:** zip uploaded + sha256 spot-check against §1.
- [ ] ⚑ **Owner:** listing copy pasted.
- [ ] ⚑ **Owner:** price set (**$19 one-time** (default per intake + precedent chain)).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URL copied.
- [ ] Seat (post-click, no money moved): record the launch durably on `main` —
      verified listing URL, price, timestamp — in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../../launch/stripe-webhook-test-kit/LAUNCH-LOG.md),
      arm the intake's 30-day kill clock as a `KILL-CHECK:` line here, and
      cross-link the cookbook from the Field Manual / False-Green Test
      Trap surfaces (same agent-builder audience).

---

**Verdict: publish-ready up to the owner gate.** Built + priced + listing
drafted + checkout/format verified + sha recorded (all evidenced above);
the product parks at §7 (owner clicks) by design. Honest caveats: the
guide is ~8 pages of prose + recipes, sized to what the committed material
supports; the prose is verified by citation, the recipes by parse-check,
and only the enabler pattern by production merge events — Recipe 2 was
never production-run and is labeled so in its header, the FAQ, and ch.7;
platform workarounds rot (the source ledger's own re-verify notes); the
buyer TAM is narrow on a concentrated channel (intake distribution 3/5) —
expect ~$0 absent distribution; and a live purchase remains unverified
until the owner's own test purchase.
