import os
import openai
import urllib.request
from PIL import Image

openai.api_key = os.getenv("OPENAI_API_KEY")

query = input(">> ")

response = openai.Image.create(prompt=query, n=1, size="1024x1024")
image = response["data"][0]["url"]
urllib.request.urlretrieve(image, "image.png")
img = Image.open("image.png")
img.show()
