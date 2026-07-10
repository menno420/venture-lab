# substrate-kit upgrade report — v1.6.0 → v1.7.0

> Generated 2026-07-10 by `bootstrap.py upgrade`. Rollback: `python3 bootstrap.py upgrade --rollback`.

**Docs:** consumer-edited: 3 · diverged: 1 · unchanged: 15

| planted doc | class | note |
|---|---|---|
| CONSTITUTION.md | unchanged | template identical across versions |
| docs/decisions.md | unchanged | template identical across versions |
| docs/architecture.md | unchanged | template identical across versions |
| docs/ownership.md | unchanged | template identical across versions |
| docs/runtime_contracts.md | unchanged | template identical across versions |
| docs/repo-navigation-map.md | unchanged | template identical across versions |
| docs/helper-policy.md | unchanged | template identical across versions |
| docs/collaboration-model.md | unchanged | template identical across versions |
| docs/ai-project-workflow.md | unchanged | template identical across versions |
| docs/owner-profile.md | unchanged | template identical across versions |
| docs/AGENT_ORIENTATION.md | unchanged | template identical across versions |
| docs/current-state.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| docs/question-router.md | unchanged | template identical across versions |
| docs/CAPABILITIES.md | unchanged | template identical across versions |
| docs/ideas/README.md | unchanged | template identical across versions |
| .session-journal.md | unchanged | template identical across versions |
| control/README.md | diverged | both the template and the doc moved — manual merge |
| control/inbox.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |
| control/status.md | consumer-edited | template unchanged — consumer-owned, nothing to apply |

## Template deltas for diverged docs

### control/README.md

```diff
--- control/README.md (template@old, current slots)
+++ control/README.md (template@new, current slots)
@@ -37,6 +37,10 @@
   Stop hook's overwrite reminder clears when any lane's heartbeat is fresh (it cannot know which
   lane a session belongs to). An empty list falls back to the default — misconfiguration never
   silently disables the gate.
+- **One command, not hand-edits** — a Project joining a SHARED repo runs
+  `bootstrap adopt --lane <name>`: it plants `control/status-<name>.md` (skip-if-exists),
+  declares it in `heartbeat_files`, and leaves `inbox.md`/`README.md` single — a second lane
+  never re-plants the first Project's files (the double-adoption fix).
 
 ## Per-session ritual (every session, and every routine wake)
 
```

