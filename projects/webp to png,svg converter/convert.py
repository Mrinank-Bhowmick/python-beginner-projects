from PIL import Image

import cairosvg


def convert_webp_to_png(input_path, output_path):
    """
    Convert a WEBP image to PNG format.

    :param input_path: Path to the input WEBP file
    :param output_path: Path to save the output PNG file
    """
    try:
        # Open the WEBP image
        img = Image.open(input_path)

        # Save the image as PNG
        img.save(output_path, 'PNG')
        print(f"Image saved as {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")


def convert_webp_to_svg(input_path, output_path):
    """
    Convert a WEBP image to SVG format.

    :param input_path: Path to the input WEBP file
    :param output_path: Path to save the output SVG file
    """
    try:
        # Convert the WEBP to PNG first (as SVG needs a format like PNG or JPEG)
        img = Image.open(input_path)
        png_temp_path = input_path.replace('.webp', '.png')
        img.save(png_temp_path, 'PNG')

        # Use cairosvg to convert PNG to SVG
        cairosvg.svg2png(url=png_temp_path, write_to=output_path)
        print(f"Image saved as {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")
