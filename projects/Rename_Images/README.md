# Rename Images

A console tool that walks a given directory and lets the user interactively rename each image file (jpg, png, jpeg).

## Example

```text
Enter the directory path of the images: /home/alice/photos
Enter the new name for IMG_001.jpg (without extension): vacation_beach
Enter the new name for IMG_002.png (without extension): sunset_view
Done renaming images.
```

Each image in the directory is presented one at a time; entering a name that already exists prompts for a different name.

## How to run on localhost

```sh
python rename_images.py
```

## Dependencies

Standard library only (uses `os`).
