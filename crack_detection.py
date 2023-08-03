import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\sample4.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3,3), 2)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(blur, 40,400, apertureSize=3)

# Apply Hough transform to detect lines
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)

# Draw the detected lines on the original image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 250, 255), 1)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
