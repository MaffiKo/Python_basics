class Matrix:
    def __init__(self, my_m):
        self.my_m = my_m

    def __str__(self):
        return '\n'.join(map(str, self.my_m))

    def __add__(self, other):
        try:
            result = []
            for i in range(len(self.my_m)):
                result.append([])
                for l in range(len(self.my_m[0])):
                    result[i].append(self.my_m[i][l] + other.my_m[i][l])
            return '\n'.join(map(str, result))
        except NameError:
            return 'Эта программа отвечает за суммирование матриц, значит в ней должны быть только цифры'
        except IndexError:
            return 'Матрицы разного размера эта программа не суммирует'


m_1 = [[1, 2], [-3, 4], [5, 6]]
m_2 = [[5, 9], [12, 4], [-5, 87]]
matrix_1, matrix_2 = Matrix(m_1), Matrix(m_2)
print(matrix_1, '\n' * 2, matrix_2, '\n' * 2, 'Сумма матриц:\n', matrix_1 + matrix_2)
