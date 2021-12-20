import cv2
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print('Camera open failed')
    exit()

#ret, frame = cam.read()
#cv2.imwrite('output.jpg',frame)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))


while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('frame',frame)
    out.write(frame)
    if cv2.waitKey(10) == 13:
        break

cam.release()
out.release()
cv2.destroyAllWindows()