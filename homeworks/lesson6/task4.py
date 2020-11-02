"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
from random import randrange


class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

        self._speed_now = 0

    def go(self):
        self._speed_now = randrange(1, self._speed)
        print(f'Машина "{self._name}" едет.')

    def stop(self):
        self._speed_now = 0
        print(f'Машина "{self._name}" остановилась.')

    def turn(self, direction):
        print(f'Машина "{self._name}" повернула {direction}.')

    def show_speed(self):
        print(f'Скорость "{self._name}" - {self._speed_now} к/ч')


class TownCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self._speed_now > 60:
            print('Превышение скорости!')


class WorkCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self._speed_now > 40:
            print('Превышение скорости!')


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, True)


class SportCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)


tcar = TownCar(100, 'белый', 'Toyota Corolla')
tcar.go()
tcar.show_speed()
tcar.turn('вправо')
tcar.stop()
tcar.show_speed()

wcar = WorkCar(90, 'черный', 'Ford F-150')
wcar.go()
wcar.show_speed()
wcar.turn('вправо')
wcar.stop()
wcar.show_speed()

pcar = PoliceCar(90, 'зелный', 'Ford F-150')
pcar.go()
pcar.show_speed()
pcar.turn('влево')
pcar.stop()
pcar.show_speed()

scar = SportCar(350, 'красный', 'Ferrari 488')
scar.go()
scar.show_speed()
scar.turn('прямо')
scar.stop()
scar.show_speed()
