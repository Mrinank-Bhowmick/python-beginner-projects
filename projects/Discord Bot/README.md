# Discord Bot

A simple Discord bot built with discord.py. It responds to `!hello` and `!random` messages and provides an `?ask` command that gives a random Magic 8-Ball style answer.

## Example

```
# In a Discord channel:

User:  !hello
Bot:   Hello @User!

User:  !random
Bot:   47

User:  ?ask Will it rain tomorrow?
Bot:   @User asks: **Will it rain tomorrow?**
       My reply: **Outlook good**

User:  ?ask
Bot:   You didn't provide me with a question!
```

## How to run on localhost

```
pip install discord.py
python main.py
```

Replace `"Your Token Here"` in the script with a valid Discord bot token.

## Dependencies

- `discord.py`
