import json
import requests

print("--------Weather Forecaster------------")
place = input("Enter the place :")


# the API key to access the weatherstack API (you can get your API key from weatherstack and put it here _
key = ""


# defining endpoint 
url = f"http://api.weatherstack.com/current?access_key={key}&query={place}"


# hitting the endpoint 
res = requests.get(url=url) 
response = json.loads(res.content)

# Navigating through the json response to get the required data 
country = response["location"]["country"]
local_time = response["location"]["localtime"]
weather_desc = response["current"]["weather_descriptions"][0]
temperature = response["current"]["temperature"]
wind_speed = response["current"]["wind_speed"]
humidity= response["current"]["humidity"]
is_day = response["current"]["is_day"]

if is_day=="no":
    time = "Night"
else:
    time = "Day"

# Printing the final data into the terminal 
print(f"""
{place} lies in {country} 
Local Time : {local_time}

{place}'s Weather Data : 

Description : {weather_desc} {time}
Temperature : {temperature} deg Celsius
Wind Speed : {wind_speed} km/hr
Humidity : {humidity}""") 


