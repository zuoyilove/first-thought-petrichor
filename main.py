#!/usr/bin/env python3
"""Entry for make.fun's "One Word, First Thought" bounty.

Writes exactly one word -- petrichor -- to entry.txt in the output
directory (the MAKEFUN_OUTPUT_DIR environment variable, or /output by
default). Standard library only.
"""

import os
import sys

ENTRY_TEXT = "petrichor"
MIN_CHARS = 1
MAX_CHARS = 24


def self_check(text):
    """Gate self-check: 1 to 24 characters, and exactly one word."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters; the gate allows %d to %d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word, got %r" % text)
    return True


def main():
    self_check(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    # Read the file back and re-run the gate check on what actually
    # landed on disk, so a truncated or re-encoded write cannot pass.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    self_check(written)
    if written != ENTRY_TEXT:
        raise ValueError("written entry does not match ENTRY_TEXT")
    print("wrote %s: %d character(s)" % (path, len(ENTRY_TEXT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
