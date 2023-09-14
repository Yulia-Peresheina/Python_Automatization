# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from typing import Callable
from random import randint


def try_to_guess(guess: int) -> Callable[[int], int]:
    def your_try(count: int) -> int:
        for i in range(1, count + 1):
            x = int(input("Ваш вариант: "))
            if x == guess:
                return i
            elif x > guess:
                print("Превышение!")
            else:
                print("Недобор!")
        return 0

    return your_try


first = try_to_guess(5)
print(type(first))
print(first(5))
