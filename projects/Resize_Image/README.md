# Resize Image

A console tool that resizes one image or all images in a directory to a user-specified width and height, then saves the results to an output folder.

## How to run

```sh
pip install pillow
python resize.py
```

## Dependencies

- pillow

## Pyodide-runnable

No - it uses the `pillow` package and reads/writes image files on the real filesystem, which is not available in the browser sandbox.
