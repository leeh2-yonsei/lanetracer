import numpy as np
from PIL.Image import Image

import matplotlib.pyplot as plt

from utils.vector import get_center


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