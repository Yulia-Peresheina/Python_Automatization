# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import random
import string


def my_func(*, expantion, min_len=6, max_len=30, min_byts=256, max_byts=4096, quantity=1):
    for i in range(quantity):
        name = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(min_len, max_len + 1)))
        size = random.randint(min_byts, max_byts + 1)
        file_name = ".".join([name, expantion])
        with open(file_name, "bw") as f:
            f.write(random.randbytes(size))



