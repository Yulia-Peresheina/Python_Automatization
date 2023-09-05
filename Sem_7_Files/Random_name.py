# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл
import random
import string


def create_names():
    name = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(3, 6)))
    if not is_there_vowels(name):
        name = ''.join([name, random.choice("eyuioa")])
        name = list(name)
        random.shuffle(name)
        name = "".join(name)
    return name.capitalize()


def print_name_to_file():
    with open("file_with_names.txt", "a", encoding="utf-8") as f:
        print(create_names(), file=f)


def is_there_vowels(name: str):
    vowels = ["e", "y", "u", "i", "o", "a"]
    for letter in name:
        if letter in vowels:
            return True
    return False


print(create_names())
print_name_to_file()
