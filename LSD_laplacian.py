import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\sample4.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Laplacian edge detection
laplacian = cv2.Laplacian(blur, cv2.CV_64F)

# Convert the Laplacian result to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Apply thresholding to detect edges
edges = cv2.threshold(laplacian, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# Apply LSD algorithm to detect line segments
lsd = cv2.createLineSegmentDetector()
lines, width, prec, nfa = lsd.detect(edges)

# Draw the detected line segments on the original image
for i, line in enumerate(lines):
    x1, y1, x2, y2 = map(int, line[0])
    thickness = width[i]
    if thickness >= 1:
        color = (0, 0, 255) # red for cracks with thickness between 5-3
    elif thickness >= 0:
        color = (0, 255, 255) # yellow for cracks with thickness between 3-1
    else:
        color = (0, 255, 0) # green for cracks with thickness less than 1
    cv2.line(img, (x1, y1), (x2, y2), color, 2)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
