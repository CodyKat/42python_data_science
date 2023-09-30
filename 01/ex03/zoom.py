import cv2
import numpy as np
from load_image import ft_load


def zoom():
    """Zoom on the image"""
    img: np.array = ft_load('animal.jpeg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    start_row = 100
    start_col = 450

    cropped_image_2d = \
        gray_img[start_row:start_row + 400, start_col:start_col + 400]
    print('2d shape : ', cropped_image_2d.shape)
    cropped_image_3d = np.expand_dims(cropped_image_2d, axis=-1)
    print('3d shape : ', cropped_image_3d.shape)
    print(cropped_image_3d)

    cv2.imshow('Zoomed Image', cropped_image_3d)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    zoom()
