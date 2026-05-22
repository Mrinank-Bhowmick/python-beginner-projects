# Live AQI

A Tkinter app that fetches the live Air Quality Index for a given city, state, and country from the AirVisual API.

## Example

1. The window opens showing three labeled entry fields: City, State, and Country, plus a blue "Get AQI" button.
2. Type `Los Angeles` in City, `California` in State, and `USA` in Country.
3. Click "Get AQI".
4. The labels below update to show:
   - City: Los Angeles
   - State: California
   - AQI: 42

## How to run on localhost

```
pip install requests
python main.py
```

Requires an AirVisual API key set in `main.py`.

## Dependencies

tkinter (standard library), requests.
