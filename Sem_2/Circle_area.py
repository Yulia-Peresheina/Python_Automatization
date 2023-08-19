# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import decimal
import math


def circle_area_and_length():
    diametr = int(input("Введите диаметр: "))
    decimal.getcontext().prec = 42
    area = math.pi * (diametr / 2) ** 2
    length = math.pi * diametr
    area = decimal.Decimal(area)
    length = decimal.Decimal(length)
    print("Площадь круга: ", area)
    print("Длина окружности: ", length)

circle_area_and_length()