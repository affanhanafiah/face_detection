import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test3.jpg')
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

# Convert into grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(resized, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', resized)
cv2.waitKey()
