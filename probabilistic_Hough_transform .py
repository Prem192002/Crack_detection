import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\sample4.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3,3), 2)

# Apply morphological gradient to enhance cracks
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30,30))
gradient = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)

# Apply Scharr edge detection to the gradient image
gradient_x = cv2.Scharr(gradient, cv2.CV_64F, 1, 0)
gradient_y = cv2.Scharr(gradient, cv2.CV_64F, 0, 1)
gradient_abs = cv2.addWeighted(cv2.convertScaleAbs(gradient_x), 0.5,
                               cv2.convertScaleAbs(gradient_y), 0.5, 0)

# Apply thresholding to detect edges
edges = cv2.threshold(gradient_abs, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform morphological closing
kernel = np.ones((5,5), np.uint8)
edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Apply Hough Line Transform for line segment detection
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)

# Draw the detected line segments on the original image
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        color = (0,255,0)  # Red color for all cracks
        cv2.line(img, (x1, y1), (x2, y2), color, 1)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
