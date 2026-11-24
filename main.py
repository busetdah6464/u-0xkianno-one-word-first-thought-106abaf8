#!/usr/bin/env python3
"""One Word, First Thought — write exactly one word to /output/entry.txt.

The chosen word is "petrichor": the smell of rain on dry earth after
a long dry spell. It is surprising rather than safe, vivid and specific
— it calls up a clear image and feeling in nine letters — and it carries
a spark of wit in its sound: the soft "petr-" of stone meeting the
freshness of rain.
"""

import os

WORD = "petrichor"


def main():
    os.makedirs("/output", exist_ok=True)
    # Exactly one word, no trailing newline, no spaces: the gate allows
    # 1-24 characters and the brief demands a single word and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
