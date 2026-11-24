#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single static joke about office life to /output/entry.txt.
The text is locked in as a constant: no randomness, no network, no
dependencies, so every run produces byte-identical output.

The joke: the office Wi-Fi as a spirit animal. It lands because it is
a real one-line joke (not a slogan), turns on the three-beat rule of
threes at the end, and rings true for anyone who has sat through a
hybrid meeting blaming the connection.
"""

import os

JOKE = (
    "I told HR my spirit animal is the office Wi-Fi: present in every "
    "meeting, connected to nothing, and blamed for everything."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the locked-in joke to the entry file, exactly one line."""
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
