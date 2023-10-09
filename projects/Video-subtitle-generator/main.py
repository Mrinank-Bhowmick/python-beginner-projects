import os
from datetime import timedelta
import whisper


def transcribe_audio(path, output_filetype="srt", whisper_model="base"):
    # extract the filename from the path without extension
    filename = os.path.splitext(os.path.basename(path))[0]
    output_filename = os.path.join("SrtFiles", f"{filename}.{output_filetype}")
    # chcek if the output file exists, if it does, append a number to the filename
    if os.path.exists(output_filename):
        i = 1
        while os.path.exists(output_filename):
            output_filename = os.path.join(
                "SrtFiles", f"{filename}({i}).{output_filetype}"
            )
            i += 1
    if output_filetype == "srt":
        # open the output file in write mode
        with open(output_filename, "w", encoding="utf-8") as srtFile:
            srtFile.write("")
        model = whisper.load_model(whisper_model)
        print("Whisper model loaded.")
        transcribe = model.transcribe(audio=path)
        segments = transcribe["segments"]

        for segment in segments:
            startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
            endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
            text = segment["text"]
            segmentId = segment["id"] + 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
            with open(output_filename, "a", encoding="utf-8") as srtFile:
                srtFile.write(segment)
        return srtFile

    elif output_filetype == "json":
        with open(output_filename, "w", encoding="utf-8") as jsonFile:
            jsonFile.write('{\n "captions": [\n')
        model = whisper.load_model(whisper_model)
        print("Whisper model loaded.")
        transcribe = model.transcribe(audio=path)
        segments = transcribe["segments"]
        for segment in segments:
            startTime = timedelta(seconds=int(segment["start"]))
            endTime = timedelta(seconds=int(segment["end"]))
            duration = endTime - startTime  # Calculate the duration
            startTime_str = str(0) + str(startTime) + ",000"
            endTime_str = str(0) + str(endTime) + ",000"
            duration_str = str(0) + str(duration) + ",000"
            text = segment["text"]
            segmentId = segment["id"] + 1
            segment = f"{{\t\n\"id\": {segmentId},\n\"start\": \"{startTime_str}\",\n\"end\": \"{endTime_str}\",\n\"duration\": \"{duration_str}\",\n\"text\": \"{text[1:] if text[0] == ' ' else text}\"\n}},\n"
            with open(output_filename, "a", encoding="utf-8") as jsonFile:
                jsonFile.write(segment)
        # remove the last comma
        with open(output_filename, "rb+") as jsonFile:
            jsonFile.seek(-2, os.SEEK_END)
            jsonFile.truncate()
        with open(output_filename, "a", encoding="utf-8") as jsonFile:
            jsonFile.write("\n]\n}")
        return jsonFile

    elif output_filetype == "txt":
        with open(output_filename, "w", encoding="utf-8") as txtFile:
            txtFile.write("")
        model = whisper.load_model(whisper_model)
        print("Whisper model loaded.")
        transcribe = model.transcribe(audio=path)
        segments = transcribe["segments"]
        for segment in segments:
            startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
            endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
            text = segment["text"]
            segmentId = segment["id"] + 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
            with open(output_filename, "a", encoding="utf-8") as txtFile:
                txtFile.write(segment)
        return txtFile


output_dir = "SrtFiles"
# check if the output directory exists, if it does not, create it
if not os.path.exists(output_dir):
    os.mkdir("SrtFiles")
path = input("Please enter the path of the audio file:")
output_filetype = int(
    input(
        "Please enter the output file type (SRT is selected by default):\n1.SRT\n2.JSON\n3.TXT\n"
    )
)
if output_filetype == 1:
    output_filetype = "srt"
elif output_filetype == 2:
    output_filetype = "json"
elif output_filetype == 3:
    output_filetype = "txt"

whisper_model = int(
    input(
        "Please enter the name of the whisper model you want to use (base is selected by default):\n1.Tiny\n2.Base\n3.Small\n4.Medium\n5.Large\n"
    )
)
if whisper_model == 1:
    whisper_model = "tiny"
elif whisper_model == 2:
    whisper_model = "base"
elif whisper_model == 3:
    whisper_model = "small"
elif whisper_model == 4:
    whisper_model = "medium"
elif whisper_model == 5:
    whisper_model = "large"

srtFilename = transcribe_audio(path, output_filetype, whisper_model)
# extract srt file name from srtFilename
srtFilename = os.path.basename(srtFilename.name)
print(f"Your subtitles are ready. You can find them in {srtFilename}")
