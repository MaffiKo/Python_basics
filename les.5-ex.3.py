with open('text_3.txt', 'r', encoding='utf-8') as text:
    salary = []
    surname = []
    min_sal = float('20000')
    my_list = text.read().split('\n')
    print(my_list)
    for i in my_list:
        i = i.split()
        if float(i[1]) < min_sal:
            surname.append(i[0])
        salary.append(i[1])
    all_salary = sum(map(float, salary)) / len(salary)
    print(f'Оклад меньше 20.000 у: {surname}, средний оклад равен {all_salary}')


#  3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
#  (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
