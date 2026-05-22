# Spotify Player

A command-line Spotify tool that can play a searched song, recommend songs based on three seed tracks, and generate a new playlist similar to an existing one. It also texts the generated playlist link via Twilio.

## Example

```text
Enter a choice: 1
Enter Song Name: Blinding Lights
Would you like to open this song in your browser [yes/no]: yes
✅ Playing Blinding Lights - The Weeknd

Would you like to try again [yes/no]: yes

Enter a choice: 2
Enter song 1: Shape of You
Enter song 2: Perfect
Enter song 3: Photograph

Recommended song: Castle on the Hill - Ed Sheeran
Would you like to play this song [yes/no]: yes
✅ Playing Castle on the Hill - Ed Sheeran
```

## How to run on localhost

```
pip install spotipy colorama twilio
python main.py
```

Configuration values must be placed in `utils/user_secrets.py` (see `utils/user_secrets_example.py`).

## Dependencies

spotipy, colorama, twilio
