# Voice-to-Text

Captures audio from the microphone and converts it to text using Google's speech recognition service.

## How to run

```bash
pip install SpeechRecognition googletrans pyaudio
python main.py
```

## Dependencies

- SpeechRecognition
- googletrans
- pyaudio (microphone access)

## Pyodide-runnable

No — it requires microphone hardware access and network speech-recognition calls, neither available in Pyodide.
