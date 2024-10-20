import cv2
import time
import os
import numpy as np
class ColorDotTracker:
    def __init__(self, lower_color_range, upper_color_range):
        self.lower_color_range = np.array(lower_color_range)
        self.upper_color_range = np.array(upper_color_range)

    def find_dot_center(self, image_path):
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to load image from path: {image_path}")
            return None

        # Convert the image to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Create a mask for the specific color of the dot
        mask = cv2.inRange(hsv, self.lower_color_range, self.upper_color_range)

        # Find contours of the masked image
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour (assuming the dot is the largest blob)
            largest_contour = max(contours, key=cv2.contourArea)

            # Calculate the center of the contour using moments
            M = cv2.moments(largest_contour)
            if M["m00"] > 0:
                center_x = int(M["m10"] / M["m00"])
                center_y = int(M["m01"] / M["m00"])

                # Draw a circle at the center of the dot
                cv2.circle(image, (center_x, center_y), 5, (0, 255, 0), -1)  # Green dot for center

                # Display the image with the center marked
                cv2.imshow("Dot Center", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                return (center_x, center_y)
        else:
            print("No dot found.")
            return None

# Define the color range for the dot (example: red dot in HSV)
# You can adjust these values to match the color of your dot
lower_red = [0, 100, 100]    # Lower bound for the color (H, S, V)
upper_red = [10, 255, 255]   # Upper bound for the color (H, S, V)

# Initialize the color dot tracker with the red color range
dot_tracker = ColorDotTracker(lower_red, upper_red)

# Find and track the center of the colored dot in an image
center = dot_tracker.find_dot_center('0.jpg')

#img = cv2.imread(cv.samples.findFile("IMG_7252.jpg"))
cam = cv2.VideoCapture(1)

#4800 steps is 3mm about
frameno = 0
changeCenter = (0,0)
while True:
    ret, frame = cam.read()
    if ret:
        name = str(frameno) + '.jpg'
        print ('new frame captured...' + name)

        cv2.imwrite(name, frame)
        frameno += 1
    #cv2.imshow('video', frame)

    k = cv2.waitKey(1)

    trueCenter = dot_tracker.find_dot_center('0.jpg')
    center = dot_tracker.find_dot_center(name)
    changeCenter = ((center[0] - trueCenter[0]),(center[1] - trueCenter[1]))
    print(changeCenter)
    time.sleep(5)
cv2.imwrite("Test.jpg", img)
cam.release()
cv2.destroyAllWindows()

