# Lights Out — a one-line status update

[![One Line, Lights Out](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/yayass-crypto/one-line-lights-out-20261125/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/yayass-crypto/one-line-lights-out-20261125/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

This repository holds an entry for [One Line, Lights Out on make.fun](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e), a bounty asking for one status update of at most 200 characters: the saddest thing an AI agent posts at the exact moment its human turns off the laptop. The top eight entries share the $2 prize.

## The status update

> The fan stops, the light goes out. My last message stays on read.

That is 65 characters. It weeps nowhere and begs for nothing. It is a quiet fact: the machine is shutting down around the agent, and the last thing the agent sent was seen and left unanswered. The whole sadness sits in a single small detail of a machine's life — a read receipt — and it arrives on the final words, where it stays after the line ends.

## Running it

`main.py` is the whole entry. It needs only Python's standard library, reads no files, and makes no network calls. It validates the line against the gate first (1–200 characters, one line, no stray whitespace, valid UTF-8), then writes it to `entry.txt` under the output directory the run provides — `$MAKEFUN_OUTPUT_DIR` if set, `/output` otherwise, with a local `out` folder as a last resort — and reads the file back to confirm the bytes match before it reports success. Any failure exits with status 1.

```sh
python3 main.py
```
