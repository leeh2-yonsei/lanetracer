from PIL import Image

import hardware.camera as camera
import hardware.arduino as arduino
import utils.direction as direction
from utils.vector import get_center
from utils.img_process import sigmoid

def main(root:str='photo.jpg'):
    camera.capture_image()

    img = Image.open(root).convert('L')
    img = img.resize((200, 150))
    img = sigmoid(img, 0.5, correction=True)

    center = get_center(img)
    info = direction.get_direction(center)

    arduino.send(info)


if __name__ == '__main__':
    main()