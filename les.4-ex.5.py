from functools import reduce


def summ(n_1, n_2):
    return n_1 + n_2


mk_list = [i for i in range(100, 1001) if i % 2 == 0]
print("Сумма элементов =", reduce(summ, mk_list))


#  Реализовать формирование списка, используя функцию range() и возможности генератора.
#  В список должны войти четные числа от 100 до 1000 (включая границы).
#  Необходимо получить результат вычисления произведения всех элементов списка.
#  Подсказка: использовать функцию reduce().