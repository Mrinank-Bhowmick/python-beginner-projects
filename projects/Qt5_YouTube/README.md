# Qt5 YouTube Player

A PyQt5 desktop application that plays local video files and YouTube videos, with playback controls for position, volume, and speed.

## Example

1. The window titled "QTube" opens with a search box at the top, a blank video area, playback controls (play/pause button, position slider, elapsed/duration labels), a volume slider, and a speed slider.
2. Type a YouTube URL or search query (e.g. `lofi beats`) into the search box and press Enter. The player resolves the stream URL via youtube_dl and enables the play button.
3. Click the play button to start playback. The elapsed label updates in real time (e.g. `0:00:45`) and the buffer percentage is shown (e.g. `Buffer: 80%`).
4. Drag the volume slider to adjust volume; the label updates to show `🔈 75%`. Drag the speed slider to change playback rate (e.g. `Speed: 2x`).
5. Use File > Open (Ctrl+O) to load and play a local video file instead.

## How to run on localhost

```sh
pip install PyQt5 youtube_dl
python main.py
```

## Dependencies

- PyQt5
- youtube_dl
