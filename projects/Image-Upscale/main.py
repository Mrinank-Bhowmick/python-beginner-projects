import torch
from PIL import Image
from torchvision import transforms
from ESRGAN import ESRGAN

# Load the ESRGAN model
model = ESRGAN()
model.load_state_dict(torch.load("path/to/ESRGAN_model.pth"))
model.eval()

# Load the image to be upscaled
img = Image.open("path/to/image.jpg")

# Define the transformation to be applied to the image
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)

# Apply the transformation to the image
img_tensor = transform(img).unsqueeze(0)

# Upscale the image using the ESRGAN model
upscaled_img_tensor = model(img_tensor)

# Convert the upscaled image back to a PIL image
upscaled_img = transforms.ToPILImage()(upscaled_img_tensor[0].data.clamp(0, 1))

# Save the upscaled image
upscaled_img.save("path/to/upscaled_image.jpg")
