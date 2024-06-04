# file_handler.py
from datetime import datetime

def write_to_file(location, weather_data):
    try:
        with open("weatherinfo.txt", "w+") as f:
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            f.write("-------------------------------------------------------------\n")
            f.write(f"Weather Stats for - {location.upper()}  || {date_time}\n")
            f.write("-------------------------------------------------------------\n")
            if "main" in weather_data and "temp" in weather_data["main"]:
                f.write("\tCurrent temperature is : {:.2f} °C\n".format(weather_data["main"]["temp"] - 273.15))
            if "weather" in weather_data and weather_data["weather"]:
                f.write("\tCurrent weather desc   : " + weather_data["weather"][0]["description"] + "\n")
            if "main" in weather_data and "humidity" in weather_data["main"]:
                f.write("\tCurrent Humidity       : {} %\n".format(weather_data["main"]["humidity"]))
            if "wind" in weather_data and "speed" in weather_data["wind"]:
                f.write("\tCurrent wind speed     : {} km/h \n".format(weather_data["wind"]["speed"]))
            if "sys" in weather_data and "country" in weather_data["sys"]:
                f.write("\tCountry Code    : {} \n".format(weather_data["sys"]["country"]))

        print("Weather information written to weatherinfo.txt")
    except IOError as e:
        print("Error writing to file:", e)
