class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        sing = "+" if self.b >= 0 else "-"
        return f'{self.a}{sing}{abs(self.b)}i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return ComplexNumber(a, b)


alfa, beta = ComplexNumber(2, 3), ComplexNumber(-1, 1)
alfa_check, bets_check = complex(2, 3), complex(-1, 1)

print(f'{alfa} + {beta} = {alfa + beta}')  # сложение
print(f'Check by func: {alfa_check + bets_check}\n')

print(f'{alfa} * {beta} = {alfa * beta}')  # умножение
print(f'Check by func: {alfa_check * bets_check}')
