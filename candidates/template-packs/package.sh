#!/bin/sh
# package.sh — assemble a clean, buyer-facing bundle of the Agent-Workflow
# Template Pack into candidates/template-packs/dist/template-packs-v0.1.zip
#
# Buyer bundle = QUICKSTART.md + README.md + INCLUDED.md + the whole pack/ tree.
# It deliberately EXCLUDES:
#   - LISTING.md   (seller marketing, not part of the product)
#   - dist/        (build output; never nest a zip inside itself)
#   - package.sh   (build tooling)
#   - .git         (repo metadata)
#
# Deterministic-ish + idempotent: staged files are copied then stamped to a
# fixed mtime, listed via `find | sort`, and zipped with `zip -X`, so re-running
# produces the same archive. Safe to re-run.
#
# Usage:  sh package.sh        (from anywhere; paths are script-relative)
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="template-packs-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"   # fixed timestamp for reproducible archives

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT"

# --- top-level buyer docs ---
cp "$SRC/QUICKSTART.md" "$ROOT/QUICKSTART.md"
cp "$SRC/README.md"     "$ROOT/README.md"
cp "$SRC/INCLUDED.md"   "$ROOT/INCLUDED.md"

# --- the drop-in payload: copy pack/ verbatim, then prune non-product cruft ---
cp -R "$SRC/pack" "$ROOT/pack"
find "$ROOT/pack" -name '.DS_Store' -delete
find "$ROOT/pack" -name '__pycache__' -type d -prune -exec rm -rf {} +

# --- normalize mtimes for a reproducible archive ---
find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

# --- build the zip deterministically (sorted entries, no extra attrs) ---
mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
