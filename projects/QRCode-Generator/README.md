# QRCode Generator

A console script that asks for a website/URL, encodes it into a QR code, and saves the image to the `static` folder as `qrcode.jpg`.

## Example

```text
Enter the website you need to make QR Code
https://github.com
```

The script encodes `https://github.com` into a QR code image and saves it to `static\qrcode.jpg` with no further output.

## How to run on localhost

```sh
pip install qrcode pillow
python main.py
```

## Dependencies

- qrcode
- pillow
