class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'Введенная дата - {self.date}'

    @classmethod
    def do_type_num(cls, date):
        day_list = date.split('-')
        return print(f'Число - {int(day_list[0])}, месяц - {int(day_list[1])}, год - {int(day_list[2])}')

    @staticmethod
    def check_date(d):
        list_check = d.split('-')
        if 0 < int(list_check[0]) < 32:
            if 0 < int(list_check[1]) < 13:
                if 1999 < int(list_check[2]) < 2999:
                    print('Дата введена корректно')
                else:
                    print(f'\033[31mГод должен быть годом 21го века!')
            else:
                print(f'\033[31mМесяц может быть только в промежутке от 1 до 12!')
        else:
            print(f'\033[31mДень введен не правильно!')


t_day = f"{input('Введите день:')}-{input('Введите месяц:')}-{input('Введите год 21 века:')}"
print(Date(t_day))
Date.do_type_num(t_day)
Date.check_date(t_day)

# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
