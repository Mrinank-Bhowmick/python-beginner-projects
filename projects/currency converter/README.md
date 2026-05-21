# Currency Converter

A real-time currency converter with a Tkinter GUI. It fetches the latest exchange rates from an online API and lets the user convert an amount between any two currencies via dropdown menus.

## How to run

```
pip install requests
python "currency converter.py"
```

## Dependencies

- `requests`
- `tkinter` (standard library)

## Pyodide-runnable

No — it builds a `tkinter` GUI and fetches live exchange rates over the network, neither of which works in the Pyodide browser environment.
