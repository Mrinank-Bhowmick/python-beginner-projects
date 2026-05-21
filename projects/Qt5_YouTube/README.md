# Qt5 YouTube Player

A PyQt5 desktop application that plays local video files and YouTube videos, with playback controls for position, volume, and speed.

## How to run

```sh
pip install PyQt5 youtube_dl
python main.py
```

## Dependencies

- PyQt5
- youtube_dl

## Pyodide-runnable

No - it builds a PyQt5 GUI and uses `youtube_dl` for network access, neither of which works in the browser sandbox.
