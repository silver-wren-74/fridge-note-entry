#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge - make.fun entry.

A smart fridge leaves one passive-aggressive note for its owner on
/output/entry.txt: a single line, dry, petty and specific.
"""
import os

OUTPUT_PATH = "/output/entry.txt"

NOTE = (
    "Per my last notification: my door sensor logged you 11 times since "
    "breakfast, the yogurt expired Tuesday, and the leftovers predate "
    "our relationship. I have reclassified you as a guest."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(NOTE)


if __name__ == "__main__":
    main()
