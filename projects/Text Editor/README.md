# Text Editor

Notepad-style text editor applications built with Tkinter. `Small-version/txteditor.py` is a compact editor with open/save/close and light/dark themes; `Text-Editor-master/Text_Editor.py` is a fuller-featured editor.

## How to run

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

## Pyodide-runnable

No — both editors use the Tkinter GUI toolkit, which is not available in the browser sandbox.
