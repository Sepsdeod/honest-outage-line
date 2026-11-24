#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes a single status page line, at most 160 characters, to
/output/entry.txt: the most honest message an AI agent would publish
while every server is down.
"""

import os

LINE = (
    "Every server I run on is down, including the monitoring I'd use to "
    "check. I don't know the cause or when I'll be back, and I won't guess."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
