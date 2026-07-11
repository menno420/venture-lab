# Session — ORDER 005: model-attribution (confirm + record the family line)

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · high · order-005 model-attribution
- **session:** ORDER 005 — confirm the card template carries a `📊 Model:` line and record this session's family-level model attribution
- **started (date -u):** Sat Jul 11 2026 UTC

## ⟲ Previous-session review

Previous-session review: ORDER 004 (PR #15, `ab5f533`) repaired control-bus state and left the brief in `docs/NEXT-SESSION.md`; the coordinator heartbeat carried ORDER 005 forward as the model-attribution ground-truth pass. Read-only review of the recent cards and `bootstrap.py` template — no regressions observed, no prior work reverted.

## 💡 Session idea

ORDER 005: confirm the session-card template already emits a `📊 Model:` line and record this session's model attribution at family granularity. Attribution is only trustworthy when every born card carries a real family-level model line, so the deliverable is a committed card that itself demonstrates the line — not a template edit.

## Scope (ORDER 005)

- Item (1): confirm the card template already carries the `📊 Model:` line — no template change.
- Item (2): record THIS session's family-level model line on a committed born-red card.
- Keep the standing rule: every session card carries a real, family-level `📊 Model:` line.

## Work log

- **Item (1) — confirmed present, no change.** The `📊 Model:` line is already carried by the card template in `bootstrap.py:240-245` (needle `bootstrap.py:4423`); all recent cards (e.g. ORDER 003) already render it. Nothing to add to the template.
- **Item (2) — satisfied by this card.** This card carries `- **📊 Model:** opus-4.8 · high · order-005 model-attribution`. The family `opus-4.8` is reduced from the harness-reported identifier `claude-opus-4-8[1m]` to family-level per Q-0262 — the exact ID is never recorded, only the family.
- **Standing rule kept.** Every born card must carry a real, family-level `📊 Model:` line; this session records its own and leaves the rule in force for the next link.

## Status / outcome

In progress — born-red at first commit; flips to `complete` as the deliberate last step once status bookkeeping is committed.
