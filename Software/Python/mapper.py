class Mapper:
    def __init__(self, input, output):
        self.input = input
        self.output = output
    
    def parse(self, data):
        if data < self.input[0]:
            return self.output[0]
        if data > self.input[-1]:
            return self.output[-1]
        
        for in_low, in_high, out_low, out_high in zip(self.input, self.input[1:], self.output, self.output[1:]):
            if data <= in_high:
                return out_low + (data - in_low) * (out_high - out_low) / (in_high - in_low)