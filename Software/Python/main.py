import sys
import glob
import serial


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
    with serial.Serial(port, 115200, timeout=1) as arduino:
        while True:
            data = input()
            arduino.write(data.encode())
            print(arduino.readline().decode())


if __name__ == '__main__':
    main()
