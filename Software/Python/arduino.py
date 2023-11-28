from enum import Enum


class RegisterError(Exception):
    def __init__(self):
        super().__init__("Register cannot be called after reading from the device")


class DataLengthError(Exception):
    def __init__(self, read, expected_len):
        super().__init__(f"Read {read} bytes, expected {expected_len} bytes")


def register_check(func):
    def wrapper(self, *args, **kwargs):
        if self._register_finished:
            raise RegisterError
        return func(self, *args, **kwargs)
    return wrapper


class DataType(Enum):
    Uint10 = 10


class ArduinoReader:
    def __init__(self, serial):
        self._register_finished = False
        self._schema = []
        self._serial = serial
        self._schema_byte_len = 0
    
    @register_check
    def registerUint10(self):
        self._schema.append(DataType.Uint10)
        self._schema_byte_len += 2
        
    def read(self):
        data = self._serial.read_until(b'\0')
        
        def readData(value):
            return value & 0x7f
        
        def readUint10(bytes):
            return (readData(bytes[1]) << 5) | readData(bytes[0])

        result = []
        i = 0
        if self._schema_byte_len != len(data):
            raise DataLengthError(len(data), self._schema_byte_len)

        for size in self._schema:
            if size == DataType.Uint10:
                result.append(readUint10(data[i:i+2]))
                i += 2
        return result
