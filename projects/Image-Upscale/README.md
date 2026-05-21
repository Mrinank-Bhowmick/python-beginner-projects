# Image Upscale

Upscales an image using the ESRGAN super-resolution model built on PyTorch.

## How to run

```
pip install torch torchvision pillow
python main.py
```

You also need a trained ESRGAN model file and an input image; update the paths in `main.py`.

## Dependencies

torch, torchvision, Pillow (and an ESRGAN module/model).

## Pyodide-runnable
No — it relies on PyTorch and local image files, which are not available in the browser.
