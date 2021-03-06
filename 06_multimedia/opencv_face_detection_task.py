import cv2
cam = cv2.VideoCapture(0)

face_c = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

if not cam.isOpened():
    print('Camera open failed')
    exit()


try:
    while True:
        ret,frame = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_c.detectMultiScale(gray)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('frame',frame)
        if cv2.waitKey(10) == 27:
             break
finally:
    cam.release()
    cv2.destroyAllWindows()
        