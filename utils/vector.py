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

def get_line(img: Image | np.ndarray) -> list[tuple[float, float]]:
    if isinstance(img, Image):
        img = np.array(img) / 255.0

    weights = 1 - img
    height, lenth = img.shape
    y, x = np.indices((height, lenth))

    center_list = []

    unit = height // 4
    for i in range(4):
        area = weights[unit*i:unit*(i+1)]
        area_weights = np.sum(area)
        if area_weights == 0:
            continue
        else:
            center = np.array([
                np.sum(x[unit*i:unit*(i+1)] * area) / area_weights,
                np.sum(y[unit*i:unit*(i+1)] * area) / area_weights,
            ])
            center_list.append(center)

    return center_list

def line_to_angle(center_list: list[tuple[float, float]]) -> float:
    angle_list = []
    for i in range(len(center_list) - 1):
        vector = np.array(center_list[i+1]) - np.array(center_list[i])
        angle = np.arctan2(vector[1], vector[0])
        angle_list.append(angle)

    if len(angle_list) == 0:
        return 90
    else:
        return np.degrees(sum(angle_list) / len(angle_list))
