import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("M.png")
image = cv2.resize(image, (500, 500))

matrix = np.ones((20,20), dtype=np.int8)
# print(matrix)
erosion = cv2.erode(image, matrix, iterations=1)
dilation = cv2.dilate(image, matrix, iterations=1)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(erosion)
plt.title("Erosion Image")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dilation)
plt.title("Dilation Image")
plt.axis('off')

plt.tight_layout()
plt.show()