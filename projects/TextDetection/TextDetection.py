import argparse
import io
from google.cloud import vision
from google.cloud.vision import types


def main(image_file):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    # Loads the image into memory
    with io.open(image_file, "rb") as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    # Perform label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations
    for label in labels:
        print(label.description)


if __name__ == "__main__":
    parser = argparse._ArgumentParser()
    parser.add_argument("image_file", help="The image you'd like to label.")
    args = parser.parse_args()
    main(args.image_file)
