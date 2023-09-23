# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Circle:

    def __init__(self, rad):
        self._rad = rad

    def circle_length(self):
        return 2 * math.pi * self._rad

    def circle_square(self):
        return math.pi * self._rad ** 2


first = Circle(5)
print(f"{first.circle_square() = }, {first.circle_length() = }")
