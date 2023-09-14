# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import json

import random
import csv
import math


def decor(file_name):
    my_data = []
    with open(file_name, "r", newline="") as f_read:
        csv_file = csv.DictReader(f_read, fieldnames=["a", "b", "c"], quoting=csv.QUOTE_NONNUMERIC, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            if i != 0:
                a = line['a']
                b = line['b']
                c = line['c']
                my_data.append([a, b, c])

    def deco(func):

        def wrapper(*args):
            all_result = []
            for el in my_data:
                result = func(el[0], el[1], el[2])
                # print(result)
                all_result.append(result)

            return all_result
        return wrapper
    return deco


def decor_2(file_name):
    def dec(func):
        def wrapper(*args):
            dict_data_result = []
            with open(file_name, "w", encoding="utf-8") as f_json, open("my_file.csv", "r", newline='') as f_csv:
                csv_file = csv.DictReader(f_csv, fieldnames=["a", "b", "c"], quoting=csv.QUOTE_NONNUMERIC, dialect='excel-tab')
                for i, line in enumerate(csv_file):
                    if i != 0:
                        # print(line['c'])
                        dict_data_result.append({f"{line['a']}, {line['b']}, {line['c']}": func(line['a'], line['b'], line['c'])})
                json.dump(dict_data_result, f_json, indent=2)
            return dict_data_result
        return wrapper
    return dec


@decor("my_file.csv")
@decor_2("my_file.json")
def func_1(a, b, c):
    d = b ** 2 - 4 * a * c
    result = []
    if d > 0:
        x_1 = -b + math.sqrt(d) / 2 * a
        result.append(x_1)
        x_2 = -b - math.sqrt(d) / 2 * a
        result.append(x_2)
    elif d == 0:
        x = -b / 2 * a
        result.append(x)
    return result


def print_random_to_cvs():
    with open("my_file.csv", "w", newline="", encoding="utf-8") as f_cvs:
        csv_write = csv.DictWriter(f_cvs, fieldnames=["a", "b", "c"], dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()

        all_data = []
        for i in range(random.randint(100, 1001)):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = random.randint(-100, 100)
            all_data.append({'a':a, 'b': b, 'c': c})
        csv_write.writerows(all_data)


func_1(1, 1, 1)

# func_2()
