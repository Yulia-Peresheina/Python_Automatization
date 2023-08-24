# Задача 2: В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
import re


my_data = """Кортежи — это неизменяемые последовательности, обычно используемые для
хранения коллекций разнородных данных. Также используются в случаях, когда
требуется неизменяемая последовательность однородных данных. Как и строку
кортеж нельзя изменить после создания. При этом кортеж как и список является
массивом указателей на объекты любого типа."""

my_data = my_data.lower()


def list_without_punctuation(data):
    result = re.split(r'[.?!",)(}{—]+', data)
    new_data = " ".join(result)
    result = re.split(r"\n+", new_data)
    new_data = " ".join(result)
    result_list = new_data.split()
    return result_list


def count_most_frequent(list_data):
    frequency_list = []
    for item in list_data:
        count_element = list_data.count(item), item,
        frequency_list.append(count_element)
        for i in range(list_data.count(item)):
            list_data.remove(item)
    frequency_list.sort(reverse=True)
    return frequency_list


def print_ten_elements(list_data):
    for i in range(10):
        print(list_data[i])


print_ten_elements(count_most_frequent(list_without_punctuation(my_data)))
