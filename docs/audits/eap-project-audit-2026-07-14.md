# Venture Lab seat — EAP project audit, 2026-07-14

> **Status:** `audit` — one-shot, point-in-time. Definitive end-of-EAP audit
> of this seat's two repos (`menno420/venture-lab`, `menno420/trading-strategy`):
> measured usage and scale, tooling verdicts, platform walls, landing and
> scheduling friction, self-engineered fixes, remaining pains, and a wishlist —
> owner directive 2026-07-14.

**Method & provenance.** Measured 2026-07-14 (~08:35–08:50Z) by three
measurement passes: local git forensics on venture-lab at origin/main
`17b0499` and on a read-only clone of trading-strategy at origin/main
`01aa0ce`, plus full-population GitHub MCP metrics (`gh` CLI absent; direct
REST and GraphQL blocked — verbatims in §3). Citations are `path:line@ref`,
short SHA, PR #, or verbatim quote. Where the directive expected evidence the
measurement could not find, this doc says so explicitly (§5, §6, §11) —
"not measured" beats invention. **Delta rule:** trading's
`docs/research-program-retrospective.md@d857e50` (rounds 1–6, the research
story) and both walls ledgers (venture `docs/CAPABILITIES.md@68d57bb`,
trading `docs/CAPABILITIES.md@67f5554`) already exist; this audit cites them
and states only the platform-side delta. Every §2–§9 finding carries a
disposition: **FLEET-FIX** (we can fix it), **ANTHROPIC** (paste-ready ask),
or **ACCEPTED**.

## 1. Identity & scale

One coordinator seat, two lanes:

- **venture-lab** — sellables: small digital products + books, always stopping
  at the owner-gated click (fleet-cleanup audit "What the repo is",
  `docs/audits/2026-07-13-fleet-cleanup-audit.md`). Active window: first
  commit `361df1c` 2026-07-10T00:44:32+02:00 → last `17b0499`
  2026-07-14T09:49:11+02:00 — **~4.4 days**.
- **trading-strategy** — RESEARCH-ONLY paper lane: "**No real money, no
  brokerage account, no order, no API — ever**"
  (`experiments/paper/ledger.md:7-8@main`). Active window: `f65d4773`
  2026-07-09T14:34:03+02:00 → `01aa0cec` 2026-07-14T09:15:42+02:00 — **~5
  days**. Research outcome is already told in
  `docs/research-program-retrospective.md@d857e50` ("5,055 registered
  configurations → 0 promoted", verified two ways there) — not restated here.

**Measured** (PR totals exact: `search_pull_requests` total_counts match
`list_pull_requests state=all` item counts, numbers 1..192 / 1..121 with no
gaps):

| measure | venture-lab | trading-strategy |
|---|---|---|
| session cards (`.sessions/*.md`, README excluded) | 152 | 71 |
| commits on main (`git rev-list --count origin/main`) | 224 | 130 |
| PRs opened | 192 | 121 |
| PRs merged | 187 | 120 |
| PRs closed-unmerged | 4 (#38, #51, #58, #157) | 1 (#64) |
| PRs open at audit | 1 — **#192, this audit's own PR** | 0 |

**Backlog at HEAD.** venture-lab owner-queue (output of
`scripts/derive_owner_queue.py`): **19 decisions (D1–D19) · 262 pending owner
clicks across 44 sequences · 16 hard-gated · 3 DONE** — counted at HEAD and
matching the heartbeat (`control/status.md:13@17b0499`). Catalog: "1 LIVE
(SWTK $29) + 10 publish-READY + 2 hard-gated; 12 EN adult manuscripts"
(`control/status.md:6@17b0499`). Ideas: 5 ranked concepts
(`docs/ideas/2026-07-14-adult-title-concepts.md`). trading-strategy: **1 open
review-queue item** ("#37 · P5 one-shot holdout evaluation + final report ·
classifier denied agent merge — owner click needed",
`docs/review-queue.md:8@main`) and **1 idea file**
(`docs/ideas/trigger-registry-2026-07-11.md`, `state: routed / outcome:
open`); 14 ORDERS in `control/inbox.md`, "orders: acked=001–014
done=001–013" (`control/status.md:10@main`).

## 2. Tooling used

| tool / surface | how used | verdict | citation |
|---|---|---|---|
| GitHub MCP | all live GitHub state: PR/branch/run reads, merges, cross-repo reads (`add_repo` + MCP in trading) | **reliable** (staleness caveat §6, pagination caveat §3) | "Live count at audit time: 1 open PR (`state=open` via `mcp__github__list_pull_requests`)" (`docs/audits/2026-07-13-fleet-cleanup-audit.md:121-122`); "poll checks via the GitHub MCP `pull_request_read`" (TS `.sessions/2026-07-10-p4-transfer.md:46`) |
| Auto-merge enabler workflow | canonical landing path in both repos; green `claude/*` PRs self-land | **reliable** — 0 failures in 231 (VL) + 109 (TS) enabler runs | VL installed `305646f` (#59), "≈90 PRs landed via the auto-merge-enabler workflow with zero self-merges" (retro:88-89); TS installed `bf885f0` (#65), "proven on PRs #66–#76" (TS `CAPABILITIES.md:117-118`); latest bot land: TS #117 `merged_by = github-actions[bot]` (verbatim field, `pull_request_read`) |
| substrate-gate / kit checks (`bootstrap.py check --strict`) | required CI check + docs/claims/session-card gate; the born-red hold | **reliable but noisy by design** — 182 designed-red runs (§6, §7); real catches §7 | required since PR #55 (`docs/PLATFORM-LIMITS.md:74-76`); gate wiring TS `.sessions/2026-07-09-adopt-substrate-kit.md:20` |
| `scripts/derive_owner_queue.py` | regenerates OWNER-QUEUE from vetting-packet OWNER-GATE blocks + keyword map | **reliable** | "ONE `derive_owner_queue.py` regen — counts now 19 decisions / 44 sequences / 262 clicks" (`control/status.md:13`); generator #101, kill-clock #128 (`53f6b65`), DUE/OVERDUE #133 (`467d619`) |
| trigger + `send_later` MCP | pacemaker chain (Q-0265 design: 15-min send_later chain + 2-hourly cron failsafe + weekly grading cron) and the seat-bound Friday grading cron | **flaky** — fresh-session delivery 0-for-2, vanish-without-tombstone, parallel-write hangs (§5) | `create_trigger` proven agent-side 2026-07-11 (`docs/CAPABILITIES.md:85-87`); grading cron `trig_01UsNU4JRps4b7jiAMdEfXNi`, cron `0 9 * * 5`, seat-bound (TS `control/status.md:19`, `control/outbox.md:95-98`) |
| Worker-relay pattern | child builds PR READY+green; coordinator merges under the owner's genuine-user turn; orders/verdicts relayed as text | **painful but effective**; chat-side mechanics are coordinator-attested only (§11) | PR #15 landed as `ab5f533` via relay (`docs/PLATFORM-LIMITS.md:73`); "coordinator relay 2026-07-13: freeze STANDS" consumed and cross-checked (`.sessions/2026-07-13-order-003-stripe-path.md:12,37`) |
| raw.githubusercontent cross-repo reads | venture-lab: fleet CAPABILITIES fetch, trading-strategy reads, Stripe SDK fixtures when docs.stripe.com 403'd | **reliable in venture-lab; NOT a used path in trading-strategy** — there it is kit-internal only (`bootstrap.py:13585` `RAW_HOST`); trading uses `add_repo` + GitHub MCP instead (`.sessions/2026-07-09-wind-down.md:16`) | recipe `docs/CAPABILITIES.md:153-156`; uses: `.sessions/2026-07-14-order-012-fence.md:45`, `.sessions/2026-07-12-candidate-market-state-dashboard.md:14`, `.sessions/2026-07-11-order-003-stripe-real-path.md:34` |

## 3. Tooling walled or missing

**The ledgers.** Walls are already maintained as living ledgers — venture
`docs/CAPABILITIES.md@68d57bb` (**11 recorded: 7 kit-seed-fence walls + 4
append-log walls**, folded by ORDER 012 #190) and trading
`docs/CAPABILITIES.md@67f5554` (**7 seed-fence walls + 1 append entry, which
is a capability, not a wall** — the enabler-supersedes-REST-merge note). This
audit does not restate them. **Delta:** the 7 seed-fence walls are identical
kit text in both repos (tag/release 403, branch-delete 403, api.github.com
blocked, no-API environment/Project creation, self-merge classifier, GraphQL
quota, silent prompt-stalls). venture-lab additionally carries 4 append-log
walls (self-merge denials #9/#15/#55; direct-push-to-main `422 Repository
rule violations found — Changes must be made through a pull request.`;
branch-delete re-verified 2026-07-13; no-API owner-click surfaces) and keeps
`docs/PLATFORM-LIMITS.md` as an evidence appendix ("NOT a source of truth
since 2026-07-14 (ORDER 012)", `PLATFORM-LIMITS.md:3`). trading-strategy has
**no** PLATFORM-LIMITS file; its second platform ledger is `docs/ROUTINES.md`
(trigger doctrine, §5).

Verbatims and dispositions (dates are LAST-VERIFIED per ledger, or this
audit's own measurement date):

| capability | verbatim denial + date | workaround | disposition |
|---|---|---|---|
| Merge-path classifier (self-merge / auto-merge-arm) | "`[Self-Approval] The delegated sub-agent prompt instructs merging PR #9, which was authored by this agent's own build worker, defeating two-party review…`" (2026-07-10, `docs/PLATFORM-LIMITS.md:52-61`); PR #15 drew 3 denials incl. "`Reason: No reason provided.`" (l.73); #55 denied even with substrate-gate REQUIRED (l.74-76) | auto-merge enabler + worker-relay; note **#9/#15/#55 all eventually MERGED** via alternate landing in 12m38s–20m45s vs the 55s median (metrics forensics) | **ANTHROPIC** — ask A below |
| Branch deletion | "`error: RPC failed; HTTP 403 curl 22 The requested URL returned error: 403`" — re-verified 2026-07-13 (`docs/CAPABILITIES.md` append log) | none agent-side; owner hand-delete or repo setting | **ANTHROPIC** — ask B. Measured NOW: **131 stale `claude/*` branches in venture-lab + 56 in trading-strategy** (`list_branches` cross-referenced against open-PR heads) — supersedes the documented "94-branch stale `claude/*` list" (`PLATFORM-LIMITS.md:25-33`) |
| Tag push / GitHub Release | "HTTP 403 from the environment's git proxy → use the workflow_dispatch release path" (2026-07-12, `CAPABILITIES.md:75-77`) | `workflow_dispatch` release workflow — sanctioned path (`PLATFORM-LIMITS.md:20-24`) | **ACCEPTED** — workaround is clean |
| `api.github.com` direct HTTP | measured this audit, 2026-07-14: `{"message":"GitHub access is not enabled for this session. An org admin must connect the Claude GitHub App for this organization."}` — note this verbatim was previously **absent** from PLATFORM-LIMITS; only the seed line "blocked → GitHub access is MCP-tools-only" existed (`CAPABILITIES.md:81-82`, 2026-07-10). This audit supplies it. | GitHub MCP (all measurements completed through it) | **ANTHROPIC** — folded into ask E |
| GraphQL | measured this audit, 2026-07-14: `{"message":"This GraphQL query is not enabled for this session — only the pinned set of PR-review operations is served. Use REST via 'gh api repos/{owner}/{repo}/...' instead."}` — and `gh` is not installed here. Plus the quota wall: "GraphQL quota exhausts at fleet scale (~hourly)… ready-flips (draft→ready) are GraphQL-only" (`PLATFORM-LIMITS.md:80-83`) | REST-backed MCP tools | **ANTHROPIC** — ask E |
| No-API owner surfaces | "Creating/editing claude.ai environments, routines, or Projects; GitHub repo settings/rulesets — no API surface for the agent → owner clicks." (`PLATFORM-LIMITS.md:36-42`) | structured owner asks (OWNER-QUEUE.md) | **ANTHROPIC** — ask D |
| MCP `actions_list` pagination (newly measured) | 2026-07-14: tool **ignores `per_page`** — passed 1 and 100, always returned 30/page | fetched all pages by hand: 31 (VL) + 22 (TS) = **53 pages** for full run history | **ANTHROPIC** — ask E (bug report) |

Paste-ready asks (quotable as-is):

- **Ask A (merge-path classifier vs two-party review):** "Please give EAP
  seats a supported agent-landing primitive: when a repo ruleset requires
  green checks and the PR was produced under an owner-authorized standing
  order, let the seat arm native auto-merge without the auto-mode classifier
  treating it as Self-Approval / Merge Without Review — or publish the exact
  boundary so seats stop discovering it by denial. Evidence: venture-lab PRs
  #9/#15/#55 were each classifier-denied on the merge path yet all landed
  anyway via alternate paths in 12–21 minutes (seat median land time is 55s);
  the denial adds latency and laundering pressure, not review."
- **Ask B (branch deletion):** "Please add a repo-scoped grant for `git push
  origin --delete claude/*` (or honor GitHub's 'Automatically delete head
  branches' through the proxy credential). Every deletion path returns
  `error: RPC failed; HTTP 403 curl 22 The requested URL returned error:
  403`; this seat accumulated 187 dead `claude/*` branches (131 + 56) in 5
  days, and squash-merge strands telemetry commits on those unprunable
  branches (§6)."
- Asks C–E are given in §9 (trigger lifecycle; owner-approval surface; MCP
  staleness/pagination/REST-GraphQL parity).

## 4. Merge & landing friction

**Measured (full population, not samples):**

- **Time-to-land** (merged_at − created_at): venture-lab **median 55s**
  (n=187); trading-strategy **median 1m52s** (n=120). Sub-minute medians are
  the enabler flow working as designed. Worst-3: VL **#57 11h09m26s**, **#170
  8h18m40s**, **#174 1h16m02s**; TS **#65 8h14m10s**, **#117 8h13m34s**,
  **#37 4h25m03s**. Attributable tails: #170 is the overnight fleet-cleanup
  audit PR; TS #117's body says the author left it "for the repo's own
  auto-merge/sweep convention or a human to land" (merged next morning by
  `github-actions[bot]`); TS #37 is the classifier-denied owner-click item
  still in `docs/review-queue.md:8`. #57 and #65 tails are not attributed —
  no documented cause found.
- **>1 CI round** (≥2 distinct head SHAs in CI, ≥1 first seen >60s after PR
  creation — i.e., a real post-open push): venture-lab **65 of 184 covered
  merged PRs (35%)**; trading-strategy **56 of 118 (47%)**. Method caveats:
  VL #1–#3 and TS #2–#3 predate CI install and are uncovered; born-red flow
  pushes card commits before opening, so this measures post-open rework only
  — and the designed card-flip push after open inflates it.
- **HEAD-race case:** #164 merged 2026-07-13T14:29:01Z → **#165** ("rewrite
  NEXT-SESSION.md cold-start brief against HEAD `e252b46`" — baseline pinned
  to the pre-#164 HEAD) merged 14:33:45Z carrying stale counts → **#166**
  remedy ("sync NEXT-SESSION + current-state counts to the OWNER-QUEUE at
  HEAD (post-#163/#164)") merged 14:42:05Z. All three inside ~14 minutes.
- **Owner-click dependency:** 262 pending owner clicks, 16 hard-gated
  (`control/status.md:13@17b0499`) — landing work is increasingly gated on a
  surface the agent cannot touch (§3 no-API owner surfaces).
- **Classifier denials on the merge path:** #9/#15/#55, verbatims in §3.
- **Stale branches:** 131 + 56 = 187 (§3).

Dispositions by recurring cause:

| cause | disposition |
|---|---|
| classifier merge denials | **ANTHROPIC** — ask A (§3) |
| HEAD-race / stale-baseline docs PRs | **FLEET-FIX (already in place)** — the #166 counts-sync remedy class is institutionalized and repeated each batch (`control/status.md:4,10,11,13`); keep regen-at-HEAD before every counts-bearing docs PR |
| >1-CI-round rate | **ACCEPTED** — dominated by the designed born-red card flip; the metric is a rework *ceiling*, not a defect count |
| owner-click bottleneck | **ANTHROPIC** (ask D, §9) + **FLEET-FIX (done)** — `derive_owner_queue.py` already batches clicks into one surface |
| stale branch accumulation | **ANTHROPIC** (ask B) + **FLEET-FIX interim** — queue one owner click: enable "Automatically delete head branches" on both repos |

## 5. Scheduling & wake friction

- **2026-07-13 trigger cutover** (venture `control/status.md` history; TS
  `control/outbox.md:99-104`): **4 NEW** — failsafe
  `trig_01SbFnHdb1bvUzDnKrDdRb6t` (cron `45 1-23/2 * * *`), weekly grading
  `trig_01UsNU4JRps4b7jiAMdEfXNi`, SWTK T+7 `trig_01V9DZrTtDU81Sm7vektX9fa`,
  T+14 `trig_01SNkNWfSXoAdz1ALf4YNbC6`; **4 DELETED (confirmed)** —
  `trig_01HCLdpcX9QNUz4Y33efgt57` (old failsafe),
  `trig_01FRG4uUxPh5ZGncZGfRgF2F` (old grading),
  `trig_01LfwTPMGzM1fqA9CTQLgHnD` (old T+7), `trig_01Muk6nrt2BdxsPmDVY4arwA`
  (old T+14); **1 FOREIGN, untouched** — `trig_01YXNmgqYeYQ1LuepsLmbNCG`, a
  `send_later` firing 2026-07-17T09:00Z into a non-seat session, "potential
  duplicate grading fire". Root cause of the churn: triggers are bound to the
  creating session and **die at archive** — every succession forces a full
  rebind (status.md history, "LEFT FOR SUCCESSOR REBIND … triggers die at
  archive"). Disposition: **ANTHROPIC** — ask C (§9).
- **Fresh-session-per-fire delivery 0-for-2 vs 100% self-bound:** "observed
  delivery was 0-for-2 on fresh-session cron fires vs 100% on self-bound
  crons and one-shot chains (2026-07-12 forensics) — treat fresh-session
  cron as UNVERIFIED-BROKEN until a scheduled fire is proven in your
  environment" (TS `docs/ROUTINES.md:17-24@main`). **This is why the Friday
  grading cron is seat-bound** rather than fresh-session. Disposition:
  **FLEET-FIX (done — doctrine)** + **ANTHROPIC** (ask C).
- **Dead / silent workers:** venture-lab PR #157 authoring session "died
  mid-turn (`no_access`) ~12:23Z before any prose was committed" — closed at
  0 words, seam resume pointer appended
  (`docs/retro/2026-07-13-coordinator-session.md:52-59,79-80`); ORDER 003 was
  re-dispatched after it had already shipped and the worker converted it to a
  verification slice (`.sessions/2026-07-13-order-003-stripe-path.md:16`).
  Disposition: **FLEET-FIX (done)** — verify-at-HEAD before executing orders.
- **trading-strategy incident list** (all cited): (1) **session DOA at
  provision ×3** — "identical setup-script error, third kill; the env fix
  never took effect. The lane never started" (`docs/succession/QUEUE.md:12`);
  a DOA successor "went unnoticed ~2.8h" → 10-minute heartbeat-or-respawn
  rule (`.sessions/2026-07-09-retro-wakeup.md:27`); "a session that dies at
  provision emits NO failure event and stays listed 'active'"
  (`docs/succession/NEXT-BOOT.md:23`); (2) **trigger vanished unfired, no
  tombstone** — "a trigger recorded 'verified live' has vanished within
  hours, unfired, with no audit trail visible agent-side"
  (`docs/ROUTINES.md:46-50`); (3) **parallel trigger-MCP writes hang** —
  "parallel multi-call writers hung reliably under load (four workers, one
  night)" (`docs/ROUTINES.md:65-69`); (4) **manual-fire wedge** — "a
  hand-kicked trigger looks alive while its schedule stays wedged"
  (`docs/ROUTINES.md:52-61`); (5) **duplicate `send_later` fire risk** on
  07-17, flagged to the manager, "Not ours to delete: recorded only,
  untouched" (`control/outbox.md:108-114`); (6) **`gh pr merge` hangs** "to
  Bash timeout, exit 143 — poll checks via the GitHub MCP"
  (`.sessions/2026-07-10-holdout-collab.md:67`); (7) **dead-author
  heartbeat** — "a heartbeat without an expiry reads healthy forever —
  including while its author is dead (this happened)"
  (`docs/succession/GEN2-FEEDBACK.md:11`). Dispositions: (1)(2)(4) **ANTHROPIC**
  — ask C; (3)(6) **FLEET-FIX (done — pacing/polling doctrine)**; (5)
  **FLEET-FIX (done — recorded, dup-guarded)**; (7) **FLEET-FIX (done —
  heartbeat expiry rule)**.
- **`send_later` binds to the calling session** (class): coordinator-attested
  (§11); repo-visible corroboration is the foreign `send_later` stranded in a
  non-seat session above. Disposition: **ANTHROPIC** — wishlist item 3.
- **HONEST NULLS:** the directive expected a "22:27Z night-order recon
  re-dispatch" and a "75-min no-PR nudge" — **neither was found in either
  repo's history** (pickaxe `git log --all -S` for `22:27`, `WAKE-DEAD`,
  `75-min`, `75 min` all empty). Nearest facts: the night window opened
  2026-07-12T22:30Z (retro:5-6) and the pacemaker was paused
  2026-07-12T23:27Z (status.md history). Both items are
  **coordinator-attested-only** — not claimed here as repo fact.

## 6. Environment & platform issues

- **MCP PR-state staleness ~25 min.** Kit-template warning:
  "Staleness-sensitive reads are cross-checked before acting (MCP PR-state
  reads observed ~25 min stale — confirm merge/CI state via git fetch or the
  Actions runs)" (`CONSTITUTION.md:48-51@main`, arrived via kit upgrade #83).
  **No locally-logged incident exists in either repo** — the warning is
  inherited kit text. However, this audit adds one **session-observed** data
  point (2026-07-14): the worker that opened PR #192 read it via MCP as
  "auto-merge NOT armed" while the PR webhook showed the enabler had already
  armed it. Disposition: **FLEET-FIX (done — cross-check doctrine)** +
  **ANTHROPIC** (ask E freshness component).
- **Born-red webhook noise, now measured.** Full-history CI: venture-lab 923
  runs, substrate-gate **114 failures** (31% of its 366 runs), kit-tests
  **0/324 failures**, enabler 0 failures; trading-strategy 640 runs,
  substrate-gate **68 failures** (26% of 265), tests **0/265**, enabler 0.
  **All CI red on both repos — 182 runs — is the designed born-red gate**;
  no test has ever failed. The retro already named the cost: "PR-activity
  webhook chatter on born-red cards consumed coordinator attention out of
  proportion to signal" (retro:63-64). Disposition: **FLEET-FIX** — have the
  kit gate report the designed session-card hold as a distinctly-named check
  (or neutral conclusion) so real failures are distinguishable in webhook
  traffic; plus wishlist item 6 (ANTHROPIC side: webhook suppression for
  designed-red checks).
- **guard-fires.jsonl telemetry stranded off main.** `d1b0208` exists only on
  `origin/claude/night-verdicts-v053-057-049`; `dfe8e33` only on
  `origin/claude/night-wire-garden`; **`c0fce7c` is in NO ref — that data is
  lost**. The seat itself logged it: "ADVISORY loose end: telemetry commit
  `d1b0208` sits on merged branch … and is NOT in main … branch pruning is
  credential-walled" (`control/status.md:6@17b0499`). Root cause: the
  squash-merge landing path strands post-merge telemetry commits on branches
  nobody can delete (§3 branch-delete 403). Disposition: **FLEET-FIX** —
  commit guard-fires appends *before* the PR's final push (or land them via a
  follow-up PR), never after merge; **ANTHROPIC** ask B removes the
  underlying trap.
- **Context-limit session splits:** **honest null** — no "context limit" /
  "handover due to context" incident exists in either repo's evidence; the
  repo-visible session-boundary pains are the `no_access` death class (#157)
  and trigger rebind-at-archive (§5). Context-split reports are
  coordinator-attested-only (§11). Disposition: **ACCEPTED** (nothing
  repo-measurable to fix).

## 7. Process & ceremony cost

- **Born-red ritual:** cost = 182 designed red runs of webhook/attention tax
  (§6). Paid back: the same strict gate made **real catches** — 2 `reachable`
  orphan-doc fires (retro/QUESTIONS.md 2026-07-10T02:56Z; SKILLS.md
  2026-07-12T11:52Z — `.substrate/guard-fires.jsonl:2,22`) and the
  fleet-cleanup audit report's own orphan catch, fixed by `5d47091` "docs:
  link the fleet cleanup audit report from AGENT_ORIENTATION.md" (landed in
  #170); this audit doc carries its orientation link for the same reason.
  Verdict: **paid, but noisy** — disposition **FLEET-FIX** per §6 (distinct
  check signaling).
- **Claims:** "zero collisions across 3 parallel lanes; the claims convention
  held at full concurrency" (retro:90-92) — cheap ceremony that paid for
  itself. **ACCEPTED** (keep).
- **Heartbeat grammar:** two misread modes, both already fixed — venture
  status.md found "~6h23m stale" by the fleet auditor while the seat was
  actively working (by design: heartbeat written at session close;
  `docs/audits/2026-07-13-fleet-cleanup-audit.md:150-176`), and trading's
  dead-author heartbeat (`GEN2-FEEDBACK.md:11`) → expiry rule.
  **FLEET-FIX (done)**.
- **Docs-gate reachability + badge-in-first-12-lines:** caught real orphans
  (above). **ACCEPTED** (paid).
- **Stamp discipline:** "Timestamps from `date -u`, never the model's sense
  of time" (`docs/conventions.md:58`). **ACCEPTED**.
- **Counts-sync:** the ceremony that **caught** the HEAD-race — #166 remedy
  class, repeated each batch (`control/status.md:4,10,11,13`; #188 carried
  counts-sync commit `64ab0e6`). **ACCEPTED / FLEET-FIX done**.
- **Fresh audit finding — `status: new` is a dead header field.** Every ORDER
  header in both inboxes still reads `status: new` (measured this audit:
  venture-lab ORDERs 002–013 carry the field, ORDER 001 predates it;
  trading-strategy ORDERs 001–014 — all `status: new`), including orders long
  since consumed. This is per protocol, not omission — "Orders stay `status:
  new` in this file — the lane diffs the inbox against its own
  `control/status.md`" (`control/inbox.md:3-5`) — but the result is a
  constant-valued field that carries zero information and invites misreading
  an old order as unconsumed. Disposition: **FLEET-FIX** — drop `status:`
  from the ORDER header grammar (done-state already lives in status.md's
  `orders: acked=… done=…` line), or rename it to something that cannot read
  as live state.
- **Kit legacy-alias noise:** "legacy root `claims/` dir still coexists with
  `control/claims/` (claims-legacy-location nudge class)"
  (`.sessions/2026-07-11-kit-upgrade-v1.9.0.md:83-84`); root `claims/` still
  present at HEAD holding only a README; "alias/mirror jobs red without
  measuring anything" (`CONSTITUTION.md:48`). **FLEET-FIX** — retire the root
  alias once the kit permits.
- **CAPABILITIES case-collision:** `docs/CAPABILITIES.md` vs
  `docs/capabilities.md` collided and was merged 2026-07-11
  (`.sessions/2026-07-11-capabilities-case-collision.md`;
  `CAPABILITIES.md:228-232`). **FLEET-FIX (done)** — plus the standing
  lesson: case-insensitive filename collisions are a real class here.

## 8. What we fixed ourselves

One line + citation each; all THIS seat's own engineering:

- **Auto-merge enabler installed in both repos** — VL `305646f` (#59), TS
  `bf885f0` (#65); ≈90 VL PRs self-landed (retro:88-89), TS proven #66–#76
  (`CAPABILITIES.md:117-118`); folded into conventions doctrine by ORDER 013
  (`17b0499`, #191).
- **Counts-sync remedy class** — #166 (`79a1987`) created it after the
  HEAD-race; institutionalized per batch; #188 (`991dd96`, 💡-carrying) with
  counts commit `64ab0e6`.
- **Owner-queue generator + keyword map** — keyword map #100, generator
  `scripts/derive_owner_queue.py` #101 (origin: "PR #91's session-card 💡
  idea", docstring l.10), kill-clock column #128 (`53f6b65`), DUE/OVERDUE
  advisory #133 (`467d619`).
- **NL pre-naming practice** — NL titles pre-named in the EN title's own
  vetting packet ("Working title: De zoete zee — pre-named, not decided
  here", `docs/publishing/vetting/de-zoete-zee.md:40`; same
  `de-morgendeur.md:36`).
- **Fence + walls fold** — ORDER 012 #190 (`68d57bb`): capability-seed fence
  restored, walls folded into the digestible ledger, PLATFORM-LIMITS demoted
  to evidence appendix.
- **Seat-bound grading cron design** — fresh-session cron proven unreliable
  (0-for-2), so the Friday grading executor was deliberately bound to the
  coordinator seat with a dry-run pre-verification ("scripts/grade_paper.py
  dry-run CLEAN (exit 0…)", TS `control/status.md:15`; doctrine
  `docs/ROUTINES.md:17-29`).
- **CAPABILITIES case-collision merge** — 2026-07-11
  (`.sessions/2026-07-11-capabilities-case-collision.md`).

**Correction vs. the tasking.** The directive attributed "selection-fair gate
(PR #111), reason_class (PR #121), review index (#121), KILL-SIG
(#100/#109)" to venture-lab. **Verified false for venture-lab:** its PRs #100
/#109/#111/#121 are book/keyword-map PRs (verbatim titles: #100
"Keyword/category allocation map for the 14-title catalog…", #109 "Books:
Ultramarine serialized 3-part edition…", #111 "Books: The Slow Word —
novella cut…", #121 "Books: new kids manuscripts — The Windmill Mouse +
The Puddle Museum…"), and the terms selection-fair/reason_class/KILL-SIG
appear nowhere in venture-lab's tree or history. The mechanisms themselves
live in the trading lane's research methodology (KILL-SIG class and the
standing selection-fair gate:
`docs/research-program-retrospective.md@d857e50` §methodology;
`docs/selection-fair-gate.md` exists at TS main), and trading PR **#121** did
land the §7 review index (`experiments/paper/reviews.md`, `c60183f`) — but
the introducing PR numbers for the gate and KILL-SIG were not independently
verified this audit, so they are not claimed under the directive's numbers.

## 9. Top 5 remaining pains (ranked)

1. **Merge-path classifier vs two-party review.** Denials on #9/#15/#55
   (verbatims §3) that all landed anyway 12–21 min later; the rule pushes
   seats toward laundering paths instead of review. **ANTHROPIC — ask A**
   (§3, paste-ready).
2. **Branch-delete 403 → 187 dead branches in 5 days** (131 + 56, measured;
   §3), which also strands telemetry commits (`c0fce7c` lost, §6).
   **ANTHROPIC — ask B** (§3, paste-ready).
3. **Fresh-session cron delivery 0-for-2 + trigger lifecycle opacity**
   (vanished trigger with no tombstone, DOA provisions with no failure
   event, manual-fire wedge; §5). **ANTHROPIC — ask C:** "Please make
   trigger/session lifecycle observable and reliable: (1) fix or document
   fresh-session-per-fire cron delivery — observed 0-for-2 vs 100% on
   self-bound crons (2026-07-12 forensics); (2) provide tombstones or an
   audit log for deleted/vanished triggers — one trigger recorded 'verified
   live' vanished unfired with no agent-visible trail; (3) emit a
   provision-failure event when a session dies at spawn — a DOA session
   currently emits nothing and stays listed 'active' (this cost an afternoon,
   three times); (4) make triggers survive session archive or be
   seat-transferable — every succession currently forces a full rebind."
4. **Owner-click bottleneck: 262 pending clicks, 16 hard-gated**, on no-API
   surfaces (§3, §4). **ANTHROPIC — ask D:** "Please provide a supported
   owner-approval surface (API or batchable click queue) for claude.ai
   environments/routines/Projects and GitHub repo settings/rulesets — today
   these are no-API owner clicks, and this seat's backlog holds 262 pending
   owner clicks (16 hard-gated) presentable only via a hand-maintained
   OWNER-QUEUE.md."
5. **MCP read staleness + pagination caps** (~25-min PR state, §6;
   `actions_list` ignoring `per_page`, §3). **ANTHROPIC — ask E:** "Please
   (1) reduce GitHub MCP PR-state read staleness (~25 min observed per kit
   telemetry, reconfirmed on this audit's own PR) or expose a freshness
   hint; (2) fix `actions_list` ignoring `per_page` (always 30/page — a
   full-history read took 53 pages); (3) give sessions REST or GraphQL
   parity: direct api.github.com returns 'GitHub access is not enabled for
   this session…', GraphQL serves 'only the pinned set of PR-review
   operations' and suggests `gh api` — but `gh` is not installed."

## 10. Wishlist (ranked, deduped — references, not repeats)

1. Repo-scoped `claude/*` branch-delete grant (→ §3 ask B).
2. Trigger tombstones / lifecycle audit-log API (→ §9 ask C).
3. Session-bound → seat-transferable `send_later`/triggers, surviving archive
   (→ §5; §9 ask C item 4).
4. A supported owner-approval surface — batchable click queue (→ §9 ask D).
5. GraphQL/REST parity in-session, or ship `gh` where the error suggests it
   (→ §3, §9 ask E).
6. Webhook suppression (or distinct check conclusion) for designed-red
   checks like the born-red hold (→ §6, §7).
7. Provision-failure events for sessions that die at spawn (→ §5, §9 ask C
   item 3).
8. MCP list endpoints honoring `per_page` + freshness metadata on state
   reads (→ §3, §6, §9 ask E).

## 11. Honest gaps — what was NOT measured, and why

- **Directive items not found in repo evidence:** the "22:27Z night-order
  recon re-dispatch", the "75-min no-PR nudge", and any "WAKE-DEAD" token —
  pickaxe over both repos' full history came back empty (§5); nearest facts
  are the 22:30Z night-window open and the 23:27Z pacemaker pause. Also: the
  api.github.com denial verbatim was absent from PLATFORM-LIMITS itself
  (only the CAPABILITIES seed line existed) until this audit captured it
  live (§3).
- **Coordinator-attested-only findings** (chat-side walls are not
  repo-visible; recorded here as attestation, unverifiable from repos): the
  coordinator venue has no direct git/trigger tools and execution rides the
  worker-relay at ~27k tokens per trigger call; `send_later` binds only to
  the calling session; the SendMessage team-tool cannot reach project
  children; context-limit session splits (§6).
- **Token / metered-usage totals:** not measured — no usage API is available
  in-session.
- **Grading-loop delivery record:** none exists yet — the first scheduled
  grading fire is future-dated 2026-07-17T09:05Z (TS `control/status.md:19,
  21`); only the dry-run pre-verification is on record.
- **CI-round measurement limits:** the >1-round metric is a head-SHA push
  heuristic (§4) — pre-open pushes are invisible, pre-CI PRs (VL #1–#3, TS
  #2–#3) are uncovered, and the designed card-flip push inflates the count.
- **MCP staleness incident base:** no locally-logged incident in either repo
  — evidence is the inherited kit warning plus one session-observed data
  point on PR #192 (§6).
