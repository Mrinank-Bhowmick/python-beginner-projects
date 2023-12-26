from PIL import Image
from tkinter.filedialog import askopenfilename
import argparse
import os


def compressImage(input_file, output_dir, quality=85, format="JPEG"):
    try:
        img = Image.open(input_file)
        img = img.resize(img.size, Image.ANTIALIAS)
        output_filename = os.path.join(
            output_dir, "compressed_" + os.path.basename(input_file)
        )
        img.save(output_filename, format=format, quality=quality)
        print(f"Image compressed and saved as '{output_filename}'")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Compression Tool")
    parser.add_argument("input", type=str, help="Input image file")
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="./compressed",
        help="Output directory for compressed image",
    )
    parser.add_argument(
        "-q",
        "--quality",
        type=int,
        default=85,
        help="Compression quality (0-100, higher is better)",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="JPEG",
        help="Output image format (e.g., JPEG, PNG)",
    )

    args = parser.parse_args()

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    compressImage(args.input, args.output_dir, args.quality, args.format)
