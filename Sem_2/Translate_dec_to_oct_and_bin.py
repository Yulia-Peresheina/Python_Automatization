# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.

number_in_dec = int(input("Введите число: "))

def number_to_bin(number):
    result = ''
    while number // 2 > 1:
        result = str(number % 2) + result
        number = number // 2
    result = str(number // 2) + str(number % 2) + result
    return  result

def number_to_oct(number):
    result = ''
    while number // 8 > 8:
        result = str(number % 8) + result
        number = number // 8
    result = str(number // 8) + str(number % 8) + result
    return  result

print(number_in_dec, " -> ", number_to_bin(number_in_dec), " проверка: ", bin(number_in_dec))
print(number_in_dec, " -> ", number_to_oct(number_in_dec), " проверка: ", oct(number_in_dec))