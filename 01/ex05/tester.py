import cv2
from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey

array = ft_load("landscape.jpg")
array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
cv2.imshow('Original Image', array)
cv2.waitKey(0)
cv2.destroyAllWindows()

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)