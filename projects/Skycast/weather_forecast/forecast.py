import requests
import pandas as pd


class WeatherForecast:
    def __init__(self, latitude, longitude, api_key, days):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key
        self.days = days
        self.base_url = "https://api.weatherbit.io/v2.0/forecast/daily"

    def get_weather_forecast(self):
        params = {
            "lat": self.latitude,
            "lon": self.longitude,
            "key": self.api_key,
            "include": "hourly",
            "days": self.days,
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            hourly_forecast = data["data"]
            weather_details = []

            for forecast in hourly_forecast:
                weather_details.append(
                    {
                        "city_name": data["city_name"],
                        "country_code": data["country_code"],
                        "date": forecast["datetime"],
                        "temperature": forecast["temp"],
                        "min_temp": forecast["min_temp"],
                        "max_temp": forecast["max_temp"],
                        "weather_description": forecast["weather"]["description"],
                        "wind_speed": forecast["wind_spd"],
                        "wind_direction": forecast["wind_cdir_full"],
                        "cloud_coverage": forecast["clouds"],
                        "visibility": forecast["vis"],
                        "uv_index": forecast["uv"],
                        "dew_point": forecast["dewpt"],
                    }
                )

            df = pd.DataFrame(weather_details)
            return df
        else:
            print("Error:", response.status_code)
            return None
