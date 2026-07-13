# Session — ORDER 010: apply sim-lab pricing verdicts V037/V039/V040/V041

> **Status:** `in-progress`

- **📊 Model:** Fable 5 · worker slice · ORDER 010 (Q-0264 verdict fan-out)
- **session:** Consume the four sim-lab pricing verdicts (control/inbox.md ORDER 010, landed PR #161 squash `84d4bcb`; source sim-lab `afe18f3`, fm outbox `a32eb2c`, fm PR #166) and apply each ruling minimally to the corresponding vetting-packet price rows / §7 owner-gate blocks, regenerate `docs/publishing/OWNER-QUEUE.md`, and ack in `control/status.md`. No publish click is unlocked by this slice — owner gates unchanged.
- **started (date -u):** Mon Jul 13 13:58:34 UTC 2026
- **closed (date -u):** [[fill:closed]]

## ⟲ Previous-session review

[[fill:previous-session review]]

## 💡 Session idea

[[fill:idea]]

## Scope

- V037 → `docs/publishing/vetting/ultramarine.md`: single volume $4.99 RATIFIED; $2.99/episode serial PARKED behind observed carry-through p2·(1+p3) ≥ 200/299 ≈ 0.6689; free-first-episode funnel is not a revenue arm.
- V039 → `docs/publishing/vetting/photo-packs.md`: $5-fixed per pack RATIFIED; two-pack bundle row added inside [$9.09, $10] (recommend $9.99); no unmeasured $3 golden-hours anchor; no PWYW switch; G6 hard gate unchanged.
- V040 → `docs/publishing/vetting/bundle-starter.md`: $59 one-time fixed RATIFIED; $64 PARKED behind retention ≥ 50589/54944 ≈ 0.9207; never $68; ⚑B/⚑D hard gate unchanged.
- V041 → `docs/publishing/vetting/merge-wall-cookbook.md`: $19 one-time fixed RATIFIED; no PWYW switch unmeasured; template-packs stays the catalog's designated PWYW instrument (its packet does not contradict — left untouched).
- Regenerate OWNER-QUEUE via `scripts/derive_owner_queue.py` (never hand-edited); heartbeat ack in `control/status.md`.
