# QRCode Generator

A console script that asks for a website/URL, encodes it into a QR code, and saves the image to the `static` folder as `qrcode.jpg`.

## How to run

```sh
pip install qrcode pillow
python main.py
```

## Dependencies

- qrcode
- pillow

## Pyodide-runnable

No - it depends on the `qrcode` and `pillow` packages and writes an image file to a real disk path.
