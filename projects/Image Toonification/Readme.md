# Image Toonifier
**An App to toonify images in PC. Have Fun Toonifying yourselves.**

Just apply your images the cartoon effect and Enjoy!!

### Tools/FrameWorks used:
 - opencv-python
 - numpy

## Example

1. Place your input image as `images/filename.jpg` inside the project folder.
2. Run `python3 main.py`.
3. The script applies K-Means color quantization (49 colors), detects edges with adaptive thresholding, and combines them with a bilateral filter to produce a cartoon-style image saved as `images/filename.png`.

## Installation
Simple, Just clone this repository to your local storage and run the below command.
` pip install -r requirements.txt `

## Execution
 - Place your images in the images/Folder

 - Run the below command in command prompt or terminal.
`python3 main.py`

### If something does not work try changing the inner values such as blur value and line size. It should work now.
