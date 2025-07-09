from PIL.Image import Image

import numpy as np


def power(image: Image | np.ndarray, level: int):
    if isinstance(image, Image):
        image = np.array(image) / 255.0

    image_array = np.array(image)
    return image_array ** level



def sigmoid(image: Image | np.ndarray, center: float, correction:bool = False) -> np.ndarray:
    if isinstance(image, Image):
        image = np.array(image) / 255.0

    img_array = np.array(image)
    if not correction:
        img_array = 1 / (1 + np.exp(-20 * (img_array - center)))
        mean = img_array.mean()
        pass
        return img_array
    else:
        while True:
            test = sigmoid(img_array, center, False)
            mean = test.mean()
            if mean < 0.75:
                center -= 0.02
            else:
                return test


def binaryzation(image: Image | np.ndarray, criteria: float) -> np.ndarray:
    if isinstance(image, Image):
        image = np.array(image) / 255.0

    image_array = np.array(image)
    binary = (image_array > criteria).astype(int)
    binary = binary.astype(np.float64)
    return binary


def classify(image: np.ndarray, n_interation: int, step:int = 1, size:int = 3) -> np.ndarray:
    """
    :param n_interation: interation
    :param step: step size
    :param size: size of select area (odd number)
    :param image: binary image
    :return: classified image
    """
    delta = (size - 1) // 2

    image = image + 0.5
    image = image.clip(max=1)

    lenth, height = image.shape[1], image.shape[0]  # width=32
    image[int(0.85 * height):int(height), int(0.35 * lenth):int(0.65 * lenth)] = 0.

    for _ in range(n_interation):
        for h in range(height-delta-1, delta, -step):
            for l in range(delta, lenth-delta-1, step):
                if np.min(image[h-delta:h+delta+1, l-delta:l+delta+1]) == 0:
                    image[h-delta:h+delta+1, l-delta:l+delta+1] = (image[h-delta:h+delta+1, l-delta:l+delta+1] - 0.5)*2
                    image[h-delta:h+delta+1, l-delta:l+delta+1] = image[h-delta:h+delta+1, l-delta:l+delta+1].clip(min=0)

    return image

