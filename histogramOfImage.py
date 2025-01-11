import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

re_size = cv2.resize(image, (400, 600))

img = np.reshape(image, image.shape[0]*image.shape[1])
img = np.sort(img)
result = np.zeros(256)
for i in img:
    result[i] = result[i] + 1

result = result/(400*600)
plt.bar(np.arange(256), result)
plt.show()