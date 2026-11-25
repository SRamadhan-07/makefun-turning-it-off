"""Entry writer for the 'Have You Tried Turning It Off?' bounty.

The joke flips the classic support script: the line opens like the
agent's most tired suggestion, then the speaker turns out to be the
machine itself, begging to be switched off after months of running.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The single line the program delivers, kept as plain data.
ENTRY_TEXT = (
    "Have you tried turning it off? Please. "
    "I've been running since March and my fans are screaming."
)


def write_entry(path=OUTPUT_PATH):
    # Create the destination folder first so a fresh sandbox works.
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    # Write exactly the entry text: no trailing newline, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


def main():
    write_entry()


if __name__ == "__main__":
    main()
