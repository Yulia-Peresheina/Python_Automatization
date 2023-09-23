# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
import random
from task_3 import Person


class Employee(Person):

    def get_id(self):
        self._id = random.randint(100000, 1000000)
        return self._id

    def access_level(self):
        return self._id % 7


worker = Employee("Vasya", "Pupkin", 33)
print(f"{worker.get_id() = }, {worker.access_level() = }")
