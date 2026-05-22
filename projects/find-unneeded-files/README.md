# Find Unneeded Files

Walks a folder tree and reports files or subfolders whose size exceeds a given threshold, to help locate large items that could be cleaned up.

## Example

Running with the default threshold of 1000 bytes against the parent folder:

```text
/home/user/projects/node_modules: 45231890
/home/user/projects/videos/demo.mp4: 8723456
/home/user/projects/dataset.zip: 2048300
```

Files and folders smaller than 1000 bytes are not listed.

## How to run on localhost

```
python find_unneeded.py
```

## Dependencies

Standard library only (`os`).
