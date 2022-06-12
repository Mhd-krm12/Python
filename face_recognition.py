
import cv2
import face_recognition
import time

cap = cv2.VideoCapture(0)
while True:
    
    ret, frame = cap.read()
    tic=time.time()
    frame = cv2.resize(frame,(600,400))
    face_locations= face_recognition.face_locations(frame)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, bottom), (right, top),(0, 0, 255), 2)
      
    toc=time.time()
    fps=1/(toc-tic)
    print(fps)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
