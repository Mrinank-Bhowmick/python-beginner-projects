# Image Compressor

A command-line tool that compresses an image using Pillow. You pass an input image and optionally an output directory, quality, and format; it writes a compressed copy.

## Example

```text
$ python imagecompressor.py photo.jpg -o ./out -q 70 -f JPEG
Image compressed and saved as 'out/compressed_photo.jpg'
```

## How to run on localhost

```
pip install pillow
python imagecompressor.py <input_image> [-o output_dir] [-q quality] [-f format]
```

## Dependencies

- pillow
