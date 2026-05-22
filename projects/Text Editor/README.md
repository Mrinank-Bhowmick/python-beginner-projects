# Text Editor

Notepad-style text editor applications built with Tkinter. `Small-version/txteditor.py` is a compact editor with open/save/close and light/dark themes; `Text-Editor-master/Text_Editor.py` is a fuller-featured editor.

## Example

1. The Tkinter window opens showing a blank text area with a menu bar at the top.
2. Type or paste text directly into the editing area.
3. Use **File → Open** to load an existing `.txt` file into the editor.
4. Edit the content, then use **File → Save** to write the changes back to disk.
5. In the small version, use the theme toggle to switch between light and dark mode.
6. Use **File → Close** to clear the editor, or close the window to exit.

## How to run on localhost

```
pip install pygments
python Small-version/txteditor.py
```

or

```
python Text-Editor-master/Text_Editor.py
```

## Dependencies

tkinter (standard library); the small version also imports pygments.
