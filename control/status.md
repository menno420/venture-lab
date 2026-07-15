# Venture Lab — coordinator heartbeat
updated: 2026-07-15T04:01:46Z

**Rebooted 2026-07-15** on the owner's v3.6 reboot prompt (the per-seat go per ORDER 015). The 2026-07-14 dormancy is superseded; EAP extended through 2026-07-21. Predecessor dormancy record: control/status.md @ commit 9ed6a35.

**ORDER 015: acknowledged** (EAP extension; routine re-arm authorized by the reboot go). Extension feature tests (add_repo, overview panel) queued this session.

**Routines (verified via list_triggers):**
- Failsafe: trig_01GeQiMM3nHMQTyuLMsWj7q3 · "Venture Lab failsafe wake" · cron 45 1-23/2 * * * · bound to the coordinator session · next fire 2026-07-15T05:45Z
- Weekly grading (business cron): trig_01BsYsMABu2vfH4d2MzuSLs6 · "Venture Lab weekly grading" · cron 0 9 * * 5 · bound to the coordinator session · next fire 2026-07-17T09:08Z
- Pacemaker send_later chain alive (~15 min cadence)
- Foreign trigger trig_01YXNmgqYeYQ1LuepsLmbNCG (fires 2026-07-17T09:00Z): not this seat's — untouched. Old trading failsafe trig_01YBaVeKAW2fSD83S9F37s2d: auto-disabled (env deleted), inert.

**PRs:** none parked at reboot; open = this reboot-ack PR.

**Parked owner work (pointers):** publish queue (262 clicks, 19 decisions) → docs/publishing/OWNER-QUEUE.md; NK2 length-band decision open; SWTK kill clocks per docs.

⚑ owner: the Project's custom instructions are dictionary v3.4; the registry copy is v3.6 — re-paste from fm:projects/venture-lab/instructions.md.

**Known-stale:** docs/current-state.md (says kit v1.15.0/PR #83; live is v1.17.0/PR #199) — refresh queued.

**Next 2:** (1) add_repo + overview-panel capability tests → docs/CAPABILITIES.md; (2) docs/current-state.md refresh. Friday grading pass covered by the armed cron.

kit: v1.17.0
