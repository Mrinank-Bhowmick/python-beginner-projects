import os

from PIL import Image, ImageDraw, ImageFont


def create_instagram_post(template, text, output_path):
    # Load the template image
    template_path = os.path.join(
        os.path.dirname(__file__), "templates", "basic_template.jpg"
    )
    img = Image.open(template_path)

    # Initialize the drawing context
    draw = ImageDraw.Draw(img)
    font_path = os.path.join(os.path.dirname(__file__), "fonts", "Poppins-Regular.ttf")
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (img.width - text_width) // 2
    y = img.height - text_height - 20

    # Add text to the image
    draw.text((x, y), text, font=font, fill="white")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the final image
    img.save(output_path)
    print(f"Instagram post saved to {output_path}")


template_name = "basic_template"
post_text = "My Instagram Post"
output_file = "output/post.jpg"

create_instagram_post(template_name, post_text, output_file)
