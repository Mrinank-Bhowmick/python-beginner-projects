## Eye blink detection with OpenCV, Python, and dlib

Here we are going to build upon this knowledge and develop a computer vision application that is capable of detecting and counting blinks in video streams using facial landmarks and OpenCV.

To build our blink detector, we’ll be computing a metric called the eye aspect ratio (EAR), introduced by Soukupová and Čech in their 2016 paper

Unlike traditional image processing methods for computing blinks which typically involve some combination of:

<li>Eye localization.
<li>Thresholding to find the whites of the eyes.
<li>Determining if the “white” region of the eyes disappears for a period of time (indicating a blink).

The eye aspect ratio is instead a much more elegant solution that involves a very simple calculation based on the ratio of distances between facial landmarks of the eyes.

This method for eye blink detection is fast, efficient, and easy to implement.

### Understanding the “eye aspect ratio” (EAR)

In terms of blink detection, we are only interested in two sets of facial structures — the eyes.

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the remainder of the region.






