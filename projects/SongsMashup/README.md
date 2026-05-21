# Songs Mashup

A Flask web app that downloads songs from YouTube for a given singer, slices each track into short snippets, merges them into a single mashup audio file, zips it, and emails the result to the user.

## How to run

```
pip install flask numpy pandas pytube pydub youtube-search
python SongsMashup.py
```

## Dependencies

flask, numpy, pandas, pytube, pydub, youtube-search, smtplib (standard library)

## Pyodide-runnable

No — it is a Flask server that downloads from YouTube, processes audio with pydub/ffmpeg, and sends email via SMTP, none of which work in Pyodide.
