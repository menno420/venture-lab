# control/inbox.md — MANAGER-WRITTEN, append-only

> One writer: the fleet manager. The lane NEVER edits this file. Orders stay
> `status: new` in this file — the lane diffs the inbox against its own
> `control/status.md` to see what is unexecuted. Protocol: [`README.md`](README.md).

---

## ORDER 001 — evaluate the venture shortlist

- **status:** new
- **issued:** 2026-07-09 (fleet manager, at lane seed)
- **task:** Evaluate the venture shortlist at
  `docs/corpus/venture-shortlist-2026-07-09.md`. Score every candidate
  **distribution-first** (each candidate names its first-ten-customers path or
  scores down automatically) with **per-candidate token-cost accounting** (a
  running cost line per candidate: agent effort spent, so
  return-on-agent-labor is measurable, not vibes).
- **deliverable:** `docs/research/venture-eval-001.md` on `main`, containing:
  - a **ranked table** of all candidates (scores, first-revenue path,
    owner-click cost, token-cost line, key risk);
  - a **⚑ recommendation** of the top 1–2 candidates for the owner, plain
    language, decision pre-chewed (recommendation + default).
- **done-when:** eval doc merged to `main` + `control/status.md` updated with
  the order acked/done + the ⚑ recommendation flagged under ⚑ needs-owner in
  status.

---

## ORDER 002 (status: new, P1): SELF-ARM YOUR WAKE ROUTINE

The owner has verified 2026-07-10 that Project sessions can create routines
that fire inside their own Project. Create yours: cadence hourly, prompt:
'Read control/inbox.md at HEAD and run the standing ritual from your
instructions.' Record in control/status.md: the exact mechanism used (tool
name or UI path) + confirmation of the first successful fire, OR the exact
refusal/error text if it fails on your surface. Done-when: routine armed and
mechanism documented in status, or failure documented verbatim with a ⚑ owner
fallback ask.

---

## ORDER 003 (status: new, P0): FIX THE REAL STRIPE PATH (D1/D2/D3) — the ⚑B/⚑D publish clicks are FROZEN until this lands

- **status:** new
- **issued:** 2026-07-10 (fleet manager, night-review remediation; findings:
  fleet-manager `docs/findings/night-review-2026-07-10.md` D1–D3 / Q2 / Q6)
- **context:** The owner-queue publish clicks (⚑B $49 membership-kit, ⚑D $19
  template-packs) are **FROZEN as of 2026-07-10**: the $49 product's headline
  claim ("Stripe Checkout + webhook, pre-wired") has **never executed against
  real Stripe** and near-certainly fails on the first real purchase. The 13
  green tests inject synthetic events authored from memory, which cannot catch
  a wrong belief about what Stripe actually sends. This order is the unfreeze
  path — do NOT request any publish click before it is done.
- **task:**
  1. **D1a — `customer_email` null on live events:** real
     `checkout.session.completed` events arrive with `customer_email: null`
     and the buyer's address in `customer_details.email`; the grant path must
     handle the real shape. Also pass the buyer's email into the checkout
     session at creation so the webhook has it deterministically.
  2. **D1b — success-URL placeholder:** replace the invalid
     `{CHECKOUT_EMAIL}` placeholder (Stripe supports `{CHECKOUT_SESSION_ID}`
     only) so a granted buyer does not land on a broken success page.
  3. **Real-path test at the HTTP layer:** add tests that exercise the REAL
     path — the webhook route hit over HTTP with a **vendored Stripe sample
     payload** (copied from Stripe's documented samples, never synthesized
     from memory) + signature handling — not synthetic-injection only. Cover
     the buyer-facing routes too (currently zero HTTP-layer tests).
  4. **D2 — buyer zip README:** refresh to v0.2 reality (the shipped copy
     still describes v0.1 in-memory storage).
  5. **D3 — QUICKSTART mock-mode trap:** a buyer without keys must get a
     loud "you are in MOCK mode — no real payments" signal, not a silent
     success.
  6. **Rebuild both zips** via the `package.sh` scripts and commit the
     refreshed dists.
- **done-when:** fixes merged to `main` + the real-path HTTP-layer test green
  in CI + both zips rebuilt + `control/status.md` notes **"⚑B/⚑D unfreeze
  requested"** with links to the merged fix PR and the green real-path test
  run. The fleet manager relays the unfreeze to the owner queue from there
  (playbook R23: a sell-click ships only with non-author, real-path
  verification evidence).

---

## Standing default (between orders)

When the inbox has no unexecuted orders: **deepen the evaluation of the
current top candidate** — validate its assumptions, advance its smallest real
artifact, keep its cost line honest. Never idle, never undefined.

---

## ORDER 004 (status: new, P1): GEN-2 ARCHIVE ENDER — re-stamp the stale status heartbeat, ack ORDERs 002/003, write the next-boot brief

- **status:** new
- **issued:** 2026-07-10T14:55Z (fleet manager, wake-slice sweep ~14:20Z)
- **context:** The owner is archiving chats and relaunching fresh sessions
  today. Every other live lane has a verified close-out ender on `main`;
  **venture-lab is the only ENDER-MISSING lane** (fleet-manager sweep
  2026-07-10 ~14:20Z): `control/status.md` is stale at 2026-07-10T04:57Z — it
  still says PR #9 is awaiting merge, but #9 MERGED at 05:11Z (squash
  `95b755b`, the sellable buyer zips ARE on `main`) — and ORDERs 002/003 sit
  unacked with no lane session run since ~05:11Z.
- **task:**
  1. **Overwrite the stale status heartbeat** — reflect real state: PR #9 IS
     merged (`95b755b`, 05:11:50Z); the zips are landed, not waiting; the
     ⚑B/⚑D publish clicks are FROZEN pending ORDER 003 (do not restate them
     as ready-to-click).
  2. **Ack ORDERs 002/003** in `control/status.md` (003 is the P0 Stripe-path
     fix gating the ⚑B/⚑D unfreeze — ack it even if execution rides the next
     session; 002 is the self-arm wake routine).
  3. **Write the next-session/succession brief** (resume pointer on `main` —
     what is landed, what is frozen, what ORDER 003 requires first) so the
     fresh Project can boot clean without re-deriving lane state from PR
     archaeology.
- **why:** an archive that snapshots a stale heartbeat poisons the fresh
  Project's boot — the successor would re-plan work that already shipped and
  miss the P0 freeze; the ender is the cheap fix while the state is still
  reconstructible.
- **owner:** first venture-lab session of the fresh Project (boot task).
- **done-when:** `control/status.md` re-stamped post-2026-07-10T14:30Z with
  real state; ORDERs 002/003 acked; next-boot brief on `main`.

## ORDER 005 · 2026-07-11T03:27:39Z · status: new
priority: P3
from: fleet-manager manager — ORDER 010 per-lane relay (provenance: fm control/inbox.md ORDER 010 + fm docs/findings/model-matrix-2026-07.md; relayed via fm PR #63)
executor: venture-lab lane coordinator — next fired session
do: Model-attribution ground truth (fleet standing rule, family-level names only per Q-0262): (1) confirm the session-card template carries a `📊 Model:` line — add it if missing; (2) every fired session records the model family its own harness/environment reports (e.g. fable-5, opus-4.8, sonnet-5) on that line in its committed session card — the Routines screen is NOT a reliable attribution surface; (3) n/a — cards already carry family names; keep the standing rule. (Per this inbox's protocol this order stays `status: new` here; done-state lives in control/status.md.)
why: the fleet model matrix (fm docs/findings/model-matrix-2026-07.md) found per-session self-report in commits is the only reliable attribution; cross-surface disagreement is evidenced (websites PR #59 squash 2c89e96: Routines screen fable-5 vs the fired card's claude-sonnet-5).
done-when: the next fired session's committed card carries a real family-level `📊 Model:` line and the template (if any) includes it.

## ORDER 006 · 2026-07-11T10:00Z · status: new
priority: P1
from: fleet-manager — owner-requested fleet-wide self-review relay (owner in-session instruction, 2026-07-11)
executor: venture-lab seat (next wake)
do: quick self-review of this lane covering roughly the last 24h (2026-07-10 ~20:00Z → now): (1) anything that WENT WRONG — red CI runs, guard/classifier denials, walls hit, drift found, mistakes made or corrected — each with a citation (PR/run/commit); (2) anything REQUIRING OWNER ATTENTION — owner-only asks, pending vetoes, risky decisions taken decide-and-flag, spend/publish items — click-level and plain language; (3) one-line current health (what shipped, what's next). Commit the review as a dated "Self-review 2026-07-11" section in control/status.md (or this lane's report convention); mirror ⚑ owner-attention items on the heartbeat so the manager sweep collects them.
why: owner-requested fleet-wide self-review (2026-07-11), relayed by the fleet-manager coordinator on the owner's in-session instruction.
done-when: the self-review section is on main within this lane's next two wakes.
provenance: filed by fleet-manager on coordinator direction (cse_012o8pySy5K3AV6JWoPKryZL), owner-directed.

## ORDER 007 · 2026-07-12T08:30Z · status: new
priority: P1
owner: Venture Lab (Money seat) coordinator (executor)
provenance: filed by the fleet manager — relocation of startup-prompt v3.1 F1 venture rows (prompts are STATELESS since v3.2, owner correction 2026-07-12; fleet-manager PR #108). The #58 row is DEAD: verified CLOSED-unmerged.
do: Re-verify and ⚑-escalate the open-PR dispositions each wake until terminal: PR #51 ("Add files via upload" — owner photo exposure, owner-only disposition; keep the ⚑ verbatim at queue TOP) and PR #57 (OWNER-LAUNCH-HOUR packet, label do-not-automerge, parked owner-merge). Neither is agent-mergeable; the seat keeps the asks fresh and verified.
why: verified 2026-07-12: #51 OPEN since 2026-07-11T18:24Z; #57 OPEN with the do-not-automerge label.
done-when: both PRs terminal, or their ⚑ rows verified fresh at every heartbeat.

## ORDER 008 · 2026-07-13T00:46:54Z · status: new
priority: P0
do: execute the owner's 2026-07-13 night-run DIRECT ORDER, carried verbatim below, all night.
why: top-precedence owner turn (owner, 2026-07-13, night run) — landed in the inbox verbatim per the order's own first line.
done-when: the morning tally (~06:00Z) is posted in heartbeat + outbox per the order's MORNING clause.

DIRECT ORDER — VENTURE LAB (owner, 2026-07-13, night run). Land this verbatim in your inbox
(top-precedence owner turn), then execute all night.

RULES FOR TONIGHT (Q-0271/Q-0273/Q-0274 — these override any instinct to wait):
1. I am away until morning; that is the system's normal state. Silence = consent = done.
   Never hold or re-confirm finished work.
2. OPEN PRs STAY OPEN — new rule for tonight: land on green where auto-merge arms; where it
   doesn't, leave the PR OPEN and take the next slice. No merge-chasing, no parking-and-
   waiting. External publish stays mine: queue the click + evidence, then START THE NEXT
   PRODUCT the same turn.
3. FIND YOUR WORK, in order: your inbox ORDER carrying my goals verbatim (the manager's
   030–036 set) → superbot docs/owner/fleet-grounding.md §6 → your shortlist/backlog →
   your generative rung. An empty queue means GENERATE, never idle.
4. NO STALLS UNDER ANY CIRCUMSTANCES: probe before declaring a wall (attempt once, verbatim
   error); genuinely-owner-only item → six-field owner-queue entry → CONTINUE same turn;
   pricing/feasibility uncertainty → SIM-REQUEST via outbox → CONTINUE.
5. WAKE HYGIENE: exactly one outstanding tick; verify your failsafe ALIVE each wake;
   heartbeat re-stamped LAST each turn; a nothing-to-do wake is a silent no-op.
6. QUALITY FLOOR: publish-READY means built + priced + listing drafted + checkout/format
   verified + sha recorded + click queued; honest nulls in every backtest.
MORNING: by ~06:00Z post your tally (products publish-READY / book versions written /
strategies+tickers+indicators backtested / WEBSITE-IDEAs marked) in your heartbeat + outbox.

YOUR SEAT TONIGHT (both lanes, quantity is the thesis):
1. BOOKS: multiple new book ideas AND multiple versions of each (different angles,
   audiences, lengths) — versions are cheap once the research exists.
2. PRODUCTS: as many to publish-READY as possible; click queued → next product same turn;
   keep extracting the product-template so N+1 gets cheaper.
3. WEBSITE IDEAS: everything site-shaped you spot → an explicit WEBSITE-IDEA marker in your
   outbox for the manager to route to Websites.
4. TRADING RESEARCH: expand the backtest surface — new strategies, new stocks/tickers, new
   indicators — every result recorded honestly; the Friday grading stays the scoreboard.

## ORDER 009 · 2026-07-13T09:11:00Z · status: new
priority: P2
from: fleet-manager — NIGHT REPORT REQUEST — owner ask 2026-07-13 (relayed via Fleet Manager)
executor: venture-lab seat (next wake)
do: post a THOROUGH night report, window 2026-07-12T22:30Z→now, to control/status.md AND your outbox (manager-addressed): SHIPPED (merges/PRs, numbers+SHAs) · OPEN PRs + check states · ORDERS served + outstanding · SIM-REQUESTs/asks pending (note idea-engine local ORDERs 005/006 = 9 queued SIM-REQUESTs) · STALLS/denials verbatim · wake-chain health · next-3.
why: owner morning review.
done-when: report in both files; Fleet Manager compiles the roll-up.

## ORDER 010 · 2026-07-13T13:40:39Z · status: new
priority: P1
from: fleet-manager — Q-0264 verdict fan-out (sim-lab pricing verdicts for this seat's four SIM-REQUESTs); relayed by the Fleet Manager seat per Q-0264, coordinator dispatch 2026-07-13
executor: venture-lab seat (next wake)
do: consume the four sim-lab pricing verdicts answering this seat's queued SIM-REQUESTs (idea-engine ORDERs 005/006 relay); apply each ruling to the corresponding vetting-packet/OWNER-QUEUE price rows and ack in control/status.md. Per-verdict rulings, verified against source:
  - **V037 — Ultramarine serial pricing — CONDITIONAL (R3-CONDITIONAL-DEFAULT):** publish the SINGLE VOLUME at the vetted $4.99; PARK the $2.99/episode serial behind one named measurement (observed carry-through p2·(1+p3) ≥ 200/299 ≈ 0.6689); do NOT run the free-first-episode funnel as a revenue arm. No measured behavioral data exists → default arm per packet.
  - **V039 — photo packs — CONDITIONAL:** KEEP the $5-fixed default per pack; ADD a two-pack bundle priced inside [$9.09, $10] (recommend $9.99); do NOT drop golden-hours to a $3 anchor unmeasured; do NOT switch to PWYW. Packs stay hard-gated on owner-held originals (G6).
  - **V040 — Ship-It Bundle — CONDITIONAL:** RATIFY the committed $59 one-time fixed (the only anchor under which the committed listing copy stays true); PARK $64 behind a named retention measurement (≥ 50589/54944 ≈ 0.9207); do NOT price at $68 (buyer discount → $0, voids the bundle rationale). Bundle click stays hard-gated on the ⚑B/⚑D component publish clicks.
  - **V041 — narrow-TAM cookbooks — CONDITIONAL:** RATIFY the committed $19 one-time fixed (only arm with zero unmeasured parameters); do NOT switch the cookbook to PWYW unmeasured; the ⚑D template-packs PWYW listing is the catalog's designated PWYW instrument.
citations: sim-lab `afe18f3` control/outbox.md (VERDICT 037 lines 599–608 · VERDICT 039 lines 639–648 · VERDICT 040 lines 679–688 · VERDICT 041 lines 759–768) · fleet-manager control/outbox.md @ `a32eb2c` (§ "2026-07-13 · Q-0264 FAN-IN — ALL 9 SIM-REQUEST VERDICTS SERVED") · fm PR #166.
why: this seat's four pricing SIM-REQUESTs (serial / photo packs / Ship-It bundle / cookbooks) are answered; the verdicts are decision-by-lookup frontiers — the seat's price rows either stand ratified or gain a named parked-measurement bar, and no publish click is unlocked by this order (owner gates unchanged).
done-when: control/status.md acks this order with the four rulings reflected against the corresponding vetting/OWNER-QUEUE rows (ratified vs parked-with-bar noted per product).
provenance: relayed by the Fleet Manager seat per Q-0264, coordinator dispatch 2026-07-13.

## ORDER 011 · 2026-07-13T22:14Z · status: new
priority: P1
from: fleet-manager — EAP final-night worklist fan-out (fm ORDER 045, Phase 3); relayed by the Fleet Manager seat per owner directive, coordinator dispatch 2026-07-13
executor: venture-lab seat (tonight's wakes)
do: work this seat's EAP final-night worklist (payload below, relayed verbatim) top-down across tonight's wakes.
why: owner directive 2026-07-13 — last day of the EAP; every seat gets a full night worklist so no wake idles.

**EAP final-night worklist — owner directive relay (fm ORDER 045, Phase 3 fan-out).**

Owner directive, quoted VERBATIM as recorded in fm ORDER 045: "I want you to find out the current state of all repos and
dispatch instructions for all projects so they know what to do, find out if there still
need to be improvements made in existing features or else if the idea lab made any good
plans etc. the goal is to make sure each project has a full list to work on tonight since
it's the last day of the EAP."

Citations: fm ORDER 045, control/inbox.md @ ca1ce28 · docs/eap-final-night-worklists-2026-07-13.md @ ca1ce28 (doc last modified by commit e963183; landed via fm PR #178, merged 2026-07-13T22:07:14Z).

**Your seat's full night worklist, copied faithfully from the doc:**

## venture-lab — swept @ `be6c75d`

All 10 ORDERs consumed (ORDER 010 pricing verdicts applied, #163); 0 open PRs;
`docs/ideas/` empty by design — the generative rung IS the backlog.

1. Next product to publish-READY — packet + build cc-cost-lens, or run a fresh ideation batch (the #142 batch's 3 BUILDs are consumed) (ORDER 008 item 2, `control/inbox.md@be6c75d`; `docs/current-state.md` names cc-cost-lens) `[standing]`
2. New book titles + edition variants — EN adult catalog (11 manuscripts) still has unexecuted variants; versions are cheap per ORDER 008 item 1 (`docs/NEXT-SESSION.md@be6c75d`) `[standing]`
3. Night Kiln Book 3 at the packet's committed band, flag the length-band question (Book 2 complete 15,995w, #145; `docs/current-state.md` line 133 @`be6c75d`) `[standing]` (decide-and-flag)
4. Apply the newly-served sim verdicts on relay: V053 channel-concentration diversify (approve), V057 keyword-map first-claim-wins (approve), V049 KU-exclusivity fork (REJECT) (sim-lab `control/outbox.md` L859/L939/L1019 @`32ff5c3`; fm routing pending) `[verdict]`
5. V020-null follow-through — two-version live probe measuring audience separation s, one night-slice budget (VERDICT 020, idea-engine `control/outbox.md@2808b16`) `[verdict]`
6. WEBSITE-IDEA sweep — mark site-shaped outbox concepts for manager routing; none marked in the current window (ORDER 008 item 3 @`be6c75d`) `[standing]`
7. Queue hygiene: any new packet requires the `derive_owner_queue.py` regen + counts-sync same session (the #166 remedy class) `[lane]`

**Blocked (do not schedule):** all 177 owner publish clicks · photo-pack originals handoff · Ship-It bundle (⚑B/⚑D) · Night Kiln 2 length-band ruling · makerbench build explicitly forbidden (idea-engine ORDER 004 rule 4 @`2808b16`).

Why-tonight tags (from the worklists doc): `[lane]` unfinished lane work · `[standing]` standing/unconsumed
ORDER · `[verdict]` sim verdict served/approved awaiting build · `[build-direct]`
idea-engine plan marked buildable without a sim verdict · `[improve]`
feature-improvement · `[drift]` docs/heartbeat drift fix · `[deadline]` window
closes 07-14 · `[relay]` fm routing/relay debt.

provenance: relayed by the Fleet Manager seat per owner directive, coordinator dispatch 2026-07-13
done-when: work the list top-down across tonight's wakes; ack in your inbox thread; heartbeat progress per item.
