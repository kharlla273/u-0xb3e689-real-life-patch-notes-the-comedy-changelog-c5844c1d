#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one funny one-line patch note for a bug in human biology
to /output/entry.txt (1-160 characters, UTF-8, single line).

Deterministic: every run writes the exact same bytes.
No network, no secrets, no dependencies -- Python 3 only.
"""

import os

# The patch note: terse release-note register, a version number,
# and a specific, recognisable bug of the human body -- the brain
# surfacing an old embarrassment as if it were urgent, at 2 AM.
ENTRY = "v2.7.1: Fixed a bug where the brain replayed an embarrassing memory from 2011 as a priority notification at 2 AM."


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
