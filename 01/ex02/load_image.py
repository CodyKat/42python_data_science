import PIL
from PIL import Image
import numpy as np
from numpy import array


def ft_load(path: str) -> array:
    """load image from path and return numpy array"""
    image: PIL.JpegImagePlugin.JpegImageFile
    try:
        image = Image.open(path)
    except FileNotFoundError:
        raise AssertionError('image file not found')

    print('The shape of image is:', np.shape(image))
    np_img = np.array(image)
    return np_img
