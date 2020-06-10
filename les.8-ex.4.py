class Warehouse:
    pass


class OfficeEquipment:

    def __init__(self, invent_num):
        self.invent_num = invent_num

    def show_num(self):
        return print(f'Инвентарный номер: {self.invent_num}')


class Printer(OfficeEquipment):

    def __init__(self, invent_num, type_printer):
        super().__init__(invent_num)
        self.type_printer = type_printer

    def __str__(self):
        return f"Its printer {self.type_printer}, inventory number: {self.invent_num}"


class Scan(OfficeEquipment):

    def __init__(self, invent_num, color_scan):
        super().__init__(invent_num)
        self.color_scan = color_scan

    def __str__(self):
        return f"Its scanner, has {self.color_scan}, inventory number: {self.invent_num}"


class Xerox(OfficeEquipment):

    def __init__(self, invent_num, size):
        super().__init__(invent_num)
        self.size = size

    def __str__(self):
        return f"Its xerox, size is {self.size}, inventory number: {self.invent_num}"


first, second, another = Printer(4564, 'usual'), Scan(952, "black/white color"), Xerox(438, 'small')
print(first)
print(second)
print(another)
