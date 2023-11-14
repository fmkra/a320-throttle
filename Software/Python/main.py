import sys
import glob
import serial
from communication import CommunicationReader
from vgamepad import VX360Gamepad


def getPort():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    
    for i, port in enumerate(result):
        print(f"{i}: {port}")
    
    selected = int(input("Select port: "))
    return result[selected]

def main():
    port = getPort()
    joystick = VX360Gamepad()
    with serial.Serial(port, 9600, timeout=5) as arduino:
        reader = CommunicationReader(arduino)
        reader.registerUint10()
        reader.registerUint10()

        while True:
            throttleLeft, throttleRight = reader.read()
            print(throttleLeft, throttleRight)
            joystick.left_joystick_float(throttleRight/512-1, throttleLeft/512-1)
            joystick.update()


if __name__ == '__main__':
    main()
