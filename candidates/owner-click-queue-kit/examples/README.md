# Worked examples

Two layouts, both derived with the same tool. Each directory commits
the EXPECTED queue output so you can verify byte-identical determinism
yourself (the kit's test suite does exactly this diff).

## `agent-fleet/` — a gates directory fed by multiple agents

Three gate files from a simulated fleet, chosen to show every grammar
feature at once:

- `gates/checkout-revamp.md` — an open **decision** with a bolded
  default, plus a `blocking` click → the whole run renders
  **HARD-GATED** and sorts last.
- `gates/status-page.md` — a pure **click-run** (no decisions), sorts
  first.
- `gates/newsletter-launch.md` — the POST-click state: **DONE-flipped**
  rows in the read-only Live section + an armed **KILL-CHECK** clock
  with the earliest checkpoint surfaced.

```
cd agent-fleet
python3 ../../ocq.py derive --gates gates --output /tmp/queue.md
diff /tmp/queue.md EXPECTED-OWNER-QUEUE.md && echo byte-identical
python3 ../../ocq.py lint --gates gates
```

## `solo-repo/` — one gate section in an ordinary doc

No gates directory: `RELEASE-GATE.md` is a normal repo doc whose
OWNER-GATE section the deriver is pointed at directly.

```
cd solo-repo
python3 ../../ocq.py derive --gates RELEASE-GATE.md --output /tmp/queue.md
diff /tmp/queue.md EXPECTED-OWNER-QUEUE.md && echo byte-identical
```

Note: the committed `EXPECTED-OWNER-QUEUE.md` files are comparison
outputs, not gates — the deriver skips `EXPECTED-*` names when scanning
a directory, so deriving over a whole example dir stays correct.
