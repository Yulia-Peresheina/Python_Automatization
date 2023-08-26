# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def create_unicode_dict(data: str) -> dict:
    unicode_dict = {}
    data = data.split()
    start = min(int(data[0]), int(data[1]))
    finish = max(int(data[0]), int(data[1]))
    while start != finish:
        unicode_dict[chr(start)] = start
        start += 1
    return unicode_dict


print(create_unicode_dict("1054 1201"))
