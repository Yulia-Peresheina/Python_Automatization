"""Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной
строки с передачей параметров.
Для выполнения взята задача из семинароа №1:
Треугольник существует только тогда, когда сумма любых
двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним"""


import logging
import argparse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


class NegLenError(Exception):
    pass


def triangle_or_not(side_a, side_b, side_c):
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise NegLenError("Стороны треугольника должны быть больше 0!")
    return side_a + side_c > side_b and side_b + side_c > side_a and side_a + side_b > side_c


def triangle_type(side_a, side_b, side_c):
    if triangle_or_not(side_a, side_b, side_c):
        if side_a == side_b == side_c:
            return 'Равносторонний'
        elif side_a == side_b or side_b == side_c or side_a == side_c:
            return 'Равнобедренный'
        else:
            return 'Разносторонний'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Определение типа треугольника')
    parser.add_argument('--a', type=float, help='Длина стороны a', required=True)
    parser.add_argument('--b', type=float, help='Длина стороны b', required=True)
    parser.add_argument('--c', type=float, help='Длина стороны c', required=True)
    args = parser.parse_args()

    try:
        a, b, c = args.a, args.b, args.c
        logging.info(f'Проверка существования треугольника со сторонами: {a}, {b}, {c}')
        if triangle_or_not(a, b, c):
            logging.info(f'Треугольник существует. Он {triangle_type(a, b, c)}.')
        else:
            logging.warning(f'Треугольник не существует')
    except NegLenError as e:
        logging.error(f'Ошибка: {e}')

# python Sem_15_Libr\hw_15\homework_15.py --a 3 --b 4 --c 5
# python Sem_15_Libr\hw_15\homework_15.py --a 3 --b 3 --c 3
# python Sem_15_Libr\hw_15\homework_15.py --a 3 --b 4 --c 3
# python Sem_15_Libr\hw_15\homework_15.py --a 6 --b 6 --c 6
