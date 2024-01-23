import os
from PIL import Image


def resize_image(image_path, size):
    im = Image.open(image_path)
    im = im.resize(size)
    return im


def main():
    choice = input("Do you want to resize multiple images? (yes/no): ")
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    size = (width, height)

    images = []
    if choice.lower() == "yes":
        dir_path = input("Enter the directory path of the images: ")
        for filename in os.listdir(dir_path):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                image_path = os.path.join(dir_path, filename)
                images.append((image_path, resize_image(image_path, size)))
    else:
        image_path = input("Enter the image path: ")
        images.append((image_path, resize_image(image_path, size)))

    output_folder = input("Enter the output folder: ")
    os.makedirs(output_folder, exist_ok=True)

    for image_path, im in images:
        new_image_name = input(
            f"Enter the new name for {os.path.basename(image_path)}: "
        )
        output_path = os.path.join(output_folder, new_image_name)
        im.save(output_path)
        print(f"Resized image is saved as {output_path}.")

    print("Done resizing images.")


if __name__ == "__main__":
    main()
