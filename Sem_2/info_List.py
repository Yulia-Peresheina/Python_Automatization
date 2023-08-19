import sys

data = [1, 3.89, "Spring"]
for i in range (len(data)):
    if isinstance(data[i],int):
        print(i,"Элемент", data[i], "id", id(data), type(data[i]), "размер", sys.getsizeof(data[i]), "целое число")
    elif isinstance(data[i], str):
        print(i, "Элемент", data[i], "id", id(data), type(data[i]), "размер", sys.getsizeof(data[i]), "Строка")
    else:
        print(i, "Элемент", data[i], "id",id(data), type(data[i]), "размер", sys.getsizeof(data[i]))
