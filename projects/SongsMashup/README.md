# Songs Mashup

A Flask web app that downloads songs from YouTube for a given singer, slices each track into short snippets, merges them into a single mashup audio file, zips it, and emails the result to the user.

## Example

1. Run `python SongsMashup.py` and open `http://0.0.0.0:5000` in a browser.
2. Fill in the form: singer name (e.g. `Ed Sheeran`), number of videos (e.g. `5`), snippet duration in seconds (e.g. `20`), and your email address.
3. Submit the form. The page redirects to a success screen while the server downloads songs from YouTube in the background.
4. Each track is sliced into a random snippet, all snippets are merged into `output.mp3`, zipped as `output.zip`, and emailed to the address you provided.

## How to run on localhost

```
pip install flask numpy pandas pytube pydub youtube-search
python SongsMashup.py
```

## Dependencies

flask, numpy, pandas, pytube, pydub, youtube-search, smtplib (standard library)
