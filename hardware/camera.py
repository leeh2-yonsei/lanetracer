import time

import picamera2

picam2 = picamera2.Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (100, 75)}))
picam2.start()

def capture_image(waiting: float or int = 0.5):
    time.sleep(waiting)

    picam2.capture_file('photo.jpg')
    print('\033[1;4;32mcaptured! photo.jpg\033[0m')


if __name__ == '__main__':
    capture_image()