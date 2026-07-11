#!/bin/sh
# Build the buyer bundle for the Agent Fleet Field Manual v0.1.
# Bundles: the buyer-facing README + LISTING, the chapters/ markdown, the
# runnable templates/, and the built single-file dist HTML.
# EXCLUDES: INTAKE.md (internal), build.py + package.sh (build tooling),
# dist/*.zip, .git, __pycache__.
# The zip is byte-reproducible: mtimes are pinned and entries are sorted.
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="agent-fleet-field-manual-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
HTML_NAME="agent-fleet-field-manual-v0.1.html"
SOURCE_DATE="200001010000.00"

# Build the HTML first so the freshly-built book is staged.
python3 "$SRC/build.py"

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT/chapters" "$ROOT/templates" "$ROOT/dist"

cp "$SRC/README.md"            "$ROOT/README.md"
cp "$SRC/LISTING.md"           "$ROOT/LISTING.md"
cp "$SRC"/chapters/*.md        "$ROOT/chapters/"
cp "$SRC"/templates/*.md       "$ROOT/templates/"
cp "$SRC/dist/$HTML_NAME"      "$ROOT/dist/$HTML_NAME"

# Pin every mtime so the archive is byte-reproducible.
find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
