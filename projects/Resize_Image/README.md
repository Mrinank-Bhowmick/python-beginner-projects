# Resize Image

A console tool that resizes one image or all images in a directory to a user-specified width and height, then saves the results to an output folder.

## Example

```text
Do you want to resize multiple images? (yes/no): no
Enter the width: 800
Enter the height: 600
Enter the image path: /home/alice/photo.jpg
Enter the output folder: /home/alice/resized
Enter the new name for photo.jpg: photo_resized.jpg
Resized image is saved as /home/alice/resized/photo_resized.jpg.
Done resizing images.
```

## How to run on localhost

```sh
pip install pillow
python resize.py
```

## Dependencies

- pillow
