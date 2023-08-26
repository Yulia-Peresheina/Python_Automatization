# Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


def create_dict_from_3_lists(names: list, rates: list, prize_percents: list) -> dict:
    name_prize_dict = {}
    for name, rate, prize_percent in zip(names, rates, prize_percents):
        prize = float(rate) * float(prize_percent.replace("%", "")) * 0.01
        name_prize_dict[name] = prize
    return name_prize_dict


workers = ["Petrov", "Ivanov", "Sidorov"]
workers_rate = [10000, 15000, 20000]
workers_prize_percent = ["10.25%", "15.20%", "5.0%"]

print(create_dict_from_3_lists(workers, workers_rate, workers_prize_percent))
