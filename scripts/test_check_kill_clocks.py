#!/usr/bin/env python3
"""scripts/test_check_kill_clocks.py — kill-clock advisory tests, stdlib only.

Covers `check_kill_clocks.py` (which imports `derive_owner_queue.parse_packet`
rather than forking the KILL-CHECK grammar):

1. upcoming — checkpoints after --today print `upcoming … (in N days)`;
2. due today — a checkpoint equal to --today prints `DUE today`;
3. overdue — checkpoints before --today print `OVERDUE … (N days overdue)`;
4. no tokens — a live packet without a KILL-CHECK line reports the
   no-checkpoints line (and a pending-only packet's tokens don't count:
   the kill clock only ticks once live);
5. malformed date tolerated — an ISO-shaped non-date (2026-13-45) is
   SKIPPED with a note, the valid sibling still classifies, exit still 0;
   plus a malformed --today and a missing --today both skip with exit 0.

Every test asserts exit code 0 (advisory contract).

Run: python3 -m unittest discover -s scripts -p "test_*.py" -v
     (or, from scripts/: python3 -m unittest test_check_kill_clocks -v)
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_kill_clocks as ckc  # noqa: E402
import derive_owner_queue as doq  # noqa: E402

FLAG = doq.FLAG
TIMER = doq.TIMER

LIVE_TWO_CLOCKS = f"""# Title Vetting — Ticking Gadget

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $29 — DONE 2026-07-12

KILL-CHECK: {TIMER} 2026-07-19 T+7 funnel checkpoint ·
  {TIMER} 2026-07-26 T+14 kill-rule deadline
"""

LIVE_NO_CLOCK = f"""# Title Vetting — Quiet Gadget

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $9 — DONE 2026-07-10
"""

PENDING_WITH_CLOCK = f"""# Title Vetting — Not Yet Live

## 7. {FLAG} OWNER-GATE — publish clicks

- [ ] {FLAG} **Owner:** the publish click (not yet executed).

KILL-CHECK: {TIMER} 2026-07-19 premature clock (product not live)
"""

LIVE_BAD_CALENDAR_DATE = f"""# Title Vetting — Broken Clock

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $19 — DONE 2026-07-12

KILL-CHECK: {TIMER} 2026-13-45 impossible month-day · {TIMER} 2026-07-20 real one
"""


class KillClockTests(unittest.TestCase):
    def _run(self, files: dict[str, str], argv: list[str]) -> tuple[int, str]:
        """check_kill_clocks.main() against a temp packet dir → (exit, stdout)."""
        with tempfile.TemporaryDirectory() as tmp:
            vdir = Path(tmp) / "vetting"
            vdir.mkdir()
            for name, content in files.items():
                (vdir / name).write_text(content, encoding="utf-8")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = ckc.main(["--vetting-dir", str(vdir), *argv])
        return code, buffer.getvalue()

    def test_upcoming(self):
        code, out = self._run({"tick.md": LIVE_TWO_CLOCKS}, ["--today", "2026-07-13"])
        self.assertEqual(code, 0)
        self.assertIn(
            f"[Ticking Gadget] {TIMER} upcoming 2026-07-19 — T+7 funnel checkpoint (in 6 days)",
            out,
        )
        self.assertIn("upcoming 2026-07-26 — T+14 kill-rule deadline (in 13 days)", out)
        self.assertIn("checked 2 checkpoints across 1 live products — 0 overdue, 0 due today, 2 upcoming", out)
        self.assertNotIn("OVERDUE", out)
        self.assertNotIn("ACTION", out)

    def test_due_today(self):
        code, out = self._run({"tick.md": LIVE_TWO_CLOCKS}, ["--today", "2026-07-19"])
        self.assertEqual(code, 0)
        self.assertIn(
            f"[Ticking Gadget] {TIMER} DUE today 2026-07-19 — T+7 funnel checkpoint", out
        )
        self.assertIn("upcoming 2026-07-26 — T+14 kill-rule deadline (in 7 days)", out)
        self.assertIn("1 due today", out)
        self.assertIn("ACTION", out)

    def test_overdue(self):
        code, out = self._run({"tick.md": LIVE_TWO_CLOCKS}, ["--today", "2026-07-27"])
        self.assertEqual(code, 0)
        self.assertIn("OVERDUE 2026-07-19 — T+7 funnel checkpoint (8 days overdue)", out)
        self.assertIn("OVERDUE 2026-07-26 — T+14 kill-rule deadline (1 day overdue)", out)
        self.assertIn("2 overdue, 0 due today, 0 upcoming", out)
        self.assertIn("ACTION", out)

    def test_no_tokens(self):
        # A live packet without KILL-CHECK and a pending packet WITH one:
        # neither yields a checkpoint (kill clocks only tick once live).
        code, out = self._run(
            {"quiet.md": LIVE_NO_CLOCK, "pending.md": PENDING_WITH_CLOCK},
            ["--today", "2026-07-13"],
        )
        self.assertEqual(code, 0)
        self.assertIn("no live kill-clock checkpoints found (2 packets scanned", out)
        self.assertNotIn("premature clock", out)

    def test_malformed_checkpoint_date_tolerated(self):
        code, out = self._run(
            {"broken.md": LIVE_BAD_CALENDAR_DATE}, ["--today", "2026-07-13"]
        )
        self.assertEqual(code, 0)
        self.assertIn("SKIPPED 2026-13-45", out)
        self.assertIn("not a real calendar date", out)
        self.assertIn("upcoming 2026-07-20 — real one (in 7 days)", out)
        self.assertIn("1 skipped (malformed date)", out)

    def test_malformed_today_tolerated(self):
        code, out = self._run({"tick.md": LIVE_TWO_CLOCKS}, ["--today", "not-a-date"])
        self.assertEqual(code, 0)
        self.assertIn("skipped — --today is not a real ISO date", out)

    def test_missing_today_tolerated(self):
        code, out = self._run({"tick.md": LIVE_TWO_CLOCKS}, [])
        self.assertEqual(code, 0)
        self.assertIn("skipped — --today YYYY-MM-DD is required", out)


if __name__ == "__main__":
    unittest.main()
