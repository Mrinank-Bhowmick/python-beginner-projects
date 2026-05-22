# Weather

A console weather app. Enter a city name and it fetches the current weather description and temperature from the OpenWeatherMap API.

## Example

```text
Enter a city name: London
Weather: light rain
Temperature: 12.45 celsius
```

If the city is not found or the API key is invalid, the script prints `An error occurred.`

## How to run on localhost

```bash
pip install requests
python main.py
```

You need an OpenWeatherMap API key; set it in the `API_KEY` variable.

## Dependencies

- requests
