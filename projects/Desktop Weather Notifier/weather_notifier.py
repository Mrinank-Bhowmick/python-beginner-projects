from plyer import notification
import requests, datetime, time, os

def formatted_hour(hr):
    if 11 >= hr > 0:
        return f"{hr}am"
    elif 23 >= hr >= 12:
        return f"{hr - 12}pm"
    elif hr == 0:
        return f"12am"
    
def formatted_wind_dir(wd):
    formatted_str = ""
    match wd[0]:
        case 'N':
            formatted_str += 'North'
        case 'E':
            formatted_str += 'East'
        case 'W':
            formatted_str += 'West'
        case 'S':
            formatted_str += 'South'

    match wd[-1]:
        case 'E':
            formatted_str += 'East'
        case 'W':
            formatted_str += 'West'

    return formatted_str

MONTHS      = [None, 'January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
 
BASE_URL    = "https://api.weatherapi.com/v1/current.json"
API_KEY     = "" # your API key from weatherapi.com
CITY        = "Haridwar"
REQUEST_URL = f"{BASE_URL}?key={API_KEY}&q={CITY}&aqi=no"

init_time   = time.time() - 3600
while True:
    if time.time() - init_time >= 3600:
        response = requests.get(REQUEST_URL)
        if response.__bool__() is True:
            
            data = response.json()
            location, current = data["location"], data["current"]
            date = datetime.date.today()
            hour = datetime.datetime.now().hour

            notification.notify(
                title   = f"Weather in {CITY} on {date.day} {MONTHS[date.month]}",
                message = f"{current['condition']['text']} at about {formatted_hour(hour)}\n\
{current['wind_kph']}kmph winds from the {formatted_wind_dir(current['wind_dir'])}\n\
Feels like {current['feelslike_c']} °C\nPrecipation: {current['precip_mm']}mm",
                app_name= "Weather Notifier",
                app_icon= os.path.dirname(__file__) + r"/weather_logo.ico",
                timeout= 20
            )

        else:
            notification.notify(
                title   = "Error encountered",
                message = f"An error was encountered.\nFailed to fetch weather data.",
                app_name= "Weather Notifier",
                app_icon= os.path.dirname(__file__) + r"/weather_logo.ico"
            )
        init_time = time.time()