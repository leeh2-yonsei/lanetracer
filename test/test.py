from PIL import Image, ImageOps

import matplotlib.pyplot as plt
import numpy as np

import utils.visualization as visual
from utils.img_process import power, sigmoid, binaryzation, classify
from utils.vector import get_center

img = Image.open('image/jpg/2.jpg').convert('L')
img = ImageOps.exif_transpose(img)
img = img.resize((240, 320))

visual.show_direction(img, get_center(img))

p_img= sigmoid(img, 0.5, correction=False)
visual.show_direction(p_img, get_center(p_img))

img = img.crop((0, 160, 240, 320))
p_img= sigmoid(img, 0.5, correction=False)
visual.show_direction(p_img, get_center(p_img))
