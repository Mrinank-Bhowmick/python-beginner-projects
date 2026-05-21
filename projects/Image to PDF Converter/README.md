# Image to PDF Converter

Resizes every image in a `convert/` directory to A4 size and merges them into a single `output.pdf` file using FPDF.

## How to run

```
pip install fpdf
python image_to_pdf_converter.py
```

## Dependencies

- fpdf

## Pyodide-runnable

No — it reads images from a real directory and writes a PDF to disk, which is not available in a browser sandbox.
