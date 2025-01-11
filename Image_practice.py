## Open and Show
import cv2
img = cv2.imread("1.jpg")
img = cv2.resize(img, (300,400))
cv2.imshow("first Image", img)

cv2.waitKey(0)
cv2.destroyWindow()

