import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("3.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (800, 900))

c = 255/np.log(1 + np.max(img))

log_img = c * np.log(img + 1)  # formula s = c * log(r + 1)

log_img = np.array(log_img, dtype=np.uint8)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Main Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(log_img)
plt.title("Logarithmic Image")
plt.axis("off")

plt.show()