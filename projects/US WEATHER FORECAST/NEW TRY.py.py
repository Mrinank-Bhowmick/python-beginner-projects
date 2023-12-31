#PLease check for the station names in the weatehr info like KJFK,KBKX
from NWS_Weather import current_weather, predicted_weather
print("Make sure you've checked the weather info pdf for proper station name")
city_code=input("Enter the city code=")
weather =current_weather(station=city_code)
for w in weather:
    print(w)