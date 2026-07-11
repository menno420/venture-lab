# 2026-07-11 — PLATFORM-LIMITS capabilities link repair

> **Status:** `🔴 in-progress`

- **📊 Model:** venture-lab worker · fix/platform-limits-capabilities-link
- **session:** repoint an orphaned doc link and drop its temporary suppression

## 💡 Session idea
PR #18 merged the two capability ledgers into `docs/CAPABILITIES.md` and deleted
`docs/capabilities.md`. That left the Discovery-rule link in
`docs/PLATFORM-LIMITS.md` pointing at a file that no longer exists — a dead
link that was papered over by a temporary `accepted_risk` allowlist entry in
`.substrate/check-exceptions.yml`. Repoint the link to the surviving uppercase
ledger and remove the now-unneeded suppression so the dead-link guard stands on
its own again.

## Previous-session review
The 2026-07-11 case-collision session (`fix/capabilities-case-collision`)
collapsed `docs/CAPABILITIES.md` + `docs/capabilities.md` into one uppercase
ledger and deleted the lowercase copy, but was contractually barred from
editing `docs/PLATFORM-LIMITS.md` (a pending append owned that file), so it
deferred the pointer fix behind a temporary allowlist entry. PR #16 has since
landed its append, freeing the file. This session finishes the deferred repair.

## Deliverables
- `docs/PLATFORM-LIMITS.md`: the Discovery-rule link `[capabilities.md](capabilities.md)`
  repointed to `[CAPABILITIES.md](CAPABILITIES.md)`.
- `.substrate/check-exceptions.yml`: the temporary `PLATFORM-LIMITS.md`/`link`
  `accepted_risk` entry removed (dead-link guard now green on its own).
- This card.
