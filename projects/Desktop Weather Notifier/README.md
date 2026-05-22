# Desktop Weather Notifier

Fetches current weather for a city from weatherapi.com once per hour and shows it as a native desktop notification, including temperature, wind, and precipitation.

## Example

1. Set your weatherapi.com API key in the `API_KEY` variable and optionally change `CITY` (default: `Haridwar`).
2. Run the script. After startup it immediately fetches weather data and shows a desktop notification titled e.g. **"Weather in Haridwar on 22 May"** with a body like:
   ```
   Partly cloudy at about 3pm
   14kmph winds from the NorthEast
   Feels like 28 °C
   Precipation: 0.0mm
   ```
3. The script then sleeps and repeats the notification every hour while running.

## How to run on localhost

```
pip install plyer requests
python weather_notifier.py
```

Set your weatherapi.com API key in the `API_KEY` variable.

## Dependencies

- `plyer`
- `requests`
