# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

company_dict = {"alpha": [-10, 20, 45, -9, -11, 30],
                "beta": [234, 67, 93, -666, 903, 74, -11],
                "gamma": [1, -7, -9, -8, -2, -1, 5, 7, 9, 15],
                "delta": [99, 81, 70, 54, 23, 9, 0, -3, -1700]}


def profit_or_loss(data: dict) -> bool:
    status = []
    for value in data.values():
        if sum(value) < 0:
            status.append(False)
        else:
            status.append(True)
    if False in status:
        return False
    return True


print(profit_or_loss(company_dict))
