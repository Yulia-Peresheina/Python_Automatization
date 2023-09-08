"""
Напишите функцию, которая получает на вход директорию и 
рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий 
размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import csv
import json
import pickle
import os

my_dir_path = 'C:\\Users\\HUAWEI\\PycharmProjects\\pythonProject\\venv\\Seminar_1\\Sem_8_JSON_CSV'


def find_all(my_path):
    list_info = []
    for dir_path, dir_name, file_name in os.walk(my_path):
        for n_file in file_name:
            f_path = os.path.join(dir_path, n_file)
            f_size = os.path.getsize(f_path)
            my_dict = {'object_type': 'file', 'name': n_file, 'size': f_size, 'parent_directory': dir_path}
            list_info.append(my_dict)
        for n_dir in dir_name:
            d_path = os.path.join(dir_path, n_dir)
            d_size = 0
            for pardir, dirs_in, file_in in os.walk(d_path):
                for f in file_in:
                    f_par_path = os.path.join(pardir, f)
                    d_size += os.path.getsize(f_par_path)
            my_dict = {'object_type': 'directory', 'name': n_dir, 'size': d_size, 'parent_directory': dir_path}
            list_info.append(my_dict)
    print(list_info)

    json_data = json.dumps(list_info)
    with open('hw_8_j.json', 'w', encoding='utf-8') as j_file:
        j_file.write(json_data)

    with open('hw_8_c.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(list_info[0].keys())
        for item in list_info:
            writer.writerow(item.values())

    with open('hw_8_p.pickle', 'wb') as p_file:
        pickle.dump(list_info, p_file)


find_all(my_dir_path)
