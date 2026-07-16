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

Plus the packet-level `KILL-CHECK: ⏲ <ISO date> <label> [· ⏲ …]` line
(kill-clock checkpoints for live products, rendered in the Live section):

5. tokens parse and render earliest-first regardless of source order;
6. a packet WITHOUT the line renders byte-identically to before (no ⏲);
7. a malformed date is SKIPPED with a manual-review note (tolerant-parser
   contract — never a hard error), valid sibling tokens still render;
8. a KILL-CHECK line on a pending-only packet renders nothing (the kill
   clock only ticks once live).

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
TIMER = doq.TIMER

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

# KILL-CHECK tokens deliberately OUT of date order — rendering must sort.
KILLCHECK_PACKET = f"""# Title Vetting — Ticking Gadget

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $29 — DONE 2026-07-12

KILL-CHECK: {TIMER} 2026-07-26 T+14 kill-rule deadline ·
  {TIMER} 2026-07-19 T+7 funnel checkpoint
"""

KILLCHECK_MALFORMED_PACKET = f"""# Title Vetting — Broken Clock

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $9 — DONE 2026-07-12

KILL-CHECK: {TIMER} 07/19/2026 T+7 checkpoint · {TIMER} 2026-07-26 T+14 deadline
"""

KILLCHECK_PENDING_PACKET = f"""# Title Vetting — Not Yet Live

## 7. {FLAG} OWNER-GATE — publish clicks

- [ ] {FLAG} **Owner:** the publish click at $5.

KILL-CHECK: {TIMER} 2026-07-19 premature checkpoint
"""

# A hard-gated NL edition: the ONLY thing setting `blocked` is the word
# "blocking" inside the proofread checkbox — there is NO D-item in this packet.
# The HARD-GATED suffix must name that proofread row, not a phantom D-item.
PROOFREAD_GATED_PACKET = f"""# Title Vetting — De Testtaart

## 7. {FLAG} OWNER-GATE — publish clicks

- [ ] {FLAG} **Owner:** EN edition published first (sequencing dependency).
- [ ] {FLAG} **Owner:** native-speaker proofread pass approved/commissioned
      (blocking quality gate for this title).
- [ ] {FLAG} **Owner:** the publish click + KDP Select enrollment.
"""

# A hard-gated NL edition whose proofread checkbox OMITS the literal
# "blocking" keyword — exactly the owner-queue understatement bug this slice
# fixes. Detection must hard-gate it on the native-speaker proofread-pass
# signal ALONE, and the ordinary ⚑ Owner publish-click / cover / price rows
# must NOT be mis-flagged as gates.
PROOFREAD_NO_KEYWORD_PACKET = f"""# Title Vetting — De Ongemarkeerde

## 7. {FLAG} OWNER-GATE — publish clicks

- [ ] {FLAG} **Owner:** EN edition published first (sequencing dependency).
- [ ] {FLAG} **Owner:** native-speaker proofread pass approved/commissioned.
- [ ] {FLAG} **Owner:** cover type-swap approved / any incremental spend.
- [ ] {FLAG} **Owner:** the publish click + KDP Select enrollment.
"""

# A hard-gated group whose blocking row genuinely IS a D-item: a numbered
# OWNER-ACTION step carries an inline flag (making it a decision), and the
# blocking owner checkbox shares its keyword ("illustration") — so `linked`
# is true and the legacy "a D-item above blocks this sequence" wording stays.
DITEM_GATED_PACKET = f"""# Title Vetting — Test Stones

## 7. {FLAG} OWNER-GATE — publish clicks

**OWNER-ACTION — Publish "Test Stones"**
1. {FLAG} **Illustration decision (default recommend Park):** Commission / AI / Park.

- [ ] {FLAG} **Owner:** KDP account + tax/bank interview.
- [ ] {FLAG} **Owner:** illustration money-decision — Commission / AI / Park.
      Blocking: nothing below proceeds without it.
- [ ] {FLAG} **Owner:** the publish click itself.
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

    def test_killcheck_tokens_parse_and_render_earliest_first(self) -> None:
        output, result = self._run({"ticking.md": KILLCHECK_PACKET})
        self.assertEqual(len(result.live), 1)
        cps = result.live[0].checkpoints
        self.assertEqual(
            cps,
            [
                {"date": "2026-07-19", "label": "T+7 funnel checkpoint"},
                {"date": "2026-07-26", "label": "T+14 kill-rule deadline"},
            ],
        )
        self.assertEqual(result.manual, [])
        first = f"- {TIMER} **Next checkpoint:** 2026-07-19 — T+7 funnel checkpoint"
        second = f"- {TIMER} then: 2026-07-26 — T+14 kill-rule deadline"
        self.assertIn(first, output)
        self.assertIn(second, output)
        # Earliest-first: 07-19 renders BEFORE 07-26 despite source order.
        self.assertLess(output.index(first), output.index(second))

    def test_absent_token_renders_unchanged(self) -> None:
        output, result = self._run({"live.md": LIVE_PACKET})
        self.assertEqual(result.live[0].checkpoints, [])
        self.assertNotIn(TIMER, output)
        self.assertNotIn("Next checkpoint", output)

    def test_malformed_date_skipped_with_manual_note(self) -> None:
        # Tolerant-parser contract: a bad date is a manual-review note,
        # never a hard error — and the valid sibling token still renders.
        output, result = self._run({"broken.md": KILLCHECK_MALFORMED_PACKET})
        self.assertEqual(len(result.manual), 1)
        self.assertIn("KILL-CHECK", result.manual[0][1])
        self.assertIn("07/19/2026", result.manual[0][1])
        self.assertEqual(
            result.live[0].checkpoints,
            [{"date": "2026-07-26", "label": "T+14 deadline"}],
        )
        self.assertIn(
            f"- {TIMER} **Next checkpoint:** 2026-07-26 — T+14 deadline", output
        )

    def test_killcheck_on_pending_packet_renders_nothing(self) -> None:
        output, result = self._run({"pending.md": KILLCHECK_PENDING_PACKET})
        self.assertEqual(result.live, [])
        self.assertNotIn("Live / completed", output)
        self.assertNotIn("Next checkpoint", output)
        # The pending click still queues exactly as before.
        self.assertEqual(len(result.groups), 1)
        self.assertEqual(len(result.groups[0].clicks), 1)

    def test_proofread_gated_sequence_names_real_blocking_row(self) -> None:
        # The blocker is a per-title proofread quality gate, NOT a D-item.
        # The HARD-GATED suffix must name that row and must NOT claim a D-item.
        output, result = self._run({"de-testtaart.md": PROOFREAD_GATED_PACKET})
        self.assertEqual(len(result.groups), 1)
        group = result.groups[0]
        self.assertTrue(group.blocked)
        self.assertFalse(group.blocking_is_ditem)
        self.assertIn("native-speaker proofread pass", group.blocking_row)
        self.assertIn(
            "**HARD-GATED** — blocking row: native-speaker proofread pass", output
        )
        # The phantom-D-item wording must be gone for this sequence.
        self.assertNotIn("(a D-item above blocks this sequence)", output)

    def test_proofread_gate_without_blocking_keyword_is_hard_gated(self) -> None:
        # The understatement bug: a proofread checkbox that OMITS the literal
        # "blocking" word must still hard-gate the sequence — an NL edition
        # must never be shown click-ready while it still needs the blocking
        # native-speaker proofread pass.
        output, result = self._run(
            {"de-ongemarkeerde.md": PROOFREAD_NO_KEYWORD_PACKET}
        )
        self.assertEqual(len(result.groups), 1)
        group = result.groups[0]
        self.assertTrue(group.blocked)  # hard-gated despite no "blocking" word
        self.assertFalse(group.blocking_is_ditem)
        self.assertIn("native-speaker proofread pass", group.blocking_row)
        self.assertIn(
            "**HARD-GATED** — blocking row: native-speaker proofread pass", output
        )
        # Regression: ordinary ⚑ Owner rows are NOT treated as blocking gates,
        # so detection stays scoped to the proofread/quality-gate row.
        self.assertFalse(
            doq.is_blocking_box("the publish click + KDP Select enrollment.")
        )
        self.assertFalse(
            doq.is_blocking_box("cover type-swap approved / any incremental spend.")
        )
        self.assertFalse(doq.is_blocking_box("EN edition published first."))
        self.assertFalse(
            doq.is_blocking_box("NL title ratified (De Nachtoven, series-aware pick).")
        )
        # ...and the proofread row itself IS a blocking gate on the phrase alone.
        self.assertTrue(
            doq.is_blocking_box(
                "native-speaker proofread pass approved/commissioned."
            )
        )

    def test_ditem_gated_sequence_keeps_ditem_wording(self) -> None:
        # When the blocking row genuinely links to a same-packet D-item, the
        # original "a D-item above blocks this sequence" wording is retained.
        output, result = self._run({"test-stones.md": DITEM_GATED_PACKET})
        self.assertEqual(len(result.groups), 1)
        group = result.groups[0]
        self.assertTrue(group.blocked)
        self.assertTrue(group.blocking_is_ditem)
        self.assertIn(
            "**HARD-GATED** (a D-item above blocks this sequence)", output
        )
        self.assertNotIn("blocking row:", output)

    def test_pending_totals_unaffected_by_live_packet(self) -> None:
        _, legacy_only = self._run({"legacy.md": LEGACY_PACKET})
        _, with_live = self._run({"legacy.md": LEGACY_PACKET, "live.md": LIVE_PACKET})
        pending_before = sum(len(g.clicks) for g in legacy_only.groups)
        pending_after = sum(len(g.clicks) for g in with_live.groups)
        self.assertEqual(pending_before, pending_after)
        self.assertEqual(len(legacy_only.groups), len(with_live.groups))


if __name__ == "__main__":
    unittest.main()
