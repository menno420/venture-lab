#!/usr/bin/env bash
# SessionStart hook — prints an orientation reminder, then exits 0 (never blocks).
# Wire it via hooks/settings.template.json. Edit the reading list for your repo.
set -euo pipefail

cat <<'EOF'
── session start ──────────────────────────────────────────
Read before working:
  1. CLAUDE.md          — the working agreement + rails
  2. <FILL: your status/ledger doc>  — current state
  3. session-discipline.md — heartbeat-before-work, close ritual
Reminder: first act of the session is a heartbeat commit
(a status line or a born-red session card), NOT silent work.
───────────────────────────────────────────────────────────
EOF

exit 0
