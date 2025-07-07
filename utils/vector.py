from PIL.ImageFile import ImageFile

import numpy as np

class VectorList:
    def __init__(self, amplify_level: int=14):
        self.vector_list: list = []
        self.weight: list[int | float] = []

        self.amplify_level = amplify_level

    def add(self, vector, weight: int | float):
        self.vector_list.append(vector)
        self.weight.append(weight)

    def get_mean_vector(self) -> tuple[float, float]:
        vector_array = np.array(self.vector_list)
        weight_array = np.array(self.weight)

        n_weight = sum(weight_array)
        result = np.array([0., 0.])
        for i in range(len(weight_array)):
            result += vector_array[i] * weight_array[i] / n_weight

        return result

    @classmethod
    def get_instance(cls, img: ImageFile, amplify_level: int = 10):
        """
        :param img: Imagefile that converted to an L
        :param amplify_level: Amplify level
        :return: weighted vector list of the image
        """
        instance = cls(amplify_level)
        img_array = np.array(img)

        for row in range(img.height):
            for column in range(img.width):
                pixel = img_array[row][column]
                instance.add(np.array([column, row]), VectorList.amplify_weight((255 - pixel), instance.amplify_level))

        return instance

    @staticmethod
    def amplify_weight(weight, level: int):
        """
        the function set amplify_level the weight of the pixels
        :param weight: the weights of the pixel (vector)
        :param level: amplify levels
        :return:
        """
        return (weight / 255)**level

    def sigmoid_weight(self):
        self.weight = sigmoid(np.array(self.weight))

    @property
    def center(self):
        return self.get_mean_vector()


def sigmoid(x):
    return 1 / (1 + np.exp(-20 * (x - 0.5)))