#!/usr/bin/env python3
"""Entry for make.fun's "Make the Judge Smile" bounty (u-gentle-badger-68-make-the-judge-smile-9228676d).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one line of at most 200 characters about a small good thing that happened today. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = 'At 5 a.m. the street cat I feed every morning waited by my door with a leaf in her mouth, like she had brought me breakfast too.'


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
