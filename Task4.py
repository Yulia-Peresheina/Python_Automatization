# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def operation_With_Numbers():
    result = 0
    while True:
        num = int(input("Enter the number from 1 to 999: "))
        if num >= 1 and num < 1000:
            break
    if num < 10:
        return"The square of number is "+str(num * num)
    elif num >= 10 and num < 100:
        return"The product of numbers is "+str(int(num % 10 * num / 10))
    elif num >= 100 and num < 1000:
        return "The mirrow number is "+ str(int(num%10)) + str(int((num / 10) % 10)) + str(int(num / 100))


print(operation_With_Numbers())