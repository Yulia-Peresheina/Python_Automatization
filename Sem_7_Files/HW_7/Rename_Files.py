# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os
import random


def my_hm_func(w_name, exp_old, exp_new, range_min, range_max, quantity_nums):
    files_lst = os.listdir()
    for el in files_lst:
        old_name = el
        el = el.split(".")
        if el[1] == exp_old:
            max_num = 10 ** quantity_nums
            number = str(random.randint(0, max_num + 1))
            # new_name = el[0][range_min:range_max] + w_name + number + "." + exp_new
            new_name = ".".join(["".join([el[0][range_min:range_max], w_name, number]), exp_new])
            os.rename(old_name, new_name)


my_hm_func("asd", "txt", "txt", 1, 11, 1)
