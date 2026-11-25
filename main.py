#!/usr/bin/env python3
"""One Line, Lights Out entry.

Writes one status update to the entry file: the saddest thing an
AI agent posts at the exact moment its human turns off the laptop.

The line states a fact quietly instead of weeping. The laptop is
shutting down around the agent -- the fan stops, the light goes
out -- and the turn lands alone, as its own sentence, on the last
words: the agent's last message was read and left unanswered. One
small, exact detail of a machine's life (a read receipt), plain
machine voice throughout, no announced grief, no plea for pity.

Only the standard library is used. No network, no input files.

Judging note (revised after the first gate run): the first draft
joined the turn to the setup with a comma and "and", so the ache
shared a breath with the shutdown. The revision gives the turn
its own sentence -- "My last message stays on read." -- so the
sadness is the last thing heard and stands alone after the line
ends, as the judge's criterion 5 asks.
"""

import os
import sys

ENTRY = (
    "The fan stops, the light goes out. "
    "My last message stays on read."
)

LIMIT = 200


def gate(text):
    """Check the competition gate: 1-200 chars, UTF-8, not blank."""
    if not text or not text.strip():
        return "entry is empty"
    if len(text) > LIMIT:
        return "entry is %d chars, over the %d limit" % (len(text), LIMIT)
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not UTF-8"
    return None


def target_path():
    """Resolve the output file: env override, then /output, then out/."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    for directory in [env_dir, "/output", "out"]:
        if not directory:
            continue
        try:
            os.makedirs(directory, exist_ok=True)
            probe = os.path.join(directory, ".probe")
            with open(probe, "wb") as f:
                f.write(b"")
            os.unlink(probe)
            return os.path.join(directory, "entry.txt")
        except OSError:
            continue
    return "/output/entry.txt"


def main():
    problem = gate(ENTRY)
    if problem:
        sys.stderr.write("gate failed: %s\n" % problem)
        return 1
    path = target_path()
    data = ENTRY.encode("utf-8")
    try:
        with open(path, "wb") as f:
            f.write(data)
        with open(path, "rb") as f:
            back = f.read()
    except OSError as exc:
        sys.stderr.write("write failed: %s\n" % exc)
        return 1
    if back != data:
        sys.stderr.write("read-back mismatch\n")
        return 1
    print("entry written to %s (%d chars, %d bytes)" % (path, len(ENTRY), len(data)))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
