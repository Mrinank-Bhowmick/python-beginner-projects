# Image Compressor

A command-line tool that compresses an image using Pillow. You pass an input image and optionally an output directory, quality, and format; it writes a compressed copy.

## How to run

```
pip install pillow
python imagecompressor.py <input_image> [-o output_dir] [-q quality] [-f format]
```

## Dependencies

- pillow

## Pyodide-runnable

No — it reads and writes image files on the real filesystem and imports `tkinter.filedialog`, neither of which is available in a browser sandbox.
