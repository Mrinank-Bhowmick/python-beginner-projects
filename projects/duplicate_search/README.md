# Duplicate File Search

Recursively searches a directory for duplicate files by comparing MD5 checksums, then interactively lets you delete unwanted copies.

## Example

```text
$ python main.py /home/user/downloads

0. /home/user/downloads/report.pdf
1. /home/user/downloads/backup/report.pdf
Delete? (e.g. 0,1,3) 1

0. /home/user/downloads/photo.jpg
1. /home/user/downloads/photos/photo.jpg
2. /home/user/downloads/photos/copy/photo.jpg
Delete? (e.g. 0,1,3) 1,2
```

## How to run on localhost

```
python main.py [directory]
```

If no directory is given, it searches the current directory.

## Dependencies

Standard library only (`hashlib`, `sys`, `collections`, `pathlib`).
