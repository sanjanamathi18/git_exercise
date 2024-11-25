class Calculation:
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        sum = self.value1 + self.value2
        return sum

    def sub(self):
        minus = self.value1 - self.value2
        return minus


operation = Calculation(10, 5)
print(operation.add())
print(operation.sub())
