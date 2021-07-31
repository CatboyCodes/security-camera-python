import cv2


face_cascade = cv2.CascadeClassifier('face.xml')

cap = cv2.VideoCapture(0)
cam = "Sercurity Cam"
printed = "human has been detected"

while True:
    ret, frame = cap.read()

    frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05,minNeighbors=5, minSize=(30, 30))

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        print(printed)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow(cam, frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows() 