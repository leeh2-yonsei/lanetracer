import numpy as np
from PIL.Image import Image

import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes

from utils.vector import get_center, get_line


def show_direction(img: Image | np.ndarray, center: tuple[float, float] = None):
    if isinstance(img, Image):
        img = np.array(img) / 255.0
    heigt, lenth = img.shape

    if center is None:
        center = get_center(img)

    plt.imshow(img, cmap='gray')
    plt.plot([center[0], lenth // 2], [center[1], heigt], color='r')
    plt.scatter(center[0], center[1], color='red', s=50)
    remove_axis(heigt)
    plt.show()


def show_direction_list(img_list: list[np.ndarray], cordinate:bool = False):
    height, lenth = img_list[0].shape

    if cordinate:
        center_list = [get_center(img_list[0])] * len(img_list)
    else:
        center_list = [get_center(img) for img in img_list]

    axes: list[Axes]
    fig, axes = plt.subplots(len(center_list), 1)

    for i in range(len(center_list)):
        axes[i].imshow(img_list[i], cmap='gray')
        axes[i].scatter(center_list[i][0], center_list[i][1], color='red', s=50)
        axes[i].plot([center_list[i][0], lenth//2], [center_list[i][1], height], color='r')
        axes[i].axis('off')

    plt.show()

def show_line(img: np.ndarray, center_list: list[tuple[float, float]] = None):
    height, lenth = img.shape

    if center_list is None:
        center_list = get_line(img)

    plt.imshow(img, cmap='gray')
    plt.plot([center[0] for center in center_list], [center[1] for center in center_list], color='red')
    plt.scatter([center[0] for center in center_list], [center[1] for center in center_list], color='red')
    remove_axis(height)
    plt.show()


def show_line_list(img_list: list[np.ndarray], cordinate:bool = False):

    if cordinate:
        line_list = [get_line(img_list[0])] * len(img_list)
    else:
        line_list = [get_line(img) for img in img_list]

    axes: list[Axes]
    fig, axes = plt.subplots(len(line_list), 1)
    for i in range(len(line_list)):
        axes[i].imshow(img_list[i], cmap='gray')
        axes[i].plot([center[0] for center in line_list[i]], [center[1] for center in line_list[i]], color='red')
        axes[i].scatter([center[0] for center in line_list[i]], [center[1] for center in line_list[i]], color='red')
        axes[i].axis('off')

    plt.show()



def remove_axis(height: int):
    plt.axis('off')
    plt.ylim(height, 0)


def show(img: Image or np.ndarray):
    plt.cla()
    plt.imshow(img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    image = Image.open('../test/image/jpg/1.jpg').convert('L')
    image = image.resize((200, 150))
    show_direction(image)