# audioconverter

Convert audio files with pydub.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pydub.

```bash
pip install pydub
```

## Example

```text
$ python audioconverter.py song.mp3 wav
Converting from mp3 to wav
File saved to /home/user/music/song.wav
```

## Usage

```bash
python audioconverter.py <path to audio file> <format>
```
Run `ffmpeg -formats` to view supported formats, since Pydub uses ffmpeg.
