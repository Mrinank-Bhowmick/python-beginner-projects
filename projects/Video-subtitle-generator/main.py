import os
from datetime import timedelta
import whisper


def transcribe_audio(path):
    model = whisper.load_model("base")  # Change this to your desired model
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe["segments"]

    for segment in segments:
        startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
        endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
        text = segment["text"]
        segmentId = segment["id"] + 1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

        srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
        with open(srtFilename, "a", encoding="utf-8") as srtFile:
            srtFile.write(segment)

    return srtFilename


os.mkdir("SrtFiles")
path = input("Please enter the path of the audio file:")
srtFilename = transcribe_audio(path)
print(f"Your subtitles are ready. You can find them in {srtFilename}")
