"""
file_handler.py - A module for writing weather information to a file.

This module contains a function `write_to_file` that writes weather information
to a text file named 'weatherinfo.txt'.

Functions:
    write_to_file(location, weather_data): Writes weather information to a file.


"""

from datetime import datetime


def write_to_file(location, weather_data):
    """
    Writes weather information to a text file named 'weatherinfo.txt'.

    Parameters:
        location (str): The location for which weather information is being written.

    Returns:
        None

    Raises:
        IOError: If an error occurs while writing to the file.
    """
    try:
        # Open the file in write mode (creates if not exists) and append if exists
        with open("weatherinfo.txt", "w+") as f:
            # Get current date and time
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            # Write header with location and date time
            f.write("-------------------------------------------------------------\n")
            f.write(f"Weather Stats for - {location.upper()}  || {date_time}\n")
            f.write("-------------------------------------------------------------\n")

            # Write temperature if available
            if "main" in weather_data and "temp" in weather_data["main"]:
                f.write("\tCurrent temperature is : {:.2f} °C\n".format(weather_data["main"]["temp"] - 273.15))

            # Write weather description if available
            if "weather" in weather_data and weather_data["weather"]:
                f.write("\tCurrent weather desc   : " + weather_data["weather"][0]["description"] + "\n")

            # Write humidity if available
            if "main" in weather_data and "humidity" in weather_data["main"]:
                f.write("\tCurrent Humidity       : {} %\n".format(weather_data["main"]["humidity"]))

            # Write wind speed if available
            if "wind" in weather_data and "speed" in weather_data["wind"]:
                f.write("\tCurrent wind speed     : {} km/h \n".format(weather_data["wind"]["speed"]))

            # Write country code if available
            if "sys" in weather_data and "country" in weather_data["sys"]:
                f.write("\tCountry Code    : {} \n".format(weather_data["sys"]["country"]))

        # Print confirmation message
        print("Weather information written to weatherinfo.txt")
    except IOError as e:
        # Handle IO errors
        print("Error writing to file:", e)
