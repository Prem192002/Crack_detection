import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\univ5.jpg")

# Apply Bilateral Filter to reduce noise while preserving edges
blur = cv2.bilateralFilter(img, 9, 75, 75)

# Convert the image to grayscale
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(gray, 50, 150)

# Apply Probabilistic Hough Transform to detect line segments
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=10, maxLineGap=20)

# Draw the detected line segments on the original image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
