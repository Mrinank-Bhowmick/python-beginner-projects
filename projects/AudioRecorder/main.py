import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening")
    audio = r.listen(source)

# write audio to a RAW file
with open("microphone-results.raw", "wb") as file:
    file.write(audio.get_raw_data())

# write audio to a WAV file
with open("microphone-results.wav", "wb") as file:
    file.write(audio.get_wav_data())

# write audio to an AIFF file
with open("microphone-results.aiff", "wb") as file:
    file.write(audio.get_aiff_data())

# write audio to a FLAC file
with open("microphone-results.flac", "wb") as file:
    file.write(audio.get_flac_data())
