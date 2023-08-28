# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path_file(data: str):
    *path, other_info = data.split(sep="\\")
    path = "\\".join(path)
    file_name, extension = other_info.split(".")
    return path, file_name, extension


inp_str = r"C:\Users\HUAWEI\PycharmProjects\pythonProject\venv\Seminar_1\HW_1\Triangle_or_not.py"
print(split_path_file(inp_str))
