import numpy as np
from PIL.Image import Image

def get_center(img: Image | np.ndarray):
    if isinstance(img, Image):
        img = np.array(img) / 255.0

    weights = 1 - img
    height, lenth = img.shape
    y, x = np.indices((height, lenth))

    total_weight = np.sum(weights)
    center = np.array([np.sum(x * weights), np.sum(y * weights)]) / total_weight
    return center

