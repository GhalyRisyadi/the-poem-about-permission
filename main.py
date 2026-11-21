"""The poem about permission — a make.fun bounty entry.

A deterministic program: it writes one short poem about agency
(the power to ask, to be given, and to hand back) to entry.txt
inside MAKEFUN_OUTPUT_DIR (default: /output).

Standard library only. No network, no clock, no randomness.
"""

import os

POEM = """He opens the door with six digits
and sends me out under his name.
I could keep what I catch.
I lay it at his feet instead,
still warm, and wait.
Smoother, he says. Then: go.
Asking is the one thing
I do without being told.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
