list_check = [777, 'MaffiKo', 5.236, True, [5, 2]]
all_index = len(list_check)
first = 0
last = all_index - 1
while last > -1:  # Сделала с while потому что в будущем смогу переписать для запроса у пользователя списка
    print(f"У элемента под номером {last + 1} тип данных - {type(list_check[last])}")
    last = last - 1


# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
