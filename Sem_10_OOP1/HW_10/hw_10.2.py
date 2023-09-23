# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


class JsonConverter:
    def __init__(self, file_data, file_to_write):
        self._file_data = file_data
        self._file_to_write = file_to_write

    def file_to_json(self):
        with open(self._file_data, "r", encoding="utf-8") as f_r, open(self._file_to_write, "w", encoding="utf-8") as f_w:
            my_dict = {}
            for line in f_r:
                line = line.replace("\n", "").split(" - ")
                my_dict[line[0].capitalize()] = float(line[1])
            json.dump(my_dict, f_w, indent=1)


f = JsonConverter("task10_2.txt", "task10_2.json")
f.file_to_json()



