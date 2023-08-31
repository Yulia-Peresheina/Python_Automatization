# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint


def func(start, finish, tries):
    find = randint(start, finish)
    for i in range(0, tries):
        my_try = int(input("Guess number! "))
        if my_try > find:
            print("More!")
        elif my_try < find:
            print("Less!")
        elif my_try == find:
            return True
    return False


# func(1, 10, 7)
