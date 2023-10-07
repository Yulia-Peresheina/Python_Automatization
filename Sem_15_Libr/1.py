# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

# Тут основной файл

import logging


FORMAT = "{levelname:<8} - {asctime}.  В строке {lineno:>3d}  в {created} секунд записано сообщение {msg}"
logging.basicConfig(level=logging.ERROR, format=FORMAT, style="{", filename="errors.log", filemode="a", encoding="utf-8", )
logger = logging.getLogger(__name__)


def division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logging.error("Поймали ошибку деления на 0")
        return float('inf')
    return res

if __name__ == "__main__":
    division(15, 0)

