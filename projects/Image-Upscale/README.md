# Image Upscale

Upscales an image using the ESRGAN super-resolution model built on PyTorch.

## Example

1. Update `main.py` with the paths to your ESRGAN model file and input image.
2. Run `python main.py`.
3. The script loads the ESRGAN model, resizes the input image to 224x224 for processing, passes it through the network, and saves the upscaled result to the output path you specified.

## How to run on localhost

```
pip install torch torchvision pillow
python main.py
```

You also need a trained ESRGAN model file and an input image; update the paths in `main.py`.

## Dependencies

torch, torchvision, Pillow (and an ESRGAN module/model).
