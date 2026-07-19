#!/usr/bin/env python3
"""check_funnel_assets.py — guard per-KIT funnel-asset completeness (ENG-4).

Why this exists
---------------
A shippable kit's owner CLICK PATH is only as good as its funnel assets. When the
owner works the OWNER-QUEUE / OWNER-LAUNCH-HOUR, each kit's `docs/launch/<sku>/`
folder is the surface those clicks turn into a live listing: the landing/sales
copy the owner pastes into the storefront, and the owner-publish click-script that
tells them exactly what to do. If a shippable kit's launch folder is missing one of
those, the owner reaches a dead step — there is copy but no instructions, or
instructions but nothing to list.

ENG-5 (`check_built_registered.py`, #262) proved every packaged candidate
(`candidates/<sku>/dist/`) is launch-REGISTERED — i.e. its `docs/launch/<sku>/`
directory EXISTS (plus a vetting packet + a catalog row). It deliberately does not
look INSIDE that directory. ENG-3 (`check_funnel_coverage.py`, #256) is the
per-CLUSTER counterpart — it asserts each cross-sell cluster has a top-of-funnel
lead magnet. This guard is the per-KIT, one-level-down counterpart to both: for
each SHIPPABLE kit, assert its launch folder carries the FULL required funnel-asset
SET, not merely that the folder exists.

"Shippable" reuses ENG-5's BUILT signal for consistency, so the two guards agree
----------------------------------------------------------------------------------
A candidate counts as SHIPPABLE when it carries a `candidates/<sku>/dist/`
packaged-artifact dir — the exact "reached a sellable, packaged state" marker
ENG-5 uses (`check_built_registered.BUILD_MARKER`), which separates a real product
from a book-lane / WIP-intake / notes candidate. We restrict the funnel-completeness
requirement to those built kits: ENG-5 already guarantees each has a launch folder;
this guard checks that folder's CONTENTS. Non-built launch rows (e.g. the owner-gated
`photo-packs` lane, the compositional `bundle-starter` scaffold) are ENG-5's
concern, not funnel-completeness cases, so they fall outside this guard's scope by
construction — no per-name allowlist is needed for them.

The required funnel-asset set (inferred from the live tree, two naming schemes)
-------------------------------------------------------------------------------
Read off every one of the built kits' `docs/launch/<sku>/` folders, two funnel
ROLES are universal — but under two filename conventions:

  * ROLE "landing/sales copy"  — the marketplace listing copy the owner pastes.
      modern majority : `listing-copy.md`      (20 kits)
      legacy/flagship : `LISTING.md`           (stripe-webhook-test-kit,
                                                agent-fleet-field-manual)
  * ROLE "owner publish action" — the owner's publish click-script.
      modern majority : `owner-actions.md`     (20 kits)
      legacy/flagship : `publish-owner-action.md`

Both schemes carry the SAME two roles, so a role is satisfied by ANY of its
accepted filenames — the guard requires the ROLE, not one exact file, and so does
not falsely red the two flagship launches that predate the modern naming.

`one-pager.md`, `readme-buy-snippet.md`, `gotcha-article.md`, chapter excerpts,
`LAUNCH-LOG.md` appear on only a subset of kits — they are ENRICHMENTS, so they are
OPTIONAL, not part of the required set. Requiring them would falsely red the
majority of already-shippable kits, i.e. would flag reality rather than a
regression.

Exit 0 when every shippable kit's launch folder carries all required funnel roles;
exit non-zero with a per-kit list of the MISSING roles otherwise. Stdlib-only.
Never writes the tree.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Resolve paths relative to the repo root (this file lives in scripts/), so the
# guard works regardless of the current working directory. Tests override the
# root with --root to point at a temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Repo-relative registry locations.
CANDIDATES_DIR_REL = "candidates"        # candidates/<sku>/ build dirs
LAUNCH_DIR_REL = "docs/launch"           # docs/launch/<sku>/ funnel folders

# A candidate counts as SHIPPABLE (built to a packaged artifact) when it carries
# this subdirectory — the SAME marker ENG-5 (check_built_registered.py) uses, so
# the two guards share one definition of "shippable" and can never disagree.
BUILD_MARKER = "dist"

# The required funnel-asset SET, as (role_name, accepted_filenames) pairs. A role
# is SATISFIED when the launch folder contains at least one of its accepted
# filenames — this tolerates the two live naming conventions (modern majority +
# legacy/flagship) without hard-coding a per-kit exception. Enrichment assets
# (one-pager.md, readme-buy-snippet.md, gotcha-article.md, chapter-*.md,
# LAUNCH-LOG.md) are intentionally NOT listed: they exist on only a subset of
# shippable kits, so requiring them would flag reality, not a regression.
REQUIRED_ROLES = (
    ("landing/sales copy", ("listing-copy.md", "LISTING.md")),
    ("owner publish action", ("owner-actions.md", "publish-owner-action.md")),
)


def _subdirs(path: Path):
    """Immediate subdirectory names under `path` (empty list if absent)."""
    if not path.is_dir():
        return []
    return sorted(p.name for p in path.iterdir() if p.is_dir())


def built_skus(root=REPO_ROOT):
    """The set of SHIPPABLE skus — candidates carrying a `dist/` packaged artifact."""
    cand_dir = Path(root) / CANDIDATES_DIR_REL
    return {
        name
        for name in _subdirs(cand_dir)
        if (cand_dir / name / BUILD_MARKER).is_dir()
    }


def _launch_files(root, sku):
    """The set of file names present in docs/launch/<sku>/ (empty if the dir is absent)."""
    d = Path(root) / LAUNCH_DIR_REL / sku
    if not d.is_dir():
        return None
    return {p.name for p in d.iterdir() if p.is_file()}


def missing_roles(present_files):
    """The required roles NOT satisfied by `present_files` (a set of file names)."""
    missing = []
    for role_name, accepted in REQUIRED_ROLES:
        if not any(fname in present_files for fname in accepted):
            missing.append((role_name, accepted))
    return missing


def check(root=REPO_ROOT):
    """Assert every shippable kit's launch folder carries the full funnel-asset set.

    Returns (status, violations):
      * ("ok", [])      — every shippable kit's funnel folder is complete;
      * ("skip", why)   — nothing to check (no built candidates on the tree);
      * ("gap", [..])   — a list of human-readable per-kit missing-asset lines.

    A built kit with NO launch folder at all is left to ENG-5's built-registered
    guard (which owns the built<->registered correspondence) — this guard reports
    the CONTENTS of folders that exist, and does not double-report a missing folder.
    """
    built = built_skus(root)
    if not built:
        return "skip", (
            "no built candidates under {c}/<sku>/{m}/ — no shippable kit to "
            "check funnel completeness for".format(c=CANDIDATES_DIR_REL, m=BUILD_MARKER)
        )

    violations = []
    for sku in sorted(built):
        present = _launch_files(root, sku)
        if present is None:
            # No launch folder — ENG-5's built-registered guard owns this class.
            continue
        gaps = missing_roles(present)
        if gaps:
            parts = [
                "{role} (expected one of: {names})".format(
                    role=role_name, names=", ".join(accepted)
                )
                for role_name, accepted in gaps
            ]
            violations.append(
                "INCOMPLETE-FUNNEL: docs/launch/{s}/ is missing {n} required "
                "funnel asset(s): {parts}".format(
                    s=sku, n=len(gaps), parts="; ".join(parts)
                )
            )

    if violations:
        return "gap", violations
    return "ok", []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=REPO_ROOT,
        help="repo root to check (default: the repo this script lives in)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="suppress the OK/skip banner on success",
    )
    args = parser.parse_args(argv)

    status, detail = check(args.root)

    if status == "gap":
        print("INCOMPLETE FUNNEL: a shippable kit is missing a required funnel asset.")
        print(
            "Every built kit (candidates/<sku>/{m}/) must carry, in its\n"
            "docs/launch/<sku>/ folder, a landing/sales-copy doc AND an "
            "owner-publish-action doc\n(each satisfiable by either naming "
            "convention). Fix by adding the missing funnel asset\nto the kit's "
            "launch folder — do NOT hand-edit this guard's REQUIRED_ROLES to hide "
            "a real gap.\n".format(m=BUILD_MARKER)
        )
        print("--- {n} incomplete kit(s) ---".format(n=len(detail)))
        for line in detail:
            print("  * " + line)
        print("FAIL: a shippable kit's owner click path is missing a funnel asset.")
        return 1

    if status == "skip":
        if not args.quiet:
            print("SKIP: {why}".format(why=detail))
        return 0

    if not args.quiet:
        built = built_skus(args.root)
        print(
            "OK: {n} shippable kit(s) all carry the full required funnel-asset set "
            "(landing/sales copy + owner publish action).".format(n=len(built))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
