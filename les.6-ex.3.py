class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return print(f'Full name is {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        return print(f'Full income = {total_income}')


get = Position('Mary', 'Brown', 'Admin', 40000, 500)
get.get_full_name()
get.get_total_income()

#  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#  name, surname, position (должность), income (доход).
#  Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#  оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
#  дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
#  (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).