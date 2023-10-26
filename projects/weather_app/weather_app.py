import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "Temperature (Celsius)": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
        }
        return weather_data
    else:
        return "City not found or API request failed."

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)

    if isinstance(weather_data, dict):
        print(f"Weather in {city}:")
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print(weather_data)

if __name__ == "__main__":
    main()
