import numpy as np
from PIL import Image, ImageOps

import matplotlib.pyplot as plt

import utils.visualization as vsl
from utils.vector import VectorList

img = Image.open('image/jpg/3.jpg').convert('L')
img = ImageOps.exif_transpose(img)
img = img.resize((200, 150))

v_list = VectorList.get_instance(img, 1)
v_list.sigmoid_weight()

vsl.show_direction(img, v_list.center)

