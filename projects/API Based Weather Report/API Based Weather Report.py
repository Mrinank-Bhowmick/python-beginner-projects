import requests
from datetime import datetime
from Util_Functions import (
    wind_degree_to_direction,
    unix_timestamp_to_localtime,
    convert_temperature,
)


def fetch_weather(api_key, location):
    """
    Function to fetch weather data from OpenWeatherMap API.

    Parameters:
    api_key (str): API key.
    location (str): City name.

    Returns:
    str: The JSON response string.
    """
    try:
        # Constructing the API link with the provided API key and location
        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

        # Sending GET request to OpenWeatherMap API
        api_link = requests.get(complete_api_link)

        # Parsing the JSON response
        api_data = api_link.json()

        # Returning the fetched weather data
        return api_data

    # Handling exceptions related to request errors
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None


def write_to_file(weather_data, temperature_unit):
    """
    Function to write weather information to a text file.

    Parameters:
    weather_data (str): The JSON API response string.
    temperature_unit (str): 'C' for Celsius, 'F' for Fahrenheit.
    """

    try:
        # Opening the file "weatherinfo.txt" in write mode
        with open("weatherinfo.txt", "w+") as f:
            # Getting the current date and time
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            # Writing header information to the file
            if (
                "name" in weather_data
                and "sys" in weather_data
                and "country" in weather_data["sys"]
            ):
                f.write(
                    "-------------------------------------------------------------\n"
                )
                f.write(
                    f"Weather Stats for - {weather_data['name']} | {weather_data['sys']['country']} "
                    f"| {date_time}\n"
                )
                f.write(
                    "-------------------------------------------------------------\n"
                )

            # Writing temperature information to the file
            if "main" in weather_data and "temp" in weather_data["main"]:
                f.write(
                    "\tCurrent temperature is : "
                    + convert_temperature(
                        weather_data["main"]["temp"], temperature_unit
                    )
                    + "\n"
                )

            # Writing weather description information to the file
            if "weather" in weather_data and weather_data["weather"]:
                f.write(
                    "\tCurrent weather desc   : "
                    + weather_data["weather"][0]["description"]
                    + "\n"
                )

            # Writing humidity information to the file
            if "main" in weather_data and "humidity" in weather_data["main"]:
                f.write(
                    "\tCurrent Humidity       : {} %\n".format(
                        weather_data["main"]["humidity"]
                    )
                )

            # Writing wind speed information to the file
            if "wind" in weather_data and "speed" in weather_data["wind"]:
                f.write(
                    "\tCurrent wind speed     : {} km/h \n".format(
                        weather_data["wind"]["speed"]
                    )
                )

            # Writing wind direction information to the file
            if "wind" in weather_data and "deg" in weather_data["wind"]:
                f.write(
                    "\tCurrent wind direction : "
                    + wind_degree_to_direction(weather_data["wind"]["deg"])
                    + " \n"
                )

            # Writing sunrise local time to the file
            if (
                "sys" in weather_data
                and "sunrise" in weather_data["sys"]
                and "timezone" in weather_data
            ):
                f.write(
                    "\tToday's sunrise time   : "
                    + unix_timestamp_to_localtime(
                        weather_data["sys"]["sunrise"], weather_data["timezone"]
                    )
                    + " \n"
                )

            # Writing sunset local time to the file
            if (
                "sys" in weather_data
                and "sunset" in weather_data["sys"]
                and "timezone" in weather_data
            ):
                f.write(
                    "\tToday's sunset time    : "
                    + unix_timestamp_to_localtime(
                        weather_data["sys"]["sunset"], weather_data["timezone"]
                    )
                    + " \n"
                )

        # Printing confirmation message after writing to file
        print("Weather information written to weatherinfo.txt")

    # Handling IOError when writing to file
    except IOError as e:
        print("Error writing to file:", e)


def main():
    """
    Main function.
    """
    # Printing welcome messages and instructions
    print("Welcome to the Weather Information App!")
    print("You need an API key to access weather data from OpenWeatherMap.")
    print(
        "You can obtain your API key by signing up at https://home.openweathermap.org/users/sign_up"
    )

    # Prompting the user to input API key, city name, and temperature unit
    api_key = input("Please enter your OpenWeatherMap API key: ")
    location = input("Enter the city name: ")
    temperature_unit = input(
        "Enter the temperature unit. 'C' for Celsius and 'F' for Fahrenheit: "
    )

    if not (temperature_unit.upper() == "C" or temperature_unit.upper() == "F"):
        print("Temperature unit must either be 'C' or be 'F'.")
        return

    # Fetching weather data using the provided API key and location
    weather_data = fetch_weather(api_key, location)

    # Checking if weather data was successfully fetched
    if weather_data:
        # Checking if the API key is invalid
        if weather_data["cod"] == "401":
            print("Invalid API key.")
            return

        # Checking if the city is not found
        if weather_data["cod"] == "404":
            print("City not found.")
            return

        # Writing weather information to file
        write_to_file(weather_data, temperature_unit)

        # Printing weather information to console
        print(
            "Current City          : "
            + weather_data["name"]
            + ", "
            + weather_data["sys"]["country"]
        )
        print(
            "Current temperature is: "
            + convert_temperature(weather_data["main"]["temp"], temperature_unit)
        )
        print("Current weather desc  : " + weather_data["weather"][0]["description"])
        print("Current Humidity      :", weather_data["main"]["humidity"], "%")
        print("Current wind speed    :", weather_data["wind"]["speed"], "kmph")
        print(
            "Current wind direction:",
            wind_degree_to_direction(weather_data["wind"]["deg"]),
        )
        print(
            "Today's sunrise time  :",
            unix_timestamp_to_localtime(
                weather_data["sys"]["sunrise"], weather_data["timezone"]
            ),
        )
        print(
            "Today's sunset time   :",
            unix_timestamp_to_localtime(
                weather_data["sys"]["sunset"], weather_data["timezone"]
            ),
        )
    else:
        # Printing error message if weather data fetching fails
        print("Failed to fetch weather data. Please check your input and try again.")


# Ensuring the main function is executed when the script is run
if __name__ == "__main__":
    main()
