
class Math:
    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        return Math(self.value + other.value)

    def __sub__(self, other):
        return Math(self.value - other.value)

    def multiplication(self):
        return Math(self.value)

    def division(self):
        return Math(self.value)

value1 = Math(5)
value2 = Math(8)
result = value1 + value2
print(result.value)

value1 = Math(9)
value2 = Math(8)
result = value1 - value2
print(result.value)

result = 9 * 2
print(result)

result = 15 / 3
print(result)