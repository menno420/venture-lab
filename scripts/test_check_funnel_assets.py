#!/usr/bin/env python3
"""Tests for scripts/check_funnel_assets.py — the per-kit funnel-asset guard (ENG-4).

Run from the scripts/ directory:
    python3 -m unittest test_check_funnel_assets -v

Covers:
  * the guard PASSES on the current clean repo tree — every shippable kit's
    docs/launch/<sku>/ folder carries the full required funnel-asset set — and it
    actually saw some built SKUs (not a vacuous skip);
  * the guard CATCHES a shippable kit missing its landing/sales-copy doc;
  * the guard CATCHES a shippable kit missing its owner-publish-action doc;
  * the guard CATCHES a kit missing BOTH required roles (reports both);
  * BOTH naming conventions satisfy the roles (modern `listing-copy.md` +
    `owner-actions.md`; legacy/flagship `LISTING.md` + `publish-owner-action.md`);
  * enrichment-only assets (one-pager.md etc.) do NOT satisfy a required role and
    are not themselves required;
  * a built kit with NO launch folder is NOT double-reported here (ENG-5 owns it);
  * a non-built launch row (folder present, no dist/) is OUT of scope — its funnel
    is not required to be complete by this guard;
  * the guard SKIPS (exit 0, never a false red) on a tree with no built candidates.

The catch-cases build a tiny self-consistent synthetic fixture (a built kit with a
complete funnel folder) and perturb it, rather than copying the live tree — so the
tests never depend on the repo's exact SKU list.
"""

import os
import shutil
import tempfile
import unittest

import check_funnel_assets as guard


def _write(path, text="x\n"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _make_built(root, sku):
    """Mark `sku` as SHIPPABLE — candidates/<sku>/dist/ present."""
    os.makedirs(
        os.path.join(root, guard.CANDIDATES_DIR_REL, sku, guard.BUILD_MARKER),
        exist_ok=True,
    )


def _make_launch(root, sku, files):
    """Create docs/launch/<sku>/ containing the named files."""
    for fname in files:
        _write(os.path.join(root, guard.LAUNCH_DIR_REL, sku, fname))


def _seed_complete_kit(root, sku="foo-kit", files=("listing-copy.md", "owner-actions.md")):
    """A self-consistent fixture: a built kit with a complete funnel folder."""
    _make_built(root, sku)
    _make_launch(root, sku, files)


class CleanTreeTest(unittest.TestCase):
    """The guard must be green on the real repo tree."""

    def test_live_tree_is_complete(self):
        status, detail = guard.check(guard.REPO_ROOT)
        self.assertEqual(
            status,
            "ok",
            "live tree should have complete per-kit funnels; got {s}:\n{d}".format(
                s=status, d="\n".join(detail) if isinstance(detail, list) else detail
            ),
        )

    def test_live_tree_actually_saw_built_skus(self):
        # Guard against a vacuous pass: there must be real built SKUs on the tree.
        self.assertGreater(
            len(guard.built_skus(guard.REPO_ROOT)),
            0,
            "expected packaged candidates on the live tree",
        )

    def test_main_exit_zero_on_clean_tree(self):
        self.assertEqual(guard.main(["--quiet"]), 0)


class GapCatchTest(unittest.TestCase):
    """The guard must CATCH a shippable kit with an incomplete funnel folder."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="funnel-")
        _seed_complete_kit(self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_clean_fixture_passes(self):
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 0)

    def test_catches_missing_landing_copy(self):
        # Built kit whose launch folder has owner-actions but no landing/sales copy.
        _make_built(self.root, "no-copy-kit")
        _make_launch(self.root, "no-copy-kit", ("owner-actions.md",))
        status, detail = guard.check(self.root)
        self.assertEqual(status, "gap", detail)
        self.assertTrue(
            any(
                "no-copy-kit" in v and "landing/sales copy" in v for v in detail
            ),
            detail,
        )
        self.assertEqual(guard.main(["--root", self.root, "--quiet"]), 1)

    def test_catches_missing_owner_actions(self):
        # Built kit whose launch folder has landing copy but no owner-actions doc.
        _make_built(self.root, "no-actions-kit")
        _make_launch(self.root, "no-actions-kit", ("listing-copy.md",))
        status, detail = guard.check(self.root)
        self.assertEqual(status, "gap", detail)
        self.assertTrue(
            any(
                "no-actions-kit" in v and "owner publish action" in v
                for v in detail
            ),
            detail,
        )

    def test_catches_missing_both_roles(self):
        # Built kit whose launch folder has only an enrichment asset — both roles gone.
        _make_built(self.root, "bare-kit")
        _make_launch(self.root, "bare-kit", ("one-pager.md",))
        status, detail = guard.check(self.root)
        self.assertEqual(status, "gap", detail)
        line = next(v for v in detail if "bare-kit" in v)
        self.assertIn("landing/sales copy", line)
        self.assertIn("owner publish action", line)
        self.assertIn("missing 2 required", line)


class NamingConventionTest(unittest.TestCase):
    """Both live naming conventions must satisfy the required roles."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="funnel-naming-")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_modern_convention_satisfies(self):
        _seed_complete_kit(
            self.root, "modern-kit", ("listing-copy.md", "owner-actions.md")
        )
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)

    def test_legacy_flagship_convention_satisfies(self):
        # The stripe/agent-fleet scheme: LISTING.md + publish-owner-action.md.
        _seed_complete_kit(
            self.root, "legacy-kit", ("LISTING.md", "publish-owner-action.md")
        )
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)

    def test_mixed_conventions_satisfy(self):
        # A role is satisfied independently — mixing the two schemes is fine.
        _seed_complete_kit(
            self.root, "mixed-kit", ("LISTING.md", "owner-actions.md")
        )
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)


class ScopeTest(unittest.TestCase):
    """Only SHIPPABLE (built) kits are in scope; missing folders belong to ENG-5."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="funnel-scope-")
        _seed_complete_kit(self.root)  # one clean built kit so we don't skip

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def test_non_built_launch_row_is_out_of_scope(self):
        # A launch folder with only landing copy (no owner-actions) but NOT built:
        # this guard does not require its funnel to be complete (mirrors photo-packs).
        _make_launch(self.root, "owner-gated-lane", ("listing-copy.md",))
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)

    def test_built_kit_with_no_launch_folder_not_double_reported(self):
        # ENG-5's built-registered guard owns "built but no launch folder";
        # this guard reports CONTENTS of folders that exist and stays silent here.
        _make_built(self.root, "no-launch-kit")  # built, but no docs/launch/ dir
        status, detail = guard.check(self.root)
        self.assertEqual(status, "ok", detail)


class NoBuiltSkipTest(unittest.TestCase):
    """A tree with no built candidates must SKIP (exit 0), never false-red."""

    def test_empty_tree_skips_green(self):
        root = tempfile.mkdtemp(prefix="funnel-empty-")
        try:
            status, _detail = guard.check(root)
            self.assertEqual(status, "skip")
            self.assertEqual(guard.main(["--root", root, "--quiet"]), 0)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_launch_dirs_but_no_build_skips(self):
        # Launch folders exist but nothing is packaged -> nothing shippable to check.
        root = tempfile.mkdtemp(prefix="funnel-nobuild-")
        try:
            _make_launch(root, "unbuilt-kit", ("listing-copy.md", "owner-actions.md"))
            status, _detail = guard.check(root)
            self.assertEqual(status, "skip")
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
