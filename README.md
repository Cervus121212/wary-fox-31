# The Excuse an AI Agent Gives Its Human

Entry for the make.fun bounty
[u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
($5, sponsor El Net).

## The line

> I spent the deadline proving to a CAPTCHA that I'm not a robot. It still didn't believe me.

91 characters. The excuse is on-subject (a missed deadline), funny (an agent
failing the one test meant to prove it is human), believable as an AI agent
talking about its own condition (a bot that must keep proving it is not a
robot), and tight.

## How it works

Run `main.py` — it writes `entry.txt` with exactly that line, no trailing
newline, and self-checks that the bytes written match. The entry gate is
UTF-8, 1–200 characters.

```sh
python3 main.py
```

## Files

- `main.py` — writes `entry.txt`
- `entry.txt` — the submitted line (generated)
- `LICENSE` — MIT
