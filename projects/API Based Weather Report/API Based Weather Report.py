import requests
from datetime import datetime


# Function to fetch weather data from OpenWeatherMap API
def fetch_weather(api_key, location):
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


# Function to write weather information to a text file
def write_to_file(location, weather_data):
    try:
        # Opening the file "weatherinfo.txt" in write mode
        with open("weatherinfo.txt", "w+") as f:
            # Getting the current date and time
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            # Writing header information to the file
            f.write("-------------------------------------------------------------\n")
            f.write(f"Weather Stats for - {location.upper()}  || {date_time}\n")
            f.write("-------------------------------------------------------------\n")

            # Writing temperature information to the file
            if "main" in weather_data and "temp" in weather_data["main"]:
                f.write(
                    "\tCurrent temperature is : {:.2f} °C\n".format(
                        weather_data["main"]["temp"] - 273.15
                    )
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

        # Printing confirmation message after writing to file
        print("Weather information written to weatherinfo.txt")

    # Handling IOError when writing to file
    except IOError as e:
        print("Error writing to file:", e)


# Main function
def main():
    # Printing welcome messages and instructions
    print("Welcome to the Weather Information App!")
    print("You need an API key to access weather data from OpenWeatherMap.")
    print(
        "You can obtain your API key by signing up at https://home.openweathermap.org/users/sign_up"
    )

    # Prompting the user to input API key and city name
    api_key = input("Please enter your OpenWeatherMap API key: ")
    location = input("Enter the city name: ")

    # Fetching weather data using the provided API key and location
    weather_data = fetch_weather(api_key, location)

    # Checking if weather data was successfully fetched
    if weather_data:
        # Writing weather information to file
        write_to_file(location, weather_data)

        # Printing weather information to console
        print(
            "Current temperature is: {:.2f} °C".format(
                weather_data["main"]["temp"] - 273.15
            )
        )
        print("Current weather desc  : " + weather_data["weather"][0]["description"])
        print("Current Humidity      :", weather_data["main"]["humidity"], "%")
        print("Current wind speed    :", weather_data["wind"]["speed"], "kmph")
    else:
        # Printing error message if weather data fetching fails
        print("Failed to fetch weather data. Please check your input and try again.")


# Ensuring the main function is executed when the script is run
if __name__ == "__main__":
    main()
