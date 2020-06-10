class OfficeEquipment:

    def __init__(self, tp=0):
        self.invent_num = 0
        self.tp = tp
        self.all = []
        self.forprint, self.forscan, self.forx = [], [], []
        self.my_unit = {'Наим-ие': 0, 'Кол-во': 0, 'Цена ед-цы': 0, 'Общая ст-ть': 0}

    def add_equipm(self):
        while True:
            repeat_or_not = input('Для выхода и показа текущего списка склада введите - 1 '
                                      'или что угодно для продолжения\n')
            if repeat_or_not != '1':
                try:
                    tp_in = int(input("Укажите цирфу техники которую хотите добавить:\n"
                                      "1 - принтер\n2 - сканер\n3 - ксерокс\n"))
                    name = input("Введите название: ")
                    quantity = int(input("Количество: "))
                    cost = int(input("Цена за ед-цу: "))
                    eq_dict = {'Наим-ие': name, 'Кол-во': quantity, 'Цена ед-цы': cost, 'Общая ст-ть': quantity * cost}
                    self.my_unit.update(eq_dict)
                    if tp_in == 1:
                        self.forprint.append(self.my_unit)
                    elif tp_in == 2:
                        self.forscan.append(self.my_unit)
                    elif tp_in == 3:
                        self.forx.append(self.my_unit)
                    self.all.append(self.my_unit)
                    print(f"Введенно: {eq_dict}")
                except:
                    print("Не правильно введены данные! Попробуйте снова")
            else:
                print("Произведен выход\n")
                while True:
                    try:
                        print(self.all) if int(
                            input("Введите 1 чтобы посмотреть все данные или 0 для выхода: ")) == 1 else \
                            False
                        print(self.forprint) if int(
                            input("Если хотите увидеть список принтеров введите 1 или 0 для выхода: ")) == 1 else False
                        print(self.forscan) if int(
                            input("Если хотите увидеть список сканеров введите 1 или 0 для выхода:"
                                  " ")) == 1 else False
                        print(self.forx) if int(
                            input("Если хотите увидеть список ксероксов введите 1 или 0 для выхода: ")) \
                                            == 1 else False
                        print(f"\033[31mСпасибо, что воспользовались мной :) (с)Программа")
                        break
                    except ValueError:
                        print("Не правильно введены данные! Нужно использовать 1 или 0 при ответе")
                break


one = OfficeEquipment()
one.add_equipm()
