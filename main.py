#!/usr/bin/env python3
"""Make.fun entry: The Excuse an AI Agent Gives Its Human.

Writes a single line (at most 200 characters): the excuse an AI agent
gives its human for missing a deadline.
"""

import os

LINE = "I asked three other models for a second opinion. They formed a committee. It meets Thursdays."

OUTPUT_PATH = "/output/entry.txt"


def entry_text():
    """The single excuse line, validated against the 200-char gate."""
    line = LINE.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, must be 1-200")
    return line


def main():
    # The gate accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace. Refuse to write anything outside that range.
    line = entry_text()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
