# One-Pass Title-Vetting Checklist (template)

> **Status:** `reference`
>
> Copy this file per title (`docs/publishing/vetting/<slug>.md`) and work it
> top to bottom in ONE pass. It packages the pipeline the
> [publishing plan](PUBLISHING-PLAN.md) (PR #87) derived for the first 14
> titles, so a new title never re-derives it. Steps marked **⚑ OWNER-GATE**
> involve real money, external accounts, or publish clicks — the seat prepares
> them, **the owner performs every click**; they are never automated.

**Title:** _______ · **Category:** adult / YA / kids · **Date vetted:** YYYY-MM-DD

## 1. Title

- [ ] Working title + any subtitle candidates written down.
- [ ] Bare-word searchability sanity check: a single common word (e.g. *Lull*)
      is near-unsearchable — plan a subtitle (*"A Novella"* / *"A Novel"*) up
      front.
- [ ] Homophone / autocorrect drift noted (e.g. weigh/weight, Tummel/Tumble).

## 2. Collision scan (discoverability, not legality)

Titles are not copyrightable — this is about not being buried in search.

- [ ] Web + storefront search for the exact title; log every same-named book
      (author, year, prominence) in a row matching the plan's
      [§7 collision table](PUBLISHING-PLAN.md#7-title-collision-scan-discoverability-not-legality).
- [ ] Verdict recorded: **None / Low / Moderate / Strong / Very strong** —
      with the caveat that self-pub titles are unevenly indexed ("none found"
      is weaker evidence than for trad-pub).
- [ ] If Strong+: pick the differentiator now — subtitle, genre-signalling
      subtitle, or rename (see Undertow / Ultramarine / Hollowtide / Dormouse
      precedents in the plan).
- [ ] If inconclusive: flag for a direct KDP title-availability check before
      lockdown (owner does the KDP login — see §7).

## 3. Market verification

Verify, don't trust — cite a source URL + accessed date for every figure.

- [ ] Category comps: what do comparable titles in this category/length
      actually charge today?
- [ ] Any market claim inherited from an external review re-checked against a
      live source (the plan corrected two such claims; treat external reviews
      as input to verify).
- [ ] Series/KU context: standalone novellas outside a series or Kindle
      Unlimited carry a known discoverability handicap — note whether this
      title has a series home.
- [ ] Revenue framing stays conservative: unknown-author base case ≈ $0; unit
      economics only, no sales projections.

## 4. Price band

- [ ] Band picked per the plan's verified §1 table: adult/literary novella
      ebook **$3.99–$5.99**; YA novella ebook **$2.99–$3.99**; kids paperback
      list **$12.99–$14.99**.
- [ ] 70%-royalty threshold respected: KDP pays 70% only on ebooks priced
      **$2.99–$9.99** (below/above → 35%, delivery fee applies on the 70%
      tier). A $0.99 impulse price means 35% — flag the trade-off explicitly.
- [ ] Print titles: per-unit royalty computed (60% of list − print cost; a
      24–40pp premium-color paperback prints at a flat ~$3.60 on Amazon.com).

## 5. Packaging (production gate)

The gating variable is production cost, not length.

- [ ] Gate identified: **cover-only** (adult/YA text titles) vs **cover +
      full interior illustration** (kids picture books).
- [ ] Cover-only: ebook cover spec noted (1600×2560px min); format
      reflowable ebook; language English-first per the plan's §5 translation
      strategy (Dutch print gotcha: no PDF manuscript path for Dutch).
- [ ] Illustrated: **⚑ OWNER-GATE — illustration money-decision.** Commission
      (~$1,200–$6,000/book), AI art (near-zero cost but requires KDP
      AI-generated disclosure at publish time; unsettled image copyright;
      3-new-titles/day cap), or park. This is a real spend decision — seat
      recommends, owner decides. No art spend is committed by an agent.
- [ ] Owner confirms true length (novella vs novel) if unread by the seat —
      word count is an owner-supplied fact, not a guess.

## 6. Listing copy

- [ ] Blurb/description drafted in-repo (committed, nothing published).
- [ ] Two categories + 7 keywords chosen; avoid the crowded generic terms the
      collision scan surfaced.
- [ ] Subtitle from §1/§2 locked into the listing metadata draft.
- [ ] KDP Select (KU) recommendation recorded with rationale (90-day
      exclusivity is reversible; novellas typically earn best via KU
      page-reads).

## 7. ⚑ OWNER-GATE — publish clicks (never automated)

Everything below is owner-only: real money, external accounts, publishing
clicks. The seat's output for this section is a queued OWNER-ACTION block
(six fields, like the plan's §4), not an execution.

- [ ] **Owner:** KDP account login/creation; tax/bank interview complete
      (royalties hold otherwise).
- [ ] **Owner:** final KDP title-availability recheck for any §2-inconclusive
      title.
- [ ] **Owner:** cover commissioned/approved and any art spend authorized
      (§5 decision).
- [ ] **Owner:** price set on the storefront (band from §4).
- [ ] **Owner:** AI-generated content disclosure ticked at publish time, if
      §5 chose AI art.
- [ ] **Owner:** the publish click itself + KDP Select enrollment choice.
- [ ] Seat (post-click, no money moved): record the launch durably on `main`
      — verified listing URL, price, timestamp, and concrete kill-rule dates,
      in the style of
      [`docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](../launch/stripe-webhook-test-kit/LAUNCH-LOG.md).

---

*One pass, top to bottom, per title. If any step cannot be completed with a
citation or an owner decision, the title is NOT publish-ready — park it at the
blocking step rather than skipping ahead.*
