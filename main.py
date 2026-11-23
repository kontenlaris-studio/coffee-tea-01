#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Candidates weighed:
  B (tea): the quiet underdog ritual — calm, steeped, patient.
  A (coffee): the first letter, the first thing of the day.

Final pick: A. Coffee is the world's default morning fuel and A is
the default letter — first of the alphabet, grade A, "A.M." — and
the article "a" literally precedes coffee in everyday speech
("a coffee, please"). In a pairwise duel of single letters, A is
the bolder, truer, more vivid answer: the letter the day starts with.
"""
import os

LETTER = "A"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER + "\n")


if __name__ == "__main__":
    main()
