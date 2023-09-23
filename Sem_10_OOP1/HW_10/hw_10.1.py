# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.



class Factory:
    def chooose_animal(self, animal, name, race, price, size, owner):
        if animal == "bird":
            return Bird(name, race, price)
        if animal == "dog":
            return Dog(name, race, owner)
        if animal == "fish":
            return Fish(name, race, size)


class Bird:
    def __init__(self, name, race, price):
        self._name = name
        self._race = race
        self._price = price

    def info(self):
        return f"Птица {self._name} вида {self._race} стоит {self._price}"


class Fish:
    def __init__(self, name, race, size):
        self._name = name
        self._race = race
        self._size = size

    def info(self):
        return f"Рыба {self._name} вида {self._race} имеет размер {self._size} "


class Dog:
    def __init__(self, name, race, owner):
        self._name = name
        self._race = race
        self._owner = owner

    def info(self):
        return f"Собака {self._name} породы {self._race}, хозяин {self._owner}"


animal = Factory()

first = animal.chooose_animal("dog", "Долли", "Спаниель", 1000, "крупный", "Иванов Сергей")
second = animal.chooose_animal("bird", "Поля", "гусь", 1000, "средний", "Васильева Аня")
third = animal.chooose_animal("fish", "Пират", "карп", 1000, "мелкий", "магазин Перекресток")
print(f"{first.info() = }, \n{second.info() = }, \n{third.info() = }")
