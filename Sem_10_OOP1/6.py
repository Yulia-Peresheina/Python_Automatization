# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size


class Fish(Animal):
    def __init__(self, name, size, type_fish):
        super().__init__(name, size)
        self._type = type

    def get_type(self):
        return self._type


class Dog(Animal):
    def __init__(self, name, size, owner):
        super().__init__(name, size)
        self._owner = owner

    def get_owner(self):
        return self._owner


class Bird(Animal):
    def __init__(self, name, size, price):
        super().__init__(name, size)
        self._price = price

    def get_price(self):
        return self._price


dog = Dog("Billy", "big", "Sam")
print(f"{dog.get_owner() = }, {dog.get_size() = }, {dog.get_name() = }")