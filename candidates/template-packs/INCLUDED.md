# Included — file manifest

Every file in the Agent-Workflow Template Pack and what it does. All pack files
carry `<FILL: ...>` placeholders where a repo-specific value belongs.

## Pack contents

| file | what it does |
| --- | --- |
| `pack/CLAUDE.md.template` | Starter **agent constitution**: working agreement, act-vs-ask autonomy rails, PR & merge conventions, an explicit **done-when** completion contract, and a **quality-floor** rule (one command that must pass before every push). Drop in as `CLAUDE.md`. |
| `pack/session-card.template.md` | A **session-log card** carrying the discipline markers: a Status badge (`in-progress` → `complete`), a `💡` idea line, a `⟲ previous-session review` handoff, a `📊 Model:` line, and started/completed timestamps from `date -u`. Open each session with it, close each session by flipping it. |
| `pack/session-discipline.md` | The **1-page playbook** behind the templates: heartbeat-before-work, claim-before-build, the close ritual, timestamps from `date -u`, and forward-only git — with a short note on *why* each rule exists (the parallel-agent failure it prevents). |
| `pack/hooks/settings.template.json` | A **Claude Code hooks** block wiring `SessionStart`, `Stop`, and `PostToolUse` to the three scripts below. Merge into `.claude/settings.json`. |
| `pack/hooks/README.md` | The hooks **install contract**: stage under `.claude/`, never auto-write; fill the paths; all hooks are advisory and fail open (exit `0`). |
| `pack/hooks/scripts/agent-orient.sh` | `SessionStart` hook — prints the reading list + heartbeat reminder. |
| `pack/hooks/scripts/session-close-check.sh` | `Stop` hook — nudges if today's session card is missing or still `in-progress`/`drafted`. |
| `pack/hooks/scripts/post-edit-reminder.sh` | `PostToolUse` (Edit\|Write) hook — reminds to run the quality floor before pushing. |

## Top-level docs (not part of the drop-in pack)

| file | what it does |
| --- | --- |
| `README.md` | What the pack is, who it's for, quickstart, honest scope. |
| `LISTING.md` | Publish-ready marketplace copy (Gumroad / Lemon Squeezy). |
| `INCLUDED.md` | This manifest. |

## Install order

1. `pack/CLAUDE.md.template` → `CLAUDE.md` (resolve `<FILL>`s).
2. `pack/session-discipline.md` → repo root (read once).
3. `pack/hooks/` → `.claude/settings.json` + `scripts/` (see hooks/README.md).
4. `pack/session-card.template.md` → your session-log dir (use per session).
