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

## Standing default (between orders)

When the inbox has no unexecuted orders: **deepen the evaluation of the
current top candidate** — validate its assumptions, advance its smallest real
artifact, keep its cost line honest. Never idle, never undefined.
