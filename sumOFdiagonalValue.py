import cv2
import numpy as np

image = cv2.imread('M.png', cv2.IMREAD_GRAYSCALE)

diagonals = np.diag(image)

diagonal_sum = np.sum(diagonals)

print("Sum of diagonals:", diagonal_sum)

## Putting the sum value in the middle
mid_row = image.shape[0] // 2
mid_col = image.shape[1] // 2

image[mid_row, mid_col] = np.clip(diagonal_sum, 0, 255)

cv2.imshow("New image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()