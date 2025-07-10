from PIL import Image, ImageOps
import argparse
import time

import numpy as np

import hardware.camera as camera
import utils.direction as direction
from utils.vector import get_center
from utils.img_process import sigmoid

parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true', default=False, help='Start Test without Arduino')

def main(root:str='photo.jpg', test:bool=False):
    camera.capture_image(waiting=0.5)

    img = Image.open(root).convert('L')
    img = ImageOps.exif_transpose(img)
    img = img.resize((200, 150))
    original_img = img
    img = sigmoid(img, 0.5, correction=True)  # <y, x>

    center = get_center(img)  # <x, y>
    vector = np.array([center[0] - img.shape[1]/2, img.shape[0] - center[1]])
    info = direction.get_direction(vector / np.linalg.norm(vector))

    if not test:
        arduino.send(info)
    else:
        print('-' * 30)
        print(f"direction: {info} | vector: {vector / np.linalg.norm(vector)}")
        print(f"center: {center} | criteria: {np.array([img.shape[1] / 2, img.shape[0]])}")
        print(f"angle: {np.degrees(np.arctan2(vector[1], vector[0]))}")
        print('-' * 30)

        from utils.visualization import show_direction
        show_direction(original_img, center)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.test:
        start_time = time.time()
        print("\033[1m\033[1;32mTest mode started successfully\033[0m")
        main(test=True)
        end_time = time.time()
        print(f"The program is done in {(end_time - start_time):.2f} seconds.")
    else:
        print("\033[1m\033[32mReal mode started successfully\033[0m")
        import hardware.arduino as arduino
        main(test=False)