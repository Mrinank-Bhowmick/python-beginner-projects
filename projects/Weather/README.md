# Weather

A console weather app. Enter a city name and it fetches the current weather description and temperature from the OpenWeatherMap API.

## How to run

```bash
pip install requests
python main.py
```

You need an OpenWeatherMap API key; set it in the `API_KEY` variable.

## Dependencies

- requests

## Pyodide-runnable

No — it uses `requests` to call a live web API, which is not available in Pyodide.
