# Напишите программу банкомат.
#  Начальная сумма равна нулю
#  Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def atm_mashine():
    i = 1
    j = 1
    summ: int = 0
    while True:
        action = input("Выберете действие:\n - Пополнить\n - Снять\n - Выйти\n")
        if summ > 5_000_000:
            print("Удержан налог на богатство в размере 10% от суммы на счету: ", int(summ * 0.1))
            summ = int(summ * 0.9)
            print("Остаток на счете:", summ)
        match(action.lower()):
            case "пополнить":
                put = int(input("Введите сумму пополнения, кратно 50: "))
                put = (put // 50) * 50
                if i % 3 == 0:
                    print("Процент за пополнение: 3% от суммы пополнения")
                    comission_percent = 0.03
                else:
                    comission_percent = 0
                comission = int(comission_percent * put)
                summ = int(summ + put - comission)
                i += 1
                j = 1
                print("Комиссия: ", comission, "Внесено: ", put - comission)
                print("Остаток на счете: ", summ)

            case "снять":
                comission = 0
                min_comission = 30
                max_comission = 600
                take_off = int(input("Введите сумму снятия, кратно 50: "))
                take_off = (take_off // 50) * 50
                if take_off > summ:
                    print("Сумма снятия превышает остаток на счете!")
                else:
                    if j % 3 == 0:
                        print("Процент за снятие: 3% от суммы снятия, но не менее 30 и не более 600 у.е.")
                        comission_percent = 0.03
                    else:
                        print("Процент за снятие: 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.")
                        comission_percent = 0.015
                    comission = comission_percent * take_off
                    if comission < min_comission:
                        comission = min_comission
                    elif comission > max_comission:
                        comission = max_comission
                    print("Сумма на счете: ", summ, "Сумма снятия: ", take_off, "Комиссиия: ", comission)
                    if take_off + comission > summ:
                        print("Недостаточно средств на счете для снятия с учетом комиссии!")
                    else:
                        summ = summ - take_off - comission
                        print("Остаток на счете: ", summ)
                        j += 1
                        i = 1
            case "выйти":
                # print()
                break
            case _:
                print("Некорректный ввод. Попробуйте еще. ")


atm_mashine()