from PIL import Image, ImageOps
import argparse
import time

import numpy as np

import hardware.camera as camera
import utils.direction as direction
from utils.vector import get_center
from utils.img_process import sigmoid

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, required=True, help='Choice Mode Type')

def main(root:str, mode:str):
    camera.capture_image(waiting=0.)

    img = Image.open(root).convert('L')
    img = ImageOps.exif_transpose(img)
    img = img.resize((200, 150))
    original_img = img
    img = sigmoid(img, 0.5, correction=True)  # <y, x>

    center = get_center(img)  # <x, y>
    vector = np.array([center[0] - img.shape[1]/2, img.shape[0] - center[1]])
    info = direction.get_direction(vector / np.linalg.norm(vector))

    if mode == 'real':
        arduino.send(info)
    elif mode == 'test':
        print('-' * 30)
        print(f"direction: {info} | vector: {vector / np.linalg.norm(vector)}")
        print(f"center: {center} | criteria: {np.array([img.shape[1] / 2, img.shape[0]])}")
        print(f"angle: {np.degrees(np.arctan2(vector[1], vector[0]))}")
        print('-' * 30)
    elif mode == 'show':
        from utils.visualization import show_direction
        show_direction(original_img, center)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.mode == 'test':
        start_time = time.time()
        print("\033[1m\033[1;32mTest mode started successfully\033[0m")
        main('photo.jpg', 'test')
        end_time = time.time()
        print(f"The program is done in {(end_time - start_time):.2f} seconds.")

    elif args.mode == 'real':
        print("\033[1m\033[32mReal mode started successfully\033[0m")
        import hardware.arduino as arduino

        for _ in range(int(input("Please Enter the number of repetition: "))):
            main('photo.jpg', 'real')

    elif args.mode == 'show':
        print("\033[1m\033[32mShow mode started successfully\033[0m")
        main('photo.jpg', 'show')