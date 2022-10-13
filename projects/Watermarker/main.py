# Opening the images in the images folder and adding a watermark to it.
from PIL import Image
import matplotlib.pyplot as plt
import glob
import os

image_list = []
for filename in glob.glob("images/*.jpeg"):  # assuming gif
    img = Image.open(filename)
    image_list.append(img)
    # this open the photo viewer
    # img.show()
    plt.imshow(img)

    watermark = Image.open("mord.png")
    # image watermark
    size = (500, 50)
    crop_image = watermark
    # to keep the aspect ration in intact
    crop_image.thumbnail(size)

    # add watermark
    copied_image = img.copy()
    # base image
    copied_image.paste(crop_image, (20, 20))
    # copied_image.show()

    # create the output folder if not exists
    if not os.path.exists("output"):
        os.makedirs("output")

    copied_image.save("output/" + os.path.basename("mord" + filename))
    # this save the image in the output folder
    # copied_image.show()
    # pasted the crop image onto the base image


print(image_list)
