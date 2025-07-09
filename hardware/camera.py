import time

import picamera2

picam2 = picamera2.Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

def capture_image(waiting: float or int = 0.5):
    time.sleep(waiting)

    picam2.capture_file('photo.jpg')
    print('captured photo.jpg')


if __name__ == '__main__':
    capture_image()