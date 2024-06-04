# main.py
from weather_api import fetch_weather
from file_handler import write_to_file

def main():
    print("Welcome to the Weather Information App!")
    print("You need an API key to access weather data from OpenWeatherMap.")
    print("You can obtain your API key by signing up at https://home.openweathermap.org/users/sign_up")
    api_key = input("Please enter your OpenWeatherMap API key: ")
    location = input("Enter the city name: ")
    status_code, weather_data = fetch_weather(api_key, location)
    if status_code == 200:
        write_to_file(location, weather_data)
        print("Current temperature is: {:.2f} °C".format(weather_data["main"]["temp"] - 273.15))
        print("Current weather desc  : " + weather_data["weather"][0]["description"])
        print("Current Humidity      :", weather_data["main"]["humidity"], "%")
        print("Current wind speed    :", weather_data["wind"]["speed"], "kmph")
        print("Country Code          :", weather_data["sys"]["country"])
    elif 400 <= status_code < 500:  # Check if status code is in the 4xx range (Client error)
        print(f"Failed to fetch weather data. Client error: Status Code {status_code} , message : {weather_data["message"]}")
    else:
        print(f"Failed to fetch weather data. Server error: Status Code {status_code}")

if __name__ == "__main__":
    main()
