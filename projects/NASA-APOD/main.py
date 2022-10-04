import credentials
import requests
import wget

url = "https://api.nasa.gov/planetary/apod?api_key=" + credentials.API_KEY

response = requests.get(url)
data = response.json()

date = data["date"]
title = data["title"]
image_url = data["url"]


image_filename = wget.download(image_url)
print("Image Successfully Downloaded: ", image_filename)
