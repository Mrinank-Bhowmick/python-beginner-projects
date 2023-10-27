from PIL import Image
import os

if os.path.exists("newImage.jpg"):
    os.remove("newImage.jpg")

img = Image.open("mars.jpg")
newImage = img.resize((200, 200))

newImage.save("newImage.jpg")
