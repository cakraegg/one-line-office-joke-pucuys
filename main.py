#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single joke about office life to /output/entry.txt.

The joke is a fixed string, chosen in advance and locked in here:
no randomness, no network, no clock, no environment input, so every
run produces byte-identical output.
"""

import os
import sys

JOKE = (
    "I asked for a raise and got a pizza party, so now I'm the only "
    "employee paid in pepperoni and broken promises."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(text):
    """Check the entry obeys the competition's shape rules."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(text):
    """Write the validated joke to the entry file, exactly one line."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


def main():
    joke = validate(JOKE)
    write_entry(joke)
    return 0


if __name__ == "__main__":
    sys.exit(main())
