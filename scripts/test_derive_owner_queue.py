#!/usr/bin/env python3
"""scripts/test_derive_owner_queue.py — DONE-disposition tests, stdlib only.

Covers the `- [x] ⚑ **Owner:** … — DONE <ISO date>` disposition added for
already-live products (SWTK was live with no way to appear in the queue):

1. a legacy packet (unchecked boxes, no DONE) parses exactly as before —
   pending clicks queued, NO Live section rendered;
2. a DONE row lands in the read-only "Live / completed" section and adds
   ZERO pending clicks;
3. a mixed packet splits correctly — pending rows queue, DONE rows go live;
4. legacy tolerance: a CHECKED box WITHOUT the DONE marker still queues
   (both marks are required for the live disposition).

Run: python3 -m unittest discover -s scripts -p "test_*.py" -v
     (or, from scripts/: python3 -m unittest test_derive_owner_queue -v)
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import derive_owner_queue as doq  # noqa: E402

FLAG = doq.FLAG

LEGACY_PACKET = f"""# Title Vetting — Legacy Widget

## 7. {FLAG} OWNER-GATE — publish clicks (queued, never automated)

**OWNER-ACTION — Publish "Legacy Widget" at $9**
1. **Storefront account:** owner signs in.
2. **Publish + record:** publish and copy the URL.

- [ ] {FLAG} **Owner:** zip uploaded + sha256 spot-check.
- [ ] {FLAG} **Owner:** the publish click + public URL copied.
"""

LIVE_PACKET = f"""# Title Vetting — Live Gadget

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $29 — DONE 2026-07-12
- [x] {FLAG} **Owner:** test purchase verified end-to-end — DONE 2026-07-12
"""

MIXED_PACKET = f"""# Title Vetting — Mixed Kit

## 7. {FLAG} OWNER-GATE — publish clicks

- [x] {FLAG} **Owner:** the publish click at $19 — DONE 2026-07-11
- [ ] {FLAG} **Owner:** post-launch coupon set up.
"""

CHECKED_NO_DONE_PACKET = f"""# Title Vetting — Checked Legacy

## 7. {FLAG} OWNER-GATE — publish clicks

- [x] {FLAG} **Owner:** the publish click (checked by hand, no DONE marker).
"""


class DeriveOwnerQueueDoneDisposition(unittest.TestCase):
    def _run(self, packets: dict[str, str]) -> tuple[str, doq.ParseResult]:
        """Write packets to a temp vetting dir, parse, render; no keyword map."""
        result = doq.ParseResult()
        with tempfile.TemporaryDirectory() as tmp:
            vdir = Path(tmp) / "vetting"
            vdir.mkdir()
            for name, body in packets.items():
                (vdir / name).write_text(body, encoding="utf-8")
            for packet in sorted(vdir.glob("*.md")):
                doq.parse_packet(packet, result)
        return doq.render(result, "vetting"), result

    def test_legacy_packet_unchanged(self) -> None:
        output, result = self._run({"legacy.md": LEGACY_PACKET})
        self.assertEqual(len(result.groups), 1)
        self.assertEqual(len(result.groups[0].clicks), 2)
        self.assertEqual(result.live, [])
        self.assertEqual(result.manual, [])
        self.assertIn("- [ ] **WHAT:** zip uploaded + sha256 spot-check.", output)
        self.assertNotIn("Live / completed", output)
        self.assertNotIn("- [x]", output)

    def test_done_row_lands_in_live_section(self) -> None:
        output, result = self._run({"live.md": LIVE_PACKET})
        self.assertEqual(result.groups, [])  # ZERO pending click sequences
        self.assertEqual(len(result.live), 1)
        self.assertEqual(len(result.live[0].done), 2)
        self.assertEqual(result.live[0].done[0]["date"], "2026-07-12")
        self.assertEqual(result.manual, [])  # all-DONE packet is NOT manual-review
        self.assertIn("## 4. Live / completed — already published, read-only", output)
        self.assertIn("- [x] the publish click at $29 · **DONE:** 2026-07-12", output)
        # §2 pending click-run carries nothing at all.
        self.assertIn("*(none parsed)*", output)

    def test_mixed_packet_splits_pending_and_done(self) -> None:
        output, result = self._run({"mixed.md": MIXED_PACKET})
        self.assertEqual(len(result.groups), 1)
        self.assertEqual(len(result.groups[0].clicks), 1)  # pending only
        self.assertEqual(len(result.live), 1)
        self.assertEqual(len(result.live[0].done), 1)
        self.assertIn("- [ ] **WHAT:** post-launch coupon set up.", output)
        self.assertIn("- [x] the publish click at $19 · **DONE:** 2026-07-11", output)
        # The DONE row must NOT also appear as a pending click.
        self.assertNotIn("- [ ] **WHAT:** the publish click at $19", output)

    def test_checked_box_without_done_still_queues(self) -> None:
        output, result = self._run({"checked.md": CHECKED_NO_DONE_PACKET})
        self.assertEqual(len(result.groups), 1)
        self.assertEqual(len(result.groups[0].clicks), 1)
        self.assertEqual(result.live, [])
        self.assertNotIn("Live / completed", output)

    def test_pending_totals_unaffected_by_live_packet(self) -> None:
        _, legacy_only = self._run({"legacy.md": LEGACY_PACKET})
        _, with_live = self._run({"legacy.md": LEGACY_PACKET, "live.md": LIVE_PACKET})
        pending_before = sum(len(g.clicks) for g in legacy_only.groups)
        pending_after = sum(len(g.clicks) for g in with_live.groups)
        self.assertEqual(pending_before, pending_after)
        self.assertEqual(len(legacy_only.groups), len(with_live.groups))


if __name__ == "__main__":
    unittest.main()
