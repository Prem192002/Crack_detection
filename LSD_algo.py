import cv2

# Load the image
img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\crack_road2.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
blur = cv2.medianBlur(gray, 5)

# Apply morphological opening to fill small gaps in the edges
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(opening, 50, 150, apertureSize=3)

# Apply LSD algorithm to detect line segments
lsd = cv2.createLineSegmentDetector()
lines, _, _, _ = lsd.detect(edges)

# Filter out short line segments
min_length = 30
lines = [line for line in lines if cv2.norm(line[0][:2] - line[0][2:]) >= min_length]

# Merge overlapping line segments
threshold_overlap = 10
merged_lines = []
while len(lines) > 0:
    line = lines.pop(0)[0]
    overlap = False
    for i, merged_line in enumerate(merged_lines):
        dist = cv2.norm(line[:2] - merged_line[-2:])
        if dist < threshold_overlap:
            merged_lines[i] = np.concatenate((merged_line, line[2:]))
            overlap = True
            break
    if not overlap:
        merged_lines.append(line)

# Draw the detected line segments on the original image
for line in merged_lines:
    x1, y1, x2, y2 = map(int, line)
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the result
cv2.imshow("Crack Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
