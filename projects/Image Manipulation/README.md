# Image Manipulation

A small Pillow script that opens a local image (`mars.jpg`), resizes it to 200x200 pixels, and saves the result as `newImage.jpg`.

## How to run

```
pip install pillow
python resizingImage.py
```

## Dependencies

- pillow

## Pyodide-runnable

No — it reads and writes image files on the real filesystem, which is not available in a browser sandbox.
