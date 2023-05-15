class MyBigInt:
    def __init__(self):
        self.value = 0

    def setHex(self, hex_string):
        self.value = int(hex_string, 16)

    def getHex(self):
        return hex(self.value)[2:]

    def INV(self):
        self.value = ~self.value

    def XOR(self, other):
        self.value ^= other.value

    def OR(self, other):
        self.value |= other.value

    def AND(self, other):
        self.value &= other.value

    def shiftR(self, n):
        self.value >>= n

    def shiftL(self, n):
        self.value <<= n
