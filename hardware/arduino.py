import serial

serial = serial.Serial('/dev/ttyACM0', 9600)

def send(info: int | str):
    serial.write(str(info).encode())

if __name__ == "__main__":
    while True:
        messg = input("Input the message to send:")

        if messg == 'quit':
            exit("Test is finished")
        send(messg)
