## Example

```text
Please enter the path of the audio file: lecture.mp3
Please enter the output file type (SRT is selected by default):
1.SRT
2.JSON
3.TXT
1
Please enter the name of the whisper model you want to use (base is selected by default):
1.Tiny
2.Base
3.Small
4.Medium
5.Large
2
Whisper model loaded.
Your subtitles are ready. You can find them in lecture.srt
```

The generated `SrtFiles/lecture.srt` file contains timestamped subtitle entries for each spoken segment.

## Required Modules

```
pip install -U openai-whisper
```

It also requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

```
