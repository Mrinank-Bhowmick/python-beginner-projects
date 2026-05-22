# File Organizer

A command-line tool that organizes a directory by file type. It scans the given directory and moves files into category folders (Music, Videos, Documents, Pictures, etc.) based on their extensions.

## Example

```text
$ python main.py /home/user/Downloads -v
Creating 'Documents' folder.
Moved 'report.pdf' to 'Documents' folder.
Moved 'notes.txt' to 'Documents' folder.
Creating 'Pictures' folder.
Moved 'photo.jpg' to 'Pictures' folder.
Creating 'Music' folder.
Moved 'song.mp3' to 'Music' folder.
Organizing files complete!
```

## How to run on localhost

```
python main.py <directory_path> [-v]
```

`-v` enables verbose output.

## Dependencies

Standard library only (`argparse`, `os`, `logging`, `shutil`).
