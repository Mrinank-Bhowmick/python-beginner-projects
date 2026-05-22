# Image to PDF Converter

Resizes every image in a `convert/` directory to A4 size and merges them into a single `output.pdf` file using FPDF.

## Example

1. Place the images you want to convert inside the `convert/` directory (e.g., `page1.jpg`, `page2.jpg`).
2. Run `python image_to_pdf_converter.py`.
3. Each image is resized to A4 dimensions (210x297 mm) and added as a separate page; the merged PDF is saved as `output.pdf` in the current directory.

## How to run on localhost

```
pip install fpdf
python image_to_pdf_converter.py
```

## Dependencies

- fpdf
