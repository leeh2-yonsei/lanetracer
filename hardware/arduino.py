import serial

serial = serial.Serial('/dev/ttyACM0', 9600)

def send(info: int):
    serial.write(str(info).encode())

