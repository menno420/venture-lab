#!/usr/bin/env python3
"""Tests for scripts/check_docs_links.py — the internal doc link/anchor guard (ENG-8).

Run from the scripts/ directory:
    python3 -m unittest test_check_docs_links -v

Covers:
  * the guard PASSES on the current clean repo tree, and it actually EXERCISED each
    dimension (not a vacuous skip): the live run checks a non-zero number of relative
    links (INV-1) and a non-zero number of anchors (INV-2);
  * INV-1 CATCHES a relative link to a missing file in the un-gated root/control set,
    and PASSES a link whose target exists;
  * INV-1 does NOT re-check link existence under docs/ (owned by the bootstrap gate) —
    a broken plain link inside docs/ is NOT flagged by this guard;
  * INV-2 CATCHES a same-file `#anchor` with no matching heading, and a `path.md#anchor`
    whose heading is absent in the target file; PASSES a resolvable anchor;
  * INV-2 applies to docs/ too (the dimension the bootstrap gate strips): a dead anchor
    inside a docs/ file IS flagged;
  * the slug convention disambiguates duplicate headings (`notes`, `notes-1`) and
    SKIPS fenced-code `#` lines (an anchor to a fenced `# not-a-heading` is dead);
  * excluded trees (.sessions/, candidates/, .substrate/) are NOT checked — a broken
    link there never reds;
  * external http(s)/mailto links are skipped (never a false red for an offline guard);
  * the guard SKIPS (exit 0) on a tree with no in-scope markdown, and main() exits
    non-zero end-to-end on a broken tree.

The catch-cases build tiny synthetic fixture trees under a temp --root and perturb
them, rather than copying the live tree — so the tests never depend on the repo's exact
doc set.
"""

import os
import shutil
import tempfile
import unittest

import check_docs_links as guard


# --- fixture builders -------------------------------------------------------------

def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


class _TmpRoot(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="docslinks-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def w(self, rel, text):
        _write(os.path.join(self.root, rel), text)


# --- live-tree green --------------------------------------------------------------

class CleanTreeTest(unittest.TestCase):
    """The guard must be green on the real repo tree, having exercised each invariant."""

    def test_live_tree_resolves(self):
        status, detail, _stats = guard.check(guard.REPO_ROOT)
        self.assertEqual(
            status,
            "ok",
            "live tree should be link/anchor-clean; got {s}:\n{d}".format(
                s=status, d="\n".join(detail) if isinstance(detail, list) else detail
            ),
        )

    def test_main_exit_zero_on_clean_tree(self):
        self.assertEqual(guard.main(["--quiet"]), 0)

    def test_live_run_is_non_vacuous(self):
        # Guard against a silent narrowing: the live tree must actually exercise BOTH
        # the link dimension (root/control relative links) and the anchor dimension.
        _status, _detail, stats = guard.check(guard.REPO_ROOT)
        self.assertGreater(stats["files"], 0)
        self.assertGreater(stats["links_checked"], 0, "expected root/control relative links")
        self.assertGreater(stats["anchors_checked"], 0, "expected anchored links to verify")


# --- INV-1: dead link in the un-gated set -----------------------------------------

class Inv1DeadLinkTest(_TmpRoot):
    def test_resolvable_root_link_passes(self):
        self.w("TARGET.md", "# Target\n")
        self.w("README.md", "See [target](TARGET.md).\n")
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "ok", findings)

    def test_catches_dead_link_in_root(self):
        self.w("README.md", "See [gone](NOPE.md).\n")
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "broken")
        self.assertTrue(any("DEAD-LINK" in f and "NOPE.md" in f for f in findings), findings)

    def test_catches_dead_link_in_control(self):
        self.w("control/claims/x.md", "Branch note -> [spec](../missing-spec.md).\n")
        status, findings, _s = guard.check(self.root)
        self.assertTrue(any("DEAD-LINK" in f for f in findings), findings)

    def test_docs_plain_link_existence_not_rechecked(self):
        # docs/ link existence is owned by the bootstrap gate — INV-1 must NOT flag a
        # broken plain link under docs/ (no duplication).
        self.w("docs/guide.md", "# Guide\n\nSee [x](does-not-exist.md).\n")
        status, findings, stats = guard.check(self.root)
        self.assertEqual(status, "ok", findings)
        self.assertEqual(stats["links_checked"], 0, "docs/ links must not be link-checked here")

    def test_external_links_skipped(self):
        self.w("README.md", "[site](https://example.com/nope) and [m](mailto:x@y.z).\n")
        status, findings, stats = guard.check(self.root)
        self.assertEqual(status, "ok", findings)
        self.assertEqual(stats["links_checked"], 0)


# --- INV-2: anchor-fragment resolution --------------------------------------------

class Inv2AnchorTest(_TmpRoot):
    def test_resolvable_same_file_anchor_passes(self):
        self.w("README.md", "# Top\n\n## The Section\n\nJump to [it](#the-section).\n")
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "ok", findings)

    def test_catches_dead_same_file_anchor(self):
        self.w("README.md", "# Top\n\nJump to [gone](#no-such-heading).\n")
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "broken")
        self.assertTrue(any("DEAD-ANCHOR" in f for f in findings), findings)

    def test_catches_dead_cross_file_anchor(self):
        self.w("OTHER.md", "# Other\n\n## Present\n")
        self.w("README.md", "See [there](OTHER.md#absent).\n")
        status, findings, _s = guard.check(self.root)
        self.assertTrue(any("DEAD-ANCHOR" in f and "absent" in f for f in findings), findings)

    def test_resolvable_cross_file_anchor_passes(self):
        self.w("OTHER.md", "# Other\n\n## Present Section\n")
        self.w("README.md", "See [there](OTHER.md#present-section).\n")
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "ok", findings)

    def test_anchor_checked_inside_docs(self):
        # docs/ IS in scope for anchors (the dimension the bootstrap gate strips).
        self.w("docs/guide.md", "# Guide\n\nBroken [ref](#nope-heading).\n")
        status, findings, stats = guard.check(self.root)
        self.assertEqual(status, "broken")
        self.assertTrue(any("DEAD-ANCHOR" in f for f in findings), findings)
        self.assertGreater(stats["anchors_checked"], 0)

    def test_duplicate_heading_disambiguation(self):
        self.w(
            "README.md",
            "# Top\n\n## Notes\n\n## Notes\n\n[first](#notes) [second](#notes-1).\n",
        )
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "ok", findings)

    def test_fenced_code_hash_is_not_a_heading(self):
        # A `#` line inside a code fence must NOT count as a heading, so an anchor to it
        # is dead — while a real heading of the same text still resolves.
        self.w(
            "README.md",
            "# Top\n\n```sh\n# fake-heading\n```\n\n[dead](#fake-heading).\n",
        )
        status, findings, _s = guard.check(self.root)
        self.assertEqual(status, "broken")
        self.assertTrue(any("fake-heading" in f for f in findings), findings)


# --- exclusions -------------------------------------------------------------------

class ExclusionTest(_TmpRoot):
    def test_sessions_tree_excluded(self):
        self.w(".sessions/2026-card.md", "Old ref [x](gone.md) and [y](#dead).\n")
        # Keep the tree non-empty with an in-scope, clean file.
        self.w("README.md", "# Ok\n")
        status, findings, stats = guard.check(self.root)
        self.assertEqual(status, "ok", findings)
        self.assertEqual(stats["files"], 1, "only README.md is in scope")

    def test_candidates_and_substrate_excluded(self):
        self.w("candidates/pack/templates/t.md", "Template [x](claims/README.md).\n")
        self.w(".substrate/notes.md", "[x](gone.md)\n")
        self.w("README.md", "# Ok\n")
        status, findings, stats = guard.check(self.root)
        self.assertEqual(status, "ok", findings)
        self.assertEqual(stats["files"], 1)


# --- skip / edge ------------------------------------------------------------------

class SkipTest(unittest.TestCase):
    def test_empty_tree_skips_green(self):
        root = tempfile.mkdtemp(prefix="docslinks-empty-")
        try:
            status, _detail, _s = guard.check(root)
            self.assertEqual(status, "skip")
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_full_check_catches_and_exits_nonzero(self):
        root = tempfile.mkdtemp(prefix="docslinks-e2e-")
        try:
            _write(os.path.join(root, "README.md"), "Bad [link](NOPE.md).\n")
            status, findings, _s = guard.check(root)
            self.assertEqual(status, "broken")
            self.assertTrue(any("NOPE.md" in f for f in findings), findings)
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 1)
        finally:
            shutil.rmtree(root, ignore_errors=True)


# --- slug unit ---------------------------------------------------------------------

class SlugifyTest(unittest.TestCase):
    def test_github_style_slug(self):
        self.assertEqual(guard.slugify("The Section"), "the-section")
        self.assertEqual(guard.slugify("2. Copy-paste skeleton"), "2-copy-paste-skeleton")
        self.assertEqual(
            guard.slugify("`docs/launch/<cluster>-lead-magnet.md`"),
            "docslaunchcluster-lead-magnetmd",
        )


if __name__ == "__main__":
    unittest.main()
