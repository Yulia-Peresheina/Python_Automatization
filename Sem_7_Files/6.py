# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
import create_diff_file_expansions as cdfe


def func5(**kwargs):
    for key, value in kwargs.items():
        my_func(expantion=key,quantity=value)


def func_6(new_dir):
    my_path = os.getcwd() + new_dir
    try:
        os.makedirs(my_path)
        os.chdir(my_path)
    except FileExistsError:
        os.chdir(my_path)
    cdfe.func5(txt=1, md=1)
    os.chdir('..')


func_6('\\Modules')




