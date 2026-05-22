# Slice Audio from any mp3 file

We all want only a portion form a particular audio file. This python scrip does the same for you in few very easy steps.

Only have to enter few things to get started and the rest is magic.

What all do you have to enter?

1.) Your file Path - Where your initial audio file(mp3) is located.
2.) Your export Path - Where you want to save your resultant sliced audio file to be saved.
3.) Start Minute - From what minute into the audio you want to slice from
4.) Start Second - From what second after the start minute you want to slice from 
5.) End Minute - Till what minute you want the final audio to be.
6.) End Second - Till what second of the End minute you want to final audio to be.

## Example

```text
Enter your path to the audio file/home/user/music/song.mp3
Enter the path you want to save the file at/home/user/music/clip.mp3
Enter Start Minute 1
Enter Start Second 30
Enter End Minute 2
Enter End Second 15
```

The script extracts the segment from 1:30 to 2:15 of `song.mp3` and saves it as `clip.mp3` at the export path.

# Requirements

Clone Repo
You need to intall pydub library for this script to run.
You can use pip - pip install pydub
More information on pydub here - https://pypi.org/project/pydub/
Use the python script slicingAudio.py
