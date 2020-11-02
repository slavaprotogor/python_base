"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print('Машина едет.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print('Speed: ', self._speed)


class TownCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, True)


class SportCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)
