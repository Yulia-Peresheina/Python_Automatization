# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


def Leap_year():
    year = int(input("Enter the year to check it for leap year: "))
    if year % 400 == 0:
        return "yes"
    elif year % 4 == 0 and year % 100 != 0:
        return "yes"
    else:
        return "no"

print(Leap_year())