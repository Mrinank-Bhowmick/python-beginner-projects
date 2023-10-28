import cv2
import os
import numpy as np
# Input and output folders
input_folder = "input"
output_folder = "output"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to process an image
def process_image(filename):
    # Read the image
    img = cv2.imread(filename)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the image to make black figures on a white background
    inverted = cv2.bitwise_not(gray)

    # Apply thresholding to segment the black figures (adjust threshold value as needed)
    _, thresh = cv2.threshold(inverted, 128, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the calculations for each black figure on the image
    img_processed = img.copy()
    for contour in contours:
        # Calculate the minimum enclosing circle
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Calculate the surface area
        area = cv2.contourArea(contour)

        # Calculate the major axis as the longest distance between any two points
        #points = contour.squeeze()
        #distances = [((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5 for p1 in points for p2 in points]
        #major_axis = max(distances)
        # Calculate the major axis points
        points = contour.squeeze()
        max_distance = 0
        major_axis_points = None
        for i, p1 in enumerate(points):
            for p2 in points[i + 1:]:
                distance = np.linalg.norm(p1 - p2)
                if distance > max_distance:
                    max_distance = distance
                    major_axis_points = p1, p2

        # Draw a line representing the major axis
        if major_axis_points is not None:
            p1, p2 = major_axis_points
            cv2.line(img_processed, tuple(p1), tuple(p2), (0, 0, 255), 2)  # Red line
        # Calculate the perimeter of the contour
        perimeter = cv2.arcLength(contour, closed=True)

        # Calculate the centroid of the contour
        M = cv2.moments(contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        centroid = (cx, cy)

        # Draw the minimum enclosing circle
        cv2.circle(img_processed, center, radius, (0, 0, 255), 2)  # Red circle
        # Draw a marker at the centroid
        cv2.circle(img_processed, centroid, 5, (0, 0, 255), -1)  # Red circle


        # Display the calculations as text
        cv2.putText(img_processed, f"Total surface area: {area:.2f}", (cx - 40, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(img_processed, f"Total Perimeter: {perimeter:.2f}", (cx - 60, cy + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(img_processed, f"Centroid: ({cx},{cy})", (cx - 40, cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(img_processed, f"Major Axis Length: {max_distance:.2f}", (cx - 60, cy + 60),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)

    # Save the processed image with calculations
    output_filename = os.path.join(output_folder, os.path.basename(filename))
    cv2.imwrite(output_filename, img_processed)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png")):
        input_image_path = os.path.join(input_folder, filename)
        process_image(input_image_path)

print("Processing complete.")
