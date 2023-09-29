import numpy as np
import cv2
from load_image import ft_load

img = ft_load('animal.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Assume we want to zoom into the center of the image
start_row = 100
start_col = 450
cropped_image = gray_img[start_row:start_row + 400, start_col:start_col + 400]

n = len(cropped_image)

rotated_image = np.zeros((n, n))

for i in range(n):
	for j in range(n):
		rotated_image[j][i] = cropped_image[i][j]
print(rotated_image)

rotated_image = np.array(rotated_image, dtype=np.uint8)

cv2.imshow('Zoomed Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()