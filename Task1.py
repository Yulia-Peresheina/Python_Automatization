# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

start_number = 1
finish_number = int(input("Enter the finish number: "))
e = int(input("Enter the frequency rate: "))
result = 0
while start_number < finish_number:
    if start_number % 2 == 0 and start_number % e != 0:
        result += start_number
    start_number += 1
print("Summ of even numbers from 1 till ", finish_number,
      ", exclude frequancy rate ", e, " is: ", result)