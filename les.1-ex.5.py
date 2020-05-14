revenue = int(input("Введите вашу выручку (в тыс.руб.) "))
cost = int(input("Введите значение издержек (в тыс.руб.) "))
profit = revenue - cost

if profit > 0:
    profitab = int(profit / revenue * 100)
    print(f"За период вы получили прибыль {profit} тыс.руб.")
    print(f"Рентабельность вашей выручки составаила {profitab} %")
    employee = int(input("Введите численность сотрудников "))
    prof_empl = int(profit/employee)
    print(f"Прибыль фирмы в расчете на 1го сотрудника составила {prof_empl} тыс. руб.")

elif profit == 0:
    print("Ваша выручка равна издержкам")

else:
    print(f"За период вы получили убыток: {profit} тыс. руб.")