import requests
import json
import tkinter as tk
from tkinter import Entry, Label, Button

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    complete_url = base_url + 'q=' + city_name + '&appid=' + api_key
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]

        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]

        result_label.config(text=f"Weather in {city_name}:\nTemperature: {temperature} K\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description}")
    else:
        result_label.config(text="City not found")

def get_weather_from_input():
    city = city_entry.get()
    get_weather(city)

# Create the main window
root = tk.Tk()
root.geometry("500x200")

root.title("Weather Forecast App")

# Create and configure widgets
city_label = Label(root, text="Enter city name:")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

search_button = Button(root, text="Search", command=get_weather_from_input)
search_button.pack()

result_label = Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
