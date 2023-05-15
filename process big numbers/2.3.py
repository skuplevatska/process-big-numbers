class MyBigInt:
    def __init__(self, value=0, block_size=8):
        self.block_size = block_size
        self.blocks = []
        self.value = value

    def setHex(self, hex_value):
        self.value = self.hex_to_int(hex_value)
        self._update_blocks()

    def getHex(self):
        return self.int_to_hex(self.value)

    def hex_to_int(self, hex_value):
        result = 0
        for digit in hex_value:
            result = result * 16 + int(digit, 16)
        return result

    def int_to_hex(self, value):
        if value == 0:
            return "0"
        result = ""
        while value > 0:
            digit = value % 16
            result = hex(digit)[2:] + result
            value //= 16
        return result

    def _update_blocks(self):
        self.blocks = []
        while self.value > 0:
            self.blocks.append(self.value & ((1 << self.block_size) - 1))
            self.value >>= self.block_size

    def ADD(self, other):
        result = MyBigInt()
        carry = 0
        max_blocks = max(len(self.blocks), len(other.blocks))
        for i in range(max_blocks):
            a = self.blocks[i] if i < len(self.blocks) else 0
            b = other.blocks[i] if i < len(other.blocks) else 0
            carry, block_sum = divmod(a + b + carry, 1 << self.block_size)
            result.blocks.append(block_sum)

        if carry > 0:
            result.blocks.append(carry)

        result._update_value()
        return result

    def SUB(self, other):
        result = MyBigInt()
        borrow = 0
        max_blocks = max(len(self.blocks), len(other.blocks))
        for i in range(max_blocks):
            a = self.blocks[i] if i < len(self.blocks) else 0
            b = other.blocks[i] if i < len(other.blocks) else 0
            borrow, block_diff = divmod(a - b - borrow, 1 << self.block_size)
            result.blocks.append(block_diff % (1 << self.block_size))

        result._update_value()
        return result

    def MOD(self, other):
        result = MyBigInt()
        if other.value == 0:
            raise ValueError("Division by zero error")
        result.value = self.value % other.value
        result._update_blocks()
        return result

    def _update_value(self):
        self.value = 0
        for block in reversed(self.blocks):
            self.value <<= self.block_size
            self.value += block
