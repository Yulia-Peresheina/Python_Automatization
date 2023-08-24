# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

dict_of_things = {
    "tent": 4000,
    "sleeping bag": 2000,
    "burner": 800,
    "sweater": 100,
    "pants": 100,
    "socks": 500,
    "lighter": 200,
    "flashlight": 500,
    "water": 100,
    "pot": 100,
    "meal": 2000,
    "first aid kit": 1000
}

capacity_of_bag = int(input("Enter the capacity of your bag: "))
you_take = []
for key, value in dict_of_things.items():
    if capacity_of_bag - value >= 0:
        you_take.append(key)
        capacity_of_bag -= value

print(you_take)
