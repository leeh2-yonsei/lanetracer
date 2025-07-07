from PIL import Image

import hardware.camera as camera
import hardware.arduino as arduino
import utils.direction as direction
from utils.vector import VectorList

def main(root:str='photo.jpg'):
    camera.capture_image()

    img = Image.open(root).convert('L')
    img = img.resize((200, 150))

    center = VectorList.get_instance(img).center
    info = direction.get_direction(center)

    arduino.send(info)

