# pip install geopy
# pip install requests
# Enter your API KEY from AIR VISUAL API

import tkinter as tk
import requests

# Create the main application window with a size of 400x400
app = tk.Tk()
app.geometry("400x400")
app.title("Live  AQI")
app.configure(bg="#F0F0F0")  # Set the background color of the window

# Create labels, entry fields, and a button for user input
city_label = tk.Label(app, text="City:")
city_label.pack()
city_label.configure(bg="#F0F0F0")  # Set the background color of the label
city_entry = tk.Entry(app)
city_entry.pack()

state_label = tk.Label(app, text="State:")
state_label.pack()
state_label.configure(bg="#F0F0F0")  # Set the background color of the label
state_entry = tk.Entry(app)
state_entry.pack()

country_label = tk.Label(app, text="Country:")
country_label.pack()
country_label.configure(bg="#F0F0F0")  # Set the background color of the label
country_entry = tk.Entry(app)
country_entry.pack()

get_aqi_button = tk.Button(
    app, text="Get AQI", bg="#3498db"
)  # Set the background color of the button
get_aqi_button.place(x=180, y=200)

# Add some space between the entry fields and the button
spacer_label = tk.Label(app, text="", bg="#F0F0F0")
spacer_label.place(x=90, y=150)

# Create labels to display the AQI information
city_label = tk.Label(app, text="City:")
city_label.pack()
city_label.configure(bg="#F0F0F0")  # Set the background color of the label
state_label = tk.Label(app, text="State:")
state_label.pack()
state_label.configure(bg="#F0F0F0")  # Set the background color of the label
aqi_label = tk.Label(app, text="AQI:")
aqi_label.pack()
aqi_label.configure(bg="#F0F0F0")  # Set the background color of the label

AIRVISUAL_API_KEY = "YOUR API KEY"
AIRVISUAL_API_URL = "https://api.airvisual.com/v2/city"


def get_aqi():
    city = city_entry.get().strip()  # Remove leading/trailing whitespaces
    state = state_entry.get().strip()
    country = country_entry.get()

    if city.lower() == "mumbai":
        city = "Mumbai"
        state = "Maharashtra"

    params = {
        "city": city,
        "state": state,
        "country": country,
        "key": AIRVISUAL_API_KEY,
    }
    response = requests.get(AIRVISUAL_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        aqi = data["data"]["current"]["pollution"]["aqius"]
        city_label.config(text=f"City: {city}")
        state_label.config(text=f"State: {state}")
        aqi_label.config(text=f"AQI: {aqi}")
    else:
        aqi_label.config(text="Error: Unable to fetch AQI data")
        city_label.config(text=f"City: -")
        state_label.config(text=f"State: -")


get_aqi_button.config(command=get_aqi)

app.mainloop()
