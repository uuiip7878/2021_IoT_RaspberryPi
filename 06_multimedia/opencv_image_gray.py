import cv2

img = cv2.imread('testjpg.jpeg')
#img2 = cv2.resize(img,(600,400))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('testjpg', img)
cv2.imshow('gray',gray)

while True:
    if cv2.waitKey(0) == 13:
        break

cv2.imwrite('testgray.jpg',gray)

cv2.destroyAllWindows()

