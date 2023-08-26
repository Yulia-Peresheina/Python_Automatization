#  Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def take_key(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            my_dict[value] = key
        except TypeError:
            my_dict[str(value)] = key
    return my_dict


print(take_key(brand="volvo", model="XC90", generation=[2019, 2020, 2021, 2022, 2023], engine="diesel", transmission="auto"))

