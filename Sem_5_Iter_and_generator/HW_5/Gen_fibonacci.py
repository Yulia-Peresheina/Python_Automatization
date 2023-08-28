# Создайте функцию генератор чисел Фибоначчи

def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(0, n):
        if i == 0:
            yield 1
        elif i == 1:
            yield 1
        else:
            yield a + b
            a, b = b, a + b


for i in enumerate(gen_fibonacci(10)):
    print(i)


