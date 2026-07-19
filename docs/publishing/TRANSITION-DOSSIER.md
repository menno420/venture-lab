# Venture Transition Dossier — venture-lab

> **Status:** `reference`
>
> **Purpose:** one neutral, verifiable snapshot of every sellable, book property, open
> owner decision, asset location, and the exact post-cutoff resume path for the venture-lab
> venture — so nothing is lost across the read-only cutover. **State as of 2026-07-19; cutoff
> 2026-07-21** (the Claude Code Projects EAP goes read-only that day). Live HEAD `2be4065`
> (PR #273); `python3 bootstrap.py check --strict` green. Compiled read-only — no repo files
> edited to produce it (this doc + one index row in `docs/publishing/README.md` are the only
> additions).

## ⚑ Known drift — read this first

`docs/current-state.md` is **stale vs the live tree**. It is stamped at HEAD `7d5229f` /
"latest merged PR #253" (restamped 2026-07-18). Live HEAD is `2be4065` / PR #273. Everything
merged after #253 is **absent from current-state.md**, most importantly:

- The **5 new book sequels** (#268–#272) — see Section 2.
- The ENG-pipeline CI guards (#262–#266) and the docs link-integrity checker.
- The end-of-session heartbeats #267 and #273.

Where current-state.md and the live tree disagree, **trust this dossier and the live tree** (and
the generated `docs/publishing/OWNER-QUEUE.md`, the authoritative owner-action queue); the drift
is flagged inline below. `docs/current-state.md` itself states "Source code and merged work always
win over this file."

---

## 1. Sellables + status

Authoritative sources: `docs/launch/CATALOG.md` (storefront comparison) and the generated
`docs/publishing/OWNER-QUEUE.md` (28 decisions D1–D28 + paste-ready click-runs). Every publish is
an **owner click** — the seat performed none.

### Currently LIVE (1)

| SKU | Price | Where it lives | What owner must do |
|---|---|---|---|
| **Stripe Webhook Test Kit** | $29 one-time | code `candidates/stripe-webhook-test-kit/` · listing `docs/launch/stripe-webhook-test-kit/LISTING.md` · packet `docs/publishing/vetting/stripe-webhook-test-kit.md` | **Already live** on Gumroad since 2026-07-12 (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>). Under a measurement **kill clock**: T+7 checkpoint 2026-07-19, **T+14 kill-rule 2026-07-26** (≥1 organic sale OR ≥1 qualified inbound, else pause/delist). 0 organic sales recorded; Gumroad views/sales are owner-dashboard-only. |

### Publish-READY (19) — built + priced + listing drafted + verified; one owner click from live

Each lives at `candidates/<slug>/` (code) + `docs/launch/<slug>/` (listing/owner-actions) +
`docs/publishing/vetting/<slug>.md` (vetting packet, §7 = owner click-run). Publish = owner Gumroad click.

| SKU | Price | Queue D# | Slug |
|---|---|---|---|
| GitHub Webhook Test Kit | $29 | D6 | `github-webhook-test-kit` |
| Slack Webhook Test Kit | $29 | D20 | `slack-webhook-test-kit` |
| Shopify Webhook Test Kit | $29 | D19 | `shopify-webhook-test-kit` |
| Idempotency Key Test Kit | $29 | D7 | `idempotency-key-test-kit` |
| Rate-Limit Test Kit | $29 | D18 | `rate-limit-test-kit` |
| Pagination Test Kit | $29 | D15 | `pagination-test-kit` |
| JWT Auth Test Kit | $29 | D9 | `jwt-auth-test-kit` |
| CORS Preflight Test Kit | $29 | D4 | `cors-preflight-test-kit` |
| Membership-Site Boilerplate Kit | $49 | D11 | `membership-kit` |
| Agent-Workflow Template Pack | $19 PWYW | D21 | `template-packs` |
| Owner-Click Queue Kit | $19 | D14 | `owner-click-queue-kit` |
| Multi-Agent Control-Plane Pack | $29 | D13 | `multi-agent-control-plane-pack` |
| Agent Fleet Field Manual | $39 | D1 | `agent-fleet-field-manual` |
| The False-Green Test Trap | $15 | D5 | `false-green-test-trap` |
| The Agent Merge-Wall Cookbook | $19 | D12 | `merge-wall-cookbook` |
| The Auto-Merge Enabler Cookbook | $19 | D3 | `auto-merge-enabler-cookbook` |
| The Idempotency & Retry Cookbook | $19 | D8 | `idempotency-retry-cookbook` |
| Kill-Rule Intake Kit | $15 | D10 | `kill-rule-intake-kit` |
| AI Novella Production Kit | $29 | D2 | `ai-novella-production-kit` |

**To ship any READY SKU:** owner opens gumroad.com → New product → Digital product (same account
as the live Stripe kit), picks the storefront, uploads the zip + sha256 spot-check, pastes listing
copy, sets price, publishes + test-purchases + copies the public URL. Paste-ready steps are in each
packet's §7 and in `docs/publishing/OWNER-QUEUE.md` §2.

### Hard-gated bundles (3) + Photo Packs — NOT publish-ready

| Item | Price | Gate (what unblocks it) | Where |
|---|---|---|---|
| **Ship-It Bundle** | $59 | Membership (D11) + Template Pack (D21) publish clicks | listing `candidates/BUNDLE-LISTING.md` · packet `docs/publishing/vetting/bundle-starter.md` |
| **Webhook Verifier Bundle** | $79 | GitHub (D6) + Slack (D20) + Shopify (D19) publish clicks (Stripe already LIVE) | `candidates/webhook-verifier-bundle/` · `docs/publishing/vetting/webhook-verifier-bundle.md` |
| **API Robustness Bundle** | $79 | Idempotency (D7) + JWT (D9) + Pagination (D15) + Rate-Limit (D18) publish clicks | `candidates/api-robustness-bundle/` · `docs/publishing/vetting/api-robustness-bundle.md` |
| **Photo Packs** (Dutch Skies + Golden Hours) | $5/pack | Owner hands off **full-res originals** (held off-repo) + licensing/curation pass; then storefront (D16) + price (D17) | `candidates/photo-packs/` · `docs/publishing/vetting/photo-packs.md` |

A bundle references its components as *existing live listings*, so it cannot be created until those
components are published.

**KDP book packages (5 new, upload-ready — arrive with PR1):** see Section 2. Each of the 5 new
sequels now has an upload-ready KDP package (compiled manuscript + KDP metadata block + self-edit
log). These are book properties on the KDP lane, hard-gated on the owner-only native-speaker
proofread; they are not Gumroad SKUs.

**Distribution assets (free, NOT sellables):** four lead-magnet funnel-tops —
`docs/launch/api-robustness-lead-magnet.md`, `docs/launch/agent-ops-lead-magnet.md`,
`docs/launch/membership-lead-magnet.md`, `docs/launch/ai-novella-lead-magnet.md` — governed by
`docs/launch/DISTRIBUTION-PLAYBOOK.md`. Posting is an owner paste-and-post, never auto-publish.
**Distribution, not catalog size, is the binding revenue constraint** (1 LIVE, 0 organic sales,
19 READY undiscovered).

---

## 2. Book properties + next hook

Books live under `candidates/`. The binding lever across the whole book catalog is the **owner-only
native-speaker proofread pass** — an AI cannot clear it; every NL edition packet is hard-gated on it,
and it is the last human step on the 5 new EN sequels' KDP packages. KDP publishing (account, title
recheck, cover, publish click) is owner-gated.

> **current-state.md is stale here.** Its "Book catalog" section predates the 5 sequels below and
> still calls the Night Kiln a two-book set. The live tree has the sequels; recount from the
> `candidates/` tree when a precise figure is needed.

### ⭐ The 5 NEW books (#268–#272, merged 2026-07-19) + their upload-ready KDP packages

| # | Series · Book | Title | Manuscript source | KDP-ready package (arrives with PR1) |
|---|---|---|---|---|
| #269 | The Night Kiln · **Book 4** | *The Winter Wheel* | `candidates/adult-novels/the-night-kiln/en/the-winter-wheel.md` | `candidates/adult-novels/the-night-kiln/kdp-ready/book-4/` |
| #272 | The Night Kiln · **Book 5** | *The Spring Cup* | `candidates/adult-novels/the-night-kiln/en/the-spring-cup.md` | `candidates/adult-novels/the-night-kiln/kdp-ready/book-5/` |
| #270 | Ultramarine · **Book 2** | *The Blue and the White* | `candidates/adult-novels/ultramarine/book2/the-blue-and-the-white.md` | `candidates/adult-novels/ultramarine/kdp-ready/book-2/` |
| #268 | Lull (Dreamline) · **Book 2** | *The Mirror City* | `candidates/dream-series/book2/` | `candidates/dream-series/kdp-ready/book-2/` |
| #271 | Lull (Dreamline) · **Book 3** | *The Fourth Hour Comes* | `candidates/dream-series/book3/` | `candidates/dream-series/kdp-ready/book-3/` |

Each KDP-ready package folder holds three files: `MANUSCRIPT-KDP.md` (compiled single-file
manuscript), `KDP-METADATA.md` (the KDP metadata block — title/subtitle/series/categories/keywords/
price/KU), and `SELF-EDIT-PASS.md` (the self-edit log). **Remaining owner-gated step for all five:**
the owner-only **native-speaker proofread**, the **keyword-map §3 niche reservation** in
`docs/publishing/keyword-map.md`, and a **vetting packet** under `docs/publishing/vetting/` (none of
the five has one yet) — after which the KDP publish click is itself owner-gated.

- **Night Kiln** is now a **5-book cozy-fantasy novella series** (en/: Bk1 *The Night Kiln*,
  Bk2 *The Morning Door*, Bk3 *The Harvest Rows*, Bk4 *The Winter Wheel*, Bk5 *The Spring Cup*),
  with a **planted (unwritten) Book-6 hook**. Cover briefs + listing copy for Bk4/Bk5 are present
  (`candidates/adult-novels/the-night-kiln/book-4-cover-brief.md`,
  `candidates/adult-novels/the-night-kiln/book-4-listing-copy.md`, and the `book-5-*` siblings).
- **Lull / Dreamline** MG portal-fantasy trilogy is now **COMPLETE (Books 1–3)** — see
  `candidates/dream-series/series-arc.md`. Published series title **Lull**; DREAMLINE is the working
  codename. Book 2/3 listing + cover-brief assets present. **Next hook:** the trilogy is closed (all
  three series questions resolved); "next" is NL editions / a fiction funnel, not more books.
- **Ultramarine Book 2** is a Delft historical-fiction sequel with a **Book-3 hook**; Book 1's public
  title is still an open owner pick (see Section 3).

### Adult novels — `candidates/adult-novels/`

EN title-lines (each has README + DECISIONS + an `en/` manuscript; most have a KDP vetting packet
under `docs/publishing/vetting/` with listing copy + title-availability + price recommendation):
`the-glass-rectory` · `the-marmalade-post` · `the-night-kiln` (5-book series) · `the-paper-orange` ·
`the-salvage-orchard` · `the-seed-catalogue-courtship` · `the-slow-word` · `the-twelfth-cake` ·
`the-weigh-house` · `the-salt-bell` · `the-sweetwater-sea` · `the-wire-garden` · `ultramarine`
(2-book series). All have KDP publish click-runs queued in OWNER-QUEUE §2 (price band $3.99–$4.99).
**Next hook:** owner KDP account + publish click; several have an open **title decision** (Section 3:
D24 Weigh House, D26 Ultramarine title).

**NL adult editions** live alongside under `candidates/adult-novels/` (each sequenced behind its EN
edition; packets under `docs/publishing/vetting/`, price band €3.99–€4.99), all **HARD-GATED on the
native-speaker proofread**. **Next hook (binding):** owner-only native-speaker NL proofread, then
title recheck + publish.

### YA novels — `candidates/ya-novels/`

Titles: `hollowtide`, `the-last-good-frequency`, `the-marginalia-society`, `the-pepper-ledger`,
`the-undertow`. `the-marginalia-society` and `the-pepper-ledger` have KDP vetting packets + publish
click-runs (price $3.99). **Next hook:** owner KDP publish; the roadmap flags a "YA line first NL
edition pilot" gated on the NL proofread.

### Middle-grade — `candidates/middle-grade/`

`the-halfway-ferry` (vetting packet + publish click-run, $3.99). **Next hook:** owner KDP publish
(art spend incl. a spot-art call).

### Dream-series (Lull) — `candidates/dream-series/`

Covered above (the 5-NEW list; Books 2–3). Bible, series arc, per-book outlines, DECISIONS, listing +
cover-brief for Bk2/Bk3. Owner-directed creative project (conservative near-term revenue $0 per its
INTAKE). **Next hook:** trilogy complete — owner creative sign-off / eventual publish path; no more
books queued.

### Children's books — `candidates/childrens-books/`

Trilingual (EN/NL/DE) title-lines incl. `painted-stones`, `the-puddle-museum`, `the-windmill-mouse`,
`bram-the-yak`, `comet-biscuit`, `dormouse`, `star-pirates`, `the-lantern-door`, `tummel`. Three have
KDP vetting packets — `the-painted-stones`, `the-puddle-museum`, `the-windmill-mouse` — each
**hard-gated on an illustration money-decision** (D22/D23/D25, Section 3), price $12.99. **Next hook:**
owner Commission / AI-art / Park decision (seat recommends **Park**); NL/DE are native-quality parallel
versions, not translations.

---

## 3. Open owner decisions

Sources: `docs/publishing/OWNER-START-HERE.md` (one-sitting digest), `docs/publishing/OWNER-QUEUE.md`
(exhaustive: 28 decisions D1–D28 + click-runs), `docs/ideas/2026-07-18-veto-ready-menu.md`,
`control/inbox.md` ORDERs.

### A. The Stripe-kit kill-clock read (time-boxed)

- **What:** Read the Gumroad dashboard views + sales for the live Stripe kit (and the dev.to article
  stats), then make the keep/iterate/delist call. **T+7 checkpoint due 2026-07-19** (read-only — the
  seat cannot see these numbers). **T+14 kill deadline 2026-07-26:** if still 0 organic sale AND 0
  qualified inbound, pause/delist.
- **Where:** `docs/publishing/OWNER-START-HERE.md`; reasoning in `docs/launch/funnel-diagnostic.md`
  + decision packet `docs/launch/kill-clock-decision-packet.md`; record
  `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`.
- **"Done" looks like:** owner has jotted views+sales, left the listing live today; the kill call is
  made by 2026-07-26. Recommendation: KEEP today, decide at T+14.

### B. Publish clicks (survive the cutover; batch pre-cutover per OWNER-START-HERE)

- **What:** The 19 READY publish clicks + 3 bundle creations, ordered highest-leverage-first:
  GitHub/Slack/Shopify $29 → Webhook Verifier Bundle $79; Idempotency/Rate-Limit/Pagination/JWT $29 →
  API Robustness Bundle $79; Membership $49 + Template Pack $19 → Ship-It Bundle $59; then the
  remaining standalone kits/guides (no bundle gate).
- **Where:** `docs/publishing/OWNER-START-HERE.md` + `docs/publishing/OWNER-QUEUE.md` §1 (storefront
  picks) & §2 (paste-ready click-runs). Pre-EAP ordering: `docs/launch/pre-eap-sprint-plan.md`.
- **"Done" looks like:** each public URL loads a purchasable page at the listed price and a test
  purchase delivers the zip; bundles deliver all component zips.

### C. Book / photo / illustration decisions in the queue (D16–D28)

- **D16/D17 Photo Packs** — storefront + price ($5/pack); hard-gated on owner handing off full-res
  originals + licensing pass (`docs/publishing/vetting/photo-packs.md`).
- **D22 The Painted Stones · D23 The Puddle Museum · D25 The Windmill Mouse** — illustration
  money-decision (Commission / AI-art / Park; seat recommends **Park**). Blocking gate on each picture
  book (packets under `docs/publishing/vetting/`).
- **D24 The Weigh House** — title + subtitle confirm (default "An Amsterdam Crime Novel").
- **D26 Ultramarine** — title pick (default "The Widow's Blue — A Novel of Delft, 1654").
- **D27 Weduwenblauw** — NL title coupling — hard-gated on the NL proofread.
- **D28 Keyword map C1** — Literary-Fiction category dispute (The Slow Word vs Ultramarine); default
  = accept proposed resolution (`docs/publishing/keyword-map.md`).
- **Native-speaker proofread pass** — the binding gate on all NL editions AND the last human step on
  the 5 new EN KDP packages (an owner commission/approval, a real reading task, not a click).

### D. The veto menu (planning skim, not a click)

- **What:** Skim `docs/ideas/2026-07-18-veto-ready-menu.md` (64 `###` proposals across seven areas)
  and strike anything the owner does not want built. Groomed/sequenced into
  `docs/ideas/2026-07-19-execution-roadmap.md`.
- **"Done" looks like:** lines struck; survivors become the seat's approved build queue.

### E. Trading data provisioning

- **Not recorded as an open owner decision in venture-lab.** `docs/current-state.md` contains no
  trading reference; the only mention is a **scope note** in the veto menu and the execution roadmap
  stating trading planning is a **separate repo/PR** with no venture work sequenced against it. If a
  trading data-provisioning decision exists, it lives in the trading repo, not here (see Section 6).

### F. Carried infrastructure flag (not a build/publish item)

- **⚑ Failsafe seat write-wall** (from current-state.md): the persistent failsafe wake session has
  **no write access** to venture-lab (`git push` → 403). Owner action: enable venture-lab write for
  that seat, or accept observe-only. Per-seat token wall, not repo-wide.

---

## 4. Asset map

| Asset class | Location (repo-relative) |
|---|---|
| Sellables code (SKUs, kits, bundles) | `candidates/<slug>/` (e.g. `candidates/stripe-webhook-test-kit/`, `candidates/webhook-verifier-bundle/`) |
| Bundle listing source | `candidates/BUNDLE-LISTING.md` |
| Storefront catalog / positioning | `docs/launch/CATALOG.md` |
| Per-SKU listing copy + owner-actions | `docs/launch/<slug>/` (e.g. `docs/launch/github-webhook-test-kit/owner-actions.md`) |
| Funnel / lead-magnet assets | `docs/launch/api-robustness-lead-magnet.md` · `docs/launch/agent-ops-lead-magnet.md` · `docs/launch/membership-lead-magnet.md` · `docs/launch/ai-novella-lead-magnet.md` · `docs/launch/DISTRIBUTION-PLAYBOOK.md` · `docs/launch/distribution-drafts.md` |
| Owner action queue (generated) | `docs/publishing/OWNER-QUEUE.md` (28 decisions + click-runs) |
| Owner one-sitting digest | `docs/publishing/OWNER-START-HERE.md` |
| Vetting packets (57) — SKUs + books | `docs/publishing/vetting/<slug>.md` (each §7 = owner click-run) |
| Keyword / category map | `docs/publishing/keyword-map.md` |
| Book manuscripts | `candidates/adult-novels/` · `candidates/ya-novels/` · `candidates/middle-grade/` · `candidates/dream-series/` · `candidates/childrens-books/` |
| KDP-ready book packages (5 new; arrive with PR1) | `candidates/adult-novels/the-night-kiln/kdp-ready/book-4/` · `.../book-5/` · `candidates/adult-novels/ultramarine/kdp-ready/book-2/` · `candidates/dream-series/kdp-ready/book-2/` · `.../book-3/` |
| Kill-clock / funnel diagnostics | `docs/launch/funnel-diagnostic.md` · `docs/launch/kill-clock-decision-packet.md` · `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md` |
| Planning menus / roadmaps | `docs/ideas/2026-07-18-veto-ready-menu.md` · `docs/ideas/2026-07-19-execution-roadmap.md` · `docs/ideas/2026-07-18-next-wave-roadmap.md` · `docs/NEXT-TASKS.md` |
| Session cards | `.sessions/` (one card per slice) |
| Control / ledgers | `control/inbox.md` (ORDERs) · `control/status.md` (heartbeat) · `control/claims/` (one file per claim) |
| Living state ledger | `docs/current-state.md` (⚑ stale — see top of this dossier) |
| Conventions / doctrine | `docs/conventions.md` · `docs/ROUTINES.md` (dormant) · `docs/PLATFORM-LIMITS.md` · `docs/review-queue.md` |
| CI guards | `.github/workflows/kit-tests.yml` · `.github/workflows/auto-merge-enabler.yml`; scripts `scripts/check_catalog_drefs.py`, `scripts/derive_owner_queue.py`, `scripts/check_ledger_drift.py`, `scripts/check_kill_clocks.py`, `scripts/lint_owner_gates.py` |
| Kit runtime / gate | `bootstrap.py` (`python3 bootstrap.py check --strict` = pre-push gate) · `substrate.config.json` |
| Publishing lane index | `docs/publishing/README.md` · `docs/publishing/PUBLISHING-PLAN.md` · `docs/publishing/CHECKLIST.md` |

---

## 5. Resume path — reopening work after the cutoff

For the owner or a future agent seat picking this up post-2026-07-21.

1. **Do NOT re-arm routines during EAP.** `control/inbox.md` ORDER 015 supersedes the dormancy/re-arm
   pending the owner's per-project reboot review — "do NOT re-arm routines yet; wait for the owner's
   per-seat go." All EAP-era triggers are DEAD. Re-arming is a deliberate owner action post-relaunch.
   Doctrine (dormant): `docs/ROUTINES.md`.

2. **Boot reading order** (per `docs/conventions.md`): working agreement → `docs/current-state.md`
   (living ledger, but **verify against the live tree — it lags**, see top of this dossier) →
   `docs/NEXT-TASKS.md` → `docs/launch/CATALOG.md` → `docs/ideas/2026-07-19-execution-roadmap.md`.
   `control/status.md` is a neutral pointer, not a source of truth.

3. **Where the backlog lives:** the standing backlog is the 64-item veto menu
   `docs/ideas/2026-07-18-veto-ready-menu.md`, groomed/sequenced in
   `docs/ideas/2026-07-19-execution-roadmap.md` (autonomous-safe lane first, owner-gated lane grouped
   by gate). Items already shipped are marked DONE — do not re-propose.

4. **Finishing the 5 new KDP book packages (deterministic next slice):** the compiled packages land at
   `candidates/adult-novels/the-night-kiln/kdp-ready/book-4/` & `.../book-5/`,
   `candidates/adult-novels/ultramarine/kdp-ready/book-2/`, and
   `candidates/dream-series/kdp-ready/book-2/` & `.../book-3/`. Each is done through the self-edit pass;
   the three remaining steps are all owner-gated / owner-only: (a) the **native-speaker proofread**,
   (b) a **keyword-map §3 niche reservation** in `docs/publishing/keyword-map.md` for each new title,
   and (c) a **vetting packet** under `docs/publishing/vetting/` per title (regenerating
   `docs/publishing/OWNER-QUEUE.md` with `scripts/derive_owner_queue.py` after adding any §7 block —
   never hand-edit the generated queue). Then the KDP publish click, itself owner-gated.

5. **Landing mechanics** (`docs/conventions.md`): born-red session card → open a READY (non-draft)
   `claude/`-headed PR → CI green → agent merges it directly (`merge_pull_request`) OR
   `auto-merge-enabler.yml` squash-merges automatically. Merging is normal agent work, never routed to
   the owner; opt out with a `do-not-automerge` label. Review is post-merge (`docs/review-queue.md`);
   veto = revert. Run `python3 bootstrap.py check --strict` (green) before every push.

6. **The walls (owner-gated, unchanged by any relaunch):** external **publish** and **spend** are
   owner-only — every publish is a manual owner Gumroad/KDP click, never a deploy (venture-lab hosts no
   running service). The **native-speaker proofread** gate is owner-only. Secrets, rulesets/settings,
   and destructive prod-data are owner-only. After any packet edit, re-run
   `scripts/derive_owner_queue.py` to regenerate `docs/publishing/OWNER-QUEUE.md` (a stale generated
   queue is a workflow bug).

---

## 6. Trading lane (one-liner)

The trading-strategy repo is a **separate paper/research lane, out of scope here** — this dossier did
not read it; within venture-lab, `docs/current-state.md` records **no** trading data-provisioning
decision (no trading reference at all), and the only cross-repo note is a scope-only line in
`docs/ideas/2026-07-18-veto-ready-menu.md` and `docs/ideas/2026-07-19-execution-roadmap.md`:
trading planning is a separate repo/PR with no venture work sequenced against it. If a trading
data-provisioning decision exists, it lives in the trading repo — verify there.

---

*Compiled read-only from the live tree at HEAD `2be4065`. Paths cross-checked against the `candidates/`
tree and `docs/publishing/OWNER-QUEUE.md`; where `docs/current-state.md` lagged the live tree it is
flagged inline. No invented metrics — all sales/traffic figures are owner-dashboard-only.*
