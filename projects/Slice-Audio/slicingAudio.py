from pydub import AudioSegment

# Example File path
# filePath = "/Users/dishantnagpal/Desktop/python/exampleAudio.mp3"

# Example Exoprt Path
# exportPath = "/Users/dishantnagpal/Desktop/python/newPortion-1.mp3"

filePath = input("Enter your path to the audio file")  # Enter your file path
exportPath = input("Enter the path you want to save the file at")  # Enter export Path

sound = AudioSegment.from_mp3(
    filePath
)  # Making an executable audio file from the given path

startMin = int(input("Enter Start Minute "))
startSecond = int(input("Enter Start Second "))

endMin = int(input("Enter End Minute "))
endSecond = int(input("Enter End Second "))


startTime = startMin * 60 * 1000 + startSecond * 1000
endTime = endMin * 60 * 1000 + endSecond * 1000


extract = sound[startTime:endTime]  # Extracting sliced Audio


extract.export(
    exportPath, format="mp3"
)  # Saving the final audio file at your export path
