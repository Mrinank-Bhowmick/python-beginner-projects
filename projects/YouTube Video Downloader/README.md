# YouTube Video Downloader

A console tool that downloads a YouTube video using `yt-dlp`. It lists the available formats and lets you pick one or auto-selects the highest resolution.

## How to run

```bash
pip install yt-dlp
python you_tube_analyzer.py
```

## Dependencies

- yt-dlp

## Pyodide-runnable

No — it uses `yt-dlp` to download from the internet, which is not available in Pyodide.
