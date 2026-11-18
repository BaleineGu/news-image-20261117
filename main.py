"""Write the 17 November 2026 news image to the output directory.

The entry image is the file ``entry.png`` next to this script.  This
program copies it to ``entry.png`` inside the output directory, which
is the ``MAKEFUN_OUTPUT_DIR`` environment variable when set, and
``/output`` otherwise.  It uses only the Python standard library and
makes no network requests, so it runs in the grader's sandbox.
"""

import os
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT = "/output"


def output_directory() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT))


def copy_entry() -> Path:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"entry image not found: {source}", file=sys.stderr)
        raise SystemExit(1)
    destination_dir = output_directory()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / SOURCE_NAME
    data = source.read_bytes()
    destination.write_bytes(data)
    if destination.stat().st_size != len(data):
        print("copied entry image has the wrong size", file=sys.stderr)
        raise SystemExit(1)
    return destination


def main() -> None:
    destination = copy_entry()
    print(f"wrote {destination}")


if __name__ == "__main__":
    main()
