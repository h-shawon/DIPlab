import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("2.jpg", cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img,(400, 500))
c = 255
gamma = 2.5
power_img = c * ((img/255)**gamma) # s = c * (r**gamma)

power_img = np.array(power_img, dtype=np.uint8)
h = np.hstack((img, power_img))
cv2.imshow("log transform",h)
cv2.waitKey(0)
cv2.destroyAllWindows()
