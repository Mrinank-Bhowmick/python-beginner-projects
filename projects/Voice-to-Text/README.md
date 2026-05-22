# Voice-to-Text

Captures audio from the microphone and converts it to text using Google's speech recognition service.

## Example

```text
Say something!
Recognising
hello how are you
```

The script listens for up to 8 seconds of speech, sends it to Google's speech recognition service, and prints the recognised text in lowercase. If the audio is unclear it prints `Could not understand audio`.

## How to run on localhost

```bash
pip install SpeechRecognition googletrans pyaudio
python main.py
```

## Dependencies

- SpeechRecognition
- googletrans
- pyaudio (microphone access)
