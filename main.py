#!/usr/bin/env python3
"""Ship the 17 November 2026 front page to the grader's output folder.

The page itself is painted by ``draw.py`` at build time and stored here
as ``entry.png`` (JPEG bytes under that name, which the competition
allows: the format is told by the file's first bytes). This program's
only job is to place an exact copy of that file at
``$MAKEFUN_OUTPUT_DIR/entry.png`` (or ``/output/entry.png`` when the
variable is unset). It uses the Python standard library only, makes no
network requests, and writes the same bytes on every run.

Before writing it checks the source is a whole image: it must start
with a PNG or JPEG signature and must not be empty. After writing it
checks the copy is the same length as the source, so a truncated write
fails loudly instead of silently shipping a broken entry.
"""

import os
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"
FALLBACK_DIR = "/output"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def where_to_write() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path(FALLBACK_DIR)


def read_entry() -> bytes:
    source = Path(__file__).resolve().parent / ENTRY_NAME
    if not source.is_file():
        print(f"no entry image next to this program: {source}", file=sys.stderr)
        raise SystemExit(1)
    data = source.read_bytes()
    if not data:
        print("entry image is empty", file=sys.stderr)
        raise SystemExit(1)
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        print("entry image is neither PNG nor JPEG", file=sys.stderr)
        raise SystemExit(1)
    return data


def ship(data: bytes) -> Path:
    out_dir = where_to_write()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY_NAME
    target.write_bytes(data)
    written = target.stat().st_size
    if written != len(data):
        print(f"short write: {written} of {len(data)} bytes", file=sys.stderr)
        raise SystemExit(1)
    return target


def main() -> None:
    data = read_entry()
    kind = "PNG" if data.startswith(PNG_MAGIC) else "JPEG"
    target = ship(data)
    print(f"wrote {target} ({target.stat().st_size} bytes, {kind})")


if __name__ == "__main__":
    main()
