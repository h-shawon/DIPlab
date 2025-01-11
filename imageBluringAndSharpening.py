import cv2 
import matplotlib.pyplot as plt

image = cv2.imread("5.jpg")
image = cv2.resize(image, (900, 1000))

blur_image = cv2.GaussianBlur(image, (25,25 ), sigmaX=0, sigmaY=0)

sharp_image = cv2.addWeighted(image, 1.5, blur_image, -0.5, 0)

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(blur_image)
plt.title("Blurred Image")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sharp_image)
plt.title("Sharp Image")
plt.axis('off')

plt.tight_layout()
plt.show()
