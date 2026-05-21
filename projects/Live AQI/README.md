# Live AQI

A Tkinter app that fetches the live Air Quality Index for a given city, state, and country from the AirVisual API.

## How to run

```
pip install requests
python main.py
```

Requires an AirVisual API key set in `main.py`.

## Dependencies

tkinter (standard library), requests.

## Pyodide-runnable
No — it uses a Tkinter GUI and makes live HTTP requests to the AirVisual API.
