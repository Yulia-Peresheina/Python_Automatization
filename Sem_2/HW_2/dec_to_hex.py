# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

def dec_number_to_hex():
    dec_number = int(input("Enter the decimal number to translate in in hex number: "))
    result = ""
    print("Check: ", hex(dec_number))
    while dec_number > 16:
        remainder = dec_number % 16
        match remainder:
            case 10:
                remainder = "A"
            case 11:
                remainder = "B"
            case 12:
                remainder = "C"
            case 13:
                remainder = "D"
            case 14:
                remainder = "E"
            case 15:
                remainder = "F"
            case _:
                remainder = str(remainder)

        result = remainder + result
        dec_number = dec_number // 16
    result = str(dec_number) + result
    print("My solution: ", result)

dec_number_to_hex()
