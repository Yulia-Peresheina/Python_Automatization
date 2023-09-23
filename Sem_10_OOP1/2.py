# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, length, width=None):
        if width is None:
            width = length
        self._length = length
        self._width = width

    def perimetr(self):
        return 2 * (self._width + self._length)

    def square(self):
        return self._width * self._length


rectangle = Rectangle(2, 3)
print(f"{rectangle.square() = }, {rectangle.perimetr() = }")