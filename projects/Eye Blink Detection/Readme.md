## Eye blink detection with OpenCV, Python, and dlib

Here we are going to build upon this knowledge and develop a computer vision application that is capable of detecting and counting blinks in video streams using facial landmarks and OpenCV.

To build our blink detector, we’ll be computing a metric called the eye aspect ratio (EAR), introduced by Soukupová and Čech in their 2016 paper

Unlike traditional image processing methods for computing blinks which typically involve some combination of:

<li>Eye localization.
<li>Thresholding to find the whites of the eyes.
<li>Determining if the “white” region of the eyes disappears for a period of time (indicating a blink).

The eye aspect ratio is instead a much more elegant solution that involves a very simple calculation based on the ratio of distances between facial landmarks of the eyes.

This method for eye blink detection is fast, efficient, and easy to implement.

## Example

```text
$ python main.py --shape-predictor shape_predictor_68_face_landmarks.dat \
                 --video sample_video.mp4

[INFO] loading facial landmark predictor...
[INFO] starting video stream thread...
```

1. An OpenCV window opens titled “Frame” showing the video with green convex-hull outlines drawn around both eyes.
2. The top-left corner displays the running blink count, e.g. `Blinks: 3`.
3. The top-right corner shows the current EAR value, e.g. `EAR: 0.31`.
4. Each time the EAR drops below 0.3 for 3 consecutive frames, the blink counter increments.
5. Press `q` to stop playback and close the window.

### Understanding the “eye aspect ratio” (EAR)

In terms of blink detection, we are only interested in two sets of facial structures — the eyes.

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the remainder of the region.
