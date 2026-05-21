# Desktop Weather Notifier

Fetches current weather for a city from weatherapi.com once per hour and shows it as a native desktop notification, including temperature, wind, and precipitation.

## How to run

```
pip install plyer requests
python weather_notifier.py
```

Set your weatherapi.com API key in the `API_KEY` variable.

## Dependencies

- `plyer`
- `requests`

## Pyodide-runnable

No — it makes network requests to a weather API and uses `plyer` to display OS-level desktop notifications.
