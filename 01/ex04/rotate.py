import numpy as np
import cv2
from load_image import ft_load


def rotate():
    """rotate image 90 degrees reverse clockwise"""
    img = ft_load('animal.jpeg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    start_row = 100
    start_col = 450
    cropped_image_2d = \
        gray_img[start_row:start_row + 400, start_col:start_col + 400]
    cropped_image_3d = np.expand_dims(cropped_image_2d, axis=-1)
    print('New shape after slicing: (400, 400, 1) or (400, 400)')
    print(cropped_image_3d)

    n = len(cropped_image_2d)

    rotated_image = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            rotated_image[j][i] = cropped_image_2d[i][j]
    print('New shape after Transpose:', rotated_image.shape)
    print(rotated_image)

    rotated_image = np.array(rotated_image, dtype=np.uint8)

    cv2.imshow('Zoomed Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    rotate()
