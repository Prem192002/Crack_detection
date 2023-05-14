import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\univ5.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(blur, 10, 600, apertureSize=7)

# Apply LSD algorithm to detect line segments
lsd = cv2.createLineSegmentDetector()
lines, width, prec, nfa = lsd.detect(edges)

# Draw the detected line segments on the original image
for i, line in enumerate(lines):
    x1, y1, x2, y2 = map(int, line[0])
    thickness = width[i]
    if thickness >= 3:
        color = (0, 255, 255) # red for cracks with thickness between 5-3
    elif thickness >= 1:
        color = (0, 0, 255) # yellow for cracks with thickness between 3-1
    else:
        color = (0, 255, 0) # green for cracks with thickness less than 1
    cv2.line(img, (x1, y1), (x2, y2), color, 1)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
