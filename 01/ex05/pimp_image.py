import cv2
from numpy import array
import numpy as np


def ft_invert(array) -> array:
    """invert the color of the image"""
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


def ft_red(array) -> array:
    """show only red color of the image"""
    copy_array = np.copy(array)
    copy_array[:, :, 0] = 0
    copy_array[:, :, 1] = 0
    print(copy_array)
    print('only red clolor of the images received')
    cv2.imshow('Red Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Red Image')
    return copy_array


def ft_green(array) -> array:
    """show only green color of the image"""
    copy_array = np.copy(array)
    copy_array[:, :, 0] = 0
    copy_array[:, :, 2] = 0
    print(copy_array)
    print('only green clolor of the images received')
    cv2.imshow('Green Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Green Image')
    return copy_array


def ft_blue(array) -> array:
    """show only blue color of the image"""
    copy_array = np.copy(array)
    copy_array[:, :, 1] = 0
    copy_array[:, :, 2] = 0
    print(copy_array)
    print('only blue clolor of the images received')
    cv2.imshow('Blue Image', copy_array)
    cv2.waitKey(0)
    cv2.destroyWindow('Blue Image')
    return copy_array


def ft_grey(array) -> array:
    """show only grey color of the image"""
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
