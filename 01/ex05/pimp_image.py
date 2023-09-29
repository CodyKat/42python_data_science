import cv2
from numpy import array
import numpy as np


def ft_invert(array) -> array:
    print('The shape of image is: ', array.shape)
    copy_array = np.copy(array)
    for i in range(len(copy_array)):
        for j in range(len(copy_array[i])):
            copy_array[i][j] = 255 - copy_array[i][j]
    print(copy_array)
    print('Inverts the clolor of the images received')
    cv2.imshow('Inverted Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Inverted Image')
    return copy_array


ft_invert.__doc__ = "invert the color of the image"


def ft_red(array) -> array:
    print('The shape of image is: ', array.shape)
    copy_array = np.copy(array)
    copy_array[:, :, 0] = 0
    copy_array[:, :, 1] = 0
    print(copy_array)
    print('only red clolor of the images received')
    cv2.imshow('Red Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Red Image')
    return copy_array


ft_red.__doc__ = "show only red color of the image"


def ft_green(array) -> array:
    print('The shape of image is: ', array.shape)
    copy_array = np.copy(array)
    copy_array[:, :, 0] = 0
    copy_array[:, :, 2] = 0
    print(copy_array)
    print('only green clolor of the images received')
    cv2.imshow('Green Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Green Image')
    return copy_array


ft_green.__doc__ = "show only green color of the image"


def ft_blue(array) -> array:
    print('The shape of image is: ', array.shape)
    copy_array = np.copy(array)
    copy_array[:, :, 1] = 0
    copy_array[:, :, 2] = 0
    print(copy_array)
    print('only blue clolor of the images received')
    cv2.imshow('Blue Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Blue Image')
    return copy_array


ft_blue.__doc__ = "show only blue color of the image"


def ft_grey(array) -> array:
    print('The shape of image is: ', array.shape)
    copy_array = np.copy(array)
    for i in range(len(copy_array)):
        for j in range(len(copy_array[i])):
            copy_array[i][j][0] = copy_array[i][j][1]
            copy_array[i][j][2] = copy_array[i][j][1]
    print(copy_array)
    print('only grey clolor of the images received')
    cv2.imshow('Grey Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Grey Image')
    return copy_array


ft_grey.__doc__ = "show only grey color of the image"
