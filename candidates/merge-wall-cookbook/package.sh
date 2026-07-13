#!/bin/sh
# package.sh — assemble a clean, buyer-facing bundle of The Agent
# Merge-Wall Cookbook into
# candidates/merge-wall-cookbook/dist/merge-wall-cookbook-v0.1.zip
#
# Buyer bundle = README + QUICKSTART + INCLUDED + guide/ + recipes/.
# It deliberately EXCLUDES (allow-list, never a blanket copy):
#   - LISTING.md    (seller pointer, not part of the product)
#   - INTAKE.md     (this candidate's own lane-internal intake)
#   - dist/         (build output; never nest a zip inside itself)
#   - package.sh    (build tooling)
#   - .git          (repo metadata)
#
# Deterministic + idempotent: staged files are copied then stamped to a
# fixed mtime, listed via `find | sort`, and zipped with `zip -X`, so
# re-running produces the byte-identical archive. Safe to re-run.
#
# Usage:  sh package.sh        (from anywhere; paths are script-relative)
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="merge-wall-cookbook-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"   # fixed timestamp for reproducible archives

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT"

# --- top-level buyer files (explicit allow-list) ---
cp "$SRC/README.md"     "$ROOT/README.md"
cp "$SRC/QUICKSTART.md" "$ROOT/QUICKSTART.md"
cp "$SRC/INCLUDED.md"   "$ROOT/INCLUDED.md"

# --- the guide + recipes: copy verbatim, then prune non-product cruft ---
cp -R "$SRC/guide"   "$ROOT/guide"
cp -R "$SRC/recipes" "$ROOT/recipes"
find "$ROOT" -name '.DS_Store' -delete
find "$ROOT" -name '__pycache__' -type d -prune -exec rm -rf {} +

# --- normalize mtimes for a reproducible archive ---
find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

# --- build the zip deterministically (sorted entries, no extra attrs) ---
mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
