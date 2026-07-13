# Title Vetting — Photo Packs (Dutch Skies + Golden Hours)

> **Status:** `plan` — **HARD-GATED: NOT publish-ready, artifact does not exist.**
>
> PRODUCT #5 packet of the 2026-07-13 night run (ORDER 008). Unlike every
> other product packet in this directory, the sellable artifact **cannot be
> built by an agent**: the PACK-SPEC public-repo safety rule keeps full-res
> originals OFF this public repo (owner-held), and the repo carries only
> ≤2048px watermarked previews. This packet therefore queues an
> **owner-gated build-then-publish sequence** — the first rows are blocking
> owner steps, and NO publish click is queued ungated. Every step marked
> **⚑ OWNER-GATE** is an owner action, never automated.

**Title:** Photo Packs — Dutch Skies + Golden Hours — Waterside · **Category:**
digital product / wallpaper packs · **Date vetted:** 2026-07-13

Product: [`candidates/photo-packs/`](../../../candidates/photo-packs/INTAKE.md)
(registry `packs.json`, 5 packs, 2 with committed previews; launch copy in
[`docs/launch/photo-packs/`](../../launch/photo-packs/listing-copy.md)).

## 1. Built — **NO (honest null: the artifact cannot exist in-repo)**

- [ ] **NOT BUILT — hard gate.** The sold zips (phone 1290×2796 / 4K
      3840×2160 / 5K 5120×2880 / ultrawide 3440×1440 tiers per
      [PACK-SPEC](../../../candidates/photo-packs/PACK-SPEC.md)) are cut from
      full-res originals that are **owner-held OFF-repo** by the PACK-SPEC
      public-repo safety rule. No agent can build, hash, or verify them.
- [x] What IS verified, executed 2026-07-13 on `claude/night-photo-packs`
      (base `d01dacd`):
  - `python3 candidates/photo-packs/validate_samples.py` → exit 0:
    "packs.json valid and 7 sample file(s) pass all checks (<= 2048px, size
    cap, naming, cross-referenced); repo-wide oversize scan clean" (scan
    covered 7 image files repo-wide).
  - `packs.json` parses as valid JSON; 5 packs; all 9 required per-pack
    fields present on every pack; all tier keys canonical; all 7 sample
    filenames match `<pack-id>__<seq>__preview.jpg` with matching pack ids;
    `count` == committed samples for both preview packs (dutch-skies 3,
    golden-hours 4).
  - Sample dimensions header-parsed (stdlib): all 7 at longest edge exactly
    2048px (5 landscape 2048×1152–1153, 2 portrait 1153×2048) — spec-compliant.
  - Watermarks visually confirmed on inspected samples: tiled body mark
    "© menno420 — PREVIEW — not for use" + solid corner mark (compliance
    per PR #52 policy line in PACK-SPEC).
  - EXIF/GPS leakage: none — no `Exif\x00\x00` APP1 segment present in any
    of the 7 JPEGs (stdlib byte scan; Pillow unavailable in this
    environment, so tag-level enumeration was not run — but with no EXIF
    segment at all there are no tags to leak).

## 2. Collision scan

- [x] Pack names are descriptive ("Dutch Skies", "Golden Hours — Waterside");
      storefront namespace is per-account, no KDP-style title gate. "Dutch
      Skies" is generic-descriptive; no trademark-style collision identified
      (not exhaustively searched — low-risk category).

## 3. Market / price (evidence: [MARKET-PLAN](../../../candidates/photo-packs/MARKET-PLAN.md), cited there)

- [x] **Recommendation: $5 fixed per pack, both packs, Gumroad direct**
      (packs.json `price_usd: 5`; MARKET-PLAN channel (a) range $3–10).
      Worked nets from the cited fee schedules: $5 on Gumroad direct ≈
      **$3.56**/sale; Gumroad Discover ≈ $3.50; Ko-fi free plan ≈ $4.30.
      Below ~$3 the fixed fees ($0.50 + ~$0.30) eat >25% of price — do not
      price under $3. Conservative expectation stays **$0–30 / first 90
      days** cold (MARKET-PLAN header; the cited $10-total creator anecdote
      is the realistic anchor, not the $1000-with-audience one).
- [x] Honest positioning: golden-hours is the **most-saturated** theme
      (PACK-SPEC: "do not lead with it"); dutch-skies leads of the two.
      The differentiated wedge (macro-bug packs, MARKET-PLAN §d) has NO
      committed samples yet — it needs owner originals before it can even
      reach preview state.
- [x] Genuine uncertainty flagged as SIM-REQUEST (via outbox lane, not this
      packet): (1) PWYW vs fixed $5 conversion for cold wallpaper packs;
      (2) whether saturated golden-hours should anchor at $3 instead;
      (3) two-pack bundle price. No cited evidence either way — defaults
      above stand until simulated or measured.

## 4–5. Packaging

- [ ] **Owner-gated.** Per-pack zip layout per PACK-SPEC tiers; built by the
      seat AFTER the owner supplies originals (§7 step 2 → seat build row).
      Nothing to package tonight; no sha exists and none is claimed.

## 6. Listing copy (drafted in-repo — nothing published)

- [x] [`listing-copy.md`](../../launch/photo-packs/listing-copy.md) drafted
      2026-07-13 for both preview packs at membership-kit/SWTK/template-packs
      parity (Title / short ≤200 chars (184 and 175) / long / bullets / FAQ),
      claim-checked against executed evidence: photo counts (3 / 4) match
      `packs.json`; tier dimensions match PACK-SPEC; "no AI, shot by a
      human" matches INTAKE provenance; the golden-hours FAQ concedes the
      free-alternative headwind rather than hiding it. Copy is paste-ready
      but explicitly headed PREVIEW-ONLY until the §7 gate clears.

## 7. ⚑ OWNER-GATE — build, then publish (queued, never automated)

Seat output = this queued OWNER-ACTION block; the seat performed **none** of
it. Sequence differs from the other product packets: the first two rows are
**blocking** — the artifact cannot exist until they clear, so every row below
them is frozen by construction. NO publish click is queued ungated.

**OWNER-ACTION — Build + publish "Dutch Skies" and "Golden Hours — Waterside" at $5 each**
1. **Originals hand-off:** owner supplies the full-res originals for the 7
   registered photos (plus any additions) to the seat via a PRIVATE channel
   (private storage / local disk) — NEVER by committing them to this public
   repo (PACK-SPEC safety rule).
2. **Licensing pass:** owner confirms per PACK-SPEC curation rules: no
   recognizable people without release, no trademarked logos, no
   private-property/protected-location issues (sunset/landscape shots need
   the people-and-property pass; PACK-SPEC calls this owner homework).
3. **Seat build (post-gate, off-repo):** seat cuts the 4 tiers per photo per
   PACK-SPEC dims, zips per pack, records sha256 of each zip in this packet
   §1 and the click-script ARTIFACT lines — zips live off-repo with the
   originals.
4. **⚑ Storefront pick:** **Gumroad** (default — MARKET-PLAN channel (a)
   default; Discover gives audience-free category browse) or Ko-fi (better
   per-sale net ≈ $4.30 vs $3.56, no marketplace browse) — owner's call.
5. **⚑ Price:** **$5 fixed per pack** (default — §3 evidence; floor $3;
   PWYW is an open SIM-REQUEST, not tonight's default).
6. **Publish + record:** upload zips (sha spot-check vs step 3), paste copy
   from [`listing-copy.md`](../../launch/photo-packs/listing-copy.md),
   publish, preview/test purchase, copy public URLs.

- [ ] ⚑ **Owner:** hand off full-res originals via a private channel —
      blocking: full-res originals are owner-held off-repo (PACK-SPEC
      public-repo safety rule); the sellable artifact cannot be built,
      hashed, or verified until this lands. Nothing below proceeds.
- [ ] ⚑ **Owner:** licensing/curation pass on the originals (people /
      logos / property per PACK-SPEC) — blocking: owner homework, not
      agent-checkable.
- [ ] Seat (post-gate, no click): build tier zips per PACK-SPEC, record
      per-zip sha256 in §1 + ARTIFACT lines, verify zips from the buyer
      side (unzip, dims, no EXIF/GPS) — then and only then the rows below
      are actionable.
- [ ] ⚑ **Owner:** storefront account + payout setup.
- [ ] ⚑ **Owner:** storefront pick (**Gumroad** (default)) — or Ko-fi.
- [ ] ⚑ **Owner:** zips uploaded + sha256 spot-check against the seat build
      record in §1.
- [ ] ⚑ **Owner:** listing copy pasted for both packs.
- [ ] ⚑ **Owner:** price set (**$5 fixed per pack** (default); floor $3).
- [ ] ⚑ **Owner:** the publish click + preview/test purchase + public URLs
      copied.
- [ ] Seat (post-click, no money moved): record the launch durably on
      `main` — verified listing URLs, price, timestamp — LAUNCH-LOG style;
      flip these rows to `- [x] … — DONE <date>` per the DONE disposition.

---

**Verdict: NOT publish-ready — hard-gated on owner-held originals, by
design.** Everything agent-doable is done and executed-verified (validator
green, registry spec-clean, previews watermarked + EXIF-free, price
recommended from cited evidence, listing copy drafted); the artifact itself
cannot exist in this public repo, so the queue shows a build-then-publish
owner sequence with the blocking rows first. Honest caveats: Pillow was
unavailable, so the EXIF check is a byte-scan for the APP1 segment (absent in
all 7 files) rather than tag enumeration; the macro-bug wedge packs have no
samples at all yet; conservative revenue expectation $0–30/90d cold stands.
