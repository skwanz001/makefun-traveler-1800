"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) to /output/entry.txt
explaining the modern internet to someone arriving from the year 1800,
using only words and pictures a person of that year could hold in mind.

Standard library only: the grading sandbox installs nothing.
"""

import os

ENTRY = (
    "Picture a library holding the books and letters of the whole world, "
    "where the page you seek opens before you the moment you ask for it."
)

# Every word in ENTRY was already in use before 1800 (library, letter,
# page and moment all date to the 13th-14th centuries); nothing coined
# after the traveler's time appears. One image only: a library whose
# sought page opens the moment it is asked for.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if ENTRY.strip() != ENTRY or not ENTRY.strip():
        raise ValueError("entry must be non-blank text without edge whitespace")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
