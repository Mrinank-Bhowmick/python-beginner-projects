import moviepy.editor
from tkinter.filedialog import *
from tkinter import *
window=Tk()
# Set the size of the tkinter window
window.geometry("700x350")
window.title("PythonGeeks")#give title to the window
Label(window, text="VIDEO TO AUDIO CONVERTER",bg='orange', font=('Calibri 15')).pack()# a label
Label(window, text="Choose a File ").pack()
pathlab = Label(window)
pathlab.pack()
#creating buttons
Button(window,text='browse',command=browse).pack()
Button(window,text='SAVE',command=save).pack()
def browse():#browsing function
    global video#global variable
    video = askopenfilename()
    video = moviepy.editor.VideoFileClip(video)
    pathlab.config(text=video)#configure method
def save():
    audio = video.audio#convert to audio
    audio.write_audiofile("sample.wav")#save as audio
    Label(window, text="Video Converted into Audio and Saved Successfully",bg='blue', font=('Calibri 15')).pack()
  # a label

