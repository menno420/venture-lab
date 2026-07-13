#!/usr/bin/env python3
"""scripts/test_lint_owner_gates.py — strict owner-gate lint tests, stdlib only.

Covers `lint_owner_gates.py` (the OCQK `lint` mode ported back into
production, PR #153's session-card 💡 follow-up):

 1. a clean pending packet lints OK (exit 0);
 2. a clean LIVE packet (DONE rows + KILL-CHECK) lints OK;
 3. the headline check — a DONE date that is date-SHAPED but IMPOSSIBLE
    (2026-13-45: month 13, day 45) is an error, even though the derive
    regex accepts it;
 4. half-flipped DONE dispositions are errors both ways (checked box
    without the marker, unchecked box carrying it);
 5. a ⚑ decision step without a parseable bolded default is an error;
 6. a missing `# Title Vetting —` H1 and a missing §7 section are errors;
 7. a §7 with no steps and no ⚑ Owner rows is an error;
 8. KILL-CHECK problems are errors — a line with no ⏲ token, and a ⏲
    token with an impossible calendar date (2026-02-30);
 9. zero packets is a FAIL (a lint that can't find its data never says OK);
10. keyword map — a ⚑ OWNER-flagged conflict without a parseable proposed
    resolution is an error; a resolved map lints clean; a MISSING map is a
    skip, not an error;
11. lint/derive lockstep — a packet the strict lint passes also parses
    with ZERO manual-review rows in `derive_owner_queue.py` (both import
    the same grammar, so clean means clean in both).

Run: python3 -m unittest discover -s scripts -p "test_*.py" -v
     (or, from scripts/: python3 -m unittest test_lint_owner_gates -v)
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import derive_owner_queue as doq  # noqa: E402
import lint_owner_gates as log_  # noqa: E402

FLAG = doq.FLAG
TIMER = doq.TIMER

CLEAN_PENDING = f"""# Title Vetting — Clean Widget

## 7. {FLAG} OWNER-GATE — publish clicks (queued, never automated)

**OWNER-ACTION — Publish "Clean Widget" at $9**
1. {FLAG} **Storefront (owner decision):** **Gumroad** (default — zero
   monthly fee) or override.
2. **Publish + record:** publish and copy the URL.

- [ ] {FLAG} **Owner:** zip uploaded + sha256 spot-check.
- [ ] {FLAG} **Owner:** the publish click + public URL copied.
"""

CLEAN_LIVE = f"""# Title Vetting — Live Gadget

## 7. {FLAG} OWNER-GATE — publish clicks (ALL EXECUTED — product live)

- [x] {FLAG} **Owner:** the publish click at $29 — DONE 2026-07-12
- [x] {FLAG} **Owner:** test purchase verified end-to-end — DONE 2026-07-12

KILL-CHECK: {TIMER} 2026-07-19 T+7 funnel checkpoint · {TIMER} 2026-08-11
  T+30 kill-rule deadline
"""

IMPOSSIBLE_DONE_DATE = f"""# Title Vetting — Bad Calendar

## 7. {FLAG} OWNER-GATE — publish clicks

- [x] {FLAG} **Owner:** the publish click — DONE 2026-13-45
"""

CHECKED_NO_DONE = f"""# Title Vetting — Half Flip A

## 7. {FLAG} OWNER-GATE — publish clicks

- [x] {FLAG} **Owner:** the publish click (checked by hand, no DONE marker).
"""

UNCHECKED_WITH_DONE = f"""# Title Vetting — Half Flip B

## 7. {FLAG} OWNER-GATE — publish clicks

- [ ] {FLAG} **Owner:** the publish click — DONE 2026-07-12
"""

DEFAULTLESS_DECISION = f"""# Title Vetting — No Default

## 7. {FLAG} OWNER-GATE — publish clicks

1. {FLAG} **Storefront (owner decision):** pick one of the venues.

- [ ] {FLAG} **Owner:** the publish click.
"""

NO_TITLE = f"""# Some Other Heading

## 7. {FLAG} OWNER-GATE — publish clicks

- [ ] {FLAG} **Owner:** the publish click.
"""

NO_SECTION7 = """# Title Vetting — Gateless

## 6. Keywords

Nothing gated here.
"""

EMPTY_SECTION7 = f"""# Title Vetting — Hollow Gate

## 7. {FLAG} OWNER-GATE — publish clicks

(prose only — no steps, no checkboxes)
"""

KILLCHECK_NO_TOKEN = f"""# Title Vetting — Tokenless Clock

## 7. {FLAG} OWNER-GATE — publish clicks

- [x] {FLAG} **Owner:** the publish click — DONE 2026-07-12

KILL-CHECK: arm the clock at T+7 and T+30.
"""

KILLCHECK_BAD_DATE = f"""# Title Vetting — Broken Clock

## 7. {FLAG} OWNER-GATE — publish clicks

- [x] {FLAG} **Owner:** the publish click — DONE 2026-07-12

KILL-CHECK: {TIMER} 2026-02-30 impossible date · {TIMER} 2026-07-20 real one
"""

KEYWORD_MAP_FLAGGED_NO_RESOLUTION = f"""# Keyword map

## 2. Conflicts

### C1 — Two packets claim the same category

{FLAG} OWNER — someone must pick, but nobody proposed anything (no bold
resolution span anywhere in this section).
"""

KEYWORD_MAP_CLEAN = f"""# Keyword map

## 2. Conflicts

### C1 — Two packets claim the same category

{FLAG} OWNER — **Proposed resolution:** hand the category to the proposed
**first-mover packet** and re-slot the newcomer.
"""


class LintOwnerGateTests(unittest.TestCase):
    def _run(self, packets: dict[str, str], keyword_map: str | None = None):
        """Run lint over a temp vetting dir; returns (exit_code, stdout)."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            vetting = root / "vetting"
            vetting.mkdir()
            for fname, content in packets.items():
                (vetting / fname).write_text(content, encoding="utf-8")
            kmap = root / "keyword-map.md"
            if keyword_map is not None:
                kmap.write_text(keyword_map, encoding="utf-8")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = log_.run(str(vetting), str(kmap))
            return code, buffer.getvalue()

    # -- clean inputs ----------------------------------------------------

    def test_clean_pending_packet_ok(self):
        code, out = self._run({"clean.md": CLEAN_PENDING})
        self.assertEqual(code, 0)
        self.assertIn("owner-gate-lint: OK — 1 input(s) clean", out)

    def test_clean_live_packet_ok(self):
        code, out = self._run({"live.md": CLEAN_LIVE})
        self.assertEqual(code, 0)
        self.assertIn("OK", out)

    # -- the headline check: impossible calendar dates --------------------

    def test_impossible_done_date_fails(self):
        # The derive regex (\d{4}-\d{2}-\d{2}) ACCEPTS 2026-13-45; the
        # lint must not.
        code, out = self._run({"bad.md": IMPOSSIBLE_DONE_DATE})
        self.assertEqual(code, 1)
        self.assertIn("`2026-13-45` is not a real calendar date", out)
        self.assertIn("FAIL", out)

    def test_killcheck_impossible_date_fails_valid_sibling_ignored(self):
        code, out = self._run({"clock.md": KILLCHECK_BAD_DATE})
        self.assertEqual(code, 1)
        self.assertIn("2026-02-30", out)
        self.assertIn("no leading valid ISO date", out)
        # exactly one error: the valid sibling token is NOT flagged
        self.assertIn("FAIL — 1 problem(s)", out)

    # -- half-flipped DONE dispositions -----------------------------------

    def test_checked_without_done_fails(self):
        code, out = self._run({"halfa.md": CHECKED_NO_DONE})
        self.assertEqual(code, 1)
        self.assertIn("checked", out)
        self.assertIn("flip both marks or neither", out)

    def test_unchecked_with_done_fails(self):
        code, out = self._run({"halfb.md": UNCHECKED_WITH_DONE})
        self.assertEqual(code, 1)
        self.assertIn("UNCHECKED", out)
        self.assertIn("flip both marks or neither", out)

    # -- structure checks --------------------------------------------------

    def test_defaultless_decision_fails(self):
        code, out = self._run({"nodefault.md": DEFAULTLESS_DECISION})
        self.assertEqual(code, 1)
        self.assertIn("no parseable default", out)

    def test_missing_title_h1_fails(self):
        code, out = self._run({"notitle.md": NO_TITLE})
        self.assertEqual(code, 1)
        self.assertIn("no `# Title Vetting — <name>` H1", out)

    def test_missing_section7_fails(self):
        code, out = self._run({"gateless.md": NO_SECTION7})
        self.assertEqual(code, 1)
        self.assertIn("no `## 7. … OWNER-GATE` section found", out)

    def test_empty_section7_fails(self):
        code, out = self._run({"hollow.md": EMPTY_SECTION7})
        self.assertEqual(code, 1)
        self.assertIn("no OWNER-ACTION steps and no ⚑ Owner", out)

    def test_killcheck_without_token_fails(self):
        code, out = self._run({"tokenless.md": KILLCHECK_NO_TOKEN})
        self.assertEqual(code, 1)
        self.assertIn(f"KILL-CHECK line carries no {TIMER} <ISO date> token", out)

    def test_zero_packets_fails(self):
        code, out = self._run({})
        self.assertEqual(code, 1)
        self.assertIn("FAIL — no packets found", out)

    # -- keyword map --------------------------------------------------------

    def test_flagged_conflict_without_resolution_fails(self):
        code, out = self._run(
            {"clean.md": CLEAN_PENDING},
            keyword_map=KEYWORD_MAP_FLAGGED_NO_RESOLUTION,
        )
        self.assertEqual(code, 1)
        self.assertIn("C1 is ⚑ OWNER-flagged but no proposed resolution parsed", out)

    def test_clean_keyword_map_ok(self):
        code, out = self._run({"clean.md": CLEAN_PENDING}, keyword_map=KEYWORD_MAP_CLEAN)
        self.assertEqual(code, 0)
        self.assertIn("OK — 2 input(s) clean", out)

    def test_missing_keyword_map_is_skip_not_error(self):
        code, out = self._run({"clean.md": CLEAN_PENDING})
        self.assertEqual(code, 0)
        self.assertIn("conflict scan skipped", out)
        self.assertIn("OK", out)

    # -- lint/derive lockstep ------------------------------------------------

    def test_lint_clean_means_derive_clean(self):
        # Both tools import the same grammar module; a packet that lints
        # OK must also derive with ZERO manual-review rows.
        code, _ = self._run({"clean.md": CLEAN_PENDING, "live.md": CLEAN_LIVE})
        self.assertEqual(code, 0)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "clean.md").write_text(CLEAN_PENDING, encoding="utf-8")
            (root / "live.md").write_text(CLEAN_LIVE, encoding="utf-8")
            result = doq.ParseResult()
            for packet in sorted(root.glob("*.md")):
                doq.parse_packet(packet, result)
            self.assertEqual(result.manual, [])
            self.assertEqual(len(result.parsed_files), 2)


if __name__ == "__main__":
    unittest.main()
