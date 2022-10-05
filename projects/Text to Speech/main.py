from gtts import gTTS
import os

mytext = "Hacktoberfest"
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("result.mp3")
os.system("result.mp3")
