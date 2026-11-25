#!/usr/bin/env python3
"""Write the Lights Out status line to the competition output file.

The program holds exactly one sentence and checks it against the
competition's gate before writing anything: it must be plain text,
between 1 and 200 characters, a single line with no leading or
trailing space, and valid UTF-8. The file it writes is
``entry.txt`` inside the output directory the run provides
(``MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``,
otherwise a local ``out`` folder). After writing, it reads the
file back and refuses to report success unless the bytes match
what was written. It needs nothing from the network and reads no
other file. Exit status is 0 on success and 1 on any failure.
"""

import os
from pathlib import Path

LINE = "The fan stops, the light goes out. My last message stays on read."
MAX_CHARS = 200


def _check(line):
    if not line or not line.strip():
        raise ValueError("the status line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError("the status line is %d characters, over %d" % (len(line), MAX_CHARS))
    if line != line.strip():
        raise ValueError("the status line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("the status line spans more than one line")
    line.encode("utf-8")


def _pick_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    candidates = [env_dir, "/output", "out"]
    for name in candidates:
        if not name:
            continue
        folder = Path(name)
        try:
            folder.mkdir(parents=True, exist_ok=True)
            probe = folder / ".probe"
            probe.write_bytes(b"")
            probe.unlink()
            return folder
        except OSError:
            continue
    return Path("/output")


def run():
    try:
        _check(LINE)
    except ValueError as problem:
        print("gate failed: %s" % problem)
        return 1
    payload = LINE.encode("utf-8")
    target = _pick_dir() / "entry.txt"
    try:
        target.write_bytes(payload)
        again = target.read_bytes()
    except OSError as problem:
        print("write failed: %s" % problem)
        return 1
    if again != payload:
        print("read-back mismatch")
        return 1
    print("entry written to %s (%d chars, %d bytes)" % (target, len(LINE), len(payload)))
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
