# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним

print("Now we check you triangle! ")
a = int(input("Enter first lendth: "))
b = int(input("Enter second lendth: "))
c = int(input("Enter third lendth: "))



def Triangle_or_not (side_a, side_b, side_c):
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return False
    else:
        return True

def What_triangle(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return "This is the equilateral triangle!"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "This is the isoscelis triangle!"
    else:
        return "This is the versatile triangle!"


if Triangle_or_not(a, b, c):
    print(What_triangle(a, b, c))
else:
    print("Sorry! This is not a triangle!")
