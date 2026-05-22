# Text-to-Speech

- This python script basically takes text from user as input and gives output in form of a voice.
- Uses Google Translate Text to Speech API.

## Example

```text
python main.py
```

The script converts the text `"Hacktoberfest"` to speech using the gTTS library,
saves it as `result.mp3` in the current directory, and opens the file in the
system's default audio player so the spoken word is heard immediately.

### Note:

- Output is available on an audio player.

### Dependencies:

- gTTS
- os
