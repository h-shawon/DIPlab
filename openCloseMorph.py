import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("Mopen.jpg")
image2 = cv2.imread("Mclose.jpg")

matrix = np.ones((10,10), dtype=np.int8)

openimg = cv2.morphologyEx(image1, cv2.MORPH_OPEN, matrix, iterations = 1)
closeimg = cv2.morphologyEx(image2, cv2.MORPH_CLOSE, matrix, iterations = 1)

plt.figure(figsize=(10,7))
plt.subplot(2, 2, 1)
plt.imshow(image1)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(openimg)
plt.title("Opened Image")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(image2)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(closeimg)
plt.title("Closed Image")
plt.axis('off')

plt.tight_layout()
plt.show()