from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

from untils import VectorList

if __name__ == '__main__':
    img = Image.open('../image/1.png').convert('L')
    img = img.resize((img.width // 2, img.height // 2))

    vector_list = VectorList.get_instance(img)
    center = vector_list.get_mean_vector()

    plt.imshow(np.array(img), cmap='gray')
    plt.scatter(center[0], center[1], color='red', s=50)
    plt.plot([center[0], img.width / 2], [center[1], img.height], 'r-')
    plt.ylim(img.height, 0)

    plt.show()