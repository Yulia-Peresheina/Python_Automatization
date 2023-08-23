# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = 1, "hello", True, 8.91, None, 34, 56, "Goodbye", False, 0.01,

def from_tuple_to_dict(data):
    my_dict = {}
    for item in data:
        if my_dict.get(type(item)) is not None:
            my_dict.get(type(item)).append(item)
        else:
            my_dict[type(item)] = [item]
    print(my_dict)


from_tuple_to_dict(my_tuple)