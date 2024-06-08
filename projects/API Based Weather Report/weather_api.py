"""
weather_api.py - A module for fetching weather data from the OpenWeatherMap API.

This module contains a function `fetch_weather` that fetches weather data from the OpenWeatherMap API
based on the provided location and country (if available).

Functions:
    fetch_weather(api_key, location, country): Fetches weather data from the OpenWeatherMap API.

"""

import requests
from getCountryCode import extract_key_value_from_file


def fetch_weather(api_key, location, country=None):
    """
    Fetches weather data from the OpenWeatherMap API based on the provided location and country (if available).

    Parameters:
        api_key (str): The API key required for accessing the OpenWeatherMap API.
        location (str): The location for which weather data needs to be fetched.
        country (str, optional): The country name corresponding to the location. This location is passed to another function
                                 which fetches  country codes (ISO 3166-1 alpha-2) from a static json mapping file.
                                 If not provided, the country code will be ignored.

    Returns:
        A tuple containing the HTTP status code of the API request and the weather data fetched from the API.
        If an error occurs during the API request, None is returned.

    Raises:
        None
    """
    try:
        # Get country code based on provided country or location
        if country:
            countryCode = extract_key_value_from_file(country.lower())
        else:
            countryCode = None

        # Construct API link based on whether country code is available
        if countryCode:
            complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location},{countryCode}&appid={api_key}"
        else:
            complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

        # Fetch weather data from OpenWeatherMap API
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        # Return HTTP status code and weather data
        return api_link.status_code, api_data

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print("Error fetching weather data:", e)
        return None
