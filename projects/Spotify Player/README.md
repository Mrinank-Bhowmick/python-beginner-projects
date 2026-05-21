# Spotify Player

A command-line Spotify tool that can play a searched song, recommend songs based on three seed tracks, and generate a new playlist similar to an existing one. It also texts the generated playlist link via Twilio.

## How to run

```
pip install spotipy colorama twilio
python main.py
```

Configuration values must be placed in `utils/user_secrets.py` (see `utils/user_secrets_example.py`).

## Dependencies

spotipy, colorama, twilio

## Pyodide-runnable

No — it calls the Spotify Web API and Twilio API over the network, opens a browser, and clears the terminal with `os.system`.
