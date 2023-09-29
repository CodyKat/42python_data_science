from numpy import array
import numpy as np
from load_image import ft_load
from PIL import Image

image : array = ft_load('animal.jpeg')
print(np.shape(image))
imagePIL = Image.fromarray(image)
image_resized = imagePIL.crop((450,100,850,500))
image2 = np.array(image_resized)
gray_image = np.mean(image2, axis=2, dtype=int)
to_print = Image.fromarray(gray_image)


print("New shape after slicing: (400, 400, 1) or (400, 400)")
print(to_print)

to_print.show()
