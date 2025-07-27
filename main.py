from PIL import Image, ImageOps
import argparse
import time

import numpy as np

import hardware.camera as camera
import utils.direction as direction
from utils.vector import get_line, line_to_angle
from utils.img_process import binaryzation, classify
from utils.visualization import show_line_list
import hardware.arduino as arduino

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, required=True, help='Choice Mode Type: [real, test, show]')

def main(root:str, mode:str):
    camera.capture_image(waiting=0.)

    img = Image.open(root).convert('L')
    img = ImageOps.exif_transpose(img)
    img = img.resize((100, 75))
    img = img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    width, height = img.size
    img = img.crop((0, height // 2, width, height))
    original_img = np.array(img) / 255.

    img = binaryzation(img, 0.5, correction=True)  # <y, x>
    img = classify(img, 1)

    line = get_line(img)
    angle = line_to_angle(line)

    if mode == 'real':
        new_angle = str(int(angle))
        arduino.send(f"{new_angle}\n")
        print(f"Direction: {int(angle)} : degree")
    elif mode == 'test':
        print('-' * 30)
        show_line_list([img, original_img], True)
        new_angle = str(int(angle))
        arduino.send(f"{new_angle}\n")
        print(f"Direction: {int(angle)} : degree")
        print('-' * 30)
    elif mode == 'show':
        show_line_list([img, original_img], True)
        print('-' * 30)
        print(f'angle: {angle}')


if __name__ == '__main__':
    args = parser.parse_args()
    if args.mode == 'test':
        start_time = time.time()
        print("\033[1m\033[1;32mTest mode started successfully\033[0m")
        for _ in range(int(input("Please Enter the number of repetition: "))):
            main('photo.jpg', 'test')
        end_time = time.time()
        print(f"The program is done in {(end_time - start_time):.2f} seconds.")

    elif args.mode == 'real':
        print("\033[1m\033[32mReal mode started successfully\033[0m")
        for _ in range(int(input("Please Enter the number of repetition: "))):
            main('photo.jpg', 'real')

    elif args.mode == 'show':
        print("\033[1m\033[32mShow mode started successfully\033[0m")
        for _ in range(int(input("Please Enter the number of repetition: "))):
            main('photo.jpg', 'show')