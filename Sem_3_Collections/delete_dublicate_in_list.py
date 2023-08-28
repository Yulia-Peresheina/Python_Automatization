# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 44, 9, 9, 9, 2, 3, 2, 44, 0, 1]

for el in my_list:
    if my_list.count(el) == 2:
        my_list.remove(el)
        my_list.remove(el)
print(my_list)