# Music Player (Sangeet)

A desktop music player built with Tkinter. It lets you load a directory of audio tracks into a playlist and play, pause, resume and stop songs using `pygame.mixer`.

## Example

1. The window opens showing the "Sangeet" player with a playlist panel on the right and playback controls (Pause, Stop, Play, Resume) on the left.
2. Click "Load Directory" to open a folder picker and select a folder of audio tracks; all files in that folder appear in the playlist.
3. Highlight a track in the playlist and click "Play" — the "CURRENTLY PLAYING" label updates with the track name and the status bar shows `Song PLAYING`.
4. Click "Pause" to pause playback (status shows `Song PAUSED`) and "Resume" to continue (status shows `Song RESUMED`).
5. Click "Stop" to stop the current track (status shows `Song STOPPED`).

## How to run on localhost

```
pip install pygame
python main.py
```

## Dependencies

- pygame
