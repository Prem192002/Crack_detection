import cv2
import numpy as np


img = cv2.imread(r"C:\Users\Prem\OneDrive\Pictures\crack_road2.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=5)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()