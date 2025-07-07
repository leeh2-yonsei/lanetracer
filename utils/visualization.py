import numpy as np
from PIL import Image, ImageFile

import matplotlib.pyplot as plt

from utils.vector import VectorList

def show_image(img: ImageFile, processed:bool=False):

    if processed:
        img_array = np.array(img)
        img_array = VectorList.amplify_weight(img_array, 20)
        plt.imshow(img_array, cmap='gray')
    else:
        plt.imshow(img, cmap='gray')
    plt.show()


def show_direction(img: ImageFile, center: tuple[float, float] = None):

    if center is None:
        center = VectorList.get_instance(img).center

    plt.imshow(img, cmap='gray')
    plt.plot([center[0], img.size[0] // 2], [center[1], img.size[1]], color='r')
    plt.scatter(center[0], center[1], color='red', s=50)
    remove_axis(img.height)
    plt.show()

def remove_axis(height: int):
    plt.axis('off')
    plt.ylim(height, 0)


if __name__ == '__main__':
    image = Image.open('../test/image/jpg/1.jpg').convert('L')
    image = image.resize((200, 150))
    show_direction(image)