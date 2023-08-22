# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
from decimal import Decimal, getcontext
import math

diametr = int(input("Введите диаметр: "))
def circle_area_and_length(diam):
    area = math.pi * (diam / 2) ** 2
    length = math.pi * diam
    print(f"Площадь круга: {area: .12f}, Длина окружности: {length: .12f}")


circle_area_and_length(diametr)


getcontext().prec = 3
print(Decimal('4.34') / 4)
