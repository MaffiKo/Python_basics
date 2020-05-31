from random import random


class Stationery:
    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print(f'Start drawing number {self.tittle}')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing number {self.tittle} by pen')


class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing number {self.tittle} by pencil')


class Handle(Stationery):
    def draw(self):
        print(f'Start drawing number {self.tittle} by handle')


def get_number():
    return random() * 1000


draw_1 = Pen(get_number())
draw_2 = Handle(get_number())
draw_3 = Pencil(get_number())
draw_1.draw(), draw_2.draw(), draw_3.draw()

#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
