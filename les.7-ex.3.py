class Cell:
    def __init__(self, n):
        self.n = int(n)

    def __add__(self, other):
        return f'Объединение даст {self.n + other.n}'

    def __sub__(self, other):
        result = self.n - other.n
        return f'Вычетание даст {result}' if result > 0 else 'Получилось отрицательное значение(у живых не может быть)!'

    def __mul__(self, other):
        return f'Умножение даст {self.n * other.n}'

    def __truediv__(self, other):
        return f'Деление даст {self.n / other.n}' if self.n > other.n else 'Деление меньшего на большее невозможно!'

    def make_order(self, times):
        a_1, a_2 = self.n // times, self.n % times
        while a_1 != 0:
            print('*' * times)
            a_1 -= 1
        print('*' * a_2)


cell_1 = Cell(int(input("Введите значение первой клетки(положительное целое число): ")))
cell_2 = Cell(int(input("Введите значение второй клетки(положительное целое число): ")))
print(f'{cell_1 + cell_2}\n{cell_1 - cell_2}\n{cell_1 * cell_2}\n{cell_1 / cell_2}')
num = cell_1 if input('Какую клетку вы хотите вывести рядами?(1 или 2): ') == '1' else cell_2
print(num.make_order(int(input('Укажите кол-во ячеек в ряду: '))))
