# PyPhotoshop
Python implementation of image filters

Use Python to adjust brightness and contrast, add blur, and detect edges! Follow along tutorial: https://youtu.be/4ifdUQmZqhM

In order to download this code, either click the green button at the top right and download as ZIP, or use `git clone https://github.com/kying18/pyphotoshop.git`. You will need to `pip install -r requirements.txt` (or use `pip3` if you are getting a module not found error).

In the folder, you will find these files:
- image.py: contains the `Image` class that will read and write the images using the PNG `Writer` and `Reader`
- png.py: pure Python PNG `Reader` and `Writer` classes from Johann C. Rocholl
- transform.py: implemented image filter functions
- transform_empty.py: empty template for image filter functions
