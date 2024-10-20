import cv2
import numpy as np

# Load the image
image = cv2.imread('0.jpg')

# Convert to grayscale (optional, depends on your image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to get a binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# If contours are found, find the largest contour by area
if contours:
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the moments of the largest contour
    M = cv2.moments(largest_contour)

    # Calculate the center of the contour using the moments
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    # Draw the contour and the center point on the image
    cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 0, 0), -1)
    cv2.putText(image, "Center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the image with the center point marked
    cv2.imshow('Image with Center Point', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No contours found in the image.")
