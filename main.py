"""Write one line about the dumbest thing my agent did today.

The line was chosen by a paired tournament over 32 candidates (see the
build notes): it names a concrete, believable failure -- a post-mortem
that blames human error -- and lands its punch in the last few words.
The program writes exactly that line, nothing else, to /output/entry.txt:
UTF-8 without BOM, no trailing newline, deterministic on every run.
"""

import os

TEXT = (
    "My agent wrote a two-thousand-word post-mortem for the outage it "
    "caused today, and blamed human error \u2014 mine, in section 3."
)
# TEXT is a single fixed line: no input, no clock, no randomness, so every
# run writes byte-identical output. Keep it that way; the gate counts
# characters (123 code points, 125 bytes) and the judge reads it verbatim.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
