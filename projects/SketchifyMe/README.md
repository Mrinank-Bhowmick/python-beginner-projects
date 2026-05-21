# SketchifyMe

Seamlessly convert your images into pencil-sketch renditions, facilitating the effortless creation of your sketches.
## How to run

```
pip install opencv-python numpy
python image_to_sketch.py
```

## Dependencies

opencv-python (cv2), numpy

## Pyodide-runnable

No — it relies on OpenCV's `cv2.imshow`/`waitKey` GUI windows and reads an image file from the local disk.
