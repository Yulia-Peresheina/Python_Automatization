text = input("Введите текст: ")
if text.isdecimal():
    print(text)
    text = int(text)
    print("Двоичное представление: ", bin(text))
    print("Восьмеричное представление: ", oct(text))
    print("Шестнадцатеричное представление", hex(text))
elif text.isascii():
    print("Текст в ASCII")
