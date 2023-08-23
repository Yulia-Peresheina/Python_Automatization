# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

import sys


def checking_data_type():
    data = input("Введите значение: ")
    if data.count(".") == 1:
        new_data = data.split(".")
        if str.isdecimal(new_data[0]) and str.isdecimal(new_data[1]):
            print("Положительное Вещественное число. ")
        elif new_data[0][0] == "-" and str.isdecimal(new_data[1]) and str.isdecimal(new_data[0][1::]):
            print("Отрицательное Вещественное число. ")
    elif str.isdecimal(data) and int(data) > 0:
        print("Целое положительное число!")
    elif str.isalpha(data) and str.istitle(data):
        print(str.upper(data))
    else:
        print(str.lower(data))

checking_data_type()