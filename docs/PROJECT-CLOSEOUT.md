# venture-lab — Project Closeout

> **Status:** `reference`
>
> The single durable cutover read for this project at the 2026-07-21 read-only
> cutoff. Written for two readers who know nothing of the autonomous agent
> sessions that built it: **the owner**, and **a fresh future Claude session**.
> If you read one file, read this one — then the live ledger
> [`current-state.md`](current-state.md) and the owner start page
> [`publishing/OWNER-START-HERE.md`](publishing/OWNER-START-HERE.md).
>
> State verified live against `main` HEAD `83faa9c` on 2026-07-21. Merged work
> and source code always win over this file.

venture-lab is the fleet's first "born-right" venture lane. Its mission (see the
root [`../README.md`](../README.md)): **find and validate the cheapest credible
path to first revenue** — agents build, the owner clicks. Every publish, spend,
or account-creation step is owner-gated by hard rail; nothing here was ever
auto-published or auto-spent. This document closes the autonomous build window.

---

## 1. What this project is & what was accomplished

Everything below is merged on `main`. Citations are PR numbers with the squash
commit's short SHA (verified in `git log`); where a PR number could not be
independently re-fetched it is still traceable to its squash commit.

### Sellables & storefront
- **Storefront catalog + positioning/comparison asset** — [`launch/CATALOG.md`](launch/CATALOG.md)
  (PR #232 `8c60cfc`). The authoritative storefront view: **1 LIVE + 19
  publish-READY SKUs + 3 hard-gated bundles + Photo Packs**.
- **Owner publish queue (generated)** — [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md),
  produced by `scripts/derive_owner_queue.py` from the vetting packets; queues
  28 decisions (D1–D28) plus the owner-gated publish click sequences. **Never
  hand-edit — regenerate.**

### Engineering — the required CI guard pipeline
The 6 required CI guards (plus the D-ref guard) that keep the catalog/queue
honest and machine-checked:
- ENG-3 funnel coverage — PR #256 `7ba09d6`
- ENG-4 funnel-asset guard — PR #263 `f1ab8dc`
- ENG-5 built-vs-registered guard — PR #262 `66b5bae`
- ENG-6 owner-queue idempotence — PR #261 `1da8222`
- ENG-7 owner-queue staleness — PR #264 `82059bf`
- ENG-8 docs link/anchor integrity — PR #265 `10e0151`
- D-ref guard `check_catalog_drefs.py` — PR #248 `2705da8`
- **sku_registry consolidation** — one authoritative SKU/registry inference
  module the guards share — PR #266 `4a89e46` (guard fix PR #280 `d0e62a8`).

### Fiction shelf (repo content; publishing stays owner-gated)
- **The Night Kiln — 6-book cozy-fantasy series.** Books 4/5/6 landed this wave:
  Bk4 PR #269 `0639567`, Bk5 PR #272 `c6b6310`, Bk6 *The Summer Ember* PR #279
  `3bb962b` (Bks 1–3 earlier in history). Back-matter consistency PR #285
  `8abb145`. A Book 7 is *planted but unwritten* — do not list it as available.
- **Lull / DREAMLINE — complete middle-grade portal-fantasy trilogy.** Bk2 *The
  Mirror City* PR #268 `6954e9a`, Bk3 *The Fourth Hour Comes* PR #271 `2daa27b`
  (Bk1 earlier).
- **Ultramarine — complete 3-book Delft trilogy.** Bk2 *The Blue and the White*
  PR #270 `9b9129c`, Bk3 *The Common Blue* PR #278 `a2ab822` (Bk1 earlier).
- **KDP-ready packages** — upload-ready `MANUSCRIPT-KDP.md` + `KDP-METADATA.md` +
  `SELF-EDIT-PASS.md` per ready sequel — PR #274 `d776fd7` (the original 5) plus
  the two new books. Folders under `../candidates/*/kdp-ready/` (see §4).

### Distribution (the binding constraint) — free top-of-funnel, not sellables
- **4 free lead magnets**, one per cluster: api-robustness PR #243 `bf8d5ec`,
  agent-ops PR #246 `661ffce`, membership (LM-1) PR #250 `f043c58`, AI-Novella
  (LM-2) PR #251 `25f1444`.
- **Distribution playbook** governing them — [`launch/DISTRIBUTION-PLAYBOOK.md`](launch/DISTRIBUTION-PLAYBOOK.md)
  (PR #249 `e8d688e`).
- **Distribution submission pack** — 11 paste-and-post channel files turning the
  4 lead magnets into one-click submissions — [`launch/submissions/README.md`](launch/submissions/README.md)
  (PR #277 `c689783`).

### Decision & planning assets
- **Funnel diagnostic** — why the one LIVE listing has zero organic sales —
  [`launch/funnel-diagnostic.md`](launch/funnel-diagnostic.md) (PR #252 `cb4ef3a`).
- **Kill-clock decision packet** — the pre-written keep/iterate/delist read for
  the LIVE SKU's T+14 call — [`launch/kill-clock-decision-packet.md`](launch/kill-clock-decision-packet.md)
  (PR #253 `7d5229f`).
- **Veto-ready menu of exactly 64 proposals** — [`ideas/2026-07-18-veto-ready-menu.md`](ideas/2026-07-18-veto-ready-menu.md)
  (PR #247 `cde8f6d`) — plus the **execution roadmap** [`ideas/2026-07-19-execution-roadmap.md`](ideas/2026-07-19-execution-roadmap.md)
  (PR #259 `20aa598`) and the **season-2 plan** [`ideas/2026-07-20-season-2-plan.md`](ideas/2026-07-20-season-2-plan.md)
  (PR #283 `56c6620`), a contingency-shaped post-cutoff build plan.
- **Transition dossier** — one neutral cutover read of the whole venture —
  [`publishing/TRANSITION-DOSSIER.md`](publishing/TRANSITION-DOSSIER.md) (PR #275 `60e9e23`).

### Infrastructure
- **substrate-kit upgraded v1.17.0 → v1.20.1** — PR #282 `83faa9c` (the current
  HEAD), with the follow-up gate fix PR #286 `5172bd9`.

---

## 2. Current true state (verified live at HEAD `83faa9c`, 2026-07-21)

- **Kit version: v1.20.1** — source of truth `substrate.config.json` (`kit_version`).
- **`python3 bootstrap.py check --strict` exits 0** ("check: all checks passed")
  at HEAD; `python3 -m pytest scripts/test_*.py` → **140 passed**. The only
  advisories are non-gating model-line nags on older `.sessions/` cards.
- **0 open PRs for this seat at closeout** (this closeout PR excepted, which lands
  itself). HEAD `83faa9c`.
- **Live SKU status:** exactly **1 LIVE product — Stripe Webhook Test Kit $29**
  on Gumroad (launched 2026-07-12, measurement mode). **0 organic sales recorded.**
  Distribution is the binding constraint (Gumroad views/sales are
  owner-dashboard-only; agent surfaces cannot see them). Kill clock: **T+14
  kill-rule 2026-07-26** — keep only on ≥1 organic sale OR ≥1 qualified inbound,
  else pause/delist. Source: [`current-state.md`](current-state.md) and the
  decision packet [`launch/kill-clock-decision-packet.md`](launch/kill-clock-decision-packet.md);
  live record [`launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](launch/stripe-webhook-test-kit/LAUNCH-LOG.md).

---

## 3. Continuation — open threads in priority order

Nothing here is *broken*; these are the owner-gated and future-session threads
the autonomous window left in a clean, resumable state. Each names the file a
fresh session opens first.

1. **Owner publish clicks (highest leverage).** The 28 queued decisions and
   publish sequences are one owner sitting. Open: [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md)
   (curated companion: [`publishing/OWNER-START-HERE.md`](publishing/OWNER-START-HERE.md)).
2. **Lead-magnet posting (unblocks distribution — the binding constraint).**
   Owner paste-and-post the 4 free articles to their channels. Open:
   [`launch/submissions/README.md`](launch/submissions/README.md).
3. **Veto skim of the 64-item menu.** Owner's veto is the filter; survivors
   become claimed slices for a fresh session. Open: [`ideas/2026-07-18-veto-ready-menu.md`](ideas/2026-07-18-veto-ready-menu.md).
4. **Book proofread + upload.** The single binding lever on the ready NL editions
   is the owner-only native-speaker proofread — an AI cannot clear it. Then the
   KDP upload clicks. Open: [`publishing/CHECKLIST.md`](publishing/CHECKLIST.md)
   and the `../candidates/*/kdp-ready/` packages (§4).
5. **Night Kiln Book 7 + season-2 build.** Bk7 is planted but unwritten; the
   post-cutoff build plan is contingency-keyed. Open: [`ideas/2026-07-20-season-2-plan.md`](ideas/2026-07-20-season-2-plan.md).
6. **Trading-data provisioning fork.** A post-cutoff branch gated on the owner
   provisioning trading data (the trading lane stays research-only until then).
   Open: [`ideas/2026-07-20-season-2-plan.md`](ideas/2026-07-20-season-2-plan.md).

---

## 4. Owner walkthrough — every valuable artifact

Plain language, quickest-first. Each link is clickable and relative to this file.

1. **[`publishing/OWNER-START-HERE.md`](publishing/OWNER-START-HERE.md)** — **start
   here.** The curated "do these in one sitting" owner checklist. Read it first.
2. **[`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md)** — the full generated
   publish queue: 28 decisions (each with a bolded default) + the click-run
   sequences. This is the paste-and-click surface for taking SKUs live.
3. **[`publishing/TRANSITION-DOSSIER.md`](publishing/TRANSITION-DOSSIER.md)** — the
   one neutral read of the whole venture state: every sellable + status, every
   book property + next hook, open owner decisions, the asset map, the resume path.
4. **[`launch/CATALOG.md`](launch/CATALOG.md)** — the storefront catalog: what
   each SKU is, its price, and its queue-decision number.
5. **[`launch/submissions/README.md`](launch/submissions/README.md)** — 11
   paste-and-post channel files (dev.to + Hashnode + a fitting subreddit each for
   the developer clusters; r/selfpublishing + r/writing for the AI-novella). Each
   is one owner paste + click, exact submit URL and front-matter baked in.
6. **KDP-ready book packages** — upload-ready manuscripts + paste-ready metadata:
   - Night Kiln Bk6: [`../candidates/adult-novels/the-night-kiln/kdp-ready/book-6/KDP-METADATA.md`](../candidates/adult-novels/the-night-kiln/kdp-ready/book-6/KDP-METADATA.md)
     (also book-4, book-5 alongside).
   - Ultramarine Bk3: [`../candidates/adult-novels/ultramarine/kdp-ready/book-3/KDP-METADATA.md`](../candidates/adult-novels/ultramarine/kdp-ready/book-3/KDP-METADATA.md)
     (also book-2).
   - Lull/DREAMLINE: [`../candidates/dream-series/kdp-ready/book-3/KDP-METADATA.md`](../candidates/dream-series/kdp-ready/book-3/KDP-METADATA.md)
     (also book-2).
7. **Planning reads** — [`ideas/2026-07-18-veto-ready-menu.md`](ideas/2026-07-18-veto-ready-menu.md)
   (64-item backlog), [`ideas/2026-07-19-execution-roadmap.md`](ideas/2026-07-19-execution-roadmap.md),
   [`ideas/2026-07-20-season-2-plan.md`](ideas/2026-07-20-season-2-plan.md).
8. **Live-SKU decision inputs** — [`launch/funnel-diagnostic.md`](launch/funnel-diagnostic.md)
   and [`launch/kill-clock-decision-packet.md`](launch/kill-clock-decision-packet.md)
   for the 2026-07-26 keep/iterate/delist call.

**Owner checklist (quickest first):**
- [ ] Open [`publishing/OWNER-START-HERE.md`](publishing/OWNER-START-HERE.md) and do the one-sitting steps.
- [ ] Paste-and-post the 4 lead magnets from [`launch/submissions/README.md`](launch/submissions/README.md) (free, no spend — moves the binding constraint).
- [ ] Make the SWTK T+14 call on 2026-07-26 using [`launch/kill-clock-decision-packet.md`](launch/kill-clock-decision-packet.md).
- [ ] Work the publish clicks in [`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md) at your pace (all owner-gated, no deadline).
- [ ] For books: do the native-speaker NL proofread, then upload the KDP packages (§4).

---

## 5. Working this repo with a fresh session

- **Boot route:** read [`current-state.md`](current-state.md) (the living ledger)
  then [`conventions.md`](conventions.md) (the working agreement — it overrides
  harness defaults). Then this file for the full picture.
- **Verify command:** `python3 bootstrap.py check --strict` (expect exit 0) and
  `python3 -m pytest scripts/test_*.py` (expect 140 passed).
- **How PRs land:** open a `claude/`-headed PR **READY (non-draft)**; its FIRST
  commit is a born-red session card (`.sessions/<date>-<slug>.md`) with
  `> **Status:** in-progress`, which holds CI red by design until you flip it to
  `complete` as the deliberate LAST commit. When `kit-tests` + `substrate-gate` +
  `main-verify` are green on the head SHA, `auto-merge-enabler.yml` squash-merges
  automatically (opt out with a `do-not-automerge` label), or an agent merges
  directly. Merging is normal agent work — it is not deploying (this repo hosts
  no running service; publishing is a manual owner action).
- **Gotchas:**
  - **Generated files are regenerated, never hand-edited.** `OWNER-QUEUE.md`
    comes from `scripts/derive_owner_queue.py`; run the generator and commit its
    output.
  - **The born-red HOLD is by design** — a red `substrate-gate` on an in-progress
    card is the designed hold, not a defect; it clears when the card flips complete.
  - **Control fast lane** — a PR whose diff is `control/**`-only rides a shorter
    gate; a mixed PR runs the full gate.
  - **`control/inbox.md` is append-only** with ORDER grammar (`## ORDER NNN ·
    ISO8601 · status: <state>` + priority/do/why/done-when). Orders stay
    `status: new` permanently; "done" is diffed against `../control/status.md`,
    never marked in the inbox.
  - **Isolated clone per parallel mutating worker** — concurrent sessions each
    claim before building (one file per claim under `../control/claims/`) and
    work in an isolated checkout to avoid merge-conflict churn.
