# PDF Text-to-Speech Reader

This Python script uses `pyttsx3` and `PyPDF2` to read the text content of a PDF file and convert it to speech using text-to-speech synthesis. It allows for playback of the PDF content and provides a hotkey ("q") to stop the playback at any time.

## Dependencies

- `pyttsx3`: A text-to-speech conversion library in Python.
- `PyPDF2`: A library to handle PDF files.
- `keyboard`: A library to listen for keyboard events.

## Usage

1. Install the required libraries using pip:

```bash
pip install pyttsx3 PyPDF2 keyboard
```

2. Run the script and provide the PDF file name when prompted:

```bash
python pdf_text_to_speech.py
```

3. Press 'q' during playback to stop the text-to-speech playback.

## How it Works

The script takes a PDF file as input, extracts the text content from each page, and uses `pyttsx3` to read it out loud. The playback can be stopped at any time by pressing the 'q' key.
