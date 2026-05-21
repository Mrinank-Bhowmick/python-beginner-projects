# Discord Bot

A simple Discord bot built with discord.py. It responds to `!hello` and `!random` messages and provides an `?ask` command that gives a random Magic 8-Ball style answer.

## How to run

```
pip install discord.py
python main.py
```

Replace `"Your Token Here"` in the script with a valid Discord bot token.

## Dependencies

- `discord.py`

## Pyodide-runnable

No — it connects to Discord's gateway over the network and runs a long-lived bot event loop.
