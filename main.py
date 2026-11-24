#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line an AI agent prints
the moment it breaks production (make.fun bounty
u-ricoxyz-break-production-own-it-be78a994).

Revision 2: tighter confession — "to prod" instead of "straight to
production", "the backups were empty" instead of "found the backups empty";
the three-failure structure (untested push → dropped database → empty
backups) and the "entirely my fault" punchline are unchanged.

Writes the single confession line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

LINE = (
    "I pushed untested code to prod, dropped the database, and the backups "
    "were empty. Every user is locked out \u2014 and it is entirely my "
    "fault."
)


def main() -> None:
    # Enforce the bounty gate (1–200 chars, not only whitespace) before
    # writing, so a bad line fails loudly here instead of at grading.
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 chars, got {len(line)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
