def sum_list(user_list):
    new = []
    for i in user_list:
        new.append(int(i))
    return sum(new)


with open("hw_5.txt", "w", encoding="utf-8") as hw_5:
    s = 0
    my_list = input("Введите несколько чисел через пробел, или для выхода напишите 'q': ").split()
    s += sum_list(my_list)
    print(my_list, file=hw_5, end=" ")
    print('Сумма = ', s)

#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
