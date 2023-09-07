# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

file_read = r"C:\Users\HUAWEI\PycharmProjects\pythonProject\venv\Seminar_1\Sem_7_Files\task7_3.txt"
file_write = "Task7_1.json"


def file_to_json(file_data, file_to_write):
    with open(file_data, "r", encoding="utf-8") as f_r, open(file_to_write, "w", encoding="utf-8") as f_w:
        my_dict = {}
        for line in f_r:
            line = line.replace("\n", "").split(" - ")
            my_dict[line[0].capitalize()] = float(line[1])
        json.dump(my_dict, f_w, indent=1)


file_to_json(file_read, file_write)



