# CodSoft AI Internship – Task 5
# Face Detection using Haar Cascade
# Created by Payal Sonwaniya

import cv2

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load the image
image_path = "face.jpg"  # Change this to your actual image name
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show the result
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
