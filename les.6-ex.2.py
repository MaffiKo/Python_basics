class Road:
    length = True
    width = False

    def __init__(self):
        self._length = int(input("Enter length(m): "))
        self._width = int(input("Enter width(m): "))

    def how_much(self):
        result = int(self._length * self._width * 2.5 * 0.05)
        return print(f'For the road we need {result} tn')


lets = Road()
lets.how_much()

#  Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
