n = str(input("Введите число (одно или несколько) чтобы узнать сумму формата n+nn+nnn: "))
n2 = int(n + n)
n3 = int(n + n + n)
n = int(n)

sum_n = int(n + n2 + n3)  # 3+33+333=369
print(f"Сумма чисел равна: {sum_n}")