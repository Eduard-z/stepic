class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.value = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return v + self.value <= self.capacity

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.value += v


a = MoneyBox(9)
a.add(2)
a.add(5)
print(a.can_add(4))
print(a.value)
a.add(5)
print(a.value)
print(a.__dict__)
