#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to /output/entry.txt, where the
make.fun program/v1 grader reads it. The line was selected by a
pairwise tournament against the competition judge's published
criteria (fortune voice + trading loss, rueful warm laugh, one
breath, fresh twist, oracular phrasing broken by the punchline).
See NOTES.md in the build workspace for the full tournament log.
"""

import os

FORTUNE = (
    "Great wealth awaits the patient trader; alas, your patience "
    "was liquidated at 3 a.m., together with everything else."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)


if __name__ == "__main__":
    main()
