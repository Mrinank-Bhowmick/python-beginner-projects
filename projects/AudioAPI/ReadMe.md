# Unofficial Whisper API

## Overview

Welcome to the Unofficial Whisper API documentation. This API allows you to utilize OpenAI's Whisper, a versatile speech recognition model trained on vast amounts of multilingual data, without the need for OpenAI API credits. With the Unofficial Whisper API, you can convert audio files into text transcripts with ease.

## Requirements

Before using the Unofficial Whisper API, ensure you have the following prerequisites:

1. **Python 3.x**: Make sure you have Python 3.x installed on your system.

2. **OpenAI's Whisper**: Install OpenAI's Whisper model on your system. You can find installation instructions on the [OpenAI Whisper GitHub repository](https://github.com/openai/whisper).

3. **Python's Flask**: Install Flask, a micro-web framework for Python, to run the API. You can install Flask using pip:

   ```bash
   pip install Flask

## Example

1. Start the server by running `python transcription.py`. Flask listens on
   `http://localhost:5000`.
2. From another terminal, send an audio file with:
   ```
   curl -X POST -F "audio=@recording.mp3" http://localhost:5000/transcribe
   ```
3. The server loads the Whisper model, transcribes the audio, and returns a
   `subtitles.vtt` file as a download containing timestamped transcript
   segments, e.g.:
   ```
   WEBVTT

   1
   0:00:00.000 --> 0:00:04.000
   Hello, welcome to the demonstration.
   ```

## Getting Started

1. Clone the repository
2. Run transcription.py
3. Open a new terminal, run this command - curl -X POST -F "audio=@C:path_to_your_audio_file" http://localhost:5000/transcribe


## Output Formats

The Unofficial Whisper API provides transcription output in various formats:

    Text: The transcribed text as a plain text string.
    VTT (WebVTT): Transcribed text with timestamps in the WebVTT format for easy integration with video players.
    SRT (SubRip): Transcribed text with timestamps in the SubRip format, suitable for subtitles.
