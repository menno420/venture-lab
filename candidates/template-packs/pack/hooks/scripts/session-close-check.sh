#!/usr/bin/env bash
# Stop hook — advisory close-ritual check. Prints a nudge if today's session
# card looks missing or unfinished, then exits 0 (never blocks the stop).
set -euo pipefail

SESSIONS_DIR="${SESSIONS_DIR:-.sessions}"   # <FILL if your logs live elsewhere>
TODAY="$(date -u +%Y-%m-%d)"

card="$(ls "${SESSIONS_DIR}"/${TODAY}-*.md 2>/dev/null | head -n1 || true)"

if [ -z "${card}" ]; then
  echo "⚠ close ritual: no session card for ${TODAY} in ${SESSIONS_DIR}/ — create one before stopping."
elif grep -qiE 'Status:.*(in-progress|drafted)' "${card}"; then
  echo "⚠ close ritual: ${card} is still in-progress/drafted — flip Status to complete and write the close-out."
else
  echo "✓ close ritual: ${card} present."
fi

exit 0
