# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_of_numbs_between_indexes(my_list: list, ind_1: int, ind_2: int) -> int | str:
    sum_between_indexes = 0
    index_min = min(ind_1, ind_2)
    index_max = max(ind_1, ind_2)
    if index_min < 0:
        index_min += len(my_list)
    if index_max < 0:
        index_max += len(my_list)
    list_index_set = set()
    for i in range(len(my_list)):
        list_index_set.add(i)
    index_set = set()
    for j in range(index_min, index_max + 1):
        index_set.add(j)
    new_set = list_index_set & index_set
    if new_set:
        for el in new_set:
            sum_between_indexes += my_list[el]
        return sum_between_indexes
    else:
        return "No elements"


my_new_list = [1, 2, 3, 4, 5]
index_1 = 2
index_2 = 3

print(sum_of_numbs_between_indexes(my_new_list, index_1, index_2))


