# Hooks — install contract

These hooks make the session discipline **automatic** instead of aspirational:
an orientation reminder at session start, a close-ritual nudge when the agent
tries to stop, and a quality-floor reminder after each edit. All three are
**advisory and fail open** — they print a message and exit `0`. They never
block a tool, an edit, or a session stop.

## What's here

| file | hook event | what it does |
| --- | --- | --- |
| `settings.template.json` | — | the hooks block to merge into `.claude/settings.json` |
| `scripts/agent-orient.sh` | `SessionStart` | prints the reading list + heartbeat reminder |
| `scripts/session-close-check.sh` | `Stop` | nudges if today's session card is missing/unfinished |
| `scripts/post-edit-reminder.sh` | `PostToolUse` (Edit\|Write) | reminds to run the quality floor before pushing |

## Install — stage, never auto-write

This pack **stages** templates; it does not write your `.claude/` tree for you.
Install deliberately:

1. Copy `scripts/` into your repo (e.g. to `scripts/`), and `chmod +x scripts/*.sh`.
2. Open `settings.template.json` and replace every `<FILL: ...>`:
   - `<FILL: interpreter>` → the runtime on your PATH (`bash`, `python3`, …).
   - `<FILL: repo-root>` → where the scripts live (an absolute path is safest).
3. Merge the `hooks` block into your repo's `.claude/settings.json`. If that
   file already has a `hooks` key, merge arrays — don't clobber it.
4. Restart your Claude Code session so `SessionStart` fires, and confirm you see
   the orientation banner.

## Customize before you trust it

Edit the reading list in `agent-orient.sh`, the `SESSIONS_DIR` and card-status
grep in `session-close-check.sh`, and the check command in
`post-edit-reminder.sh` to match your repo. Because the hooks exit `0`, a
misconfigured one degrades to silence — it will never wedge a session.
