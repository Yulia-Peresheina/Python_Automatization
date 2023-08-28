# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

list_with_repetitions = [1, 2, 3, 4, 5, 2, 1, 7, 6, 2]

def delete_repetition(my_list):
    new_list = []
    for item in my_list:
        if new_list.count(item) == 0:
            new_list.append(item)
    return new_list

print(delete_repetition(list_with_repetitions))

print(set(list_with_repetitions))