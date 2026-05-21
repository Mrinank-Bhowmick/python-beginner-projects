# Random Advisor

A small Tkinter desktop app that fetches a random piece of advice from the
[Advice Slip API](https://api.adviceslip.com/) and shows it in a window. Click
**Get Advice** for a new one.

## How to run

```bash
pip install requests
python advisor.py
```

## Dependencies

- `requests` — to call the Advice Slip API
- `tkinter` — GUI (ships with the standard Python installer)

## Pyodide-runnable

No. It uses a Tkinter window and a live HTTP request, neither of which works in
the in-browser Pyodide playground.
