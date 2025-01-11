import cv2
import numpy as np

image = cv2.imread('M.png', cv2.IMREAD_GRAYSCALE)
boundary_pixels = np.hstack([image[0, :], image[-1, :], image[:, 0], image[:, -1]])
boundary_sum = np.sum(boundary_pixels)

print("Sum of boundary pixel values:", boundary_sum)


## Putting the sum value in the middle
mid_row = image.shape[0] // 2
mid_col = image.shape[1] // 2

image[mid_row, mid_col] = np.clip(boundary_sum, 0, 255)

cv2.imshow("New image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()