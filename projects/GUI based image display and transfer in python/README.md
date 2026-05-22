# GUI Image Display and Transfer

A Tkinter desktop application for viewing and copying images. It lets you open an image through a file dialog, displays it in the window, and saves (copies) it to a new location of your choice.


## Example

1. The window opens titled "Image Viewer and Transfer" with an "Open Image" button and a "Save Image" button.
2. Click "Open Image" — a file dialog appears; select any image file (e.g. `photo.jpg`).
3. The image is displayed in the window.
4. Click "Save Image" — a save-as dialog appears; choose a destination path and filename (e.g. `copy.png`).
5. The image is copied to the chosen location.

## How to run on localhost

```
pip install pillow
python GUIimage.py
```

## Dependencies

- pillow
