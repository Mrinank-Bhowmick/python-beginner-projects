import requests
import streamlit as st
from get_geolocation.geolocation import GeolocationModel
from weather_forecast.forecast import WeatherForecast
import matplotlib.pyplot as plt


class SkyCast:
    def __init__(self):
        self.geolocation_model = GeolocationModel()
        self.api_key = "your_api_key_here"
        self.base_url = "https://api.weatherbit.io/v2.0/current"
        self.weather_option = "Today's Weather"

    def title(self):
        st.markdown(
            '<div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px;">'
            '<h1 style="text-align: center; color: #0080FF;">SkyCast 🌤️</h1>'
            "</div>",
            unsafe_allow_html=True,
        )

    def input(self):
        st.sidebar.title("Weather Options")
        self.weather_option = st.sidebar.radio(
            "Choose Weather Option",
            options=["Today's Weather", "Forecast Weather"],
            key="weather_option",
        )

        if self.weather_option == "Today's Weather":
            self.display_today_weather()
        else:
            self.display_forecast_weather()

    def display_today_weather(self):
        latitude, longitude = None, None
        # Manually enter the city name
        city_name = st.sidebar.text_input("Enter City Name", key="city_name")
        if st.sidebar.button("Submit"):
            latitude, longitude = self.geolocation_model.get_location_by_name(city_name)
        else:
            # If the submit button is not clicked, do not proceed further
            return

        st.markdown(
            f"<h2 style='text-align: center;'>Today's Weather</h2>",
            unsafe_allow_html=True,
        )

        if latitude is not None and longitude is not None:
            # Make API request
            response = self.get_weather_data(latitude, longitude)
            if response is not None:
                weather_data = response["data"][0]

                # Weather details container
                datetime_value = weather_data["datetime"]
                datetime_value = datetime_value[:-3]
                # Date and time
                st.markdown(
                    f'<h3 style="text-align: center;">{weather_data["city_name"]}, {weather_data["country_code"]}: {datetime_value}</h3>',
                    unsafe_allow_html=True,
                )

                # Additional weather information
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f'Temperature: {weather_data["temp"]}°C')
                    st.markdown(f'Wind Speed: {weather_data["wind_spd"]} m/s')
                    st.markdown(f'Cloud Coverage: {weather_data["clouds"]}%')
                    st.markdown(f'Visibility: {weather_data["vis"]} km')

                with col2:
                    st.markdown(
                        f'Weather Description: {weather_data["weather"]["description"]}'
                    )
                    st.markdown(f'Wind Direction: {weather_data["wind_cdir_full"]}')
                    st.markdown(f'UV Index: {weather_data["uv"]}')
                    st.markdown(f'Dew Point: {weather_data["dewpt"]}°C')

            else:
                st.write("Location not found.")

    def display_forecast_weather(self):
        latitude, longitude = None, None
        # Manually enter the city name
        city_name = st.sidebar.text_input("Enter City Name", key="city_name")
        days = st.sidebar.number_input(
            "How Many days do you want to Forecast",
            key="days",
            value=1,
            min_value=1,
            step=1,
            format="%d",
        )

        if st.sidebar.button("Submit"):
            latitude, longitude = self.geolocation_model.get_location_by_name(city_name)
        else:
            # If the submit button is not clicked, do not proceed further
            return
        st.markdown(
            f"<h2 style='text-align: center;'>Forecast Weather</h2>",
            unsafe_allow_html=True,
        )

        if latitude is not None and longitude is not None:
            # Create an instance of the WeatherForecast class
            weather = WeatherForecast(latitude, longitude, self.api_key, days)

            # Retrieve the weather forecast data
            forecast_df = weather.get_weather_forecast()

            # Show forecast data
            for i in range(len(forecast_df)):
                st.markdown(
                    f'<h3 style="text-align: center;">{forecast_df["date"][i]}</h3>',
                    unsafe_allow_html=True,
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f'Temperature: {forecast_df["temperature"][i]}°C')
                    st.markdown(f'Wind Speed: {forecast_df["wind_speed"][i]} m/s')
                    st.markdown(f'Cloud Coverage: {forecast_df["cloud_coverage"][i]}%')
                    st.markdown(f'Visibility: {forecast_df["visibility"][i]} km')

                with col2:
                    st.markdown(
                        f'Weather Description: {forecast_df["weather_description"][i]}'
                    )
                    st.markdown(f'Wind Direction: {forecast_df["wind_direction"][i]}')
                    st.markdown(f'UV Index: {forecast_df["uv_index"][i]}')
                    st.markdown(f'Dew Point: {forecast_df["dew_point"][i]}°C')

            temp = forecast_df["temperature"]
            min_temp = forecast_df["min_temp"]
            max_temp = forecast_df["max_temp"]
            date = forecast_df["date"]

            st.set_option("deprecation.showPyplotGlobalUse", False)
            plt.figure(figsize=(10, 6))  # Set the figure size

            # Plot the temperature line
            plt.plot(
                date, temp, label="Temperature", marker="o", linestyle="-", color="blue"
            )

            # Plot the minimum temperature line
            plt.plot(
                date,
                min_temp,
                label="Min Temperature",
                marker="o",
                linestyle="-",
                color="green",
            )

            # Plot the maximum temperature line
            plt.plot(
                date,
                max_temp,
                label="Max Temperature",
                marker="o",
                linestyle="-",
                color="red",
            )

            # Set the labels and title
            plt.xlabel("Date")
            plt.ylabel("Temperature (°C)")
            plt.title("Temperature Forecast")

            # Add a legend
            plt.legend()

            # Display the plot
            st.pyplot()

        else:
            st.write("Location not found.")

    def get_weather_data(self, latitude, longitude):
        params = {
            "lat": latitude,
            "lon": longitude,
            "key": self.api_key,
            "include": "minutely",
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                st.write(f"Error: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            st.write(f"Error: {e}")
            return None


# Create an instance of the SkyCast class
weather_forecast = SkyCast()

# Display the title and input fields
weather_forecast.title()
weather_forecast.input()
