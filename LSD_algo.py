import cv2

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\crack_road3.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(blur, 50, 150, apertureSize=3)

# Apply LSD algorithm to detect line segments
lsd = cv2.createLineSegmentDetector()
lines, width, prec, nfa = lsd.detect(edges)

# Draw the detected line segments on the original image
for line in lines:
    x1, y1, x2, y2 = map(int, line[0])
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
