This python script is used for taking images from your webcam and saving it on your local device. Path to the folder can be specified using the following command:

> python3 take_pictures_from_webcam.py --directory pathname

The default path would be your current directory.  

You can also give name to your image using following command:
> python3 take_pictures_from_webcam.py --name ImageName

## Example

```text
python3 WebcamImage.py --directory /home/user/photos --name photo
```

1. A live webcam preview window labelled "frame" opens at 600×600 pixels.
2. Press **Space** to capture the current frame — it is saved as `photo0.jpg` in `/home/user/photos` and the terminal prints `got photo0`.
3. Press **Space** again to save `photo1.jpg`, and so on.
4. Press **q** to close the window and exit.
