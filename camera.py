import cv2
import numpy as np
import math

def calculate_angle(point1_line1, point2_line1, point1_line2, point2_line2):
    # Convert points to vectors
    vector1 = np.array([point2_line1[0] - point1_line1[0], point2_line1[1] - point1_line1[1]])
    vector2 = np.array([point2_line2[0] - point1_line2[0], point2_line2[1] - point1_line2[1]])

    # Calculate the dot product of the vectors
    dot_product = np.dot(vector1, vector2)

    # Calculate the magnitudes of the vectors
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Calculate the cosine of the angle using the dot product and magnitudes
    cos_theta = dot_product / (magnitude1 * magnitude2)

    # Ensure the value is within the range [-1, 1] to avoid errors due to floating-point inaccuracies
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Calculate the angle in radians and then convert to degrees
    angle_radians = math.acos(cos_theta)
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam video capture
cap = cv2.VideoCapture(0)  # 0 for default webcam

# Get the width and height of the video frame
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate the center of the frame
center_of_screen = (frame_width // 2, frame_height // 2)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture image")
        break

    # Convert the frame to grayscale because the face detection algorithm works better on grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a circle at the center of the screen
    cv2.circle(frame, center_of_screen, 5, (0, 255, 0), 2)
    cv2.line(frame, center_of_screen, (frame_width//2, 0), (0, 0, 255), 2)

    if len(faces) > 0:
        # Find the largest face
        largest_face = max(faces, key=lambda rect: rect[2] * rect[3])  # rect[2] * rect[3] is the area (width * height)
        x, y, w, h = largest_face

        # Calculate the center of the face
        center_of_face = (x + w // 2, y + h // 2)

        # Draw a circle at the center of the face
        cv2.circle(frame, center_of_face, 5, (255, 0, 0), 2)

        # Draw the rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Draw a line from the center of the screen to the center of the face
        cv2.line(frame, center_of_screen, center_of_face, (0, 0, 255), 2)

        # Calculate the angle between the line to the top-center of the screen and the line to the face center
        angle_between_lines = int(calculate_angle(center_of_screen, (frame_width // 2, 0), center_of_screen, center_of_face))
        screenx,_ = center_of_screen
        facex,_ = center_of_face
        if screenx > facex:
            angle_between_lines += 90
        print(f"Angle: {angle_between_lines} degrees")

    # Display the resulting frame
    cv2.imshow('Face Tracking with Circles', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
