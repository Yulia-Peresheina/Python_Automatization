# Задача 1: Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = (1, 4, "hello", 44, 1, "hello", True, False, True, 44, "ever")

new_list = []
for el in my_list:
    if my_list.count(el) > 1:
        if new_list.count(el) == 0:
            new_list.append(el)
print(new_list)
