# Random Advisor

A small Tkinter desktop app that fetches a random piece of advice from the
[Advice Slip API](https://api.adviceslip.com/) and shows it in a window. Click
**Get Advice** for a new one.

## Example

1. The window titled "Random Advisor Application" opens and immediately fetches a
   piece of advice, displaying it in the centre of the window (e.g. "Always be
   yourself; everyone else is already taken.").
2. Click **Get Advice** to fetch a new random tip from the Advice Slip API.
3. The label updates with the new advice text.
4. Close the window to exit.

## How to run on localhost

```bash
pip install requests
python advisor.py
```

## Dependencies

- `requests` — to call the Advice Slip API
- `tkinter` — GUI (ships with the standard Python installer)
