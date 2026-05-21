# Text Detection

A script that detects and prints text found in an image using the Google Cloud Vision API.

## How to run

```
pip install google-cloud-vision
python TextDetection.py <image_file>
```

Requires Google Cloud credentials configured in the environment.

## Dependencies

google-cloud-vision

## Pyodide-runnable

No — it calls the Google Cloud Vision API over the network and requires cloud authentication.
