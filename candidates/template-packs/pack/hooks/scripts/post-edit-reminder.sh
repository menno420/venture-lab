#!/usr/bin/env bash
# PostToolUse (Edit|Write) hook — advisory reminder after edits. Exits 0 always.
# Keep it cheap: it runs after every file write, so no heavy work here.
set -euo pipefail

echo "↺ edited a file — before you push, run the quality floor: <FILL: your one check command, e.g. npm run ci>"

exit 0
