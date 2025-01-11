import cv2
import matplotlib.pyplot as plt

img = cv2.imread("5.jpg", 0)
gray = cv2.resize(img, (400, 400))

img1 = cv2.imread("5.jpg")
img1 = cv2.resize(img1, (400, 400))
clr = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

gray_negative = abs(255 - gray)
clr_negative = abs(255 - clr)

plt.subplot(2, 2, 1)
plt.title("Color")
plt.imshow(clr)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Grayscale")
plt.imshow(gray)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Color Negative")
plt.imshow(clr_negative)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Grayscale Negative")
plt.imshow(gray_negative)
plt.axis('off')

plt.show()