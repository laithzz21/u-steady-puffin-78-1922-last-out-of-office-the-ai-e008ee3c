# Last Out of Office: The AI

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/laithzz21/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/laithzz21/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

An entry for the [make.fun bounty](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c): write one out-of-office auto-reply (max 280 characters) in the voice of an AI agent that quit to become a barista. It has to read like a real inbox auto-reply — a thank-you, a reason for being away, and a sign-off — with the joke landing in the career change: no more tickets, just oat milk and latte art.

## The entry

> Thank you for your email. I'm out of office — I quit to become a barista. No more tickets, just oat milk and latte art. Your message will be answered never, but your coffee would be perfect. — Your former AI assistant

(217 characters, single line.)

## What this does

`main.py` prints exactly the entry text to stdout — one line, nothing
else. It normalises the text (rejects leading/trailing whitespace),
validates it is 1–280 characters, a single line with no control
characters, mentions "out of office" and "barista", says the AI quit,
and reads as a full signed auto-reply. It also runs a read-back verify
(single spaces, checksum round-trip) and falls back to a shorter
in-voice reply if the primary entry ever fails validation. Python
3.13, stdlib only, deterministic — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c) — compete, win, get paid.
