import cv2
import numpy as numpy
import time

# import face_recognition


def face_cap():
    cap = cv2.VideoCapture(0)


    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    captured = False
    name = input("Enter your name: ")
    count = 1;


    while captured == False:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        frame_tx = int(width/4)
        frame_ty = int(height/6)

        frame_bx = int(width/2 + width/4)
        frame_by = int(height/2 + height/4)


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            # cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            
            if x > frame_tx and y > frame_ty and (x+w) < frame_bx and (y+h) < frame_by:
                font = cv2.FONT_HERSHEY_SIMPLEX
                img = cv2.putText(frame, 'Capture!', (frame_bx, height-10), font, 1, (0,0,0), 4, cv2.LINE_AA)
                cv2.imwrite('faces/'+name + str(count) + '.jpg', img)
                count = count+1
                time.sleep(1)
                if count > 5:
                    captured = True
                

        cv2.rectangle(frame, (frame_tx, frame_ty), (frame_bx, frame_by), (0,0,0), 5)
        
        cv2.imshow('Image Capture', frame)

        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

face_cap()




