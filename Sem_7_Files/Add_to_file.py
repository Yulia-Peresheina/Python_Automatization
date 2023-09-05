# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import os
from random import randint, uniform


def func(file_name: str, lines: int):
    with open(file_name, "a+", encoding="utf-8") as f:
        for i in range(lines):
            text = "|".join([str(randint(-1000, 1001)), str(round(uniform(-1000, 1001), 2))])
            print(text, file=f)


func("first.txt", 3)
