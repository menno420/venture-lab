---
state: captured
origin: owner
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Overnight planning menu — 2026-07-17 (veto-ready)

> **Status:** `veto-ready menu` — quantity is deliberate. Skim the whole list and
> VETO what you don't want; your veto is the filter. Nothing here is built except
> the small hygiene fixes that shipped with this PR. All M/L items are plans only.

## Provenance

Written under the owner's live overnight autonomous order (2026-07-16 night,
relayed via the coordinator session). The agent-executable backlog was honestly
declared DRY at PR #215 — net-new inventory is paused pending owner-only decisions
(native-speaker proofread, length-band ratify, publish clicks). Per the order,
this session switched to PLANNING MODE and generated an excessive, unfiltered
menu of 38 proposals. The owner vetoes tomorrow.

### Owner overnight order (verbatim, as relayed by the coordinator)

> OVERNIGHT ORDER (owner, live — 2026-07-16 night): I'm going to sleep; run autonomously until morning. Silence = consent. 1. CONTINUE: work your planned backlog — open ORDERs in control/inbox.md, the heartbeat baton's next-tasks, roadmap/planning docs in your repo(s). Slice after slice, one PR each, landed on green via your repo's landing workflow. A blocked PR carries its named blocker; take the next slice, never stall. 2. IF THE BACKLOG IS GENUINELY DRY — switch to PLANNING MODE, and plan excessively. Generate as many concrete, distinct proposals as you honestly can for your repo(s), from small fixes to ambitious features. Write each into the repo (your ideas/ or planning/ convention) with: a 2-3 line pitch · effort (S/M/L) · risk/reversibility · what it unblocks. Quantity is deliberate — tomorrow morning I will skim the whole menu and VETO what I don't want; my veto is the filter, so don't pre-filter down to a few safe picks. Do NOT build the ambitious ones tonight — planning docs only. Small, contained, reversible improvements may be built and landed as usual. 3. HYGIENE: keep heartbeats honest (control/status.md), every PR at a terminal state or carrying a named blocker, everything in git before session end. I'm recreating some projects tomorrow, so leave records clean enough that a fresh seat picks up from the repo alone. Morning deliverable: landed work, or a veto-ready menu of plans in your repo — ideally both.

### Note — inbox not written (convention)

The coordinator asked to append this order to `control/inbox.md` as ORDER 016.
Declined the inbox write: `control/inbox.md` is MANAGER-WRITTEN-ONLY per
`control/README.md` + `docs/conventions.md` — the lane NEVER edits it (not to
ack, not to mark done, not to fix typos). The order is recorded verbatim here, in
the session card `.sessions/2026-07-17-overnight-menu.md`, and in
`control/status.md` instead. The order still governed tonight's work. If the fleet
manager wants a formal ORDER 016, that's the manager's write to make (next free
number is 016).

## How to read this

38 proposals across four lanes. Each carries a 2-3 line pitch, effort (S/M/L),
risk/reversibility, and what it unblocks. Effort is diff size / surface, not time.
Owner-spend / account-creation / publish steps are flagged owner-gated — no such
step was taken. Cross out your vetoes; survivors become future sessions' claimed
slices.

- Product / sellables — P-1 … P-12
- Publishing pipeline / automation — PUB-1 … PUB-9
- Revenue path / distribution — REV-1 … REV-8
- Ops / infra / repo-health — OPS-1 … OPS-9

---

## Product / sellables

### P-1. Slack Webhook Test Kit — $29
**Pitch:** The exact SWTK/GWTK template applied to Slack: a stdlib-only local harness that verifies Slack's `v0=` HMAC request signature (the `X-Slack-Signature` + `X-Slack-Request-Timestamp` scheme), replays vendored real-shape Slack event/interaction payloads, and fail-closes on forged or stale (>5-min) deliveries, each fixture pinned in PROVENANCE.md. Buyer: developers building Slack apps/bots who can't safely test signature verification against production. Now: it is product N+1 off the one template this lane has actually shipped live (`candidates/stripe-webhook-test-kit/`, `candidates/github-webhook-test-kit/`).
**Effort:** M
**Risk / reversibility:** Low — self-contained candidate dir, one publish click owner-gated; unbuilt/unpublished until owner go, fully revertible. Slack's signing differs from Stripe/GitHub (one learnable unknown).
**Unblocks:** First-ten path = a "verify X-Slack-Signature the right way" dev.to gotcha article + cross-link from the two live webhook-kit listings; also seeds the Trio bundle (P-3).

### P-2. Shopify Webhook Test Kit — $29
**Pitch:** Same template, Shopify's `X-Shopify-Hmac-SHA256` base64 scheme: verify HMAC, replay vendored real-shape order/product/fulfillment payloads, reject forged/tampered bodies, PROVENANCE-pinned fixtures. Buyer: the large population of Shopify-app and e-commerce integration developers — a distinctly bigger, more commercial audience than the agent-ops funnel this lane keeps over-serving. Now: reuses the proven verify/replay/tests/package.sh scaffold; steps onto a fresh channel.
**Effort:** M
**Risk / reversibility:** Low — isolated candidate, owner-gated publish, trivially reverted. Deliberately SINGLE-provider (the killed Webhook Fixture Vault was multi-provider staleness liability), so it inherits none of that maintenance burden.
**Unblocks:** First-ten path = Shopify-dev communities + Gumroad e-commerce category, a channel none of the 11 current SKUs touch.

### P-3. Webhook Test Kit Trio — bundle $59 (vs $87 single)
**Pitch:** Bundle SWTK + GitHub Webhook Test Kit + Slack Webhook Test Kit (P-1) as one "verify any inbound webhook" pack at a ~30% multi-buy discount. Buyer: any team wiring more than one provider's webhooks — the natural upsell off each single listing. Now: unlike the HARD-GATED Ship-It Bundle, this bundle's SWTK component is already LIVE and GWTK is publish-READY — it's the first bundle whose referents are mostly real.
**Effort:** S
**Risk / reversibility:** Low — a Gumroad bundle listing, deletable in one click; still gated until its components are live (Slack kit + GWTK publish clicks).
**Unblocks:** Raises AOV on the one product family with a live sale path; each single listing cross-links into it.

### P-4. The Auto-Merge Enabler Cookbook — $19
**Pitch:** The born-red card → READY `claude/` PR → CI green → self-landing auto-merge enabler that this fleet runs in production (installed PR #59, ≈90 PRs landed this way). A GitHub Actions workflow + doctrine cookbook: the enabler that merges agent PRs on green WITHOUT letting a lane arm or merge its own PR. Buyer: teams running agent-authored PRs who want hands-off landing with a safety separation. Distinct from the shipped Merge-Wall Cookbook (that's inter-agent conflict avoidance; this is the merge-on-green mechanism).
**Effort:** M
**Risk / reversibility:** Low — distillation of committed workflow files + prose; owner-gated publish, revertible.
**Unblocks:** First-ten path = an "our agents merge their own PRs safely — here's the enabler" article + cross-sell from field-manual and merge-wall listings.

### P-5. The Salt Bell — NL edition (*De zoute klok*) — publish-READY sellable
**Pitch:** Full Dutch edition of The Salt Bell (Zeeland, 1953 North Sea flood), currently EN-only. The NL title is already pre-named *De zoute klok* in the concept doc, and the subject (Watersnoodramp) is core Dutch national memory — the single highest NL-market-fit title in the catalog. Now: the older NL catalog is 13/13 but the three newest adult novels fell behind; this closes the most commercially obvious gap.
**Effort:** M
**Risk / reversibility:** Low — new file under the existing title's `versions/nl`, no effect on the EN edition; publish owner-gated; native-speaker proofread gate applies.
**Unblocks:** Adds the NL edition to the NL-language funnel that already carries 13 editions; pairs with the EN packet (PR #211) for a bilingual listing.

### P-6. NL editions for the remaining EN-only adult novels (Wire Garden) — batch
**Pitch:** The Wire Garden (WWI Dodendraad, 15,900w) has no NL edition; bring it to Dutch (subtitle mandatory per its collision note — *Een novelle van de Dodendraad*). Buyer: the same Dutch literary-historical shelf that already carries De Papieren Sinaasappel and De zoete zee. Completes NL parity across the adult line so every title is bilingual.
**Effort:** L
**Risk / reversibility:** Low per file, but larger token spend — sequence one title, verify the proofread gate, then the next. New files only; EN untouched.
**Unblocks:** NL-shelf completeness; each NL edition feeds the existing Dutch-language listing funnel.

### P-7. YA line — first NL editions (pilot: one title)
**Pitch:** All 5 YA titles are English-only — the entire YA line has zero Dutch presence despite YA being one of the strongest NL trade categories. Pilot a Dutch edition of the single strongest YA title to test whether NL demand extends past the adult/picture-book shelves. Now: the house already runs trilingual children's books and 13 adult NL editions, so NL production capability is proven — YA is the untested adjacent segment.
**Effort:** L
**Risk / reversibility:** Medium-low — a genuine new-audience swing; reversible as a file, but the YA-register work is real. Pilot ONE, don't batch.
**Unblocks:** Opens a third NL sub-shelf (YA) if the pilot shows any signal; caps downside to one title's tokens.

### P-8. The Paper Orange — German (DE) edition — ambitious swing
**Pitch:** No adult novel has a German edition — DE exists only for picture/board books. The Paper Orange (WWII Hunger Winter, the house's flagship adult title) is the natural first DE title: the German-language market for WWII-occupation literary fiction is large and thematically hungry. In-house DE capability is proven at picture-book scale; this carries it up to adult length.
**Effort:** L
**Risk / reversibility:** Medium — biggest reach in this menu and the most sensitive (occupation subject read by a German audience); reversible as a file but demands the strongest proofread gate. Flagship-only experiment, not a line-wide commitment.
**Unblocks:** Opens an entirely new language market (DE adult); if it lands, a repeatable DE-edition path for the rest of the adult shelf.

### P-9. Audiobook / narration-ready edition spec (lead title: The Paper Orange)
**Pitch:** The catalog has serial, large-print, board-book, and novella-cut editions but NO audio format. Produce a narration-ready EDITION-SPEC: chapter-segmented script, Dutch place/character-name pronunciation guide, front/back-matter read order, per-chapter runtime estimate — everything a narrator or TTS pipeline needs, no recording (recording/spend stays owner-gated). Buyer: readers plus the audiobook channel (Audible/Storytel), a surface the catalog has never touched.
**Effort:** M
**Risk / reversibility:** Low — a spec file; no recording, no spend, no publish. Fully revertible.
**Unblocks:** First audio-channel-ready asset; a reusable spec other titles can follow.

### P-10. The Night Kiln Trilogy — omnibus / box-set editions (EN + NL)
**Pitch:** All three Night Kiln books are complete in both languages (EN Books 1–3; NL De Nachtoven / De Morgendeur / De Oogstslag). Assemble an EN omnibus and an NL omnibus (single-volume front matter, unified TOC, inter-book continuity note) sold as one "box set" SKU at a modest premium over a single book. Buyer: readers who finish Book 1 and want the whole arc. Pure recombination of already-committed, already-verified manuscripts.
**Effort:** S–M
**Risk / reversibility:** Low — derived edition files; component manuscripts untouched; publish owner-gated.
**Unblocks:** Higher-AOV listing off the completed trilogy; template for future series omnibuses.

### P-11. Trilingual board-book "First Library" bundle
**Pitch:** The catalog holds 27 board-book texts (7 title-lines × EN/NL/DE, plus Comet Biscuit ×3). Bundle them as a trilingual "first library" box — a coherent multi-title, three-language board-book set for bilingual/trilingual households (a real, underserved buyer in NL/BE/DE families). The texts already exist; the bundle is a listing + edition-manifest, not new content.
**Effort:** M
**Risk / reversibility:** Low — spec/manifest files; any physical POD/print step stays hard owner-gated (like photo-packs). Digital-side fully revertible.
**Unblocks:** First bundle in the children's line; names a first-ten path (trilingual-parenting communities) distinct from every dev/agent channel.

### P-12. Pricing experiment — PWYW launch + a "Founder's Everything" tiered bundle
**Pitch:** Two grounded pricing tests written as an experiment spec. (a) Launch the AI Novella Production Kit as PWYW with a $19 floor — mirroring the template-packs $19-PWYW format that is the lane's proven low-friction on-ramp — to buy first-sale signal on the writing channel. (b) A tiered "Founder's Everything" bundle stacking the 10 publish-READY dev/agent SKUs at a steep launch discount vs the ~$250 à-la-carte sum, time-boxed, to test whether a catalog-wide anchor converts where singles haven't (0 organic sales to date).
**Effort:** S
**Risk / reversibility:** Low — a spec + draft listings; PWYW floor and time-box cap downside; every price change is a one-click owner edit, instantly reversible. Keep inside the sim-lab-ratified pricing bands (V037–V041).
**Unblocks:** First deliberate pricing signal for the catalog; the everything-bundle gives every single listing an upsell anchor once components are live.

---

## Publishing pipeline / automation

### PUB-1. NL spellcheck-in-CI lane (advisory)
**Pitch:** Wire the new `spylls 0.1.7` + OpenTaal `nl_NL` hunspell v2.20.21 capability (recorded in `docs/CAPABILITIES.md`, first used in PR #215) into a new advisory job in the host-owned `.github/workflows/kit-tests.yml` that runs the same mechanical pass over every `candidates/**/versions/nl/*.md` manuscript on PR. Reuses the exact `continue-on-error` + exit-0 advisory shape of the existing `owner-gate-lint-advisory` / `ledger-drift-advisory` jobs, so a flag never blocks a merge.
**Effort:** M
**Risk / reversibility:** Low — new advisory job only, deletable in one commit; needs to `pip install spylls` and proxy-fetch the dict in-runner (network step), so pin the dict URL/version and fail-safe to a skip line if the fetch 4xx/5xxs.
**Unblocks:** Standing mechanical NL spellcheck on every PR; removes the "did anyone re-run spellcheck after edits?" gap. Stays advisory per the hard rail.

### PUB-2. EN spellcheck lane (`en_US` hunspell) for the EN catalog
**Pitch:** Mirror PUB-1 for the far larger EN catalog (the `en/*.md` masters) using the `en_US` hunspell dictionary from the same LibreOffice source the nl_NL pass proved reachable. Same spylls engine, same filtering scaffold, same advisory contract. The EN masters are canonical (a typo there propagates into every derived edition), so checking them first has leverage.
**Effort:** M
**Risk / reversibility:** Low — second advisory job; independent of the NL lane, revert in isolation.
**Unblocks:** Mechanical proofing coverage for the ~20+ EN titles that currently have none; makes each EN master's PRE-QA a re-runnable artifact.

### PUB-3. Productionize `categorize.py` (the filter the PRE-QA already cites)
**Pitch:** Each NL `PRE-QA.md` §6c cites `categorize.py` as the auditable filter that sorted raw flags into buckets (proper nouns, craft coinages, compounds, accent forms, casing artifacts) down to genuine candidates — but that script was ephemeral and is NOT committed. Commit it under `scripts/` as the shared, tested filter both PUB-1 and PUB-2 call, with a `test_categorize.py` alongside it. Makes "140 → 2" reproducible instead of a claim in prose.
**Effort:** S
**Risk / reversibility:** Trivial — pure additive script + unit test; no workflow or manuscript changes.
**Unblocks:** A single audited filter behind the whole spellcheck lane; closes a dangling reference in four shipped PRE-QA files.

### PUB-4. `NOTES.md`-sourced allowlist as a first-class, tested artifact
**Pitch:** The §6c filter's proper-noun and craft-coinage lists were hand-lifted from each title's `NOTES.md`. Formalize that into a per-title `allowlist.txt` (or a `# Allowlist` fence parsed out of `NOTES.md`) that `categorize.py`/PUB-1 consume, plus a small linter that flags allowlist entries no longer present in the manuscript (stale) and manuscript proper-nouns absent from the allowlist (unmanaged).
**Effort:** M
**Risk / reversibility:** Low — data files + one advisory linter; no gating.
**Unblocks:** Sustainable allowlist maintenance across all NL editions and the EN catalog; stops every craft-coinage from re-flagging on each run (load-bearing, since hunspell nl_NL does no free compounding).

### PUB-5. PRE-QA scaffold generator for the remaining titles
**Pitch:** Only 4 of the 12 NL edition dirs carry a `PRE-QA.md`; the rest, plus the EN masters, have none. Write `scripts/gen_preqa.py` that emits the §1–§6 skeleton (disclaimer preamble, quote-nesting inventory, doubled-word scan, word-count expansion seams vs the EN master, empty §6 spellcheck table) for a given manuscript — mechanical sections auto-filled, human-judgment sections left as prompts.
**Effort:** M
**Risk / reversibility:** Low — generator only; output is a draft a human vets before commit.
**Unblocks:** The 8 NL editions still missing a PRE-QA, and PRE-QA coverage for the EN catalog; scales the PR #214/#215 pattern without linear hand-effort.

### PUB-6. Length-band / expansion-ratio checker
**Pitch:** PRE-QA §5 manually computed expansion over the EN source; the length-band ruling on De Morgendeur/De Oogstslag (`the-night-kiln/LENGTH-BAND-PREP.md`, awaiting a one-word owner ratify) is a live gate. A tiny `scripts/check_length_band.py` computes each version's word count against its EN master, prints the expansion ratio and per-paragraph outliers, and flags any title drifting outside its configured band. Deterministic, stdlib-only.
**Effort:** S
**Risk / reversibility:** Trivial — read-only report script; can also run as a PUB-1-style advisory CI line.
**Unblocks:** Mechanizes PRE-QA §5 for every edition; gives the owner's length-band ruling a live number instead of a stale hand count.

### PUB-7. Structured proofread packet + correction-capture format
**Pitch:** The binding constraint is the owner-only native-speaker proofread pass (19 hard-gated queue rows). Give that pass a structured proofread packet: a generated per-title file that interleaves numbered manuscript lines with the PRE-QA §1–§6 flags inline as checkboxes, plus a defined correction syntax (`L396: schifte → schiftte`) that a companion `scripts/apply_proofread.py` can replay back into the manuscript as a reviewed diff. Closes the loop from "owner marks corrections" to "corrections land on main."
**Effort:** L
**Risk / reversibility:** Medium — the apply step mutates manuscripts, so it must emit a diff for owner review and never auto-commit; the packet-generation half is low-risk on its own and can ship first.
**Unblocks:** Makes the owner's proofread pass a structured, capturable workflow; directly serves the single lever on the ~13 ready NL editions. (Still owner-gated — an AI cannot clear the pass, only tool it.)

### PUB-8. Manuscript-QA linter bundle (repeated-word, quote-nesting, curly-quote, chapter balance, series-name consistency)
**Pitch:** Package the mechanical checks PRE-QA §2/§4 did by hand into one `scripts/manuscript_qa.py` advisory linter: doubled-word finder (skipping grammatical NL pairs), single-outer/double-inner quote-nesting inventory + curly-quote contamination scan, chapter-length balance, and cross-edition name-consistency for series-recurring names. One script, several cheap deterministic checks.
**Effort:** M
**Risk / reversibility:** Low — read-only linter, advisory; slots into the PUB-1 CI lane or runs standalone.
**Unblocks:** Reusable mechanical QA across all editions (NL + EN), including the series-consistency check that currently has no automation.

### PUB-9. OWNER-QUEUE staleness / proofread-gate drift checker
**Pitch:** `OWNER-QUEUE.md` is generated by `scripts/derive_owner_queue.py`; a stale copy is a workflow bug. Add `scripts/check_owner_queue_fresh.py` (advisory, exit-0-always, `continue-on-error` CI line) that re-runs the derive in a temp path and diffs against the committed file — reddening advisory-only if a packet changed but the queue wasn't regenerated. Extend it to a proofread-gate freshness report: count hard-gated rows, list which NL editions lack a PRE-QA, flag any PRE-QA whose §6 run-date is stale vs the manuscript's last touch.
**Effort:** S
**Risk / reversibility:** Trivial — read-only checker mirroring the existing drift/lint advisory scripts; non-gating by construction.
**Unblocks:** Guarantees `OWNER-QUEUE.md` never silently drifts from packets; surfaces PRE-QA/proofread coverage gaps as a standing report.

---

## Revenue path / distribution

### REV-1. ORDER 003 real-Stripe-path spec + vendored-payload test harness (the ⚑B/⚑D unfreeze, kept plan-only)
**Pitch:** ORDER 003 (P0) freezes the ⚑B membership-kit ($49) and ⚑D template-pack ($19) publish clicks because the kit's "Stripe Checkout + webhook, pre-wired" claim never ran against real Stripe. An agent can pre-build the fix as a spec + test harness now: D1a (`customer_email: null` → read `customer_details.email`, pass buyer email into session creation), D1b (kill the invalid `{CHECKOUT_EMAIL}` success-URL placeholder — Stripe supports `{CHECKOUT_SESSION_ID}` only), plus HTTP-layer tests driven by a vendored Stripe sample payload.
**Effort:** M
**Risk / reversibility:** Fully reversible; docs+code only. **Owner-gated:** the ⚑B/⚑D publish clicks stay frozen until owner go; a real Stripe live signing secret for a true end-to-end run is owner-only.
**Unblocks:** first dollar on the $49 + $19 tier — the unfreeze path that lets the owner queue the ⚑B/⚑D clicks with non-author real-path evidence.

### REV-2. "Why zero sales" funnel diagnostic for the live SWTK before the T+14 kill clock
**Pitch:** The live Stripe Webhook Test Kit ($29) is in measurement mode with a hard kill rule: ≥1 organic sale OR ≥1 qualified inbound by 2026-07-26 or delist; T+7 checkpoint 2026-07-19 (3 days out). An agent can write a diagnostic that decomposes the funnel into the two agent-visible signals (dev.to reactions/comments; owner-dashboard Gumroad views/sales) and enumerates ranked zero-sale causes, each with the cheapest disambiguating test.
**Effort:** S
**Risk / reversibility:** Pure analysis doc, zero risk, no spend. **Owner-gated:** the authoritative sales/view numbers live only on the owner's Gumroad dashboard.
**Unblocks:** turns the 2026-07-19 checkpoint into an evidence-based keep/pivot/delist call; protects the one live SKU.

### REV-3. Conversion-tracking / UTM instrumentation spec across the funnel
**Pitch:** The funnel has no attribution — agent surfaces can't see sales and dev.to view counts are private, so the owner can't tell which channel drove a click. Spec a lightweight no-JS tracking convention: distinct UTM-tagged listing URLs per channel, a naming scheme for the 45 queued click-run sequences, and a one-page "read your Gumroad analytics" owner playbook mapping UTM → channel ROI.
**Effort:** S
**Risk / reversibility:** Spec only, reversible, no spend. **Owner-gated:** owner pastes the UTM'd URLs when posting.
**Unblocks:** first-ten-customers attribution — the owner learns which channel converts, so effort concentrates on the winner.

### REV-4. Catalog landing/SEO microsite — static, self-hosted, agent-buildable now
**Pitch:** 10 publish-READY SKUs + 1 live, but the only web presence is scattered Gumroad listings and one dev.to article. Build a static catalog site — one SEO-targeted landing page per product reusing the already-written `docs/launch/*/listing-copy.md` + `one-pager.md` + the real `demo-transcript.md` — with keyword-targeted titles. Ships as HTML in-repo; publishes only on owner go.
**Effort:** M
**Risk / reversibility:** Build-in-repo, fully reversible; nothing goes live without owner deploy. **Owner-gated:** hosting/domain/DNS and the deploy are owner spend + owner click.
**Unblocks:** an evergreen SEO funnel-top feeding all live listings — first-ten via search intent rather than one-shot forum posts.

### REV-5. Product-Hunt / HN / Reddit launch kit + email-capture sequence spec
**Pitch:** `docs/distribution/launch-posts.md` already has Show HN + Reddit + X drafts for the membership kit, but no Product Hunt asset, no launch-day sequencing, no email capture. Extend the kit: a Product Hunt listing draft, a launch-day runbook (channel order, spacing, comment-reply templates), and an email-capture + 3-email nurture sequence spec. All drafted, none sent.
**Effort:** M
**Risk / reversibility:** Drafts only, reversible. **Owner-gated:** every post and every email SEND is owner-only; an email-capture form needs an owner-created ESP account.
**Unblocks:** a repeatable launch playbook for each of the 10 ready SKUs, plus a captured audience.

### REV-6. Free-tier lead magnet + bundle-economics experiment from the existing catalog
**Pitch:** Spec a lead-magnet strategy — carve a genuinely-free micro-kit (e.g. the vendored Stripe gotcha fixtures + the "false-green test trap" one-pager) given away for an email, funneling into the $29/$49 paid kits — plus a bundle-economics memo modelling the anchor pricing already in the packets and proposing one measured cross-sell (SWTK buyers → GitHub Webhook Test Kit). Pricing stays inside the sim-lab-ratified bands.
**Effort:** S
**Risk / reversibility:** Spec/memo only; respects the V037–V041 pricing verdicts. **Owner-gated:** the free kit needs the owner's ESP/storefront; any new price is an owner click.
**Unblocks:** top-of-funnel email volume + a first-dollar path that doesn't depend on cold traffic converting at full price.

### REV-7. Book-catalog revenue path — KDP-first spec with a Leanpub/serialization/newsletter fork
**Pitch:** The catalog is enormous (15 EN adult manuscripts, 13/13 NL editions, YA/MG/picture lines) but the entire revenue path is 268 owner clicks stalled at "KDP account + tax/bank interview," 19 sequences hard-gated on native-speaker proofreads. Write the revenue-path spec: (a) a minimal KDP launch-wave plan — which 2-3 un-gated EN novels go first to de-risk account setup; (b) a Leanpub/serialization fork as an alternative to KDP-Select exclusivity; (c) a reader-newsletter spec turning the catalog into a recurring owned channel.
**Effort:** M
**Risk / reversibility:** Planning doc, reversible; consumes existing packet pricing. **Owner-gated:** KDP account + tax/bank interview, cover-art spend, and native-speaker proofread commissioning are all owner-only.
**Unblocks:** first-ten-readers — sequences the dormant book inventory into an actual launch wave; names the non-Amazon revenue options.

### REV-8. Cross-sell hub + storefront consolidation for the dev-tool kit family (ambitious swing)
**Pitch:** Six dev-tool kits share one buyer persona (the agent-fleet / indie-dev operator) yet sell as isolated Gumroad listings with no cross-sell. Spec a "dev-tools hub": a consolidated storefront/collection page, cross-sell copy blocks appended to each listing, a tiered offer ladder (single kit → Ship-It bundle → an all-kits "fleet bundle"), and the bundle economics for a larger multi-kit bundle.
**Effort:** L
**Risk / reversibility:** All copy/spec, reversible; a larger multi-kit bundle price needs a sim-lab verdict before any click (flagged). **Owner-gated:** creating the storefront collection, any new bundle SKU, and every listing edit are owner clicks.
**Unblocks:** raises average order value and repeat-buyer lifetime value across the kit family — a first-hundred-customers structure.

---

## Ops / infra / repo-health

### OPS-1. Retire the legacy root `claims/` dir — one claim home, not two
**Pitch:** Two claim directories exist — canonical `control/claims/` (pinned in `substrate.config.json`) and legacy root `claims/`, which now holds only a `README.md` and zero live claims. The checker already nags `claims-legacy-location` on anything landing in root `claims/`. Delete root `claims/` and leave a one-line redirect, or fold its README into `control/claims/README.md`.
**Effort:** S
**Risk / reversibility:** Trivial — dir is empty of live claims; fully reversible. Confirm no script hard-codes root `claims/`.
**Unblocks:** One canonical claim path; kills a standing source of `claims-legacy-location` noise and reader confusion.

### OPS-2. Heartbeat-freshness advisory on `control/status.md`
**Pitch:** `status.md` carries an `updated:` ISO stamp but nothing flags when it goes stale relative to main HEAD. A tiny stdlib advisory — same exit-0-always contract as `check_ledger_drift.py` — that prints `heartbeat: fresh / stale by Nh` gives a fresh seat an instant "is the last heartbeat trustworthy?" read.
**Effort:** S
**Risk / reversibility:** Very low — advisory-only, exits 0 on every path; delete to revert. Never gates.
**Unblocks:** Fast staleness read for cold starts; a candidate line for the scheduled `main-verify.yml` summary.

### OPS-3. Promote the owner-gate lint from advisory to a required gate
**Pitch:** `scripts/lint_owner_gates.py` is a strict, deterministic, stdlib-only linter but runs `continue-on-error: true` in `kit-tests.yml`, so a malformed §7 OWNER-GATE never reds a PR — the exact silent-drift class the script catches. Since the OWNER-QUEUE is the click surface the owner acts on, a broken gate shipping green is high-cost. Flip this one advisory to a required check (keep `check_ledger_drift` advisory).
**Effort:** S
**Risk / reversibility:** Low but real — a strict gate can red a legitimate PR on a malformed packet; reversible by flipping `continue-on-error` back. Recommend a short bake as reported-but-non-required first.
**Unblocks:** Owner-facing queue data can't silently drift into malformed §7 without CI catching it.

### OPS-4. Scheduled sweeper that prunes claim files whose PR has merged
**Pitch:** Claims are "delete at session close," but sessions that die mid-turn leave them behind. Automate it: a scheduled job that, for each `control/claims/*.md`, checks whether its branch token's PR is merged (or the claim is >72h idle) and opens a prune PR. Advisory-open-a-PR (not auto-delete) keeps the enabler in the loop.
**Effort:** M
**Risk / reversibility:** Medium — must never prune a live claim; key off merged-PR state before age; open-a-PR not auto-delete; fully reversible.
**Unblocks:** `control/claims/` reliably reflects only in-flight work; less collision-scan noise for concurrent lanes.

### OPS-5. Docs-freshness checker — flag stamped docs that lag main HEAD
**Pitch:** Many docs self-stamp a refresh date + HEAD/PR pin and drift: `docs/NEXT-SESSION.md` — the cold-start brief — is stamped at PR #165 while main is at PR #215. A stdlib advisory that scrapes header stamps and prints which docs lag current HEAD beyond a threshold turns "is this brief current?" into a checked fact (allow a `Status: historical` opt-out).
**Effort:** S–M
**Risk / reversibility:** Low — advisory, exits 0; heuristic scrape may false-positive on intentionally historical docs (opt-out marker). Reversible by deletion.
**Unblocks:** A recreating owner / fresh seat can trust which orientation docs are current.

### OPS-6. Doc link-checker + planted-set orphan checker
**Pitch:** `docs/AGENT_ORIENTATION.md` asserts its planted doc set "reaches every live doc" — a contract nothing enforces. A stdlib checker that (a) resolves every relative Markdown link under `docs/` + root and reds on a broken target, and (b) flags any `docs/*.md` not reachable from the planted set (orphan detection). Links are clean today, so this locks in a good state cheaply.
**Effort:** M
**Risk / reversibility:** Low — start advisory (report-only), promote to gating once the orphan list is triaged. Anchor-fragment checking can be phase 2.
**Unblocks:** Cross-doc references stay resolvable as the tree churns; new docs can't silently become orphans.

### OPS-7. Auto-merge / merge-queue readiness self-check script
**Pitch:** The landing path depends on two owner-set repo settings no agent can read via API ("Allow auto-merge" ON, a ruleset making `substrate-gate` required). A `scripts/check_merge_readiness.py` (run in `main-verify.yml`) that probes the branch ruleset for the required `substrate-gate` context and prints a green/red readiness line gives a fresh seat on a recreated project an immediate "can my PRs actually self-land?" answer.
**Effort:** M
**Risk / reversibility:** Low — read-only probe, advisory output; reversible by deletion.
**Unblocks:** Detects the "required check missing → PRs merge instantly, or never" misconfiguration before it costs a landing.

### OPS-8. One canonical START-HERE doc + a 5-question orientation self-test
**Pitch:** Boot reading is spread across `CONSTITUTION.md`, `docs/AGENT_ORIENTATION.md`, `docs/NEXT-SESSION.md`, `docs/current-state.md`, `docs/reading-path.md` — a fresh seat must reconstruct the boot ritual from five cross-pointing files. Add a single top-level `START-HERE.md`: the exact preflight commands, the inbox-diff rule, born-red-card-first, the ordered read list, and a 5-question orientation self-test — a thin router pointing at the existing sources of truth, not a new copy of record.
**Effort:** M
**Risk / reversibility:** Low — additive doc; risk is minting a sixth competing entry point, so it must be a thin router. Reversible by deletion.
**Unblocks:** A recreated-tomorrow seat picks up from the repo alone; cuts orientation turn-cost.

### OPS-9. Machine-readable repo-state file + "60-second state" / dashboard generator
**Pitch:** Every session rebuilds the same state picture by hand-reading prose and running greps; `project.index.json` is still an untouched stub. Add a generator that emits a derived, byte-deterministic `STATE.json` (+ a rendered 60-second summary): catalog counts, live products + kill-clock status, open-PR state, session-card count, last-heartbeat age, PR-velocity. Same "derived render, never edited" contract as `docs/seat-digest.md`.
**Effort:** L
**Risk / reversibility:** Medium — must be generated from sources of truth (regenerate, never hand-edit) to avoid a fourth authored copy that drifts; deterministic (no wall-clock in the JSON body). Reversible by deletion.
**Unblocks:** Big cut to per-session orientation tool-call cost; a machine surface the fleet-manager and a fresh seat can both consume.

---

## Shipped with this PR (small, reversible hygiene)

- **Pruned 3 stale claim files** for merged PRs #213/#214/#215 (`control/claims/2026-07-16-proofread-gate-detection.md`, `-pre-qa-notes.md`, `-nl-spellcheck.md`) — convention is delete-at-session-close; direct precedent PR #212.
- **Staleness banner on `docs/NEXT-SESSION.md`** — its catalog counts are stamped at PR #165 (2026-07-13) and predate ~50 merged PRs; the banner points to `docs/current-state.md` (refreshed 2026-07-16) as the fresher ledger. A recreate-tomorrow seat won't act on 3-day-old numbers.

## Spotted but deferred (owner/manager call)

- **Retire the empty legacy root `claims/` dir** (OPS-1) — a convention decision left for owner/manager veto rather than done unilaterally tonight.
