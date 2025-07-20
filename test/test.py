from PIL import Image, ImageOps

import matplotlib.pyplot as plt
import numpy as np

import utils.visualization as visual
from utils.img_process import power, sigmoid, binaryzation, classify
from utils.vector import get_center

img = Image.open('image/jpg/10.jpg').convert('L')
img = ImageOps.exif_transpose(img)
img = img.resize((240, 320))

visual.show_direction(img, get_center(img))

p_img= binaryzation(img, 0.5, correction=True)
p_img = classify(p_img, 1)
visual.show_direction(p_img, get_center(p_img))

