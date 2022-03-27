import cv2
import numpy as np
from datetime import datetime, timedelta
from speak import say


#path for face cascade, path where it is stored specific classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


def say_hello():
    #print('Hello!')
    say('I see you, baby!')


detected_face_time = datetime.now()
detected_nobody_time = datetime.now()
delta_face = 0
delta_nobody = 0

def detect_entry(face_in_cam):
    if face_in_cam:
        global detected_face_time
        global detected_nobody_time
        delta_face = datetime.now() - detected_face_time
        if delta_face > timedelta(seconds=2):
            
            detected_face_time = datetime.now()
            if (detected_face_time - detected_nobody_time) < timedelta(seconds=2):
                say_hello()

    else: 
        delta_nobody = datetime.now() - detected_nobody_time
        if delta_nobody > timedelta(seconds=2):
            print('nobody')
            detected_nobody_time = datetime.now()

# imgfile_name = 'images/im01.jpg'
# img = cv2.imread(imgfile_name, 0) # -1 unchanged, 0- gray
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) 
# #draw rectangle over image
# img = cv2.rectangle(img, (300, 300), (200, 200), (134, 56, 132), 6)

# cv2.imshow('Image', img)

# cv2.waitKey(0) #time to display, 0 - wait for key
# cv2.destroyAllWindows()

# print(img.shape) #2d array for gray, 3d arr for color rgb


# video from camera 0
cap = cv2.VideoCapture(0) 

while True:
    face_in_cam = False
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),3)

        roi_gray = gray[y:y+w,x:x+w]
        roi_color = frame[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
        face_in_cam = True

    detect_entry(face_in_cam)
        

    cv2.imshow('frame',frame)

    cv2.imshow('Frame', frame)#color
    #cv2.imshow('Gray', gray)
    #ord(char) takes a char as a parameter and returns its ASCII value.
    if (cv2.waitKey(1)==ord('e')):  #press key e to escape
        break
cap.release()
cap.destroyAllWindows()