import serial

serial = serial.Serial('/dev/ttyACM0', 9600)

def send(info: int | str):
    serial.write(str(info).encode())

if __name__ == "__main__":
    messg = input("Input the message to send:")
    send(messg)
