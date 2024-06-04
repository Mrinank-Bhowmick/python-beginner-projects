# weather_api.py
import requests

def fetch_weather(api_key, location):
    try:
        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        return api_link.status_code, api_data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
