# Text Detection

A script that detects and prints text found in an image using the Google Cloud Vision API.

## Example

```text
python TextDetection.py sign.jpg

OPEN
Mon-Fri 9am-5pm
Sat 10am-3pm
Closed Sunday
```

Each detected text annotation from the image is printed on its own line.

## How to run on localhost

```
pip install google-cloud-vision
python TextDetection.py <image_file>
```

Requires Google Cloud credentials configured in the environment.

## Dependencies

google-cloud-vision
