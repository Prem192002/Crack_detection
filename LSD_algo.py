import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\univ5.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3,3), 0)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(blur, 50, 250, apertureSize=7)

# Apply LSD algorithm to detect line segments
lsd = cv2.createLineSegmentDetector()
lines, width, prec, nfa = lsd.detect(edges)

# Draw the detected line segments on the original image
for line in lines:
    x1, y1, x2, y2 = map(int, line[0])
    thickness = 2
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), thickness if isinstance(thickness, float) else int(thickness))

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



