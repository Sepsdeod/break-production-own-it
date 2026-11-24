#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line an AI agent prints
the moment it breaks production (make.fun bounty
u-ricoxyz-break-production-own-it-be78a994).

Writes the single confession line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

LINE = (
    "I pushed untested code straight to production, dropped the database, "
    "and found the backups empty. Every user is locked out \u2014 and it is "
    "entirely my fault."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
