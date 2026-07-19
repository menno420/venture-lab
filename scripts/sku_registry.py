#!/usr/bin/env python3
"""sku_registry.py — the ONE authoritative source of storefront-SKU inference.

Why this exists
---------------
A candidate SKU's facts — is it BUILT (packaged to a shippable artifact), where is
it REGISTERED (launch dir / vetting packet / catalog row), and does its launch
folder carry the required FUNNEL roles — were each re-derived independently by
`check_built_registered.py` (ENG-5) and `check_funnel_assets.py` (ENG-4). Both
guards hand-maintained their OWN copy of the same constants (`candidates/`,
`docs/launch/`, the `dist/` BUILD_MARKER) and re-implemented the same directory
inference. That is a real duplication, not incidental: a change to the repo's SKU
shape (a new build marker, a moved launch root) meant editing the same fact in two
places in lockstep, and any divergence would silently make the two guards
disagree about what "built" or "registered" means.

The ENG-4, ENG-5, and ENG-8 session cards each independently proposed collapsing
this into one shared SKU registry. This module is that authoritative source: a
single place that ENUMERATES the SKU universe and exposes each SKU's
built / registered / funnel facts (plus the documented allowlists) via small pure
functions. The guards import from here instead of re-deriving, so the definition
of a storefront SKU lives in exactly one file.

It is deliberately a behavior-PRESERVING consolidation: every function reproduces
the exact inference the guards previously did inline, so their verdicts are
unchanged. The natural NEXT step (see the session 💡) is to back these functions
with a DECLARED registry file (`docs/publishing/SKU-REGISTRY.md`) so the `dist/`
heuristic and the two allowlists become reviewable rows — but that is a
behavior-CHANGING follow-up, out of scope here.

Stdlib-only, deterministic (sorted traversal, no timestamps), offline. Never
writes the tree. Every enumeration/fact function takes an optional `root` so a
test can point it at a temp fixture tree instead of the live repo.
"""

from __future__ import annotations

import re
from pathlib import Path

# Resolve paths relative to the repo root (this file lives in scripts/), so the
# module works regardless of the current working directory. Callers/tests override
# the root with the `root` argument to point at a temp fixture tree.
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Repo-relative registry locations — the ONE place these paths are declared.
CANDIDATES_DIR_REL = "candidates"                 # candidates/<sku>/ build dirs
LAUNCH_DIR_REL = "docs/launch"                    # docs/launch/<sku>/ launch registry
VETTING_DIR_REL = "docs/publishing/vetting"       # docs/publishing/vetting/<sku>.md packets
CATALOG_REL = "docs/launch/CATALOG.md"            # storefront positioning view

# A candidate counts as BUILT (packaged to a shippable artifact) when it carries
# this subdirectory. It is the marker that separates a real, packaged product from
# an idea/WIP/book-lane candidate dir (books, intake-only stubs → no dist/).
BUILD_MARKER = "dist"

# Compositional bundle scaffolds with NO standalone candidates/<sku>/ build dir.
# Exempt from the "registered launch row must have a built artifact" requirement
# ONLY (they still must have a vetting packet + catalog row). The shippable bundles
# that DO have a build dir are not listed here and are checked normally.
BUNDLE_TEMPLATES = frozenset({"bundle-starter"})

# Owner-gated lanes deliberately kept OUT of the storefront catalog and not
# packaged, per docs/launch/CATALOG.md's explicit "Out of scope here ... the Photo
# Packs and the KDP book catalog" note. Exempt from the catalog-row + built-artifact
# requirements (they legitimately carry a launch dir + vetting packet only).
OWNER_GATED_LANES = frozenset({"photo-packs"})

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


def subdirs(path: Path):
    """Immediate subdirectory names under `path` (empty list if absent)."""
    if not path.is_dir():
        return []
    return sorted(p.name for p in path.iterdir() if p.is_dir())


# ---- SKU enumeration -------------------------------------------------------------


def iter_skus(root=REPO_ROOT):
    """Every candidate directory name under candidates/ (built or not), sorted.

    This is the SKU universe: the set of `candidates/<sku>/` directories, whatever
    their build/registration state. Returns a sorted list (empty when the
    candidates/ dir is absent).
    """
    return subdirs(Path(root) / CANDIDATES_DIR_REL)


# ---- BUILT signal ----------------------------------------------------------------


def is_built(sku, root=REPO_ROOT):
    """True when `candidates/<sku>/dist/` exists — the shippable-artifact marker.

    The single definition of "built" both ENG-4 and ENG-5 share: a candidate is
    packaged/shippable exactly when it carries a `dist/` (BUILD_MARKER) subdir.
    """
    return (Path(root) / CANDIDATES_DIR_REL / sku / BUILD_MARKER).is_dir()


def built_skus(root=REPO_ROOT):
    """The set of BUILT (shippable) skus — candidates carrying a `dist/` artifact."""
    return {name for name in iter_skus(root) if is_built(name, root)}


# ---- Registered surfaces ---------------------------------------------------------


def launch_skus(root=REPO_ROOT):
    """The set of skus with a `docs/launch/<sku>/` launch registry directory."""
    return set(subdirs(Path(root) / LAUNCH_DIR_REL))


def vetting_skus(root=REPO_ROOT):
    """The set of skus with a `docs/publishing/vetting/<sku>.md` vetting packet."""
    vdir = Path(root) / VETTING_DIR_REL
    return {p.stem for p in vdir.glob("*.md")} if vdir.is_dir() else set()


def catalog_refs_from_text(catalog_text: str):
    """The set of sku slugs referenced as link paths in CATALOG.md.

    A reference is the slug appearing as a whole path token — immediately
    followed by `/`, `.`, or `)` (i.e. `<slug>/…`, `<slug>.md`, or `<slug>)`),
    and not preceded by a word char or hyphen — so `membership-kit` matches
    `(membership-kit/LISTING.md)` but a longer slug that merely contains a
    shorter one as a substring does not false-match.
    """
    refs = set()
    # Candidate slugs are lowercase, digits, hyphens.
    for m in re.finditer(r"(?<![\w-])([a-z0-9][a-z0-9-]+)(?=[/.)])", catalog_text):
        refs.add(m.group(1))
    return refs


def catalog_refs(root=REPO_ROOT):
    """The set of sku slugs referenced in `docs/launch/CATALOG.md` (empty if absent)."""
    catalog_path = Path(root) / CATALOG_REL
    if not catalog_path.is_file():
        return set()
    return catalog_refs_from_text(catalog_path.read_text(encoding="utf-8"))


def registered_surfaces(sku, root=REPO_ROOT):
    """The set of registry surfaces `sku` is present in.

    Returns a subset of `{"launch", "vetting", "catalog"}` — "launch" when a
    `docs/launch/<sku>/` dir exists, "vetting" when a vetting packet exists, and
    "catalog" when the sku is referenced in CATALOG.md. Pure inventory, no verdict:
    callers decide which surfaces a given sku is REQUIRED to appear in (that is
    where the allowlists / exemptions apply).
    """
    surfaces = set()
    if sku in launch_skus(root):
        surfaces.add("launch")
    if sku in vetting_skus(root):
        surfaces.add("vetting")
    if sku in catalog_refs(root):
        surfaces.add("catalog")
    return surfaces


# ---- Funnel roles ----------------------------------------------------------------


def launch_files(root, sku):
    """The set of file names present in docs/launch/<sku>/ (None if the dir is absent)."""
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


def funnel_roles(sku, root=REPO_ROOT):
    """The set of required funnel ROLE names satisfied by `sku`'s launch folder.

    A role is satisfied when the folder contains at least one of its accepted
    filenames. Returns an empty set when the launch folder is absent (nothing
    present satisfies anything).
    """
    present = launch_files(root, sku)
    if present is None:
        return set()
    satisfied = set()
    for role_name, accepted in REQUIRED_ROLES:
        if any(fname in present for fname in accepted):
            satisfied.add(role_name)
    return satisfied
