## A computer vision system that can automatically detect driver drowsiness in a real-time video stream and then play an alarm if the driver appears to be drowsy.

We already did an eye-blink detector python project earlier, using Facial landmarks.
Now we will extend this feature to determine for how long does the eye of a person is closed. If the eyes are closed for a certain time, and the pattern is recurring, we'll assume the driver is dozing off and the alarm will be played.

We'll use librarries like openCV, dlib 

## Drowsiness detector algorithm

<li>If a face is found , we'll apply the facial landmark detection and extract the eye region

<li> When the eye is found, we'll compute the eye aspect ratio(EAR) to determine whether eyes are closed or not.</li>

<li> If the EAR indicates that the eyes have been closed for a sufficiently long amount of time, we'll play the alarm</li>

### Explaining the Code

We are using the SciPy package, so we can compute the Euclidean distance between the facial landmark points in the EAR 
The imutils package make working with OpenCV much better

You can install the packages by

 `pip install <package-name>` \
 `pip install --upgrade <package-name>`

If you want to install imutils, type this in the terminal

`pip install --upgrade imutils` 

We are also using the "Thread" class, so we can play our alarm in separate thread
In order to play the MP3/WAV music file as an alarm, we need the "playsound" library

`pip install playsound`

(Mac users also need to import pyobj)

The return value of the eye aspect ratio will be approximately constant when the eye is open. The value will then rapid decrease towards zero during a blink.

If the eye is closed, the eye aspect ratio will again remain approximately constant, but will be much smaller than the ratio when the eye is open.


## Command Line Argument

<li>--shape-predictor : This is the path to dlib’s pre-trained facial landmark detector. You can download the detector along with the source code to this tutorial by using the “Downloads” section at the bottom of this blog post.
<li>--alarm : Here you can optionally specify the path to an input audio file to be used as an alarm.
<li>--webcam : This integer controls the index of your built-in webcam/USB camera.</li>



















