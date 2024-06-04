# weather_api.py
import requests
from getCountryCode import extract_key_value_from_file

def fetch_weather(api_key, location, country):
    global countryCode
    try:
        countryCode= extract_key_value_from_file(country.lower())
        if countryCode:
            complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location},{countryCode}&appid={api_key}"
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            return api_link.status_code, api_data
        else:
            complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            return api_link.status_code, api_data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
