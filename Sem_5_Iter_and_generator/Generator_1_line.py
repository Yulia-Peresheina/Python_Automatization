# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


my_gen = (f"{i} * {j} = {i * j}; " for i in range(2, 10) for j in range(2, 10))

for char in my_gen:
    print(char, end="")