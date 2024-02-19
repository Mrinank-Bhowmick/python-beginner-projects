import os


from PIL import Image, ImageDraw, ImageFont


def make_cards(guestList):
    """Makes custom cards for each guest
    Args:
        guestList (str): Path to file containing guest list
    Returns:
        None
    """
    # make folder to store resulting images
    os.makedirs("imageCards", exist_ok=True)

    # load flower image
    flowerImg = Image.open("flower.png")

    # read each guest from file
    with open(guestList) as file:
        for line in file:
            guest = line[:-1]

            # create image
            card = Image.new("RGBA", (288, 360), "white")
            # add flower image
            card.paste(flowerImg, (0, 0))

            # create border around image
            border = Image.new("RGBA", (291, 363), "black")
            border.paste(card, (3, 3))

            # draw guest name
            draw_obj = ImageDraw.Draw(border)
            card_font = ImageFont.truetype("Pacifico.ttf", 24)
            draw_obj.text((120, 100), guest, fill="red", font=card_font)

            # save resulting image
            imageName = "{}_card.png".format(guest)
            border.save(os.path.join("imageCards", imageName))


if __name__ == "__main__":
    make_cards("guests.txt")
