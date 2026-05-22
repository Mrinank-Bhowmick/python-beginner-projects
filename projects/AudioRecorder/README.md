# Audio Recorder

Records audio from the system microphone and saves it to RAW, WAV, AIFF, and FLAC files.

## Example

```text
Listening
```

Speak into the microphone. When you finish, the program saves the recording to
`microphone-results.raw`, `microphone-results.wav`, `microphone-results.aiff`,
and `microphone-results.flac` in the current directory.

## How to run on localhost

```
pip install SpeechRecognition pyaudio
python main.py
```

## Dependencies

- SpeechRecognition
- pyaudio (microphone input backend)
