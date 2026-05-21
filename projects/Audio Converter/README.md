# audioconverter

Convert audio files with pydub.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pydub.

```bash
pip install pydub
```

## Usage

```bash
python audioconverter.py <path to audio file> <format>
```
Run `ffmpeg -formats` to view supported formats, since Pydub uses ffmpeg.


## Pyodide-runnable

No - uses the pydub package and reads/converts audio files from disk via sys.argv, which is not available in a browser sandbox.
