# NASA-APOD

[Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) is a popular website from NASA. This app retrives the metadata of an image from APOD and the image itself (including the explanation of the picture).

## Example

```text
Image Successfully Downloaded: Pillars_of_Creation.jpg
```

The script fetches today's APOD metadata from the NASA API, downloads the image file into the current directory, and prints a confirmation message with the saved filename.

### Pre-Req

```
pip install -r requirements.txt
```

### How to run on localhost the app

1. Create a account in nasa.gov and generate your API KEY
2. Pass it in `credentials.py`
3. Run the application `python main.py`
