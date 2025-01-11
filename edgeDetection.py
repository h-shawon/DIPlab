import cv2 

image = cv2.imread("1.jpg")
image = cv2.resize(image, (500, 500))

new_image = cv2.Canny(image, 150, 150, L2gradient=True)

cv2.imshow("Original", image)
cv2.imshow("Canny Edge Detection", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()