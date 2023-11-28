class RegisterError(Exception):
    def __init__(self):
        super().__init__("Register cannot be called after reading from the device")


def register_check(func):
    def wrapper(self, *args, **kwargs):
        if self._register_finished:
            raise RegisterError
        return func(self, *args, **kwargs)
    return wrapper


class ArduinoReader:
    def __init__(self, serial):
        self._register_finished = False
        self.schema = []
        self.serial = serial
    
    @register_check
    def registerUint10(self):
        self.schema.append(10)
        
    def read(self):
        data = self.serial.read_until(b'\0')
        
        def readData(value):
            return value & 0x7f
        
        def readUint10(bytes):
            return (readData(bytes[1]) << 5) | readData(bytes[0])

        result = []
        i = 0
        for size in self.schema:
            if size == 10:
                result.append(readUint10(data[i:i+2]))
                i += 2
        return result
