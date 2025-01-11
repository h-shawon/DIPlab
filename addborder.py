import cv2
import numpy as np

img = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (300, 400))
img1 = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, value = 2)
img1 = cv2.resize(img1,(300, 400))
h = np.hstack((img, img1))
cv2.imshow("Image", h)
cv2.waitKey(0)
cv2.destroyAllWindows()