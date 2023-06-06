import cv2
import numpy as np

# Load the video
video_path = r"D:\coratia\InShot_20230604_204945432.mp4"
cap = cv2.VideoCapture(video_path)

# Check if video capture is successful
if not cap.isOpened():
    print("Error opening video file.")
    exit()

# Create a VideoWriter object to save the output video
output_path = r"D:\coratia\video.mp4"
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

# Process each frame in the video
while True:
    # Read a frame
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (3, 3), 1)

    # Apply Scharr edge detection
    gradient_x = cv2.Scharr(blur, cv2.CV_64F, 1, 0)
    gradient_y = cv2.Scharr(blur, cv2.CV_64F, 0, 1)
    gradient_abs = cv2.addWeighted(cv2.convertScaleAbs(gradient_x), 0.5,
                                   cv2.convertScaleAbs(gradient_y), 0.5, 1)

    # Apply thresholding to detect edges
    edges = cv2.threshold(gradient_abs, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Apply LSD algorithm to detect line segments
    lsd = cv2.createLineSegmentDetector()
    lines, width, prec, nfa = lsd.detect(edges)

    # Draw the detected line segments on the frame
    if lines is not None:
        for i, line in enumerate(lines):
            x1, y1, x2, y2 = map(int, line[0])
            thickness = width[i]

            # Set the color based on crack size
            if thickness > 25:
                color = (0, 0, 255)  # Red for larger cracks
            elif thickness > 10:
                color = (0, 255, 255)  # Yellow for medium cracks
            else:
                color = (0, 255, 0)  # Green for small cracks

            cv2.line(frame, (x1, y1), (x2, y2), color, 1)

    # Display the result
    cv2.imshow("Crack Detection", frame)

    # Write the frame to the output video
    output_video.write(frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
output_video.release()
cv2.destroyAllWindows()
