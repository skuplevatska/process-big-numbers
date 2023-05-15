class LargeNumber:
    def __init__(self):
        self.digits = []

    def set_from_hex(self, hex_string):
        # Отримати кожен окремий шістнадцятковий символ і перетворити на відповідні цифри
        self.digits = [int(digit, 16) for digit in hex_string]

    def get_as_hex(self):
        # Перетворити кожну цифру на шістнадцятковий символ і зібрати їх у рядок
        hex_string = ''.join(hex(digit)[2:] for digit in self.digits)
        return hex_string

    def set_from_decimal(self, decimal_string):
        # Отримати кожен окремий символ і перетворити на відповідні цифри
        self.digits = [int(digit) for digit in decimal_string]

    def get_as_decimal(self):
        # Перетворити кожну цифру на символ і зібрати їх у рядок
        decimal_string = ''.join(str(digit) for digit in self.digits)
        return decimal_string

    # Інші методи для встановлення і отримання числа, які відповідають вашим потребам

# Приклад використання
num = LargeNumber()
num.set_from_hex("B1A")
print(num.get_as_hex())  

num.set_from_decimal("12345")
print(num.get_as_decimal())  
