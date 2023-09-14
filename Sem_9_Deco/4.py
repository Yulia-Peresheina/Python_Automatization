# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.


def count(arg):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(arg):
                print(f"{i + 1} раз")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco


@count(5)
def my_sum(a, b):
    return a + b


print(my_sum(1, 2))
