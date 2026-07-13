# Session — ORDER 010: apply sim-lab pricing verdicts V037/V039/V040/V041

> **Status:** `complete`

- **📊 Model:** Fable 5 · worker slice · ORDER 010 (Q-0264 verdict fan-out)
- **session:** Consume the four sim-lab pricing verdicts (control/inbox.md ORDER 010, landed PR #161 squash `84d4bcb`; source sim-lab `afe18f3`, fm outbox `a32eb2c`, fm PR #166) and apply each ruling minimally to the corresponding vetting-packet price rows / §7 owner-gate blocks, regenerate `docs/publishing/OWNER-QUEUE.md`, and ack in `control/status.md`. No publish click is unlocked by this slice — owner gates unchanged.
- **started (date -u):** Mon Jul 13 13:58:34 UTC 2026
- **closed (date -u):** Mon Jul 13 14:02:15 UTC 2026

## ⟲ Previous-session review

Previous session: PR #162 (boot-refresh, squash `d780c78`, card
`.sessions/2026-07-13-boot-refresh.md`). Two things it did that this slice
directly benefited from: (1) it recorded ORDER 010 in the heartbeat as
"received, execution pending (apply rulings … and ack here on the next
working pass)" — an explicit baton with a precise seam, so this session's
ack was a single-sentence amendment of exactly that clause rather than a
re-derivation of what was owed; (2) its 💡 (role-keyed, not ID-keyed,
trigger records) was already applied inside its own heartbeat paragraph —
idea-to-application in zero sessions, the cheapest possible proof. Honest
nit carried forward: the heartbeat's line-3 is one very long single-line
sentence, so amending one clause requires exact-string surgery on a
300-word line; a future heartbeat format with one fact per line would make
seam amendments diff-cleaner.

## 💡 Session idea

**Give parked-with-bar pricing a machine-readable token, and stop
annotation text leaking into derived DEFAULTs.** This slice recorded two
PARKED-WITH-BAR arms (V037 serial: carry-through ≥ 0.6689; V040 $64:
retention ≥ 0.9207) as prose only — nothing can enumerate "which price
arms are parked, behind which named measurement" without re-reading four
packets. A `PARKED-BAR: <arm> until <metric> ≥ <value>` line in §7, parsed
by the same tolerant grammar as `KILL-CHECK:` (⏲ precedent), would let
`derive_owner_queue.py` render a read-only "parked pricing arms" section
and let a future measurement session grep its release bar. Directly
observed second half: `extract_default`'s paren-fallback captured this
slice's whole ratification annotation into ultramarine's derived
`**DEFAULT:**` ("$4.99 recommended; ratified per ORDER 010 …") — the
fallback should clip at the first `;`/`—` separator so defaults stay
one-word-agreeable. Deduped against `.sessions/`: night-photo-packs (blocked
flag granularity) and night-bundle-packet (`blocking[until:]` gate types)
propose machine-readable CLICK gating; no existing card proposes a parked
PRICE-arm token or the default-extractor clip. Guard recipe:
`extract_default` + `derive_owner_queue.py` (paren-fallback branch), pinned
via the kit's grammar tests.

## Scope

- V037 → `docs/publishing/vetting/ultramarine.md`: single volume $4.99 RATIFIED; $2.99/episode serial PARKED behind observed carry-through p2·(1+p3) ≥ 200/299 ≈ 0.6689; free-first-episode funnel is not a revenue arm.
- V039 → `docs/publishing/vetting/photo-packs.md`: $5-fixed per pack RATIFIED; two-pack bundle row added inside [$9.09, $10] (recommend $9.99); no unmeasured $3 golden-hours anchor; no PWYW switch; G6 hard gate unchanged.
- V040 → `docs/publishing/vetting/bundle-starter.md`: $59 one-time fixed RATIFIED; $64 PARKED behind retention ≥ 50589/54944 ≈ 0.9207; never $68; ⚑B/⚑D hard gate unchanged.
- V041 → `docs/publishing/vetting/merge-wall-cookbook.md`: $19 one-time fixed RATIFIED; no PWYW switch unmeasured; template-packs stays the catalog's designated PWYW instrument (its packet does not contradict — left untouched).
- Regenerate OWNER-QUEUE via `scripts/derive_owner_queue.py` (never hand-edited); heartbeat ack in `control/status.md`.
