import cv2
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print('Camera open failed')
    exit()

#ret, frame = cam.read()
#cv2.imwrite('output.jpg',frame)



while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edged_frame = cv2.Canny(frame,50,100)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray_frame)
    cv2.imshow('edge',edged_frame)
    if cv2.waitKey(10) == 13:
        break

cam.release()
cv2.destroyAllWindows()