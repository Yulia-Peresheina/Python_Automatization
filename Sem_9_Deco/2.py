# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию
# угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
from typing import Callable
from random import randint


def main(func: Callable):
    def wrapper(a, b):
        number = a if 0 < a < 100 else randint(0, 101)
        attempts = b if 0 < b < 11 else randint(0, 11)
        result = func(number, attempts)
        return result

    return wrapper


@main
def guess_number(number: int, tries: int) -> int:
    for i in range(1, tries + 1):
        x = int(input("Ваш вариант: "))
        if x == number:
            return i
        elif x > number:
            print("Превышение!")
        else:
            print("Недобор!")
    return 0


first = main(guess_number)
print(type(first))
print(first(500, 11))
