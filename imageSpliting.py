import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("5.jpg")

image = cv2.resize(image, (800, 900))
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width, dim = image.shape

# split int 4 parts
top_left = image_rgb[0:height//2, 0:width//2]
top_right = image_rgb[0:height//2, width//2:width]
bottom_left = image_rgb[height//2:height, 0:width//2]
bottom_right = image_rgb[height//2:height, width//2:width]

top = np.hstack((top_left, top_right))
bottom = np.hstack((bottom_left, bottom_right))
merged_image = np.vstack((top, bottom))

plt.subplot(2, 3, 1)
plt.imshow(top_left)
plt.title("Top Left")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(top_right)
plt.title("Top Right")
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(bottom_left)
plt.title("Bottom Left")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(bottom_right)
plt.title("Bottom Right")
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(merged_image)
plt.title("Merged Image")
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

plt.tight_layout()
plt.show()