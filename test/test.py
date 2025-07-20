from PIL import Image, ImageOps

import matplotlib.pyplot as plt
import numpy as np

import utils.visualization as visual
from utils.img_process import power, sigmoid, binaryzation, classify
from utils.vector import get_center, get_line, line_to_angle

img = Image.open('image/jpg/12.jpg').convert('L')
img = ImageOps.exif_transpose(img)
img = img.resize((240, 320))

visual.show_direction(img, get_center(img))

p_img= binaryzation(img, 0.5, correction=True)
p_img = classify(p_img, 1)
print(get_line(p_img))
visual.show_line(p_img, get_line(p_img))
print(line_to_angle(get_line(p_img)))

