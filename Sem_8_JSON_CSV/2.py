# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
import os
'''Функция не работает, на семинаре взяли более простое решение, оно ниже'''
#
# def func7_2():
#     while True:
#         want_stop = input("Продолжаем? 1 - да, 0 - нет")
#         if not want_stop:
#             return
#         name = input("Введите имя: ")
#
#         pers_id = input("Введите личный идентификатор: ")
#         level = input("Введите уровень доступа: ")
#         if not 0 < int(level) < 8:
#             continue
#         my_dict = {level: {pers_id: name}}
#         with open("pers_data.json", "r+", encoding="utf-8") as f:
#             json_file = json.load(f)
#         res = json_file.append(my_dict)
#         if json_file != "":
#             if level in json_file.keys():
#                 if pers_id in json_file[level].keys():
#                     if name != json_file[level][pers_id]:
#                         print("идентификатор не уникален!")
#                     continue
#                 else:
#                     json_file[level][pers_id] = name
#             else:
#                 json_file[level] = {pers_id: name}
#         else:
#             json_file = {level: {pers_id: name}}
#         with open("pers_data.json", "a", encoding="utf-8") as f:
#             json.dump(json_file, f, indent=2)
#
#
# func7_2()
"""Решение препода"""
def fun_dump_json():
    # name = input("введите имя:> ")
    # user_id = input("введите id:> ")
    # level = int(input('введите уровень доступа (1-7):> '))
    name = "Петя"
    user_id = "002"
    level = 4

    with open('task8_2.json', "r", encoding='utf-8') as f:
        res = json.load(f)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open('task8_2.json', "w", encoding='utf-8') as js_f:
        res.append(my_dct)
        json.dump(res, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)


lst = []
with open('task8_2.json', "w", encoding='utf-8') as js_f:
    json.dump(lst, js_f)

s = 'n'
while s != 'y':
    fun_dump_json()
    s = input('выход y/n :>')



