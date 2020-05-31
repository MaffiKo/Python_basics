class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'Car {self.name} is go.', end=" ")

    def stop(self):
        return print(f'Car {self.name} is stop.', end=" ")

    def turn(self, direction):
        return print(f'Car {self.name} turn {direction}.', end=" ")

    def show_speed(self):
        print(f'Speed is {self.speed}.', end=" ")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Over speed! Speed is {self.speed}.', end=" ") if self.speed > 60 \
            else print(f'Speed is {self.speed}.', end=" ")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Over speed! Speed is {self.speed}.', end=" ") if self.speed > 40 \
            else print(f'Speed is {self.speed}.', end=" ")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police, is_sport=True):
        super().__init__(speed, color, name, is_police)
        self.is_sport = is_sport

    def car_type(self):
        print(f'{self.name} is sport car.', end=" ") if self.is_sport else print('Its not sport car')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def its_police_or_not(self):
        print('Its police car.', end=" ") if self.is_police else print('Its not police car.', end=" ")


def before(car):
    print(car.name, end=": ")


car_1 = PoliceCar(70, 'red', 'Mazda', True)
before(car_1), car_1.go(), car_1.turn('right'), car_1.show_speed(), car_1.its_police_or_not()
print()

car_2 = SportCar(50, 'blue', 'Romashka', False)
before(car_2), car_2.stop(), car_2.go(), car_2.car_type()
print()

car_3 = TownCar(70, 'black', 'Lada', False)
before(car_3), car_3.show_speed(), car_3.stop()
print()

car_4 = WorkCar(40, 'white', 'Porsche', False)
before(car_4), car_4.turn('left'), car_4.show_speed()

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
#  40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
