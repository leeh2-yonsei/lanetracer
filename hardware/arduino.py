import serial

import time

serial = serial.Serial('/dev/ttyACM0', 9600)

def send(info: int | str):
    serial.write(str(info).encode())


def parallel(direction: bool):
    """
    :param direction: right = true, left = false
    """
    if direction:
        send('120\n')
        time.sleep(0.10)
        send('90\n')
        time.sleep(0.10)
        send('60\n')
        time.sleep(0.10)
        send('-10\n')
        time.sleep(0.10)
        send('0\n')
    else:
        send('60\n')
        time.sleep(0.10)
        send('90\n')
        time.sleep(0.10)
        send('120\n')
        time.sleep(0.10)
        send('-10\n')
        time.sleep(0.10)
        send('0\n')
    time.sleep(0.10)
    return


if __name__ == "__main__":
    while True:
        messg = input("Input the message to send:")

        if messg == 'quit':
            exit("Test is finished")
        send(messg)
