import numpy as np
import cv2
from PIL import Image

#im = Image.open("/home/pi/Desktop/testing.jpg")
#im.save("/home/pi/Desktop/test-300.jpg", dpi=(300,300) )
size = 7016, 4961
im = Image.open("/home/pi/Desktop/testing.jpg")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("/home/pi/Desktop/my_image_resized.jpg", dpi=(300,300) )
