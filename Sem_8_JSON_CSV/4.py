# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import json

import csv


with open("task8_2.csv", "r", newline="", encoding="utf-8") as f:
    csv_file = csv.reader(f)
    # res = list[csv_file]
    # print(res)
    data_info = []
    for i, line in enumerate(csv_file):
        if i == 0:
            line.append("Hash")
            data = line
            print(type(line))
        else:
            x = 10 - len(line[1])
            for _ in range(x):
                line[1] = "0" + line[1]
            line[2] = line[2].capitalize()

            line.append(f'{hash(line[1]+line[2])}')
            data_info.append(line)
    print(data)
    print(data_info)
res = []
for el in data_info:
    my_dict = {key: value for key, value in zip(data, el)}
    res.append(my_dict)
print(res)
with open("final8_4.json", "a", encoding="utf-8") as f:
    json.dump(res, f, indent=2)
