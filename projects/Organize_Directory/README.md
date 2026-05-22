# Organize Directory

A file organiser. Given a directory path, it sorts the files inside it into category folders (images, music, video, executables, archives, torrent, documents, code, design files) based on their file extensions.

## Example

```text
Enter the directory path of the files: /home/user/Downloads
Organising your files into [ images - music - video - executable - archive - torrent - document - code - design files]
Finished organising your files
```

Files in the given directory are moved into sub-folders (`images/`, `music/`, `video/`, `executables/`, `archives/`, `torrent/`, `documents/`, `code/`, `design-files/`) based on their extension.

## How to run on localhost

```
python organizer.py
```

## Dependencies

Standard library only (`os`, `shutil`).
