import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("2.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (400, 400))


hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.figure(figsize=(10, 7))
plt.subplot(2,2,1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,2,2)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')


equ = cv2.equalizeHist(img)
hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.subplot(2,2,3)
plt.imshow(equ)
plt.title("Equalized image")
plt.axis('off')

plt.subplot(2,2,4)
plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

plt.tight_layout()
plt.show()