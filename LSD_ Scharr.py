import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\sample4.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3,3), 1)

# Apply Scharr edge detection
gradient_x = cv2.Scharr(blur, cv2.CV_64F, 1, 0) 
gradient_y = cv2.Scharr(blur, cv2.CV_64F, 0, 1)
gradient_abs = cv2.addWeighted(cv2.convertScaleAbs(gradient_x), 0.5,
                               cv2.convertScaleAbs(gradient_y), 0.5, 1)

# Apply thresholding to detect edges
edges = cv2.threshold(gradient_abs, 50, 500, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Apply LSD algorithm to detect line segments
lsd = cv2.createLineSegmentDetector()
lines, width, prec, nfa = lsd.detect(edges)

# Draw the detected line segments on the original image
for i, line in enumerate(lines):
    x1, y1, x2, y2 = map(int, line[0])
    thickness = width[i]
    
    # Set the color based on crack size
    if thickness > 3:
        color = (0, 0, 255)  # Red for larger cracks
    elif thickness > 1:
        color = (0, 255, 255)  # Yellow for medium cracks
    else:
        color = (0, 255, 0)  # Green for small cracks
    
    cv2.line(img, (x1, y1), (x2, y2), color, 2)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
