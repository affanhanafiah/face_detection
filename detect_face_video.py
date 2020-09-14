import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('coba.mp4')
# Membuat frame yang akan direkam
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
total_frame=1
while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('Deteksi Wajah', img)
    # Rekam
    out.write(img)

    total_frame=total_frame+1

    # Stop if escape key is pressed
    # k = cv2.waitKey(1) & 0xff
    # if k==27:
    #     break
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the VideoCapture object
print(total_frame)
cap.release()
out.release()
cv2.destroyAllWindows()