from PIL.Image import Image

import numpy as np


def power(image: Image | np.ndarray, level: int):
    if isinstance(image, Image):
        image = np.array(image) / 255.0

    image_array = np.array(image)
    return 1 - (1-image_array)**level


def sigmoid(image: Image | np.ndarray, center: float, correction:bool = False) -> np.ndarray:
    if isinstance(image, Image):
        image = np.array(image) / 255.0

    img_array = np.array(image)
    if not correction:
        img_array = 1 / (1 + np.exp(-20 * (img_array - center)))
        return img_array
    else:
        while True:
            test = sigmoid(img_array, center, False)
            mean = test.mean()
            if mean < 0.75:
                center -= 0.02
            else:
                return test


def binaryzation(image: Image | np.ndarray, criteria: float, correction:bool = False) -> np.ndarray:
    if isinstance(image, Image):
        image = np.array(image) / 255.0

    if not correction:
        binary = (image > criteria).astype(int)
        binary = binary.astype(np.float64)
        return binary
    else:
        while True:
            test = binaryzation(image, criteria, False)
            if test.mean() < 0.75:
                criteria -= 0.02
            else:
                return test


def classify(image: np.ndarray, iteration: int) -> np.ndarray:
    """
    :param iteration: interation
    :param image: binary image
    :return: classified image
    """

    image = image + 0.5
    image = image.clip(max=1)

    lenth, height = image.shape[1], image.shape[0]  # width=32
    image[int(0.85 * height):int(height), int(0.30 * lenth):int(0.70 * lenth)] = 0.

    for _ in range(iteration):
        for h in range(height-2, 0, -1):
            for l in range(1, lenth-2, 1):
                if np.min(image[h-1:h+2, l-1:l+2]) == 0:
                    image[h-1:h+2,l-1:l+2] = (image[h-1:h+2, l-1:l+2] - 0.5) * 2
                    image[h-1:h+2,l-1:l+2] = image[h-1:h+2, l-1:l+2].clip(min=0)

            for l in range(lenth-1, 0, -1):
                if np.min(image[h-1:h+2, l-1:l+2]) == 0:
                    image[h-1:h+2,l-1:l+2] = (image[h-1:h+2, l-1:l+2] - 0.5) * 2
                    image[h-1:h+2,l-1:l+2] = image[h-1:h+2, l-1:l+2].clip(min=0)

    image = (image * 2).clip(max=1)

    return image

