# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Fish:
    def __init__(self, name, type, size):
        self._name = name
        self._type = type
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def get_type(self):
        return self._type


class Dog:
    def __init__(self, name, owner, size):
        self._name = name
        self._owner = owner
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def get_owner(self):
        return self._owner


class Bird:
    def __init__(self, name, price, size):
        self._name = name
        self._price = price
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def get_price(self):
        return self._price


dog = Dog("Billy", "Sam", "big")
print(f"{dog.get_name() = }")