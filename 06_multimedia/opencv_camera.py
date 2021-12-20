import cv2
cam = cv2.VideoCapture('output.avi')
if not cam.isOpened():
    print('Camera open failed')
    exit()

#ret, frame = cam.read()
#cv2.imwrite('output.jpg',frame)



while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('frame',frame)

    if cv2.waitKey(10) == 13:
        break

cam.release()
cv2.destroyAllWindows()