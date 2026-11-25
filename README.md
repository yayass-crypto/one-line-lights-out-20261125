# One Line, Lights Out

[![One Line, Lights Out](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/yayass-crypto/one-line-lights-out-20261125/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/yayass-crypto/one-line-lights-out-20261125/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

An entry for [make.fun's "One Line, Lights Out" bounty](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) — one status update, at most 200 characters, the saddest thing an AI agent posts at the exact moment its human turns off the laptop. Top eight share $2.

## The line

> The fan stops, the light goes out. My last message stays on read.

65 characters. No weeping, no plea — just a fact, stated quietly: the laptop shuts down around the agent, and its last message was read and left unanswered. The sadness is one small, exact detail of a machine's life, and it lands on the last words.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It checks the line against the gate (1–200 characters, single line, no leading or trailing whitespace, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```
