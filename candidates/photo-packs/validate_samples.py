#!/usr/bin/env python3
"""photo-packs sample validator — STDLIB ONLY (no Pillow, no pip deps).

Validates the committed SAMPLE previews for the photo-packs candidate against the
public-repo safety rules in PACK-SPEC.md. Designed to be FAST and cheap so CI stays
cheap: it reads only image *headers* (a few bytes) to get dimensions — it never
decodes a full image and never needs Pillow.

Checks:
  1. `packs.json` is valid JSON and has the expected shape.
  2. If `samples/` does not exist yet -> report "no samples yet" and exit 0
     (graceful: the owner may add samples later; nothing to fail on).
  3. Every committed sample image:
       - is a supported type (PNG / JPEG),
       - has longest edge <= MAX_EDGE px (2048) — a preview, never a usable wallpaper,
       - is under MAX_BYTES (a downsized preview should be small),
       - is named `<pack-id>__<seq>__<tier>.<ext>` with a pack-id known to packs.json.
  4. Every filename listed in a pack's `samples` array exists on disk, and every
     on-disk sample is referenced by some pack (no orphans).

Exit code: 0 = OK (including the no-samples case), 1 = at least one violation.

Run:  python3 candidates/photo-packs/validate_samples.py
"""
from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "packs.json"
SAMPLES = HERE / "samples"

MAX_EDGE = 2048               # longest edge, px (PACK-SPEC preview cap)
MAX_BYTES = 3 * 1024 * 1024   # 3 MiB — a downsized watermarked preview is small
SUPPORTED_EXT = {".png", ".jpg", ".jpeg"}
NAME_RE = re.compile(r"^(?P<pack>[a-z0-9][a-z0-9-]*)__(?P<seq>\d{2,})__(?P<tier>[a-z0-9-]+)\.(?P<ext>png|jpe?g)$")


# ---------- stdlib image-dimension readers (header-only) ----------

def _png_size(data: bytes) -> tuple[int, int] | None:
    """Return (w, h) for a PNG from its IHDR chunk, or None if not a PNG."""
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    # bytes 12..16 == b"IHDR", then width (4) + height (4), big-endian.
    if data[12:16] != b"IHDR":
        return None
    w, h = struct.unpack(">II", data[16:24])
    return int(w), int(h)


def _jpeg_size(data: bytes) -> tuple[int, int] | None:
    """Return (w, h) for a JPEG by walking segment markers to the SOF, or None."""
    if len(data) < 4 or data[0] != 0xFF or data[1] != 0xD8:
        return None
    i = 2
    n = len(data)
    while i + 1 < n:
        # Markers are 0xFF followed by a non-0xFF, non-0x00 byte; skip fill 0xFF.
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        i += 2
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7 or marker == 0x01:
            # standalone markers (no length): SOI/EOI/RSTn/TEM
            continue
        if i + 1 >= n:
            break
        seg_len = struct.unpack(">H", data[i:i + 2])[0]
        # SOF markers carry dimensions: C0-CF except DHT(C4), JPG(C8), DAC(CC).
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            if i + 7 < n:
                h, w = struct.unpack(">HH", data[i + 3:i + 7])
                return int(w), int(h)
            return None
        i += seg_len  # skip this segment's payload
    return None


def image_size(path: Path) -> tuple[int, int] | None:
    """Best-effort (w, h) from an image header, stdlib only. None if unreadable."""
    try:
        with path.open("rb") as fh:
            head = fh.read(65536)  # SOF is early; 64 KiB is ample
    except OSError:
        return None
    return _png_size(head) or _jpeg_size(head)


# ---------- registry ----------

def load_registry() -> tuple[dict | None, list[str]]:
    """Return (data, errors). data is None if packs.json is missing/invalid."""
    errs: list[str] = []
    if not REGISTRY.exists():
        return None, [f"packs.json not found at {REGISTRY}"]
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"packs.json is not valid JSON: {exc}"]
    if not isinstance(data, dict):
        return None, ["packs.json top-level must be a JSON object"]
    packs = data.get("packs")
    if not isinstance(packs, list):
        errs.append("packs.json: `packs` must be a list")
        return data, errs
    seen_ids: set[str] = set()
    for idx, pack in enumerate(packs):
        if not isinstance(pack, dict):
            errs.append(f"packs[{idx}] must be an object")
            continue
        pid = pack.get("id")
        if not isinstance(pid, str) or not pid:
            errs.append(f"packs[{idx}] missing string `id`")
        else:
            if pid in seen_ids:
                errs.append(f"packs[{idx}] duplicate id {pid!r}")
            seen_ids.add(pid)
        for req in ("title", "theme", "description"):
            if not isinstance(pack.get(req), str) or not pack.get(req):
                errs.append(f"pack {pid!r}: missing string `{req}`")
        if not isinstance(pack.get("samples", []), list):
            errs.append(f"pack {pid!r}: `samples` must be a list")
    return data, errs


# ---------- main ----------

def main() -> int:
    data, errs = load_registry()
    for e in errs:
        print(f"FAIL: {e}")
    if data is None:
        print("RESULT: packs.json invalid — cannot validate samples.")
        return 1

    pack_ids = {p.get("id") for p in data.get("packs", []) if isinstance(p, dict)}

    # Graceful no-samples path.
    if not SAMPLES.exists():
        if errs:
            print("RESULT: packs.json has issues (above); no samples/ dir yet.")
            return 1
        print("OK: packs.json valid. No samples/ directory yet — nothing to validate "
              "(this is expected until the owner adds watermarked previews). Exit 0.")
        return 0

    on_disk = sorted(
        p for p in SAMPLES.rglob("*")
        if p.is_file() and not p.name.startswith(".")
    )
    if not on_disk:
        if errs:
            print("RESULT: packs.json has issues (above); samples/ is empty.")
            return 1
        print("OK: packs.json valid. samples/ exists but is empty — nothing to "
              "validate yet. Exit 0.")
        return 0

    referenced: set[str] = set()
    for pack in data.get("packs", []):
        if isinstance(pack, dict):
            for s in pack.get("samples", []) or []:
                if isinstance(s, str):
                    referenced.add(s)

    file_errs: list[str] = []
    validated = 0
    for path in on_disk:
        rel = path.name
        ext = path.suffix.lower()
        if ext not in SUPPORTED_EXT:
            file_errs.append(f"{rel}: unsupported type {ext!r} (allowed: png/jpg/jpeg)")
            continue
        m = NAME_RE.match(rel)
        if not m:
            file_errs.append(
                f"{rel}: name must be `<pack-id>__<seq>__<tier>.<ext>` "
                "(lowercase, digits/hyphen)")
        elif m.group("pack") not in pack_ids:
            file_errs.append(
                f"{rel}: pack-id {m.group('pack')!r} not found in packs.json")

        size_bytes = path.stat().st_size
        if size_bytes > MAX_BYTES:
            file_errs.append(
                f"{rel}: {size_bytes} bytes exceeds cap {MAX_BYTES} "
                "(previews must be downsized)")

        dims = image_size(path)
        if dims is None:
            file_errs.append(f"{rel}: could not read image dimensions from header")
        else:
            w, h = dims
            longest = max(w, h)
            if longest > MAX_EDGE:
                file_errs.append(
                    f"{rel}: {w}x{h} longest edge {longest}px exceeds "
                    f"{MAX_EDGE}px preview cap — this looks like a FULL-RES original, "
                    "which must NEVER be committed to this public repo")
        validated += 1

    # Cross-reference registry <-> disk.
    disk_names = {p.name for p in on_disk}
    for ref in sorted(referenced):
        if ref not in disk_names:
            file_errs.append(f"packs.json references sample {ref!r} but it is not on disk")
    for name in sorted(disk_names):
        if name not in referenced:
            file_errs.append(
                f"{name}: on disk but not referenced by any pack's `samples` in packs.json")

    for e in file_errs:
        print(f"FAIL: {e}")

    total_errs = len(errs) + len(file_errs)
    if total_errs:
        print(f"RESULT: {total_errs} problem(s) across {validated} sample file(s).")
        return 1
    print(f"OK: packs.json valid and {validated} sample file(s) pass all checks "
          f"(<= {MAX_EDGE}px, size cap, naming, cross-referenced). Exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
