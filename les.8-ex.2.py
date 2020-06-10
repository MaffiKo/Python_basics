class ErDivZero(Exception):
    def __init__(self, text):
        self.text = text


n = 0
while True:
    n += 1
    try:
        lets_div = int(input('На какое число вы хотите поделить 100? '))
        if lets_div == 0:
            raise ErDivZero('Деление на ноль этой программой невозможно!')
    except ValueError:
        print('Нужно вводить только число!')
    except ErDivZero as er_zero:
        print(er_zero)
    else:
        print(f'Результат = {100 / lets_div}')
        break
    finally:
        print(f'Мы завершили попытку под номером {n}\n')


# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
