# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json

from typing import Callable
from inspect import signature


def deco(func):
    my_dict = {}

    def wrapper(*args, **kwargs):
        # args_name = (str(signature(func))[1:-1])
        # args_list = args_name.split(", ")
        my_dict['arguments'] = args
        for key, value in kwargs.items():
            my_dict[key] = value
        # my_dict = {arg_name: arg for arg_name, arg in zip(args_list, args)}
        result = func(*args, **kwargs)
        my_dict[func.__name__] = result
        with open(f"{func.__name__}.json", "a", encoding="utf-8") as f:
            json.dump(my_dict, f, indent=2)
        return result

    return wrapper


@deco
def func_example(a, b, *, c):
    my_summ = a + b
    all_summ = my_summ + c
    return [my_summ, all_summ]


print(func_example(3, 4, c=5))


