This python script is used for taking images from your webcam and saving it on your local device. Path to the folder can be specified using the following command:

> python3 take_pictures_from_webcam.py --directory pathname

The default path would be your current directory.  

You can also give name to your image using following command:
> python3 take_pictures_from_webcam.py --name ImageName

## Pyodide-runnable

No — it captures frames from a webcam with OpenCV (`cv2.VideoCapture`) and shows GUI windows, neither of which works in the browser sandbox.
