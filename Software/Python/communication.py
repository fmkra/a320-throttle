class RegisterError(Exception):
    def __init__(self):
        super().__init__("Register cannot be called after reading from the device")


def register_check(func):
    def wrapper(self, *args, **kwargs):
        if self._register_finished:
            raise RegisterError
        return func(self, *args, **kwargs)
    return wrapper


class CommunicationReader:
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
        
        