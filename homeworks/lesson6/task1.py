"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time
from itertools import cycle


class Color:

    def __init__(self, name, delay):
        self.name = name
        self.delay = delay


class TrafficLight:

    def __init__(self):
        self.__colors = []

    def add_color(self, color: Color):
        self.__colors.append(color)

    def running(self):
        for color in cycle(self.__colors):
            print('Свет: ', color.name)
            time.sleep(color.delay)


tl = TrafficLight()

tl.add_color(Color('красный', 7))
tl.add_color(Color('желтый', 2))
tl.add_color(Color('зеленый', 5))

tl.running()
