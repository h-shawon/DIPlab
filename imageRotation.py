import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('3.jpg', cv2.IMREAD_GRAYSCALE)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
angle = 45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

plt.figure(figsize=(7,5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title('Rotated Image')
plt.axis('off')

plt.tight_layout()
plt.show()

