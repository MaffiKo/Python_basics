def alt_my_func(x, y):
    return print(f"Возведение в степень с использованием ** : {x ** y}")


def my_func(x, y):
    exp_alt = 1
    result = 0
    """
    Эту программу я написала не только для отрицательной степени(как было указано в задании), но и для положительной.
    Возможно код выглядит слишком большим, но я пыталась написать по другому и не выходило, так что оставила так :)
    """
    if y >= 0:
        while y > 0:
            exp_alt *= x
            y -= 1
        print('Альтернативное возведение в степень : ', exp_alt)
    else:
        y = abs(y)
        while y > 0:
            exp_alt *= x
            y -= 1
        result = 1 / exp_alt
        print('Альтернативное возведение в степень : ', result)
    return


exp_1 = int(input("Введите действительное положительное число: "))
exp_2 = int(input("Введите целое число для степени: "))

alt_my_func(exp_1, exp_2)
my_func(exp_1, exp_2)

#  Программа принимает действительное положительное число x и целое отрицательное число y.
#  Необходимо выполнить возведение числа x в степень y.
#  Задание необходимо реализовать в виде функции my_func(x, y).
#  При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
