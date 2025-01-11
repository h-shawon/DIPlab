import cv2
import numpy as np
img1 = cv2.imread("2.jpg")
img2 = cv2.imread("4.jpg")
re_image1 = cv2.resize(img1, (500, 300))
re_image2 = cv2.resize(img2, (500, 300))
h = np.hstack((re_image1, re_image2))
cv2.imshow("Merged Image", h)
cv2.waitKey(0)
cv2.destroyAllWindow()