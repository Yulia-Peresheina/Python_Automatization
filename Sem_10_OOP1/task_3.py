# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person:

    def __init__(self, name, surname,  age):
        self._fullname = None
        self._name = name
        self._surname = surname
        self._age = age

    def birthday(self):
        self._age += 1
        return self._age

    def fullname(self):
        return self._name + " " + self._surname

    def get_age(self):
        return self._age


person = Person("Yulia", "Per", 35)
print(f"{person.get_age() = }, {person.birthday() = }, {person.fullname()}")

