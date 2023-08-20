# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import fractions
import math

fraction1 = input("Введите первую дробь вида a/b: ")
fraction2 = input("Введите вторую дробь вида a/b: ")


def actions_with_frac(frac_1, frac_2):
    frac_1 = frac_1.split(sep="/")
    frac_2 = frac_2.split(sep="/")
    nomin_1 = int(frac_1[0])
    denom_1 = int(frac_1[1])
    nomin_2 = int(frac_2[0])
    denom_2 = int(frac_2[1])
    denom_summ = denom_1 * denom_2
    nomin_summ = nomin_1 * denom_2 + nomin_2 * denom_1
    denom_mult = denom_1 * denom_2
    nomin_mult = nomin_1 * nomin_2
    if math.gcd(nomin_summ, denom_summ):
        gcd_summ = math.gcd(nomin_summ, denom_summ)
        nomin_summ = nomin_summ // gcd_summ
        denom_summ = denom_summ // gcd_summ
    if math.gcd(nomin_mult, denom_mult):
        gcd_mult = math.gcd(nomin_mult, denom_mult)
        nomin_mult = nomin_mult // gcd_mult
        denom_mult = denom_mult // gcd_mult
    summ_frac = "".join([str(nomin_summ), "/", str(denom_summ)])
    mult_frac = "".join([str(nomin_mult), "/", str(denom_mult)])
    return [summ_frac, mult_frac]

def check_fractional(frac_1, frac_2, data_to_check):
    frac_1 = frac_1.split(sep="/")
    frac_2 = frac_2.split(sep="/")
    f1 = fractions.Fraction(int(frac_1[0]),int(frac_1[1]))
    f2 = fractions.Fraction(int(frac_2[0]), int(frac_2[1]))
    if data_to_check[0] == str(f1 + f2):
        if data_to_check[1] == str(f1 * f2):
            return True
    return False

if check_fractional(fraction1, fraction2, actions_with_frac(fraction1, fraction2)):
    print("Сумма дробей: ", actions_with_frac(fraction1, fraction2)[0])
    print("Произведение дробей: ", actions_with_frac(fraction1, fraction2)[1])
else:
    print("You broke it all")
