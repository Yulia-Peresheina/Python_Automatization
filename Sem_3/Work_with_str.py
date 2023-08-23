# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = input("Enter the text: ")
list_of_text = text.split()
list_of_text.sort()
print(max(list_of_text))
max = len(list_of_text[0])
for el in list_of_text:
    if len(el) > max:
        max = len(el)
for i in range(len(list_of_text)):
    print(f"{i + 1} {list_of_text[i]:>{max}}")