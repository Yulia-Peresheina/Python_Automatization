# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
    input_number = int(input("Enter the number from 1 to 100 000: "))
    if input_number > 0 and input_number <= 100000:
        break

def Prime_or_not(number):
    print("Is it prime? ")
    for i in range (2, number):
        if number % i == 0:
            return "No!"
    return "Yes!"
print(Prime_or_not(input_number))