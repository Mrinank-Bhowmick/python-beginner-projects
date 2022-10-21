import os, sys
from pydub import AudioSegment

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} <audio file> <format>")
    sys.exit(1)

filename = sys.argv[1]
frm = sys.argv[2]

# get absolute file paths
filepath = os.path.abspath(filename)
filebase = os.path.basename(filename)
fileext = filename.split(".")[-1]

print(f"Converting from {fileext} to {frm}")

# only run if converting to a different format
if not (filename.endswith(str("." + frm))):
    track = AudioSegment.from_file(filename, fileext)
    newname = filebase.replace(fileext, frm)

    # save to the same folder as original file
    newpath = filepath.replace(filebase, newname)
    track.export(newpath, format=frm)
    print(f"File saved to {newpath}")
